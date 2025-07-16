import asyncio
import json
import logging
import os
import sqlite3

import click

from .db import create_tables, get_db_path
from .llm import llm_manager
from .models import LLMProvider
from .project_operations import (
    process_project,
    show_project_summary,
    show_project_tasks,
)

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@click.command()
@click.option("--name", help="Project name")
@click.option("--description", help="Project description")
@click.option(
    "--force", is_flag=True, help="Force task decomposition even if tasks already exist"
)
@click.option("--list", is_flag=True, help="List all projects and their task counts")
@click.option(
    "--use-llm",
    type=click.Choice(["ollama", "claude", "gemini", "random"]),
    default="ollama",
    help="Choose LLM provider",
)
@click.option(
    "--check-health", is_flag=True, help="Check health status of LLM providers"
)
@click.option(
    "--reset-config", is_flag=True, help="Reset the configuration to default values"
)
def main(
    name: str,
    description: str,
    force: bool,
    list: bool,
    use_llm: str,
    check_health: bool,
    reset_config: bool,
):
    async def async_main():
        nonlocal description  # This line allows us to modify the outer scope variable
        try:
            if reset_config:
                llm_manager.create_default_config()
                click.echo("Configuration has been reset.")
                return

            llm_manager.config.provider = LLMProvider(use_llm)
            llm_manager.save_config(llm_manager.config)

            if check_health:
                await llm_manager.update_health_status(force_check=True)
                click.echo(
                    f"Ollama health: {'Healthy' if llm_manager.config.ollama_healthy else 'Unhealthy'}"
                )
                click.echo(
                    f"Claude health: {'Healthy' if llm_manager.config.claude_healthy else 'Unhealthy'}"
                )
                click.echo(
                    f"Gemini health: {'Healthy' if llm_manager.config.gemini_healthy else 'Unhealthy'}"
                )
                return

            create_tables()

            if list:
                show_project_summary()
            elif name:
                if force and not description:
                    conn = sqlite3.connect(get_db_path())
                    c = conn.cursor()
                    c.execute(
                        "SELECT definition FROM project_versions WHERE id = ?", (name,)
                    )
                    result = c.fetchone()
                    conn.close()

                    if result:
                        try:
                            existing_project = json.loads(result[0])
                            description = existing_project.get(
                                "description", "No description available"
                            )
                        except json.JSONDecodeError:
                            click.echo(
                                f"Error: Invalid JSON data for project '{name}'. Please provide a description."
                            )
                            return
                    else:
                        click.echo(
                            f"Error: No existing project found with name '{name}'. Please provide a description."
                        )
                        return

                if description or force:
                    await process_project(name, description, force)
                else:
                    show_project_tasks(name)
            else:
                click.echo(
                    "Please provide a project name or use --list to see all projects."
                )
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")
            click.echo("An error occurred. Please check the logs for more information.")

    asyncio.run(async_main())


if __name__ == "__main__":
    main()

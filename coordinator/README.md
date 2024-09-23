# Coordinator: AI-Powered Project Management System

Coordinator is an advanced project management and task coordination system designed to streamline software development processes using AI-driven insights and automation.

## Features

- Task decomposition and prioritization
- RFC (Request for Comments) generation and management
- Project planning and timeline estimation
- Integration with multiple AI providers (Ollama, Claude)
- Database-backed task and project storage
- Extensible architecture for adding new AI agents and capabilities

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-org/coordinator.git
   cd coordinator
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```
   export ANTHROPIC_API_KEY=your_claude_api_key_here
   ```

## Usage

### Basic Command

Run the Coordinator with:

```
python -m coordinator --name "Project Name" --description "Project description"
```

### Options

- `--name`: Specify the project name
- `--description`: Provide a project description
- `--force`: Force task decomposition even if tasks already exist
- `--list`: List all projects and their task counts
- `--use-llm`: Choose LLM provider (ollama, claude, random)
- `--check-health`: Check health status of LLM providers
- `--reset-config`: Reset the configuration to default values

### Examples

1. Create a new project:
   ```
   python -m coordinator --name "Web App Redesign" --description "Redesign the company's web application for better user experience"
   ```

2. List all projects:
   ```
   python -m coordinator --list
   ```

3. Force re-decomposition of an existing project:
   ```
   python -m coordinator --name "Web App Redesign" --force
   ```

4. Use a specific LLM provider:
   ```
   python -m coordinator --name "API Optimization" --description "Optimize backend APIs for better performance" --use-llm claude
   ```

## Configuration

The Coordinator uses a configuration file `llm_config.json` to store settings. You can reset this configuration using the `--reset-config` option.

## Project Structure

- `coordinator/`: Main package directory
  - `__init__.py`: Package initialization
  - `main.py`: Entry point for the Coordinator
  - `db.py`: Database operations
  - `llm.py`: LLM provider management
  - `models.py`: Data models
  - `project_operations.py`: Project-related operations
  - `prompts.py`: System prompts for AI agents
  - `utils.py`: Utility functions
  - `llms/`: LLM provider implementations

## Extending the Coordinator

To add new AI agents or capabilities:

1. Create a new agent in `prompts.py`
2. Implement the agent's logic in `project_operations.py`
3. Update `models.py` if new data structures are needed
4. Modify `main.py` to incorporate the new agent into the workflow

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue on the GitHub repository or contact the maintainers at support@coordinator-project.com.

---

We hope you find the Coordinator helpful in managing your software projects! Your feedback and contributions are always welcome.

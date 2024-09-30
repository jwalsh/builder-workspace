"""Main entry point for the AICodeReviewer application."""

import logging
from .code_analyzer import CodeAnalyzer
from .vcs_integrator import VCSIntegrator
from .ai_suggester import AISuggester
from .security_checker import SecurityChecker
from .ui_generator import UIGenerator

# Rest of the main.py content...

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting AICodeReviewer")

    # Initialize components
    code_analyzer = CodeAnalyzer()
    vcs_integrator = VCSIntegrator()
    ai_suggester = AISuggester()
    security_checker = SecurityChecker()
    ui_generator = UIGenerator()

    # Main workflow
    try:
        # Fetch code changes
        changes = vcs_integrator.fetch_changes()

        # Analyze code
        analysis_results = code_analyzer.analyze(changes)

        # Generate AI suggestions
        suggestions = ai_suggester.generate_suggestions(analysis_results)

        # Check for security vulnerabilities
        security_warnings = security_checker.check_vulnerabilities(changes)

        # Generate UI for results
        ui = ui_generator.generate_ui(analysis_results, suggestions, security_warnings)

        # Display or send results
        ui.display()

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()

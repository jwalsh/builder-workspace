"""Coordinator: AI-powered project management and task coordination system

This module provides a suite of tools for managing software development projects,
including task decomposition, RFC generation, and project planning.

Usage:
    from coordinator import main
    
    # Run the main coordination process
    main()

The coordinator can be configured to use different LLM providers (e.g., Ollama, Claude)
and supports various project management functions such as task creation, updating,
and project summarization.

See the README.md file for more detailed usage instructions and configuration options.
"""

from .db import *

# Import the main function last to avoid circular imports
from .main import main

# Import necessary modules, but avoid circular imports
from .models import *
from .prompts import *
from .utils import *

# Version of the coordinator package
__version__ = "0.1.0"

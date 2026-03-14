"""
Partner OS — Centralized Logging Utility
========================================
Provides a standardized logging interface for all agents and modules.
Ensures consistent formatting, log levels, and persistence to disk.
"""

import logging
import sys
from pathlib import Path
from config import LOG_DIR, LOG_LEVEL, LOG_FORMAT, LOG_DATE_FORMAT

def setup_logging():
    """
    Initializes the logging system.
    Creates the log directory if it doesn't exist and configures
    the root logger with console and file handlers.
    """
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_DIR / "partner_os.log", encoding="utf-8")
        ]
    )

def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance for the given name.
    
    Args:
        name: The name of the module or agent (typically __name__).
        
    Returns:
        A logging.Logger instance.
    """
    # Ensure setup_logging is called if not already configured
    if not logging.getLogger().hasHandlers():
        setup_logging()
        
    return logging.getLogger(name)

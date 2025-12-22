#!/usr/bin/env python3
"""
BallCODE Local Email System - Main Entry Point
Simplest way to use the email system
"""

import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Change to email_system directory
os.chdir(current_dir)

# Import CLI
try:
    import cli
    cli_obj = cli.cli
except ImportError as e:
    # Try alternative import
    try:
        from email_system import cli
        cli_obj = cli.cli
    except ImportError:
        print(f"❌ Error: Could not import cli module: {e}")
        print(f"Current directory: {os.getcwd()}")
        print(f"Files in directory: {os.listdir(current_dir)}")
        sys.exit(1)

if __name__ == '__main__':
    cli_obj()


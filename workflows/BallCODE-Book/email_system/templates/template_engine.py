"""
Email Template Engine
Processes templates with variable substitution
"""

import re
from typing import Dict, Optional
from pathlib import Path

class TemplateEngine:
    """Email template engine with variable substitution"""
    
    def __init__(self, templates_dir: str = "templates"):
        """
        Initialize template engine
        
        Args:
            templates_dir: Directory containing template files
        """
        self.templates_dir = Path(__file__).parent / templates_dir
        self.templates_dir.mkdir(exist_ok=True)
    
    def render(self, template_name: str, variables: Dict) -> str:
        """
        Render template with variables
        
        Args:
            template_name: Name of template file
            variables: Dictionary of variables to substitute
            
        Returns:
            Rendered template string
        """
        template_path = self.templates_dir / f"{template_name}.txt"
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_name}")
        
        with open(template_path, 'r') as f:
            template = f.read()
        
        # Replace variables: {{ variable_name }}
        for key, value in variables.items():
            template = template.replace(f"{{{{ {key} }}}}", str(value))
            template = template.replace(f"{{{{{key}}}}}", str(value))
        
        return template
    
    def render_html(self, template_name: str, variables: Dict) -> str:
        """
        Render HTML template with variables
        
        Args:
            template_name: Name of template file
            variables: Dictionary of variables to substitute
            
        Returns:
            Rendered HTML template string
        """
        template_path = self.templates_dir / f"{template_name}.html"
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_name}")
        
        with open(template_path, 'r') as f:
            template = f.read()
        
        # Replace variables
        for key, value in variables.items():
            template = template.replace(f"{{{{ {key} }}}}", str(value))
            template = template.replace(f"{{{{{key}}}}}", str(value))
        
        return template




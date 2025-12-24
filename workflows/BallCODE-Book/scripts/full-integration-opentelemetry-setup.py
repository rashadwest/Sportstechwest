#!/usr/bin/env python3
"""
Full Integration: OpenTelemetry Setup
Sets up OpenTelemetry instrumentation for Full Integration scripts.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def setup_opentelemetry(config_json: str) -> dict:
    """Set up OpenTelemetry instrumentation."""
    try:
        # Parse config
        if isinstance(config_json, str):
            try:
                config = json.loads(config_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', config_json)
                if json_match:
                    config = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            config = config_json
        
        results = {
            "status": "success",
            "opentelemetry_setup": False,
            "instrumentation_added": [],
            "errors": []
        }
        
        # Check if opentelemetry is installed
        try:
            import opentelemetry
            opentelemetry_installed = True
        except ImportError:
            opentelemetry_installed = False
            results["errors"].append("OpenTelemetry not installed. Install with: pip install opentelemetry-api opentelemetry-sdk")
        
        if opentelemetry_installed:
            # Create instrumentation template
            instrumentation_template = '''"""
OpenTelemetry Instrumentation for Full Integration Scripts
Add this to the top of Full Integration scripts for tracing.
"""

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor

# Set up tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Add console exporter (can be replaced with OTLP exporter for production)
console_exporter = ConsoleSpanExporter()
span_processor = BatchSpanProcessor(console_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Usage in scripts:
# with tracer.start_as_current_span("script_name"):
#     # Your code here
#     pass
'''
            
            # Save instrumentation template
            template_path = PROJECT_ROOT / "scripts" / "opentelemetry_instrumentation.py"
            template_path.write_text(instrumentation_template, encoding='utf-8')
            
            results["opentelemetry_setup"] = True
            results["instrumentation_added"].append(str(template_path))
            results["message"] = "OpenTelemetry instrumentation template created. Add to scripts as needed."
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "opentelemetry_setup": False,
            "errors": [str(e)]
        }

if __name__ == "__main__":
    # Default config
    default_config = json.dumps({
        "setup_instrumentation": True
    })
    
    input_json = sys.argv[1] if len(sys.argv) > 1 else default_config
    
    result = setup_opentelemetry(input_json)
    print(json.dumps(result, indent=2))
    
    if result.get("status") == "error":
        sys.exit(1)


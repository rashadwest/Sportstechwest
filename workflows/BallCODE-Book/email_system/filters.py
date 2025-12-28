"""
Email Filtering and Rule Engine
Auto-categorize, tag, and filter emails
"""

import re
from typing import Dict, List, Optional
from datetime import datetime

class EmailFilter:
    """Email filtering and rule engine"""
    
    def __init__(self):
        self.rules = []
        self._load_default_rules()
    
    def _load_default_rules(self):
        """Load default filtering rules"""
        self.rules = [
            {
                "name": "Sales Inquiry",
                "condition": lambda email: any(keyword in email.get('subject', '').lower() 
                                               or keyword in email.get('body', '').lower() 
                                               for keyword in ['buy', 'purchase', 'price', 'cost', 'quote', 'sales']),
                "action": "tag",
                "tag": "sales",
                "category": "sales"
            },
            {
                "name": "Support Request",
                "condition": lambda email: any(keyword in email.get('subject', '').lower() 
                                               or keyword in email.get('body', '').lower() 
                                               for keyword in ['help', 'support', 'issue', 'problem', 'bug', 'error']),
                "action": "tag",
                "tag": "support",
                "category": "support"
            },
            {
                "name": "Newsletter/Spam",
                "condition": lambda email: any(keyword in email.get('from_address', '').lower() 
                                               for keyword in ['noreply', 'no-reply', 'newsletter', 'unsubscribe']),
                "action": "tag",
                "tag": "newsletter",
                "category": "newsletter"
            },
            {
                "name": "High Priority",
                "condition": lambda email: any(keyword in email.get('subject', '').lower() 
                                               for keyword in ['urgent', 'asap', 'important', 'critical']),
                "action": "priority",
                "priority": "high"
            }
        ]
    
    def add_rule(self, name: str, condition, action: str, **kwargs):
        """
        Add custom rule
        
        Args:
            name: Rule name
            condition: Function that takes email dict and returns bool
            action: Action to take (tag, category, priority, forward)
            **kwargs: Action-specific parameters
        """
        rule = {
            "name": name,
            "condition": condition,
            "action": action,
            **kwargs
        }
        self.rules.append(rule)
    
    def process_email(self, email: Dict) -> Dict:
        """
        Process email through filter rules
        
        Args:
            email: Email dictionary
            
        Returns:
            Email with tags, category, priority added
        """
        result = email.copy()
        result.setdefault("tags", [])
        result.setdefault("category", "general")
        result.setdefault("priority", "normal")
        
        for rule in self.rules:
            try:
                if rule["condition"](email):
                    action = rule["action"]
                    
                    if action == "tag":
                        tag = rule.get("tag")
                        if tag and tag not in result["tags"]:
                            result["tags"].append(tag)
                    
                    if action == "category":
                        result["category"] = rule.get("category", result["category"])
                    
                    if action == "priority":
                        result["priority"] = rule.get("priority", result["priority"])
                    
                    if action == "forward":
                        # Forward logic would go here
                        pass
            except Exception as e:
                print(f"⚠️  Rule '{rule['name']}' failed: {e}")
        
        return result
    
    def categorize_email(self, email: Dict) -> str:
        """
        Categorize email
        
        Args:
            email: Email dictionary
            
        Returns:
            Category name
        """
        processed = self.process_email(email)
        return processed.get("category", "general")
    
    def get_tags(self, email: Dict) -> List[str]:
        """
        Get tags for email
        
        Args:
            email: Email dictionary
            
        Returns:
            List of tags
        """
        processed = self.process_email(email)
        return processed.get("tags", [])




#!/usr/bin/env python3
"""
Check OpenAI API Credits and Status
Verifies OpenAI API key, and (optionally) checks today's spend vs budget.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import requests
import argparse
import time
from datetime import datetime, timezone, timedelta

# Get API key from environment or prompt
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

OPENAI_API_BASE = "https://api.openai.com/v1"

def check_openai_api():
    """Check OpenAI API key and credits."""
    print("🔍 CHECKING OPENAI API STATUS")
    print("=" * 70)
    print()
    
    if not OPENAI_API_KEY:
        print("⚠️  OPENAI_API_KEY not set in environment")
        print()
        print("📋 TO SET API KEY:")
        print("   1. Get your API key from: https://platform.openai.com/api-keys")
        print("   2. Set environment variable:")
        print("      export OPENAI_API_KEY='your-api-key-here'")
        print("   3. Or add to ~/.zshrc:")
        print("      echo 'export OPENAI_API_KEY=\"your-api-key-here\"' >> ~/.zshrc")
        print("      source ~/.zshrc")
        print()
        return False
    
    print(f"✅ API Key found (starts with: {OPENAI_API_KEY[:7]}...)")
    print()
    
    # Test API with a simple request
    print("🧪 TESTING API CONNECTION...")
    print("-" * 70)
    
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    # Test with a simple chat completion
    test_payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Say 'API test successful' if you can read this."}
        ],
        "max_tokens": 10
    }
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=test_payload,
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ API Connection: SUCCESS")
            data = response.json()
            print(f"   Response: {data.get('choices', [{}])[0].get('message', {}).get('content', 'N/A')}")
            print()
            
            # Check usage (if available in response)
            if 'usage' in data:
                usage = data['usage']
                print("📊 USAGE FOR THIS REQUEST:")
                print(f"   Prompt tokens: {usage.get('prompt_tokens', 0)}")
                print(f"   Completion tokens: {usage.get('completion_tokens', 0)}")
                print(f"   Total tokens: {usage.get('total_tokens', 0)}")
                print()
            
            return True
            
        elif response.status_code == 401:
            print("❌ API Connection: FAILED")
            print("   Error: Invalid API key")
            print("   Check your API key at: https://platform.openai.com/api-keys")
            return False
            
        elif response.status_code == 429:
            print("⚠️  API Connection: RATE LIMITED")
            print("   Error: Too many requests")
            print("   You may have hit rate limits or need to upgrade plan")
            return False
            
        elif response.status_code == 402:
            print("❌ API Connection: PAYMENT REQUIRED")
            print("   Error: No credits or payment method required")
            print("   Add payment method at: https://platform.openai.com/account/billing")
            return False
            
        else:
            print(f"❌ API Connection: FAILED")
            print(f"   Status Code: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API Connection: ERROR")
        print(f"   Error: {str(e)}")
        print("   Check your internet connection")
        return False

def _utc_midnight_bounds(dt: datetime) -> tuple[int, int]:
    """Return (start_time, end_time) unix seconds for dt's UTC day."""
    utc_dt = dt.astimezone(timezone.utc)
    start = utc_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=1)
    return int(start.timestamp()), int(end.timestamp())

def get_today_spend_usd() -> tuple[bool, float, str]:
    """
    Fetch today's spend in USD using OpenAI Costs API.

    Uses:
      GET /v1/organization/costs?start_time=...&end_time=...&interval=1d
    """
    if not OPENAI_API_KEY:
        return False, 0.0, "OPENAI_API_KEY not set"

    start_time, end_time = _utc_midnight_bounds(datetime.now(timezone.utc))
    url = f"{OPENAI_API_BASE}/organization/costs"
    params = {
        "start_time": start_time,
        "end_time": end_time,
        "interval": "1d",
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=15)
        if resp.status_code == 401:
            return False, 0.0, "Unauthorized (invalid OpenAI API key)"
        resp.raise_for_status()
        data = resp.json()

        # Defensive parsing: accept a few potential shapes.
        total = 0.0
        if isinstance(data, dict):
            # Most likely: data["data"] is a list of buckets / line items.
            items = data.get("data")
            if isinstance(items, list):
                for item in items:
                    if not isinstance(item, dict):
                        continue
                    # Some responses include total_amount or amount fields.
                    for key in ("total_amount", "amount", "cost", "value"):
                        v = item.get(key)
                        if isinstance(v, (int, float)):
                            total += float(v)
                            break
                    # Or nested "total" dict
                    t = item.get("total")
                    if isinstance(t, dict):
                        v = t.get("amount")
                        if isinstance(v, (int, float)):
                            total += float(v)
            # Some responses include "total" at top-level.
            top_total = data.get("total")
            if isinstance(top_total, (int, float)):
                total = float(top_total)

        return True, float(total), "OK"
    except Exception as e:
        return False, 0.0, f"Costs API unavailable: {e}"

def check_usage():
    """Check OpenAI usage and billing (if API supports it)."""
    print("📊 CHECKING USAGE & BILLING...")
    print("-" * 70)
    print()
    print("ℹ️  To check credits and usage:")
    print("   1. Go to: https://platform.openai.com/usage")
    print("   2. Check your billing: https://platform.openai.com/account/billing")
    print("   3. View API keys: https://platform.openai.com/api-keys")
    print()
    print("💡 TIPS:")
    print("   • Free tier: Limited credits")
    print("   • Paid tier: Pay-as-you-go")
    print("   • Check usage dashboard for detailed stats")
    print()

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Check OpenAI API status and daily spend guardrails")
    parser.add_argument("--warn", type=float, default=float(os.getenv("OPENAI_DAILY_WARN_USD", "3")), help="Warn threshold in USD (default: 3)")
    parser.add_argument("--cap", type=float, default=float(os.getenv("OPENAI_DAILY_CAP_USD", "5")), help="Cap threshold in USD (default: 5)")
    parser.add_argument("--spend-only", action="store_true", help="Only check spend (skip chat completion test)")
    args = parser.parse_args()

    success = False
    if not args.spend_only:
        success = check_openai_api()

    ok, spend, msg = get_today_spend_usd()
    print("💸 TODAY'S SPEND (USD)")
    print("-" * 70)
    if ok:
        print(f"   Today: ${spend:.2f}")
        print(f"   Warn:  ${args.warn:.2f}")
        print(f"   Cap:   ${args.cap:.2f}")
    else:
        print(f"   Could not fetch spend: {msg}")
        print("   Fallback: use https://platform.openai.com/usage to verify spend.")
    print()

    # Print static links as fallback/help
    check_usage()
    
    print("=" * 70)
    exit_code = 0
    if ok and spend >= args.cap:
        print("🛑 Daily spend CAP exceeded")
        exit_code = 20
    elif ok and spend >= args.warn:
        print("⚠️  Daily spend WARN threshold exceeded")
        exit_code = 10

    if args.spend_only:
        # Spend-only mode: success means spend endpoint returned.
        if ok:
            print("✅ Spend check completed")
        else:
            print("⚠️  Spend check could not be completed (missing key or API not available)")
            # Keep exit code 0 so monitoring dashboards don't fail hard.
    else:
        if success:
            print("✅ OpenAI API is working!")
            print("   Your API key is valid and can make requests")
        else:
            print("❌ OpenAI API check failed")
            print("   Fix the issues above before using in n8n")
    print()
    
    return exit_code if success else 1

if __name__ == '__main__':
    sys.exit(main())


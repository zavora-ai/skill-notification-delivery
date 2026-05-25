#!/usr/bin/env python3
"""Check user notification preferences and determine best channel."""
import json, sys

PRIORITY_CHANNELS = {
    "critical": ["push", "sms", "email"],
    "high": ["push", "email"],
    "normal": ["email", "in_app"],
    "low": ["in_app"],
}

def best_channel(data):
    prefs = data.get("preferences", {})
    priority = data.get("priority", "normal")
    channels = PRIORITY_CHANNELS.get(priority, ["email"])
    
    for channel in channels:
        if prefs.get(channel, True):  # default to allowed
            return {"channel": channel, "priority": priority, "reason": f"User allows {channel}, highest priority channel for {priority}"}
    
    return {"channel": "in_app", "priority": priority, "reason": "All preferred channels disabled, falling back to in_app"}

if __name__ == "__main__":
    print(json.dumps(best_channel(json.loads(sys.argv[1])), indent=2))

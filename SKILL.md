---
name: notification-delivery
description: Deliver notifications via push, SMS, email, in-app, and webhooks — manage templates, schedule delivery, track status, and respect user preferences. Use when sending notifications, managing templates, checking delivery status, scheduling alerts, or configuring preferences.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [send_notification, send_from_template, broadcast, schedule_notification, list_notifications, get_status, retry_notification, list_templates, get_template, create_template, get_preferences, update_preferences, get_delivery_stats]
tags: [communication, notifications, push, sms, alerts]
metadata:
  author: Zavora AI
  mcp-server: mcp-notifications
---

# Notification Delivery

Multi-channel notifications with preference respect. Always check user preferences before sending. Never overwhelm recipients.

## Decision Tree
```
├── "notify", "alert", "send push"? → send_notification / send_from_template
├── "broadcast", "announce to all"? → broadcast (requires approval for large audiences)
├── "schedule", "send later"? → schedule_notification
├── "status", "delivered?"? → get_status / get_delivery_stats
├── "template", "create template"? → list_templates / create_template
├── "preferences", "opt out"? → get_preferences / update_preferences
├── "retry", "resend"? → retry_notification
```

## MUST DO
- Check user preferences before sending (respect opt-outs)
- Rate limit — don't send more than 3 notifications/hour to same user
- Use templates for consistency
- Include unsubscribe mechanism on marketing notifications

## MUST NOT DO
- Don't bypass opt-outs
- Don't use "critical" priority for non-critical content
- Don't broadcast without explicit approval

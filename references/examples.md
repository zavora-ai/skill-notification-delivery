# Notification Examples

## Example 1: "Alert the on-call engineer"
```
send_notification(recipient: "oncall", channel: "push", title: "🚨 P1 Incident", body: "INC-1001: DB outage", priority: "critical")
```

## Example 2: "Schedule a reminder for tomorrow"
```
schedule_notification(recipient: "usr_123", channel: "push", title: "📋 Sprint Review", body: "Sprint review in 1 hour", deliver_at: "2025-01-20T09:00:00Z")
```

## Example 3: "Check if the alert was delivered"
```
get_status(notification_id: "ntf_456") → {status: "delivered", channel: "push", read: true}
```

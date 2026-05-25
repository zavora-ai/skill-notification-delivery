# Notification Cross-MCP Workflows

## Notifications + ITSM: Incident Alerts
```
ITSM: create_ticket(priority: "critical") → {id: "INC-1001"}
NOTIFICATIONS: send_notification(recipient: oncall, channel: "push", title: "🚨 P1: INC-1001", priority: "critical")
```

## Notifications + Payments: Approval Needed
```
PAYMENTS: request_payment_approval(id: "pi_big") → pending
NOTIFICATIONS: send_notification(recipient: finance_mgr, channel: "push", title: "💰 Payment approval: $5,000", body: "Tap to review")
```

## Notifications + Identity: MFA Reminder
```
IDENTITY: check_mfa(user_id) → {enrolled: false, deadline: "overdue"}
NOTIFICATIONS: send_notification(recipient: user, channel: "push", title: "⚠️ MFA Required", body: "Enroll now or access will be restricted")
```

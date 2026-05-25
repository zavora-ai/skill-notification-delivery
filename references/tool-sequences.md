# Notification Tool Sequences

## Tools (13)
| Tool | Purpose |
|------|---------|
| `send_notification` | Send to specific user/channel |
| `send_from_template` | Send using pre-built template |
| `broadcast` | Send to multiple recipients |
| `schedule_notification` | Future delivery |
| `list_notifications` | Sent notifications |
| `get_status` | Delivery status |
| `retry_notification` | Retry failed delivery |
| `list_templates` | Available templates |
| `get_template` | Template details |
| `create_template` | Create new template |
| `get_preferences` | User channel preferences |
| `update_preferences` | Update preferences |
| `get_delivery_stats` | Delivery analytics |

## Sequence: Send with Preference Check (2 calls)
```
1. get_preferences(user_id: "usr_123") → {push: true, sms: false, email: true}
2. send_notification(user_id: "usr_123", channel: "push", title: "...", body: "...")
```

## Sequence: Broadcast from Template (2 calls)
```
1. list_templates(category: "incident") → [{id: "tpl_p1", name: "P1 Alert"}]
2. broadcast(template_id: "tpl_p1", recipients: ["team_oncall"], variables: {ticket: "INC-1001"})
```

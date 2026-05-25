# Notification Delivery Skill

> Multi-channel notifications for AI agents — push, SMS, email, in-app with templates, scheduling, preference respect, and delivery tracking via mcp-notifications.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--notifications-green)](https://github.com/zavora-ai/mcp-notifications)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Send (preference-aware) | 2 | Check prefs → deliver via best channel |
| Broadcast | 2 | Template → multiple recipients |
| Schedule | 1 | Future delivery |
| Track | 1 | Delivery confirmation |

### Without this skill:
- Notifications sent to opted-out channels
- No rate limiting (users overwhelmed)
- Critical alerts sent via low-priority channels
- No delivery confirmation

### With this skill:
- User preferences checked before every send
- Rate limited (max 3/hour to same user)
- Priority-based channel selection (critical → push+SMS)
- Delivery tracked with retry on failure

## Installation

```bash
git clone https://github.com/zavora-ai/skill-notification-delivery.git \
  ~/.skills/skills/notification-delivery
```

## Requirements

**Required:** `mcp-notifications` (13 tools)

**Cross-MCP:**
- `mcp-itsm` — incident alerts to on-call
- `mcp-payments` — approval notifications to finance
- `mcp-identity` — MFA enrollment reminders

## Folder Structure

```
notification-delivery/
├── SKILL.md                       # Decision tree + preference rules
├── scripts/
│   └── check_preferences.py       # Best channel selector by priority
├── references/
│   ├── tool-sequences.md          # 13 tools
│   ├── cross-mcp-workflows.md     # Notifications + ITSM + Payments + Identity
│   └── examples.md                # Alert, schedule, check delivery
├── README.md
└── LICENSE
```

## Example

**User:** "Alert the on-call engineer about the P1 incident"

**Agent behavior:**
1. Checks preferences: on-call allows push + SMS
2. Sends via push (highest priority channel for critical)

**Result:** `🚨 P1 Incident: INC-1001 — DB outage. Acknowledge within 5 min.`

## Scripts

### `check_preferences.py`
```bash
python scripts/check_preferences.py '{"preferences": {"push": true, "sms": false}, "priority": "critical"}'
# → {"channel": "push", "reason": "User allows push, highest priority for critical"}
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Preference respect | 100% — never send to opted-out channels |
| Rate limiting | Max 3 notifications/hour per user |
| Critical delivery | Push + SMS for critical priority |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

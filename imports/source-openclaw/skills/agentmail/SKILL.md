---
name: agentmail
description: Send and receive emails via AgentMail API. Use when the user wants to send an email, check their inbox, or manage email communications. Provides tools for creating inboxes, sending emails, and reading received messages.
---

# AgentMail Skill

Email capabilities for Vesper using AgentMail API.

## Capabilities

- **Create inbox**: Get a dedicated email address
- **Send emails**: Send to any email address
- **Check inbox**: Read received messages
- **Get message**: Read specific message details

## Configuration

The API key is stored in `TOOLS.md` under `AgentMail > API Key`.

## Usage

Use the HTTP-based script (no npm dependencies required):

### Check inbox
```
cmd /c "cd C:\Users\gatom\.openclaw\workspace && node agentmail-http.js check [limit]"
```

### Send an email
```
cmd /c "cd C:\Users\gatom\.openclaw\workspace && node agentmail-http.js send <to> <subject> <text>"
```

### List inboxes
```
cmd /c "cd C:\Users\gatom\.openclaw\workspace && node agentmail-http.js list"
```

## Current Inbox

- **Email**: `vesper_mayo@agentmail.to`
- **Owner**: Mayo (vmena01@gmail.com)

## Examples

**Check inbox:**
```
User: "Check my emails" or "Do I have new messages?"
→ Run: cmd /c "cd C:\Users\gatom\.openclaw\workspace && node agentmail-http.js check"
```

**Send email:**
```
User: "Send email to test@example.com with subject Hello"
→ Run: cmd /c "cd C:\Users\gatom\.openclaw\workspace && node agentmail-http.js send test@example.com Hello \"Message body here\""
```

## Technical Notes

- Uses native `fetch` - no npm dependencies
- Works from any session (webchat, WhatsApp, etc.)
- API endpoint: `https://api.agentmail.to`
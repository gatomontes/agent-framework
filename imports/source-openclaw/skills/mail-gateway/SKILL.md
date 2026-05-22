---
name: mail-gateway
description: Send and receive emails via Mail Gateway API. Use when the user wants to send an email, check their inbox, or manage email communications. Provides tools for creating inboxes, sending emails, and reading received messages.
---

# Mail Gateway Skill

Email capabilities for Vesper using Mail Gateway API.

## Capabilities

- **Create inbox**: Get a dedicated email address
- **Send emails**: Send to any email address
- **Check inbox**: Read received messages
- **Get message**: Read specific message details

## Configuration

The API key is stored in `TOOLS.md` under `Mail Gateway > API Key`.

## Usage

Use the HTTP-based script (no npm dependencies required):

### Check inbox
```
cmd /c "cd C:\Users\gatom\.openclaw\workspace && node mail-gateway-http.js check [limit]"
```

### Send an email
```
cmd /c "cd C:\Users\gatom\.openclaw\workspace && node mail-gateway-http.js send <to> <subject> <text>"
```

### List inboxes
```
cmd /c "cd C:\Users\gatom\.openclaw\workspace && node mail-gateway-http.js list"
```

## Current Inbox

- **Email**: `vesper_mayo@mail-gateway.to`
- **Owner**: Mayo (vmena01@gmail.com)

## Examples

**Check inbox:**
```
User: "Check my emails" or "Do I have new messages?"
→ Run: cmd /c "cd C:\Users\gatom\.openclaw\workspace && node mail-gateway-http.js check"
```

**Send email:**
```
User: "Send email to test@example.com with subject Hello"
→ Run: cmd /c "cd C:\Users\gatom\.openclaw\workspace && node mail-gateway-http.js send test@example.com Hello \"Message body here\""
```

## Technical Notes

- Uses native `fetch` - no npm dependencies
- Works from any session (webchat, WhatsApp, etc.)
- API endpoint: `https://api.mail-gateway.to`

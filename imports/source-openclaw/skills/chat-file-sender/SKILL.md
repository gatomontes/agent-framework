---
name: chat-file-sender
description: Prepare and send local files or documents to a Chat Gateway chat through the configured bot. Use when the user asks to send a file, note, image, archive, or document to Chat Gateway, especially when the file may need temporary staging or size handling before delivery.
---

# Chat File Sender

Prepare a local file for Chat Gateway delivery, then send it as a document through the configured Chat Gateway bot.

## What this skill is for

Use this skill when the user wants a file delivered to Chat Gateway and you have:
- a local source path
- a target Chat Gateway chat ID
- an optional caption

## Core workflow

1. Resolve the source file path.
2. Run the helper script to stage the file safely for sending.
3. Read the helper output.
4. Send the staged file with the Chat Gateway send path that accepts file attachments.
5. Clean up the staged workspace outbox file after successful delivery when appropriate.

## Required inputs

- `source_path`: local file path
- `target_chat_id`: numeric Chat Gateway chat ID
- `caption`: optional

If the target chat ID is unknown, ask for it or derive it from a confirmed Chat Gateway interaction.

## Helper script

Run:

```bash
python3 skills/chat-file-sender/scripts/send_file.py "<source_path>" "<target_chat_id>" [caption]
```

The script prints key-value lines. Parse:
- `SEND_PATH`
- `SEND_FILENAME`
- `TARGET`
- `CAPTION`
- `READY`

Proceed only if `READY` appears.

## Delivery rules

- Send the file as a Chat Gateway document.
- Use the staged absolute file path from `SEND_PATH`.
- Preserve the caption if provided.
- After confirmed delivery, remove the staged temp file and temp directory.

## Size handling

- Files at or below Chat Gateway's practical document limit are staged as-is.
- Oversized files are zipped automatically.
- If the zipped result is still too large, fail clearly and tell the user the file needs splitting or another delivery method.

## Safety

- Never invent Chat Gateway chat IDs.
- Never claim a file was sent unless Chat Gateway confirms delivery.
- Stage files in a workspace outbox location before sending.
- Clean up staged outbox files after successful send when appropriate.


---
name: nomina-db-backup
description: Create a timestamped, restore-ready backup of the Nomina PostgreSQL database before risky local operations such as fixtures loading, destructive resets, schema experiments, data cleanup, or restore testing. Use when working in the `E:\htdocs\nomina` project and a restorable database checkpoint is needed.
---

# Nomina DB Backup

Run the project backup script at `E:\htdocs\nomina\codex\backups\backup-db.ps1`.

## Workflow

1. Confirm the current workspace is `E:\htdocs\nomina` or that the user explicitly wants the Nomina database backed up.
2. Run:

```powershell
powershell -ExecutionPolicy Bypass -File E:\htdocs\nomina\codex\backups\backup-db.ps1
```

3. Report the created dump path, file size, and timestamp.
4. If the user is about to run something destructive, mention the exact backup file that can be restored later.

## Notes

- The script writes custom-format PostgreSQL dumps to `E:\htdocs\nomina\codex\backups\db`.
- Prefer creating a fresh backup immediately before fixture loads, restore tests, migration experiments, or bulk data edits.
- Do not delete older backups unless the user asks.

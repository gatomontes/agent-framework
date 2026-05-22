---
name: nomina-db-restore
description: Restore the Nomina PostgreSQL database from a chosen backup dump after fixture loads, failed experiments, bad local data changes, or when the user wants to roll back to a known checkpoint. Use when working in the `E:\htdocs\nomina` project and a dump from `codex\backups\db` should be restored.
---

# Nomina DB Restore

Run the project restore script at `E:\htdocs\nomina\codex\backups\restore-db.ps1`.

## Workflow

1. Confirm which dump file should be restored.
2. Prefer showing the most recent files under `E:\htdocs\nomina\codex\backups\db` if the user has not named one yet.
3. For a normal restore, run:

```powershell
powershell -ExecutionPolicy Bypass -File E:\htdocs\nomina\codex\backups\restore-db.ps1 -BackupFile <full-path-to-dump>
```

4. If the user wants a full reset first, run:

```powershell
powershell -ExecutionPolicy Bypass -File E:\htdocs\nomina\codex\backups\restore-db.ps1 -BackupFile <full-path-to-dump> -RecreateDatabase
```

5. Report which dump was restored and whether `-RecreateDatabase` was used.

## Notes

- The restore targets the local Nomina PostgreSQL database configured by the project scripts.
- Treat restore as destructive to the current local database contents.
- Do not choose a backup arbitrarily when multiple restore points exist; confirm or present the latest options.

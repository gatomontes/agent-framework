---
name: vps-connect
description: Connect to and manage the VPS server (pulga-test, 45.61.50.129:2222) via Bitvise SSH Client sexec. Use when the user asks to install software, run commands, transfer files, check server status, or manage services on their VPS. Supports password-based auth, command execution, and SFTP file operations.
---

# VPS Connect

## Connection Details

- **Host:** 45.61.50.129
- **Port:** 2222
- **User:** boss
- **Password:** `@ssh0l3`
- **Sudo:** NOPASSWD (no password required for sudo commands)
- **Hostname:** pulga-test
- **Tool:** `C:\Program Files (x86)\Bitvise SSH Client\sexec.exe`

## Usage

### Run commands on VPS

Use `sexec` with the stored credentials:

```powershell
& 'C:\Program Files (x86)\Bitvise SSH Client\sexec.exe' `
  -host="45.61.50.129" -port=2222 -user=boss -pw='$EsteBicho#55' `
  -cmd="command here"
```

**Important:** Use single quotes `'...'` around the password in PowerShell to prevent `$` from being interpreted as a variable.

### SFTP file transfer

Use `sftpc` for file uploads/downloads:

```powershell
& 'C:\Program Files (x86)\Bitvise SSH Client\sftpc.exe' `
  -host="45.61.50.129" -port=2222 -user=boss -pw='$EsteBicho#55' `
  -cmd="put local-file remote-path"
```

### Interactive terminal

Use `stermc` for interactive sessions:

```powershell
& 'C:\Program Files (x86)\Bitvise SSH Client\stermc.exe' `
  -host="45.61.50.129" -port=2222 -user=boss -pw='$EsteBicho#55'
```

## Common Operations

### Check server status
```powershell
  -cmd="hostname && uptime && free -h && df -h /"
```

### Install packages
```powershell
  -cmd="apt update && apt install -y <package>"
```

### Service management
```powershell
  -cmd="systemctl status <service>"
  -cmd="systemctl start|stop|restart <service>"
```

## References

- **Bitvise sexec docs:** Parameter reference and return codes
- **Scripts:** `scripts/` for reusable connection utilities

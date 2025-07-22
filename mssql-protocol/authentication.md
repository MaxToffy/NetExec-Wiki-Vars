# Authentication

## Testing credentials

You can use two methods to authenticate to MSSQL: `windows` or `local` (default: `windows`). To use local auth, add the following flag `--local-auth`

### **Windows auth**

1. With SMB port open

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD
```

1. With SMB port close, add the flag `-d DOMAIN`

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD -d $DOMAIN
```

Expected Results:

```bash
MSSQL       10.10.10.52     1433   MANTIS           [+] HTB\james:J@m3s_P@ssW0rd! 
```

### **Local auth**

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD --local-auth
```

Expected Results:

```bash
MSSQL       10.10.10.52     1433   None             [+] admin:m$$ql_S@_P@ssW0rd! (Pwn3d!)
```

### Specify Ports

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD --port 1434
```

# Authentication

## Testing credentials

You can use two methods to authenticate to the WMI: `windows` or `local` (default: `windows`). To use local auth, add the following flag `--local-auth`

### **Windows auth**

- With SMB port open

```bash
nxc wmi $TARGET -u $USER -p $PASSWORD
```

- With SMB port close, add the flag `-d DOMAIN`

```bash
nxc wmi $TARGET -u $USER -p $PASSWORD -d $DOMAIN
```

Expected Results:

```bash
WMI       10.10.10.52     1433   MANTIS           [+] HTB\james:J@m3s_P@ssW0rd! 
```

### **Local auth**

```bash
nxc wmi $TARGET -u $USER -p $PASSWORD --local-auth
```

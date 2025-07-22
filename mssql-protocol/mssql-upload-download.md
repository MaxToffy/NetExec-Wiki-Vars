# MSSQL upload/download

### Download / Upload MSSQL file

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD --put-file /tmp/users C:\\Windows\\Temp\\whoami.txt
```

Expected Results:

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD --put-file /tmp/users C:\\Windows\\Temp\\whoami.txt
MSSQL       192.168.212.134 1433   DC01             [*] Windows 10.0 Build 20348 (name:DC01) (domain:poudlard.wizard)
MSSQL       192.168.212.134 1433   DC01             [+] poudlard.wizard\administrator:October2022 (Pwn3d!)
MSSQL       192.168.212.134 1433   DC01             [*] Copy /tmp/users to C:\Windows\Temp\whoami.txt
MSSQL       192.168.212.134 1433   DC01             [*] Size is 23 bytes
MSSQL       192.168.212.134 1433   DC01             [+] File has been uploaded on the remote machine
```

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD --get-file C:\\Windows\\Temp\\whoami.txt /tmp/file
```

Expected Results:

```bash
nxc mssql $TARGET -u $USER -p $PASSWORD --get-file C:\\Windows\\Temp\\whoami.txt /tmp/users-t
MSSQL       192.168.212.134 1433   DC01             [*] Windows 10.0 Build 20348 (name:DC01) (domain:poudlard.wizard)
MSSQL       192.168.212.134 1433   DC01             [+] poudlard.wizard\administrator:October2022 (Pwn3d!)
MSSQL       192.168.212.134 1433   DC01             [*] Copy C:\Windows\Temp\whoami.txt to /tmp/users-t
MSSQL       192.168.212.134 1433   DC01             [+] File C:\Windows\Temp\whoami.txt was transferred to /tmp/users-t
```

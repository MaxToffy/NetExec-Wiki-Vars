# Enumerate Domain Users

Enumerate domain users on the remote target

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --users
```

Export domain users on the remote target

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --users-export output.txt
```

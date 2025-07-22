# Enumerate Users by Bruteforcing RID

Enumerate users by bruteforcing the RID on the remote target

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --rid-brute
```
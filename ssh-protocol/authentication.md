# Authentication

#### Testing credentials

```bash
nxc ssh $TARGET/24 -u $USER -p $PASSWORD
```

Expected Results:

```bash
SSH         127.0.0.1       22     127.0.0.1        [*] SSH-2.0-OpenSSH_8.2p1 Debian-4
SSH         127.0.0.1       22     127.0.0.1        [+] user:password
```

#### Specify Ports

```bash
nxc ssh $TARGET/24 --port 2222
```

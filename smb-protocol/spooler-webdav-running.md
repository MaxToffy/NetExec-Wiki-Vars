# Checking for Spooler & WebDav

### Checking if the Spooler Service is Running

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M spooler
```

### Checking if the WebDav Service is Running

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M webdav
```

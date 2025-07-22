# Enumerate Shares and Access

Enumerate permissions on all shares

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --shares
```

{% hint style="info" %}
By far one of the most useful feature of nxc
{% endhint %}

If you want to filter only by readable or writable share

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --shares READ,WRITE
nxc smb $TARGET/24 -u $USER -p $PASSWORD --shares READ
nxc smb $TARGET/24 -u $USER -p $PASSWORD --shares WRITE
```

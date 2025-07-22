---
description: Dump private Keys stored for authentication or stored proxy credentials
---

# 🆕 Dump PuTTY

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

PuTTY allows users to store private keys for connections. It also allows per-connection proxy credentials to be set in the configuration, which are then stored in clear text in the registry. This module will automatically look for these attributes in the PuTTY registry path and extract them if found.

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M putty
```

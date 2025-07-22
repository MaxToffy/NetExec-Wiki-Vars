---
description: NetExec vs LAPS
---

# Defeating LAPS

### Using NetExec When LAPS Installed on the Domain

If LAPS is used inside the domain, it can be hard to use NetExec to execute a command on every computer on the domain.

Therefore, a new core option has been added `--laps`! If you have compromised an account that can read LAPS password, you can use NetExec like this

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --laps
```

{% hint style="info" %}
If the default administrator name is not `administrator` add the user after the option

`--laps name`
{% endhint %}

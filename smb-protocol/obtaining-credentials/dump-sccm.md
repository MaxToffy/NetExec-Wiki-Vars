# 🆕 Dump SCCM

### Dump the SCCM from target using methods from dploot

{% hint style="danger" %}
Requires Domain Admin or Local Admin Priviledges on target Domain Controller
{% endhint %}

```bash
2 methods are available:   
(default) 	wmi -  TODO
			disk - TODO (default)
```

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --sccm
nxc smb $TARGET -u $USER -p $PASSWORD --sccm disk
nxc smb $TARGET -u $USER -p $PASSWORD --sccm wmi
```

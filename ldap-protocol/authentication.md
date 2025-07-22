# Authentication

### LDAP Authentication

Testing if an account exists without kerberos protocol

```bash
nxc ldap $TARGET/24 -u $USER -p $PASSWORD -k
```

#### Testing credentials

```bash
nxc ldap $TARGET/24 -u $USER -p $PASSWORD
```

```bash
nxc ldap $TARGET/24 -u $USER -H $NT_HASH
```

Expected Results:

```bash
LDAP        192.168.255.131 5985   ROGER            [+] GOLD\user:password
```

{% hint style="warning" %}
Domain name resolution is expected
{% endhint %}

By default, the ldap protocol will get the domain name by making connection to the SMB share (of the dc), if you don't want that initial connection, just add the option `--no-smb`

# Enumerate Domain Groups

Enumerate all groups in the Domain:

```bash
nxc ldap $TARGET -u $USER -p $PASSWORD --groups
```

To enumerate all members in specific group via LDAP:

```bash
nxc ldap $TARGET -u $USER -p $PASSWORD --groups "Domain Admins"
```

---
description: An alternative to ldapsearch
---

# 🆕 Query LDAP

If you need to query raw ldap values you can use the query option together with filters. The returned values are not parsed in any way and should return the exact same output as ldapsearch or similar tools.

```bash
nxc ldap $TARGET -u $USER -p $PASSWORD --query "(sAMAccountName=Administrator)" ""
nxc ldap $TARGET -u $USER -p $PASSWORD --query "(sAMAccountName=Administrator)" "sAMAccountName objectClass pwdLastSet"
```

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption><p>Querying ldap with NetExec</p></figcaption></figure>

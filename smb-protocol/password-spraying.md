---
description: Using NetExec for password spraying
---

# Password Spraying

### Using Username/Password Lists

You can use multiple usernames or passwords by separating the names/passwords with a space.

```bash
nxc smb $TARGET -u $USER user2 user3 -p $PASSWORD
nxc smb $TARGET -u $USER -p $PASSWORD password2 password3
```

nxc accepts txt files of usernames and passwords. One user/password per line. Watch out for account lockout!

```bash
nxc smb $TARGET -u $USER -p $PASSWORD
nxc smb $TARGET -u $USER -p $PASSWORD
```

{% hint style="warning" %}
By default nxc will exit after a successful login is found. Using the **--continue-on-success** flag, it will continue spraying even after a valid password is found. Useful for spraying a single password against a large user list. This is incompatible with command execution.&#x20;
{% endhint %}

Usage example:

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --continue-on-success
```

### Checking 'username == password' using wordlist

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --no-bruteforce --continue-on-success
```

### Checking multiple usernames/passwords using wordlist

```bash
nxc smb $TARGET -u $USER -p $PASSWORD
```

The result will be:

* user1 => password1
* user1 => password2
* user2 => password1
* user2 => password2

{% hint style="danger" %}
Be careful to not lock accounts using this technique
{% endhint %}

### Checking one login equal one password using wordlist

{% hint style="success" %}
No bruteforce possible with this one as 1 user = 1 password
{% endhint %}

```bash
nxc smb $TARGET -u $USER -p $PASSWORD --no-bruteforce --continue-on-success
```

The result will be:

* user1 => password1
* user2 => password2

{% hint style="danger" %}
Avoid range or a list of IPs when using the `--no-bruteforce` option
{% endhint %}

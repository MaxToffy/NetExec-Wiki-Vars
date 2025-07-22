# Password spraying

### Password spraying

```bash
nxc wmi $TARGET/24 -u $USERFILE -p $PASSFILE
```

By default, nxc will exit after a successful login is found.

### Password spraying (without bruteforce)

```bash
nxc wmi $TARGET/24 -u $USERFILE -p $PASSFILE --no-bruteforce
```

By default, nxc will exit after a successful login is found. Using the `--continue-on-success` flag will continue spraying even after a valid password is found. Useful for spraying a single password against a large user list.

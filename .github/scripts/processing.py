import os
import re

ordered_replacements = [
    # 1. $TARGET/24
    (r"(^nxc (smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql|nfs) ).*?/24( |$|.*)", r"\1$TARGET/24\3"),
    # 2. $TARGET
    (r"(^nxc (smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql|nfs) )[^/]*?( |$)", r"\1$TARGET\3"),
    # 3. $USERFILE
    (r"(^nxc .*? -u )userfile(.*)", r"\1$USERFILE\2"),
    # 4. $USER
    (r"(^nxc .*? -u )[^$].*?( |$)", r"\1$USER\2"),
    # 5. $PASSFILE
    (r"(^nxc .*? -p )passwordfile(.*)", r"\1$PASSFILE\2"),
    # 6. $PASSWORD
    (r"(^nxc .*? -p )[^$].*?( |$)", r"\1$PASSWORD\2"),
    # 7. $DOMAIN
    (r"(^nxc .*? -d ).*?( |$)", r"\1$DOMAIN\2"),
    # 8. $LM_HASH:$NT_HASH
    (r"(^nxc .*? -H )[^ ]*?:[^ ]*?( |$)", r"\1$LM_HASH:$NT_HASH\2"),
    # 9. $NT_HASH
    (r"(^nxc .*? -H )[^: ]*?( |$)", r"\1$NT_HASH\2"),
    # 10. $ATTACKER_IP
    (r"<AttackerIP>", r"$ATTACKER_IP"),
]

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    for pattern, repl in ordered_replacements:
        content = re.sub(pattern, repl, content, flags=re.MULTILINE)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    for root, dirs, files in os.walk("."):
        if root.endswith("-protocol") or any(part.endswith("-protocol") for part in root.split(os.sep)):
            for file in files:
                filepath = os.path.join(root, file)
                process_file(filepath)
                print(f"Processed: {filepath}")

if __name__ == "__main__":
    main()

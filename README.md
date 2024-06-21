
# Hosts File Management Scripts Documentation

## Overview

This documentation provides detailed information on the PowerShell and Bash scripts designed to update the hosts file on Windows and macOS/Linux systems respectively. These scripts download a compressed hosts file from a specified URL and insert the new entries between designated tags in the system's hosts file.

The hosts file is pulled from a company repository: [GitHub Repository](https://github.com/lucaborruto/Hosts_file/), which sources its original data from the phishing list on [The Block List Project](https://blocklistproject.github.io/Lists/).

The source hosts file *(from The Block List Project)* has been reviewed and approved, and future versions will be reviewed by the security team.

The file has been compressed for better handling on Windows systems using a PowerShell script.

---

## Hosts File Information

The hosts file maps hostnames (e.g., `google.com`) to IP addresses (e.g., `0.0.0.0` or `127.0.0.1`). Using a custom hosts file can slow down DNS caching on Windows systems due to its size. To mitigate this, hostnames can be compressed into single lines, with a maximum of 9 hostnames per line, to improve performance:

```bash
0.0.0.0 fakename1.url fakename2.url fakename3.url fakename4.url fakename5.url fakename6.url fakename7.url fakename8.url fakename9.url
```

---

## Script Explanation

The script updates the Windows/MacOS hosts file by adding new entries from a specified URL. Below is a block-by-block explanation of what the script does:

1. **Define Hosts File Path**
    - Specifies the path to the hosts file on the Windows system:
        - Windows: `C:\Windows\System32\drivers\etc\hosts`
        - MacOS: `/etc/hosts`
2. **Define URL for New Entries**
    - Specifies the URL from which the new hosts entries file will be downloaded:
        `https://raw.githubusercontent.com/lucaborruto/Hosts_file/main/phishing_compressed.txt`
3. **Download New Entries**
    - Downloads the new entries from the specified URL using `Invoke-RestMethod` for Windows, `curl` for MacOS and stores them in a variable.
4. **Define Tags**
    - Sets start and end tags to mark the managed zone within the hosts file:
        `########## START_MANAGED_ZONE # AGICAP # DO NOT WRITE OR MODIFY ##########` & `########## END_MANAGED_ZONE # AGICAP # DO NOT WRITE OR MODIFY ##########`
5. **Read Current Hosts File**
    - Reads the existing content of the hosts file into a variable.
6. **Check and Add Tags**
    - Checks if the start and end tags are already present in the hosts file. If not, it adds these tags to the end of the file and writes the updated content back to the hosts file.
7. **Prepare New Hosts Content**
    - Iterates through the current hosts file content:
        - When it finds the start tag, it begins adding the new entries.
        - Continues adding the new entries until it encounters the end tag.
        - Ensures that content outside these tags remains unchanged.
8. **Write Updated Hosts File**
    - Writes the modified content, including the new entries between the specified tags, back to the hosts file using ASCII encoding.

---

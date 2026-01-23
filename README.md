
# Documentation

## Overview

The source hosts file is the phishing list from [StevenBlack/hosts](https://github.com/StevenBlack/hosts).

The file has been compressed for better handling on Windows systems using a Python script.

---

## Hosts File Information

Using a custom hosts file can slow down DNS caching on Windows systems due to its size. To mitigate this, hostnames can be compressed into single lines, with a maximum of 9 hostnames per line, to improve performance:

```bash
0.0.0.0 fakename1.url fakename2.url fakename3.url fakename4.url fakename5.url fakename6.url fakename7.url fakename8.url fakename9.url
```

## compress.py - Hosts Grouping Script

This repository includes a small helper script `compress.py` that reads a hosts-style file of blocked domains (by default `phishing.txt`) and writes a compressed version (`phishing_compressed.txt`) where multiple domains are grouped onto a single line to improve hosts-file handling performance.

- **Purpose:** Group up to `group_size` hostnames per line and emit lines prefixed with `0.0.0.0`.
- **Default files:** input `phishing.txt`, output `phishing_compressed.txt`.
- **Default group size:** `9` hostnames per line.

How it works:

- Skips empty lines and lines starting with `#`.
- Accepts input entries that start with either `0.0.0.0` or `127.0.0.1` and extracts the hostname from the second field.
- Writes lines in the form:

```bash
0.0.0.0 example1.com example2.com example3.com ...
```

---

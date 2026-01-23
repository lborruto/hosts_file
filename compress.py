def group_hosts(input_file="phishing.txt", output_file="phishing_compressed.txt", group_size=9):
    domains = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # skip comments & empty lines

            parts = line.split()

            # Accept both 0.0.0.0 and 127.0.0.1
            if len(parts) >= 2 and parts[0] in ("0.0.0.0", "127.0.0.1"):
                domains.append(parts[1])

    # Write grouped output
    with open(output_file, "w", encoding="utf-8") as f:
        for i in range(0, len(domains), group_size):
            group = domains[i:i + group_size]
            f.write("0.0.0.0 " + " ".join(group) + "\n")


if __name__ == "__main__":
    group_hosts()

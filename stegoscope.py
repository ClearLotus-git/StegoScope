#!/usr/bin/env python3

import os
import math
import binascii

def shannon_entropy(data: bytes) -> float:
    """
    Calculate Shannon entropy of given data.
    """
    if not data:
        return 0
    byte_counts = [0] * 256
    for byte in data:
        byte_counts[byte] += 1
    prob = [count / len(data) for count in byte_counts if count > 0]
    return -sum(p * math.log2(p) for p in prob)

def analyze_file(filepath: str):
    """
    Basic file analysis: size, entropy, strings.
    """
    with open(filepath, "rb") as f:
        data = f.read()

    entropy = shannon_entropy(data)
    size_kb = len(data) / 1024

    print(f"[+] File: {filepath}")
    print(f"    Size: {size_kb:.2f} KB")
    print(f"    Entropy: {entropy:.3f}")

    # quick heuristic
    if entropy > 7.5:
        print("    [!] High entropy detected — possible encryption or stego.")
    elif entropy < 3:
        print("    [!] Very low entropy — could be padded or fake content.")
    else:
        print("    [-] Normal entropy range.")

    # extract ASCII strings
    strings = []
    current = b""
    for b in data:
        if 32 <= b <= 126:  # printable ASCII
            current += bytes([b])
        else:
            if len(current) >= 4:
                strings.append(current.decode("utf-8", errors="ignore"))
            current = b""

    print(f"    Found {len(strings)} printable strings")
    if strings:
        print("    Sample strings:", strings[:5])

if __name__ == "__main__":
    test_file = "samples/test.png"
    if os.path.exists(test_file):
        analyze_file(test_file)
    else:
        print("[!] Add a file in samples/ and rerun.")
#!/usr/bin/env python3

import os
import math
import binascii

def shannon_entropy(data: bytes) -> float:
    """
    Calculate Shannon entropy of given data.
    """
    if not data:
        return 0
    byte_counts = [0] * 256
    for byte in data:
        byte_counts[byte] += 1
    prob = [count / len(data) for count in byte_counts if count > 0]
    return -sum(p * math.log2(p) for p in prob)

def analyze_file(filepath: str):
    """
    Basic file analysis: size, entropy, strings.
    """
    with open(filepath, "rb") as f:
        data = f.read()

    entropy = shannon_entropy(data)
    size_kb = len(data) / 1024

    print(f"[+] File: {filepath}")
    print(f"    Size: {size_kb:.2f} KB")
    print(f"    Entropy: {entropy:.3f}")

    # quick heuristic
    if entropy > 7.5:
        print("    [!] High entropy detected — possible encryption or stego.")
    elif entropy < 3:
        print("    [!] Very low entropy — could be padded or fake content.")
    else:
        print("    [-] Normal entropy range.")

    # extract ASCII strings
    strings = []
    current = b""
    for b in data:
        if 32 <= b <= 126:  # printable ASCII
            current += bytes([b])
        else:
            if len(current) >= 4:
                strings.append(current.decode("utf-8", errors="ignore"))
            current = b""

    print(f"    Found {len(strings)} printable strings")
    if strings:
        print("    Sample strings:", strings[:5])

if __name__ == "__main__":
    test_file = "samples/test.png"
    if os.path.exists(test_file):
        analyze_file(test_file)
    else:
        print("[!] Add a file in samples/ and rerun.")

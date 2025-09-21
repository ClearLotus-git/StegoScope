#!/usr/bin/env python3

import sys
import os
import math
from PIL import Image


def shannon_entropy(data: bytes) -> float:
    """Calculate Shannon entropy of given data."""
    if not data:
        return 0
    byte_counts = [0] * 256
    for byte in data:
        byte_counts[byte] += 1
    prob = [count / len(data) for count in byte_counts if count > 0]
    return -sum(p * math.log2(p) for p in prob)


def analyze_file(filepath: str):
    """Basic file analysis: size, entropy, strings."""
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


def lsb_extract(image_path):
    """Extract hidden data from PNG/JPEG images using LSB steganography."""
    try:
        img = Image.open(image_path)
        if img.format not in ["PNG", "JPEG", "JPG"]:
            print(f"    Unsupported format: {img.format}. Only PNG and JPEG supported.")
            return

        pixels = list(img.getdata())
        lsb_list = []

        for pixel in pixels:
            rgb = pixel[:3] if isinstance(pixel, tuple) else (pixel,)
            for value in rgb:
                lsb_list.append(value & 1)

        hidden_bytes = [lsb_list[i:i+8] for i in range(0, len(lsb_list), 8)]
        hidden_message = ""
        for byte in hidden_bytes:
            if len(byte) < 8:
                continue
            char = chr(int("".join(map(str, byte)), 2))
            if char == "\x00":  # stop at null terminator
                break
            if char.isprintable():
                hidden_message += char
            else:
                break

        print("    [+] LSB Analysis Result:")
        if hidden_message:
            print("    Hidden message:", hidden_message[:200])  # limit preview
        else:
            print("    No hidden message found.")

    except Exception as e:
        print(f"    Error during LSB extraction: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python stegoscope.py <file>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File not found.")
        sys.exit(1)

    analyze_file(filepath)

    # run LSB if image
    try:
        with Image.open(filepath) as img:
            if img.format in ["PNG", "JPEG", "JPG"]:
                lsb_extract(filepath)
    except Exception:
        pass


if __name__ == "__main__":
    main()
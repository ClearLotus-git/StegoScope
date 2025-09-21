import sys
import os
from PIL import Image


def lsb_extract(image_path):
    """Extract hidden data from PNG/JPEG images using LSB steganography."""
    try:
        img = Image.open(image_path)
        if img.format not in ["PNG", "JPEG", "JPG"]:
            return f"Unsupported format: {img.format}. Only PNG and JPEG supported."

        pixels = list(img.getdata())
        lsb_list = []

        for pixel in pixels:
            # Handle RGB or RGBA
            rgb = pixel[:3] if isinstance(pixel, tuple) else (pixel,)
            for value in rgb:
                lsb_list.append(value & 1)

        # Convert bits to characters
        hidden_bytes = [lsb_list[i:i+8] for i in range(0, len(lsb_list), 8)]
        hidden_message = ""
        for byte in hidden_bytes:
            if len(byte) < 8:
                continue
            char = chr(int("".join(map(str, byte)), 2))
            if char.isprintable():
                hidden_message += char
            else:
                break

        return hidden_message if hidden_message else "No hidden message found."

    except Exception as e:
        return f"Error: {e}"


def main():
    if len(sys.argv) != 2:
        print("Usage: python stegoscope.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        print("File not found.")
        sys.exit(1)

    result = lsb_extract(image_path)
    print("[+] Analysis Result:")
    print(result)


if __name__ == "__main__":
    main()


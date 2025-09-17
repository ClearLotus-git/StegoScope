# StegoScope: Hidden Data Finder

StegoScope is a forensic tool for detecting **hidden payloads** in files using entropy analysis, string extraction, and future steganography detection methods.

## Features
- Calculate file entropy (detect suspiciously high or low randomness).
- Extract printable strings from binary data.
- Flag anomalies that could indicate steganography or encryption.

## Usage
```bash
python3 stegoscope.py


##  Roadmap

###  Completed
- [x] Project structure created (main script, samples folder, README).
- [x] Entropy calculation added.
- [x] Basic ASCII string extraction added.
- [x] File analysis prints size, entropy, and sample strings.

###  In Progress
- [ ] Implement LSB (least significant bit) detection for PNG/JPEG images.
- [ ] Add export options (CSV/JSON for results).
- [ ] Improve CLI interface with argparse (custom file input).

### Future Ideas
- [ ] Add PDF/doc stego detection (metadata + embedded files).
- [ ] Integrate YARA rules for detecting common stego payloads.
- [ ] Build a simple GUI (Tkinter or web-based dashboard).
- [ ] Add OSINT integration (check suspicious file hashes online).

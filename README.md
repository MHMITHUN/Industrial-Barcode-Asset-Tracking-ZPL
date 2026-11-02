# Industrial Barcode Asset Tracking & Zebra ZPL II Studio

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Zebra%20Studio-06b6d4)](https://mhmithun.github.io/Industrial-Barcode-Asset-Tracking-ZPL/)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Hardware Support](https://img.shields.io/badge/Hardware-Zebra%20ZT411%20%7C%20TSC-orange.svg)](#supported-hardware)

Industrial-grade barcode label generation and raw network printing suite designed for ready-made garments (RMG) manufacturing, carton packing lines, cutting bundles, and enterprise IT hardware asset tagging using direct Zebra Programming Language (ZPL II) transmission over raw TCP socket port 9100.

---

## 🏷️ Live Web Studio & Thermal Label Designer

The repository features an **interactive Zebra Thermal Label Studio** (`index.html`):
- **Live Label Designer**: Customize Company/Facility Name, Industrial Zone, Purpose, Style, and Lot/Serial number.
- **Thermal Canvas Preview**: Instant rendering of thermal paper layout, 1D Code 128 barcode lines, and 2D QR matrix.
- **Raw ZPL II Script Inspector**: Real-time code compilation with one-click clipboard copying and simulated TCP socket transmission (port 9100) to Zebra ZT411 printers.

---

## 🛠️ Key Capabilities & Technical Features

1. **Raw TCP Socket Network Client (`barcode_core/zebra_socket_client.py`)**:
   - Transmits raw ZPL II byte streams directly to industrial thermal barcode printers over TCP port 9100.
   - Bypasses problematic Windows spoolers and CUPS drivers for sub-second, non-blocking label print feeds.

2. **Standardized ZPL II Template Generator (`barcode_core/zpl_generator.py`)**:
   - **RMG Export Carton Shipping Labels**: 4x6" labels with Code 128 barcodes (`^BC`), QR inspection stamps (`^BQ`), style codes, and carton serials.
   - **IT Hardware Asset Inventory Tags**: 2x1" tamper-evident tags encoding asset IDs, MAC addresses, and equipment types for enterprise IT audit compliance.

---

## 🖨️ Supported Printer Hardware

- **Zebra Technologies**: ZT411, ZT421, ZT230, ZD421, GK420t, GX430t
- **TSC Auto ID**: TTP-244 Pro, TE200, MB240
- **Honeywell / Intermec**: PC42t, PM43
- **Connectivity**: 10/100 Ethernet LAN, Raw TCP Port 9100, USB-over-IP print servers

---

## 🚀 Quick Start

### 1. Run the Interactive Web Studio
```bash
# Open index.html in any browser or launch local server:
python -m http.server 8083
# Navigate to http://localhost:8083
```

### 2. Run the Python ZPL Generation & Print Client
```bash
# Clone the repository
git clone https://github.com/MHMITHUN/Industrial-Barcode-Asset-Tracking-ZPL.git
cd Industrial-Barcode-Asset-Tracking-ZPL

# Generate sample ZPL II scripts
python barcode_core/zpl_generator.py

# Send raw test print over TCP port 9100
python barcode_core/zebra_socket_client.py
```

---

## 👤 Author

**MD. Mahamudul Hasan**  
- **Role**: IT Officer  
- **Email**: mhmmithun1@gmail.com  
- **Phone**: +880 1560-027539  
- **LinkedIn**: [linkedin.com/in/mahamudul0](https://linkedin.com/in/mahamudul0)  
- **GitHub**: [github.com/MHMITHUN](https://github.com/MHMITHUN)  

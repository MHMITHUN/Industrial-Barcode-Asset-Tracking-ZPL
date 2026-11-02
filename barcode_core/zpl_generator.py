#!/usr/bin/env python3
"""
Zebra Programming Language (ZPL II) Template Generator
Author: MD. Mahamudul Hasan
Repository: Industrial-Barcode-Asset-Tracking-ZPL
License: MIT

Generates industrial-grade raw ZPL II code for 4x6" and 2x1" thermal transfer labels
targeting Zebra ZT411, ZT230, GK420t, and TSC thermal barcode printers.
"""

from typing import Dict, Any


class ZPLTemplateGenerator:
    """Generates standardized ZPL II scripts for manufacturing and IT hardware tracking."""

    @staticmethod
    def generate_rmg_carton_label(company: str, location: str, style: str,
                                   lot_sn: str, purpose: str = "CARTON SHIPPING LABEL") -> str:
        """
        Generates standard 4x6" RMG export carton shipping label in ZPL II.
        Includes Code 128 barcode (^BC) and high-density QR code (^BQ).
        """
        zpl = f"""^XA
^PW812
^LL1218
^FO40,40^A0N,36,36^FD{company.upper()}^FS
^FO40,85^A0N,22,22^FD{location.upper()}^FS
^FO40,120^GB730,3,3^FS

^FO40,140^A0N,26,26^FDPURPOSE: {purpose.upper()}^FS
^FO40,180^A0N,30,30^FDSTYLE : {style}^FS
^FO40,225^A0N,26,26^FDLOT/SN: {lot_sn}^FS

^FO540,140^BQN,2,5^FDQA,{style}-{lot_sn}-VERIFIED^FS

^FO40,280^BY3,3,100^BCN,100,Y,N,N^FD{lot_sn}^FS

^FO40,420^GB730,2,2^FS
^FO40,435^A0N,20,20^FDQC VERIFIED · IT SURVEILLANCE & ASSET GOVERNANCE PASSED^FS
^XZ"""
        return zpl.strip()

    @staticmethod
    def generate_it_asset_tag(asset_id: str, asset_type: str, serial_num: str,
                              mac_addr: str, assigned_to: str) -> str:
        """
        Generates compact 2x1" IT asset inventory label with Code 128 barcode.
        """
        zpl = f"""^XA
^PW406
^LL203
^FO20,20^A0N,24,24^FDENTERPRISE IT ASSET^FS
^FO20,50^A0N,18,18^FDID : {asset_id} ({asset_type})^FS
^FO20,75^A0N,16,16^FDSN : {serial_num}^FS
^FO20,95^A0N,16,16^FDMAC: {mac_addr}^FS
^FO20,120^BY2,2,40^BCN,40,Y,N,N^FD{asset_id}^FS
^FO260,25^BQN,2,3^FDASSET,{asset_id},{serial_num}^FS
^XZ"""
        return zpl.strip()


if __name__ == '__main__':
    generator = ZPLTemplateGenerator()
    print("--- RMG Export Carton ZPL II Script ---")
    print(generator.generate_rmg_carton_label(
        company="ENTERPRISE APPAREL & TEXTILES LTD",
        location="CENTRAL INDUSTRIAL ZONE · SECTOR 04",
        style="EXP-JKT-882",
        lot_sn="LOT-2026-B12"
    ))
    print("\n--- IT Asset Tag ZPL II Script ---")
    print(generator.generate_it_asset_tag(
        asset_id="IT-SRV-042",
        asset_type="Dell PowerEdge R750",
        serial_num="SN-98214-BD",
        mac_addr="00:1A:2B:3C:4D:5E",
        assigned_to="Core Server Room NOC"
    ))

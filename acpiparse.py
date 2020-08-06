#!/usr/bin/python3

import sys
import struct

def print_header(table):
    out = struct.unpack("<4sIBB6sQI4sI", table[0:36])

    print("%-20s: %s" % ("signature", out[0].decode("ascii")))
    print("%-20s: %s" % ("length", out[1]))
    print("%-20s: %s" % ("revision", out[2]))
    print("%-20s: %s" % ("checksum", out[3]))
    print("%-20s: %s" % ("oem_id", out[4].decode("ascii")))
    print("%-20s: %s" % ("oem_table_id", hex(out[5])))
    print("%-20s: %s" % ("oem_revision", out[6]))
    print("%-20s: %s" % ("creator_id", out[7].decode("ascii")))
    print("%-20s: %s" % ("creator_revision", out[8]))

def print_tpm2(table):
    print_header(table)
    out = struct.unpack("<HHQI", table[36:52])

    print("%-20s: %s" % ("platform_class", out[0]))
    # out[1] reserved
    print("%-20s: %s" % ("control_area_address", hex(out[2])))
    print("%-20s: %s" % ("start_method", out[3]))

def print_apic(table):
    # Parse header
    print_header(table)
    return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: acpiparse.py <filepath>")
        exit(1)

    with open(sys.argv[1], "rb") as f:
        table = f.read()
        signature = table[0:4].decode("ascii")
        print("Parsing ACPI table with signature %s" % (signature))
        if signature == "TPM2":
            print_tpm2(table)
        elif signature == "APIC":
            print_apic(table)
        else:
            print("Table with signature %s is not supported" % (table))


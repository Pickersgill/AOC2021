import sys
import re
import numpy as np
from scanner import Scanner

def build_input(src):
    with open(src) as raw_src:
        txt = raw_src.read()

        scanner_strs = re.split("--- scanner \d+ ---", txt)[1:]

        scanners = []

        for i, s in enumerate(scanner_strs):
            new_scanner = Scanner(name="Scanner %d" % i)

            for beacon in s.splitlines():
                if len(beacon) > 1:
                    new_scanner.add_beacon_from_text(beacon)

            scanners.append(new_scanner)

        print("Loaded some scanners from '%s'..." % src)

        return scanners

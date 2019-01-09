#!/usr/bin/python
import re
GC_regex = re.compile(r'[GC]')
header_regex = re.compile(r'^>')
with open('brca2.fasta') as dna:
    line = dna.readline()
    line_count = 1
    total_count = 0
    DNA_total = 0
    while line:
        if header_regex.search(line):
            line = dna.readline()
            continue
        line_strip = line.strip()
        GC_count = len(GC_regex.findall(line))
        DNA_count = len(line_strip)
        print(str(line_count).rjust(3) + ' ' +  line_strip + ' ' +  str(float(GC_count) * 100 / DNA_count) + '%')
        line = dna.readline()
        line_count += 1
        total_count += GC_count
        DNA_total += DNA_count

    print(str(float(total_count) * 100  / DNA_total) + '%')



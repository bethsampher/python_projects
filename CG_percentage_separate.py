#!/usr/bin/python
import re
GC_regex = re.compile(r'[GC]')
header_regex = re.compile(r'^>')
#with open('/tmp/brca2_full.fasta') as dna:
with open('test.fa') as dna:
    line = dna.readline()
    line = line.strip()
    line_count = 0
    total_GC  = 0 
    total_DNA = 0  
    transcript_count = 0
    if header_regex.findall(line):
        line = dna.readline()
        line = line.strip()
        transcript_count += 1

    while line:
            if header_regex.findall(line):
                vara = (total_GC * 100.0) / total_DNA
                print('{0:-2d} {1:-5.2f}% lines: {2:d}'.format (transcript_count, vara, line_count))
                total_GC  = 0
                total_DNA = 0 
                line_count = 0
                transcript_count += 1
            else:
                GC_count = len(GC_regex.findall(line))
                DNA_count = len(line)
                line_count += 1
                total_GC  += GC_count
                total_DNA += DNA_count
            line = dna.readline()
            line = line.strip()
    
    vara = (total_GC * 100.0) / total_DNA
    print('{0:-2d} {1:-5.2f}% lines: {2:d}'.format (transcript_count, vara, line_count))


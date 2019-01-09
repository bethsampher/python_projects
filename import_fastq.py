#!/usr/bin/python

from FastqReader import FastqReader 

with FastqReader('/tmp/100_S100_L001_R1_001.fastq') as reader:
    read = reader.read()
    while (read):
        print(read.name)
        print(read.phred_calculator())
        read = reader.read()


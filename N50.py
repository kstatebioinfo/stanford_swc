#!/usr/bin/env python3
##########################################################################
#	USAGE: import N50
#   help(N50)
#   N50.main(~/stanford_swc/fasta-o-matic/fasta/normal.fa)
#   DESCRIPTION: Function that calculates N50 for a FASTA file
#   Created by Jennifer M Shelton
##########################################################################
import sys

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    fasta = open(filename, 'r')
    header_pattern = re.compile('^>.*') # pattern for a header line
    ## Initialize strings for headers and sequences and a list for lengths
    lengths = []
    dna = ''
    header = ''
    for line in fasta:
        line = line.rstrip()
        if header_pattern.match(line):
            if not dna == '': # skip the first (empty record)
                



#def main(fasta)
#input = open(full_path2, 'r')
#!/usr/bin/env python3
##########################################################################
#	USAGE: import N50
#   help(N50)
#   N50.main(~/stanford_swc/fasta-o-matic/fasta/normal.fa)
#   DESCRIPTION: Function that calculates N50 for a FASTA file
#   Created by Jennifer M Shelton
##########################################################################
import sys
import re
def n50(lengths):
    '''
        Reverse sort list of lengths and return N50
    '''
    lengths = sorted(lengths, reverse = True) # reverse sort lengths large
    # to small
    cumulative_length = sum(lengths) # get total length
    fraction = cumulative_length # set fraction of total to 100%
    my_n50 = 0 # initialize n50
    for seq_length in lengths:
        if fraction > (cumulative_length/2.0):
            fraction = fraction - seq_length
            my_n50 = seq_length
        else: # when the fraction has passed 50% total length get N50
            return(my_n50)
def main():
    '''
    calculates N50 for a FASTA file
    '''
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
                lengths.append(len(dna))
                dna = ''
        else:
            dna = dna + line
    else:
        lengths.append(len(dna))
        my_n50 = n50(lengths)
        print(my_n50)

##########################################################################
#####       Execute main unless script is simply imported     ############
#####                for individual functions                 ############
##########################################################################
if __name__ == '__main__':
    main()

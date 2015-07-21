stanford_swc
============

**count_fasta**

```
usage: bash count_fasta.sh FASTA
```

DESCRIPTION: Script counts number of sequences in a FASTA file

DEPENDENCIES: 

count_fasta has no dependencies

EXAMPLES:

```
bash ~/stanford_swc/count_fasta.sh ~/stanford_swc/fasta-o-matic/fasta/normal.fa
```


**N50** 

```
usage: N50.py FASTA
```

DESCRIPTION: Script calculates N50 for a FASTA file.

DEPENDENCIES: 

fasta_o_matic.py runs with either python2.7+ or python3.3+

EXAMPLE:

Calculate N50 :

```
python ~/stanford_swc/N50.py ~/stanford_swc/fasta-o-matic/fasta/normal.fa
```


**Fasta-O-Matic** 

Cite as: Jennifer M Shelton (2015). FASTA tools including Fasta-O-Matic 


```
usage: fasta_o_matic.py [-h] [-v] [-q] [-c] -f FILE [-s STEPS [STEPS ...]][-o OUT_DIR]
```

DESCRIPTION: Script runs quality checking and filtering based on a user-
defined list of quality checks. Command-line options that may be omitted (i.e.
are NOT required) are shown in square brackets. The actively 
maintained version of Fasta-O-Matic is at :
https://github.com/i5K-KINBRE-script-share/read-cleaning-format-conversion


DEPENDENCIES: 

fasta_o_matic.py runs with either python2.7+ or python3.3+

DETAILS:

```
optional arguments:
-h, --help            show this help message and exit
-v, --verbose         Runs reporting status updates
-q, --quiet           Does not report status updates
-c, --colorized       Colorizes log reports. Use only if printing output to
screen.
-f FILE, --fasta FILE
This is the the full path (path and filename) of the
user provided FASTA file.
-s STEPS [STEPS ...], --qc_steps STEPS [STEPS ...]
List of QC steps to perform on FASTA file (default= -s
wrap new_line header_whitespace).
-o OUT_DIR, --out_dir OUT_DIR
Output directory for any repaired FASTA created (no
trailing slash).
```

EXAMPLES:

Make output directory (your re-formatted FASTA
files will be created here) :

```
mkdir ~/out_stanford_swc

```

Fix FASTA file with inconsistantly wrapped sequence 
lines and remove spaces in headers:

```
python3 ~/stanford_swc/fasta-o-matic/fasta_o_matic.py -f ~/stanford_swc/fasta-o-matic/fasta/miswrapped.fa -c -o ~/out_stanford_swc -s wrap header_whitespace
```

Fix FASTA file with missing end of line character 
for last sequence:

```
python2.7 ~/stanford_swc/fasta-o-matic/fasta_o_matic.py -f ~/stanford_swc/fasta-o-matic/fasta/missing_last_new_line.fa -c -o ~/out_stanford_swc -s new_line
```

Fix unwrapped FASTA file:

```
python ~/stanford_swc/fasta-o-matic/fasta_o_matic.py -f ~/stanford_swc/fasta-o-matic/fasta/unwrapped.fa -c -o ~/out_stanford_swc -s wrap new_line header_whitespace
```

Remove spaces in FASTA headers:

```
python ~/stanford_swc/fasta-o-matic/fasta_o_matic.py -f ~/stanford_swc/fasta-o-matic/fasta/missing_last_new_line.fa -c -o ~/out_stanford_swc -s header_whitespace
```


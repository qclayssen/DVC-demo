import sys

in_fastq, out_bam = sys.argv[1:3]

with open(in_fastq) as fi, open(out_bam, 'w') as fo:
    fo.write('@HD\tVN:1.0\n')
    lines = [l.strip() for l in fi if l.strip()]
    for i in range(0, len(lines), 4):
        name = lines[i].lstrip('@')
        seq = lines[i+1]
        fo.write(f"{name}\t{seq}\n")

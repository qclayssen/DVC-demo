import sys

in_bam, out_vcf = sys.argv[1:3]

with open(in_bam) as fi, open(out_vcf, 'w') as fo:
    fo.write('##fileformat=VCFv4.2\n')
    fo.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')
    for idx, line in enumerate(fi):
        if line.startswith('@'):
            continue
        name, seq = line.strip().split('\t')
        ref = seq[0]
        alt = seq[-1]
        fo.write(f'chr1\t{idx+1}\t{name}\t{ref}\t{alt}\t.\tPASS\t.\n')

# % for f in *.csv; pv $f | csv2tsv | reservoir_sample.py 10  > samples/${f}.txt 
# % for f in *.csv; pv $f | csv2tsv | head -1  > samples/${f}.header.txt

from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style

import glob
bases = [f.replace(".csv.txt","") for f in glob.glob("samples/*.csv.txt")]

def opttrunc(x):
    N = 40
    if len(x) > N:
        x = x[:N-3] + "..."
    return x

for f in sorted(bases):
    header = open("{}.csv.header.txt".format(f)).read().rstrip("\n").split("\t")
    # print(header)
    tsv = [L.rstrip("\n").split("\t") for L in open("{}.csv.txt".format(f))]
    tsv = [ [opttrunc(x) for x in row] for row in tsv ]


    writer = MarkdownTableWriter(
        # table_name=f.split("\t")[-1]),
        headers=header,
        value_matrix=tsv)

    for h in header:
        writer.set_style(h, Style(align='left'))

    print("")
    print("### {}".format(f.split("\t")[-1].split("/")[-1]))
    writer.write_table()
    

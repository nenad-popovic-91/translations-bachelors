import os

dir = "path_to_SerbMR3.en"

inf = open(dir + "/SerbMR3.en")
outf = open(dir + "/SerbMR-3C.en.arff", 'w')

# Koristeći činjenicu da su recenzije u SerbMR-3C fajlu bile
# grupisane po klasama, vratićemo klase prevodima u istom redosledu.
idx = 0
flag = "POSITIVE"
for line in inf:
	new_line = "'"+line[:-1].decode('utf8')+"'," + flag + "\n"
	idx+=1
	outf.write(new_line.encode('utf8'))
	if (idx==841):
		flag = "NEUTRAL"
	if (idx==1682):
		flag = "NEGATIVE"

inf.close()
outf.close()
			

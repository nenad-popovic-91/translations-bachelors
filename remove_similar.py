import os
from operator import itemgetter

inf = open("arff_file")
file_tuples = []

i = 0
for line in inf:
    i+=1
    if (i > 7):
        review_snippet = line[:100]
        file_tuples.append((review_snippet, i))    
        
dupes = 0
for x in range(1,len(file_tuples)):
    if file_tuples[x][0] == file_tuples[x-1][0]:
		# Ukoliko je isečci recenzija identični,
		# ispisaćemo njihove redne brojeve radi provere
        print file_tuples[x-1][1]
        print file_tuples[x][1]
        print ""
        dupes +=1
print dupes

inf.close()


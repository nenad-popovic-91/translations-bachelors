import os 

dir = "folder_to_eng_corpus"
file_tuples = []
option_tuples = [("train", "small"), ("test", "large")]

# Kreiraćemo torke koje sadrže recenziju, njenu klasu sentimenta i naziv fajla.
# Sortiraćemo ih po tekstu recenzije, i zatim izbaciti duplikate prilikom upisivanja
# u konačni fajl. Prvo ćemo to učiniti sa prvih 25000 recenzija iz foldera "train", 
# da bi zatim dodali i drugih 25000 recenzija iz foldera "test". 
for option in option_tuples:
	for file in os.listdir(dir + "/"+ option[0] +"/neg"):
		if file.endswith(".txt"):
			print file
			inf = open(dir + "/"+ option[0] +"/neg/" + file)
			for line in inf:
				file_tuples.append((line.replace("'", "\\'"), "NEGATIVE", file))
			inf.close()

	for file in os.listdir(dir + "/"+ option[0] +"/pos"):
		if file.endswith(".txt"):
			print file
			inf = open(dir + "/"+ option[0] +"/pos/" + file)
			for line in inf:
				file_tuples.append((line.replace("'", "\\'"), "POSITIVE", file))
			inf.close()
			
	file_tuples = sorted(file_tuples, key=lambda tuple: tuple[0])

	outf = open(dir + "/EngMR_" + option[1] +".txt", 'w')
	outf.write("'" + file_tuples[0][0] + "', " + file_tuples[0][1] + "\n")

	dup = 0
	for i in range(1, len(file_tuples)):
		if (file_tuples[i][0] != file_tuples[i-1][0]):
			outf.write("'" + file_tuples[i][0] + "', " + file_tuples[i][1] + "\n")
		else:
			dup +=1

	print dup
	outf.close()



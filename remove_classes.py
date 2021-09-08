import os

dir = "path_to_SerbMR_files"

# Za svaku liniju svakog fajla ćemo proveriti da li počinje apostrofom
# ili se završava klasom nakon apostrofa, i te oznake ćemo ukloniti, jer
# one ne predstavljaju tekst recenzija. Ovde uzimamo pretpostavku da ne važi
# pravilo "jedna recenzija po liniji", jer smo neke morali da podelimo na 
# više linija.
for file in os.listdir(dir):
	if file.endswith(".txt"):
		inf = open(dir + "/" + file)
		print file
		outf = open(dir + "_bez_klasa/" + file, 'w')
		for line in inf:
			review = line
			if (len(review) > 1 and review[0] == '\''):
				review = review[1:]
			if (len(review) > 11 and 
			(review[-11:-1] == "',POSITIVE" or review[-11:-1] == "',NEGATIVE")):
				review = review[:-11]
			outf.write(review + "\n")
		inf.close()
		outf.close()

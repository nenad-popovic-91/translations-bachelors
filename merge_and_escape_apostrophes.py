import os

# location of SER-ENG 03 files
dir = "path_to_translated_files"

# Ovaj program spaja sve prevedene fajlove u jedan, i ujedno
# stavlja escape karakter pre svakog apostrofa.
outf = open(dir + "/SerbMR3.en", 'w')
for file in os.listdir(dir):
	if file.endswith(".txt"):
		inf = open(dir + "/" + file)
		for line in inf:
			new_line = line.decode('utf8').replace("'","\\'")
			outf.write(new_line.encode('utf8'))
		inf.close()
outf.close()
				
				
				
			

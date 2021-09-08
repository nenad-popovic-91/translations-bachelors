import os

# folder sa fajlovima nakon vraćanja dijakritika
dir = "C:/Users/Nenad/dcr_files/train/unsup"
 
# Linije u .dcr fajlovima su strukturisane na sledeći način
#		<l>.<r>.<bt>.<pt>-<kt> \t <ot> \t <dt>
#		l - redni broj linije, r - recenica fajla u kojoj se nalazi token
#		bt - redni broj tokena u recenici
#		pt - početna pozicija tokena, kt - krajnja pozicija tokena
#		ot - originalni token, dt - token sa vraćenim dijakriticima
# Dodatno, tokeni iz jedne recenice orig. fajla su odvojeni praznim redom.

for file in os.listdir(dir):
	if file.endswith(".dcr"):
		inf = open(dir + "/" + file)
		outf = open(dir + "_/" + file[:-17] + ".txt", 'w')
		entry_list = []
		prev_idx = 1;
		prev_line = '0'
		# Svaka linija .dcr fajla sadrži tačno jedan token, ili je prazna.
		# Ukoliko linija nije prazna, dodajemo popravljeni token u bafer.
		# Ukoliko je linija prazna, praznimo bafer i rekonstruišemo
		# recenicu originalnog fajla sa popravljenim tokenima iz bafera.
		for line in inf:
			if line.strip()=='':
				for entry in entry_list:
					nums = entry[0].decode('utf8').split('.')
					line_num = nums[0]
					if (line_num != prev_line):
						prev_line = line_num
						prev_idx = 1
					idcs = nums[3].split('-')
					if (int(idcs[0])>int(prev_idx)):
						for i in range(int(prev_idx), int(idcs[0])):
							outf.write(' ')
					outf.write(entry[2].encode('utf8'))
					prev_idx = int(idcs[1])+1
				
				entry_list=[]
			else:
				entry_list.append(line[:-1].decode('utf8').split('\t'))
			

import os

dir = "folder_path"

for file in os.listdir(dir):
	if file.endswith(".txt"):
		inf = open(dir + "/" + file)
		outf = open(dir + "_/" + file, 'w')
		print file
		for line in inf:
			new_line = line.decode('utf8').replace("< br / > < br / >","")
			# replace("<br /><br />"," ") 
			# za englesku verziju
			outf.write(new_line.encode('utf8'))
		inf.close()
		outf.close()
		
		
		
		
		
		
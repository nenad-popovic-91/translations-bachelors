#include <iostream>
#include <fstream>
#include <string>
#include "dirent.h"
#include <locale>
#include <codecvt>

using namespace std;

/*
	Ova funkcija uzima liniju teksta i poziciju unutar nje, i kao rezultat vraća ispravnu 
	reč koja sledi nakon te pozicije. Reč može biti ispravljena jednostavnom zamenom 
	ćiriličnih karaktera, ili ručnom izmenom reči sa "čudnim" karakterima.
*/
wstring getNextWord(wstring line, int *pidx) {
	int index = *pidx;
	wstring word = L"";
	bool weirdChar = false;
	wchar_t ch;
	while (index != line.length() && line[index] != ' ') {
		ch = line[index];
		switch (ch) {
			case 1113: ch = 353; break; // љ -> š
			case 1115: ch = 382; break; // ћ -> ž
			case 1078: ch = 263; break; // ж -> ć
			case 1080: ch = 269; break; // и -> č
			case 1088: ch = 273; break; // р -> đ
			case 1033: ch = 352; break; // Љ -> Š
			case 1046: ch = 262; break; // Ж -> Ć 
			case 1048: ch = 268; break; // И -> Č
			case 1035: ch = 381; break; // Ћ -> Ž
			case 1056: ch = 272; break; // Р -> Đ
			case 8211: ch = 45; break;  // EN DASH -> -
		}
		word += ch;
		if (ch > 1000 && ch != 8222 && ch != 8221) weirdChar = true;
		// ne tretiramo „ i ” kao 'čudne' karaktere
		index++;
	}

	// ove reči su se pojavljivale veliki broj puta,
	// i originalno su bile potpuno ćirilične,  
	// latinični karakteri su dobijeni primenom gornjih zamena
		 if (word == L"опčс") { word = L"opis"; }
	else if (word == L"Скувај") { word = L"Skuvaj"; }
	else if (word == L"покваđеност") { word = L"pokvarenost";  }
	else if (word == L"čзвоđне") { word = L"izvorne";  }
	else if (word == L"наđатčв") { word = L"narativ"; }
	else if (word == L"čсечцčма") { word = L"isečcima"; }
	else if (word == L"кčч") { word = L"kič"; }
	else if (word == L"здđавог") { word = L"zdravog"; }
	else if (word == L"наđацčју") { word = L"naraciju"; }
	else if (weirdChar) {
		// ukoliko imamo reč koja nije među ponuđenima, 
		// korisnik je ručno ispravlja
		wcout << word << endl;
		wstring fixed; wcin >> fixed;
		word = fixed;
	}
	while (index != line.length() && line[index] == ' ') index++;
	*pidx = (index == line.length())? -1 : index;

	return word;
}

// Ova funkcija fajl zadat folderom i imenom deli na pojedinačne 
// linije teksta koje zatim prethodna funkcija obrađuje reč po reč
void handleFile(string folder, string name) {
	wfstream file;
	wofstream outfile;

	file.open(folder + "\\" + name);
	file.imbue(std::locale(std::locale::empty(), 
			new std::codecvt_utf8<wchar_t, 0x10ffff, std::consume_header>));

	outfile.open(folder + "\\" + name.substr(0, name.length()-4) + "_.txt");
	outfile.imbue(std::locale(std::locale::empty(), 
			new std::codecvt_utf8<wchar_t, 0x10ffff, std::consume_header>));
	
	wcout.imbue(std::locale(std::locale::empty(), 
			new std::codecvt_utf8<wchar_t, 0x10ffff, std::consume_header>));
	wcin.imbue(std::locale(std::locale::empty(), 
			new std::codecvt_utf8<wchar_t, 0x10ffff, std::consume_header>));

	if (file.is_open()) {
		wstring line;
		while (getline(file, line))
		{
		int index = 0;
			while (index != -1) {
				wstring word = getNextWord(line, &index);
				outfile << word << " ";
				
			}
		}
		file.close();
		outfile.close();
	}
}

// Pokretanjem programa u folderu sa tekstualnim fajlovima
// prolazimo kroz svaki pozivom funkcije handleFile,
// da bismo popravili pojedinačne reči sa neispravnim karakterima
int main(int argc, char* argv[]) {
	UINT oldcodepage = GetConsoleOutputCP();
	SetConsoleOutputCP(65001);
	string exename(argv[0]);
	string base = exename.substr(0, exename.find_last_of("\\"));

	DIR *currDir = opendir(base.c_str());
	struct dirent *ent;
	int i = 0;

	while ((ent = readdir(currDir)) != NULL) {
		string fileName(ent->d_name);
		if (ent->d_type == DT_REG && fileName.substr(fileName.length() - 3, 3) == "txt")
		{
			cout << fileName << endl; i++;
			handleFile(base, ent->d_name);
		}
			
	}

	cout << "\n\n" << i << "\n\n\n" << endl;

	closedir(currDir);
	SetConsoleOutputCP(oldcodepage);

	system("PAUSE");
}
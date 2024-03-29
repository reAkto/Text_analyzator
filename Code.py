### Text_analyzator_ENG ###
# Pouze cvičný program na základě zadání / only a practice program based on assignment

# Import knihovny pro využití sys.exit()
import sys

# Import knihovny pro využití regex
import re

# Lemování
lem = "X" + 58 * "-" + "X"
graf_lem = "X" + 26 * "-" + " Graf " + 26 * "-" + "X"

# Přístupové údaje uživatelů (no real credentials)
uzivatele = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123",
}

# Vstupy uživatele
print(lem)
jmeno = input("  Zadej jméno: ")
heslo = input("  Zadej heslo: ")

# Kontrola vstupů vůči "databázi" uživatelů
if uzivatele.get(jmeno) == heslo:
    print(lem)
    print("  Vítej v programu pro analýzu textů uživateli", jmeno)
    print("  Pro analýzu máme k dispozici tři texty")
else:
    print("  Vstup zamítnut")
    sys.exit()

# Publicly available information
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Upozornění o možnostech výběru pro uživatele
print(lem)
print("  Upozornění - Vybírej text pouze pomocí čísel 1, 2 nebo 3")
vyber_textu = input("  Číslo textu: ")
cislo_textu = int(vyber_textu)
print(lem)

# Mechanismus výběru jednoho ze tří textů (ve stylu "whitelist") a následné kalkulace podúloh pomocí regexů atd.
if cislo_textu == 1:
    n_slov_1 = len(re.findall(r"\w+", TEXTS[0]))
    n_versalka_1 = len(re.findall("[A-Z]\w+", TEXTS[0]))
    n_versalky_1 = len(re.findall("\w[A-Z]", TEXTS[0]))
    n_minusky_1 = len(re.findall("\w[a-z]", TEXTS[0]))
    n_cisel_1 = len(re.findall("\d+", TEXTS[0]))
    vsechna_cisla_get_1 = (re.findall("\d+", TEXTS[0]))
    vsechna_cisla_int_1 = [int(i) for i in vsechna_cisla_get_1]
    vsechna_cisla_sum_1 = sum(vsechna_cisla_int_1)
    print("  Počet slov: " +  str(n_slov_1))
    print("  Počet slov začínajících velkým písmenem: " + str(n_versalka_1))
    print("  Počet slov psaných velkými písmeny: " + str(n_versalky_1))
    print("  Počet slov psaných malými písmeny: " + str(n_minusky_1))
    print("  Počet čísel: " + str(n_cisel_1))
    print("  Suma všech čísel: " + str(vsechna_cisla_sum_1))
    print(lem)
    print(graf_lem)
    print(lem)
    n_graf_slov_1 = (re.findall(r"\w+", TEXTS[0]))
    for delka_slova in n_graf_slov_1:
        graf_1 = len(delka_slova) * "*"
        print(graf_1)
elif cislo_textu == 2:
    n_slov_2 = len(re.findall(r"\w+", TEXTS[1]))
    n_versalka_2 = len(re.findall("[A-Z]\w+", TEXTS[1]))
    n_versalky_2 = len(re.findall("\w[A-Z]", TEXTS[1]))
    n_minusky_2 = len(re.findall("\w[a-z]", TEXTS[1]))
    n_cisel_2 = len(re.findall("\d+", TEXTS[1]))
    vsechna_cisla_get_2 = (re.findall("\d+", TEXTS[1]))
    vsechna_cisla_int_2 = [int(i) for i in vsechna_cisla_get_2]
    vsechna_cisla_sum_2 = sum(vsechna_cisla_int_2)
    print("  Počet slov: " +  str(n_slov_2))
    print("  Počet slov začínajících velkým písmenem: " + str(n_versalka_2))
    print("  Počet slov psaných velkými písmeny: " + str(n_versalky_2))
    print("  Počet slov psaných malými písmeny: " + str(n_minusky_2))
    print("  Počet čísel: " + str(n_cisel_2))
    print("  Suma všech čísel: " + str(vsechna_cisla_sum_2))
    print(lem)
    print(graf_lem)
    print(lem)
    n_graf_slov_2 = (re.findall(r"\w+", TEXTS[1]))
    for delka_slova in n_graf_slov_2:
        graf_2 = len(delka_slova) * "*"
        print(graf_2)
elif cislo_textu == 3:
    n_slov_3 = len(re.findall(r"\w+", TEXTS[2]))
    n_versalka_3 = len(re.findall("[A-Z]\w+", TEXTS[2]))
    n_versalky_3 = len(re.findall("\w[A-Z]", TEXTS[2]))
    n_minusky_3 = len(re.findall("\w[a-z]", TEXTS[2]))
    n_cisel_3 = len(re.findall("\d+", TEXTS[2]))
    vsechna_cisla_get_3 = (re.findall("\d+", TEXTS[2]))
    vsechna_cisla_int_3 = [int(i) for i in vsechna_cisla_get_3]
    vsechna_cisla_sum_3 = sum(vsechna_cisla_int_3)
    print("  Počet slov: " +  str(n_slov_3))
    print("  Počet slov začínajících velkým písmenem: " + str(n_versalka_3))
    print("  Počet slov psaných velkými písmeny: " + str(n_versalky_3))
    print("  Počet slov psaných malými písmeny: " + str(n_minusky_3))
    print("  Počet čísel: " + str(n_cisel_3))
    print("  Suma všech čísel: " + str(vsechna_cisla_sum_3))
    print(lem)
    print(graf_lem)
    print(lem)
    n_graf_slov_3 = (re.findall(r"\w+", TEXTS[2]))
    for delka_slova in n_graf_slov_3:
        graf_3 = len(delka_slova) * "*"
        print(graf_3)
else:
    print("  Nezvolil si číslo textu z nabídky. Program je ukončen.")
    sys.exit()

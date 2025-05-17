from tabor import Tabor

def adatokat_beolvas(fileNev):
    taborok = []
    with open(fileNev, encoding='utf-8') as f:
        for sor in f:
            if sor.strip():
                parts = sor.strip().split('\t')
                taborok.append(Tabor(*parts))
    return taborok

taborok = adatokat_beolvas("taborok.txt")

# for t in taborok:
#     print(t)

def masodik_feladat():
    count = len(taborok)
    elso_tabor_temaja = taborok[0].tema
    utolso_tabor_temaja = taborok[-1].tema

    print(f"A táborok száma: {count} \n A sorban az első tábor témája: {elso_tabor_temaja} \n Az utolsó témája: {utolso_tabor_temaja}")

def harmadik_feladat():
    zenei_taborok = [t for t in taborok if t.tema == "zenei"]

    if zenei_taborok:
        print("A zenei táborok kezdete: \n")
        for zt in zenei_taborok:
            print(f"{zt.kezdo_honap} . {zt.kezdo_nap}")
    else:
        print("Nincs ilyen tábor")

def negyedik_feladat():
    max_letszam = max(len(t.diakok) for t in taborok)

    # max_letszam = 0
    # for t in taborok:
    #     if len(t.diakok) > max_letszam:
    #         max_letszam = len(t.diakok)

    maxi_taborok = [t for t in taborok if len(t.diakok) == max_letszam]

    # maxi_taborok = []
    # for t in taborok:
    #     if len(t.diakok) == max_letszam:
    #         maxi_taborok.append(t)

    for t in maxi_taborok:
        print(f"{t.kezdo_honap}.{t.kezdo_nap} -- {t.tema}")

    

def sorszam(honap: int, nap: int):
    if honap == 6:
        return nap - 15
    elif honap == 7:
        return 15 + nap
    elif honap == 8:
        return 46 + nap
    
def hatodik_feladat():
    honap = int(input("Hónap: "))
    nap = int(input("Nap: "))

    ezen_a_napon = sum(t for t in taborok if sorszam(honap,nap) == sorszam(int(t.kezdo_honap),int(t.kezdo_nap)))

    # ezen_a_napon = 0
    # for t in taborok:
    #     if sorszam(honap,nap) == sorszam(int(t.kezdo_honap),int(t.kezdo_nap)):
    #         ezen_a_napon += 1


    print(f"Ezen a napon pontosan {ezen_a_napon}db tábor kezdődik")

def hetedik_feladat():
    tanulo_betujele = input("Adja meg a tanuló betűjelét: ").strip().upper()

    tanulo_taborai = [t for t in taborok if tanulo_betujele in t.diakok]

    tanulo_taborai.sort(key=lambda t: int(t.kezdo_honap))

    with open("egytanulo.txt", "w", encoding='utf-8') as f:
        for t in tanulo_taborai:
            f.write(f"{t.kezdo_honap}.{t.kezdo_nap} - {t.zaro_honap}.{t.zaro_nap}\n")
    
    utkozes = False
    if not tanulo_taborai:
        print("A tanuló egy tábor iránt sem érdeklődött.")
    else:
        if len(tanulo_taborai) == 1:
            print("Mivel a tanuló csak egy táborba jelentkezett, nincs ütközés")
        else:
            for i in range(1, len(tanulo_taborai)):
                elozo = tanulo_taborai[i-1]
                aktualis = tanulo_taborai[i]
                if int(aktualis.kezdo_honap) <= int(elozo.zaro_honap) and int(aktualis.kezdo_nap) <= int(elozo.zaro_nap):
                    utkozes = True
                    break
            if utkozes:
                print("Van ütközés")
            else:
                print("Nincs ütközés")

hetedik_feladat()








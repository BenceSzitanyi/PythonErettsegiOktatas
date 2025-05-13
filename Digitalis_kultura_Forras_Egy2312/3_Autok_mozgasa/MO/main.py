from auto import Auto

def autokat_beolvas(fajl):
    autok = []
    with open(fajl, encoding='utf-8') as f:
        for sor in f:
            if sor.strip():
                parts = sor.strip().split('\t')
                autok.append(Auto(*parts))
    return autok


autok = autokat_beolvas("jeladas.txt")


print(autok[-1].ora + ":" + autok[-1].perc + " - " + autok[-1].rendszam)

def elso_rendszam():
    elso_rendszam = autok[0].rendszam
    # idopontok = [
    #     f"{j.ora:02}:{j.perc:02}"
    #     for j in autok
    #     if j.rendszam == elso_rendszam
    # ]

    idopontok = []
    for a in autok:
        if a.rendszam == elso_rendszam:
            idopontok.append(f"{a.ora}:{a.perc}")

    print(elso_rendszam)
    print(" ".join(idopontok))

def idopontban_darab_jeladas():
    ora = input("Adja meg az órát: ")
    perc = input("Adja meg a percet: ")

    db = 0

    for a in autok:
        if a.ora == ora and a.perc == perc:
            db += 1 #db++
    
    print(f"Az ön által megadott időpontban {db}db jelzés érkezett")
def rovidebb_idopontban_darab():
    ora = input("Ora: ")
    perc = input("Perc: ")

    db = sum(1 for a in autok if a.ora == ora and a.perc == perc)
#print(autok[376].ora + " " + autok[376].perc)


def legnagyobb_sebesseg():
    legnagyobb_sebesseg = max(a.sebesseg for a in autok)
    rendszamok = [a.rendszam for a in autok if a.sebesseg == legnagyobb_sebesseg]

def tavolsagos_nyelvtani_csoda():
    rendszam = input("Adjá renccámot: ")
    auto_jelek = [a for a in autok if a.rendszam == rendszam]

    if not auto_jelek:
        print("Nincs ilyen autó te szerencsétlen")
        return
    
    #idorendbe allito
    auto_jelek.sort(key = lambda a: (a.ora, a.perc))

    print(f"{rendszam} jármű jelzései: ")
    tav = 0.0
    elozo_ido = auto_jelek[0].ora * 60 + auto_jelek[0].perc
    elozo_sebesseg = auto_jelek[0].sebesseg

    for aj in auto_jelek:
        aktualis_ido = aj.ora * 60 + aj.prec
        eltelt_perc = aktualis_ido - elozo_ido
        eltelt_ora = eltelt_perc / 60

        tav += elozo_sebesseg * eltelt_ora
        print(f"{aj.ora}:{aj.perc} - {tav} km")
        elozo_ido = aktualis_ido
        elozo_sebesseg = aj.sebesseg


def kiiro():
    from collections import defaultdict
    jarmuvek = defaultdict(list)

    for a in autok:
        jarmuvek[a.rendszam].append(a)

    
    with open("asd.txt", "w", encoding='utf-8') as f:
        for rendszam, jelek in jarmuvek.items():
            jelek.sort(key=lambda j: (j.ora, j.perc))
            elso = jelek[0]
            utolso = jelek[-1]
            f.write(f"{rendszam} {elso.ora}:{elso.perc}  |  {utolso.ora}:{utolso.perc}\n")

kiiro()
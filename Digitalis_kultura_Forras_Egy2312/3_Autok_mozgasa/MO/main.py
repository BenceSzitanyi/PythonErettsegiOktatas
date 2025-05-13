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
for auto in autok:
    print(auto)
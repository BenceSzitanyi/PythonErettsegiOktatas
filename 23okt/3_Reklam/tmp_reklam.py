#1. feladat
fajl=open('rendel.txt', 'r', encoding='utf-8')
rendel=[]
for sor in fajl:
    rendel.append(sor.strip().split(' '))
fajl.close()

# with open("rendel.txt","r",encoding='utf-8') as f:
#     for sor in f:
#         print(sor) -------> Blokkos fájl megnyitás


print('2. feladat')
print(f'A rendelések száma: {len(rendel)}')

print('3. feladat')
adott_nap=[]
nap=input('Adj meg egy napot! ')
for i in range(len(rendel)):
    if nap==rendel[i][0]:
        adott_nap.append(rendel[i])
print(len(adott_nap))

# for r in rendel:
#     r[0]

print('4. feladat')

# hiany=0
# nem=[]
# for i in range(len(rendel)):
#     if rendel[i][1]=='NR':
#         nem.append(rendel[i])
# n=nem[0][0]
# for i in range(len(nem)):
#     if int(nem[i][0])-int(n)>1:
#         hiany+=1
#     n=nem[i][0]
# print(hiany)

nincs_rendeles_db = 0
nem_reklamozott_varos = []
for r in rendel:
    if r[1] == "NR":
        nem_reklamozott_varos.append(r)

for i in range(1,len(nem_reklamozott_varos)):
    elozo = nem_reklamozott_varos[i-1]
    aktualis = nem_reklamozott_varos[i]
    if int(aktualis[0]) - int(elozo[0]) > 1:
        nincs_rendeles_db += int(aktualis[0]) - int(elozo[0])

print('5. feladat')
legnagyobb=0
for i in range(len(rendel)):
    if int(rendel[i][2])>int(legnagyobb):
        legnagyobb=rendel[i][2]
ln=[]
for i in range(len(rendel)):
    if int(rendel[i][2])==int(legnagyobb):
        ln.append(rendel[i])
print(f'Lenagyobb: {legnagyobb}, elsö nap: {ln[0][0]}')

#6. feladat
def osszes(varos, nap):
    # db=0
    # for i in range(len(rendel)):
    #     if rendel[i][0]==nap and rendel[i][1]==varos:
    #         db= db+ int(rendel[i][2])
    # return db

    rendelesek_osszege = 0
    for r in rendel:
        if int(r[0]) == nap and r[1] == varos:
            rendelesek_osszege += int(r[2])
    return rendelesek_osszege

print('7. feladat')
nap=21
varos1='PL'
varos2='TV'
varos3='NR'
db1=osszes(varos1,nap)
db2=osszes(varos2,nap)
db3=osszes(varos3,nap)
print(f'Rendelések száma a {nap}. napon: {varos1}: {db1}, {varos2}: {db2}, {varos3}: {db3}')

print('8. feladat')
print(f'Napok   1..10   11..20  21..30')
elsopl=0
masodikpl=0
harmadikpl=0

elsotv=0
masodiktv=0
harmadiktv=0

elsonr=0
masodiknr=0
harmadiknr=0
# for i in range(len(rendel)):
#     if rendel[i][1]=='PL' and int(rendel[i][0])<11:
#         elsopl=elsopl+int(rendel[i][2])
#     if rendel[i][1]=='PL'and 10<int(rendel[i][0])<21:
#         masodikpl=masodikpl+int(rendel[i][2])
#     if rendel[i][1]=='PL' and int(rendel[i][0])>20:
#         harmadikpl=harmadikpl+int(rendel[i][2])
# print(f'PL  {elsopl}    {masodikpl}    {harmadikpl}')
# for i in range(len(rendel)):
#     if rendel[i][1]=='TV':
#         if int(rendel[i][0])<11:
#             elsotv=elsotv+int(rendel[i][2])
#         if 10<int(rendel[i][0])<21:
#             masodiktv=masodiktv+int(rendel[i][2])
#         if int(rendel[i][0])>20:
#             harmadiktv=harmadiktv+int(rendel[i][2])
# for i in range(len(rendel)):
#     if rendel[i][1]=='NR':
#         if int(rendel[i][0])<11:
#             elsonr=elsonr+int(rendel[i][2])
#         if 10<int(rendel[i][2])<21:
#             masodiknr=masodiknr+int(rendel[i][2])
#         if int(rendel[i][0])>20:
#             harmadiknr=harmadiknr+int(rendel[i][2])

for r in rendel:
    if r[0] < 11:
        if r[1] == "PL":
            elsopl += int(r[2])
        elif r[1] == "TV":
            elsotv += int(r[2])
        elif r[1] == "NR":
            elsonr += int(r[2])
    elif r[0] < 21:
        if r[1] == "PL":
            masodikpl += int(r[2])
        elif r[1] == "TV":
            masodiktv += int(r[2])
        elif r[1] == "NR":
            masodiknr += int(r[2])
    else:
        if r[1] == "PL":
            harmadikpl += int(r[2])
        elif r[1] == "TV":
            harmadiktv += int(r[2])
        elif r[1] == "NR":
            harmadiknr += int(r[2])

with open('valami.txt','w',encoding='utf-8') as f:
    f.write(f"Napok \t 1..10 \t 11..20 \t 21..30 \n  PL \t {elsopl} \t {masodikpl} \t {harmadikpl} \n ")

class Verseny:
    def __init__(self,datum,nagydij,helyezes,befejezett_kor,pont,csapat,celbaert,hatrany,hibaoka):
        self.datum = datum
        self.nagydij=nagydij
        self.helyezes=helyezes
        self.befejezett_kor=befejezett_kor
        self.pont=pont
        self.csapat=csapat
        self.celbaert=celbaert
        self.hatrany=hatrany
        self.hibaoka=hibaoka

f = open("kimi.csv","rt",encoding="utf-8")
adat = []
for sor in f:
    sor  = sor.strip().split(";")
    adat.append(Verseny(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5],sor[6],sor[7],sor[8]))

print(f"3. feladat: {len(adat)-1}")



print("4. feladat: Magyar Nagydíj helyezésével")

for verseny in adat:
    if verseny.nagydij == "Magyar Nagydíj":
        if verseny.celbaert == "I":
            print(f"\t{verseny.datum} : {verseny.helyezes}. hely")


print("5. feladat: Hibastatisztika")


hiba = {}

for verseny in adat:   
    if verseny.hibaoka in hiba:
        hiba[verseny.hibaoka] += 1
    else:
        hiba[verseny.hibaoka] = 1

for k,v in hiba.items():
    if k != "":
        if v > 1:
            print(f"\t{k}: {v}")
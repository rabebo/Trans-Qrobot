ty =[1]
tz = [1]
#######################################
#heterozygotes remove the heterozygote values before excluding on the panal.
#######################################
def heterozygotes(yVal, xVal):
    for count, ele in enumerate(yVal):
        #print("Current Y list value in this loop cycle:" + str(ele))
        if yVal[count] == xVal[count] == 1: yVal[count] = xVal[count] = 0 #this is added recently
heterozygotes(ty, tz)
# Batch No:8664158
# Expiry Date: 23/08/2021
# 3 ABT cells
# Batch No:8242180
# Expiry Date: 30/08/2021
DI =  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
Leb = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
Lea = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0]
P1 =  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
s =   [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1]
S =   [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0]
N =   [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
M =   [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
Jkb = [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1]
Jka = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
Fyb = [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
Fya = [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]
Kpa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k =   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
K =   [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]
Cw =  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
e =   [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
c =   [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
E =   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
C =   [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
D =   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
################################################
#You should use Heterozygos for phenotypign, Why?
#You should be able to read a weak reaction, some blood group may show dosage ?
def phenotyping():
    def PhenoPosControl():
        print ("please enter one of the following values for Pheotyping the Positive control")
        print ("D, C, E, c, e, Cw, K, k, Kpa, Fya, Fyb, Jka, Jkb, M, N, S, s, P1, Lea, Leb, DI")
        pos = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        z = input();
        print ("antithetical y or n")
        y = 0
        n = 1
        con = input();
        if con == y:
            print ("please input the antithetical")
            antithetical = input();
            def pheno1(yVal, xVal, zVal):
                n = 0
                for count, ele in enumerate(yVal):
                    n = n+1
                    if yVal[count] == xVal[count] == zVal[count]:
                        print ("ABT", n, "Heterozozygous")
            pheno1(pos, z, antithetical)
        if con == n:
            def pheno(yVal, xVal):
                n = 0
                for count, ele in enumerate(yVal):
                    n = n+1
                    if yVal[count] == xVal[count]:
                        print ("ABT", n);
            pheno(pos, z)
    PhenoPosControl()
    PhenoPosControl()
    PhenoPosControl()
    PhenoPosControl()
    def PhenoNegControl():
        print ("please enter one of the following values for Pheotyping the Negative control")
        print ("D, C, E, c, e, Cw, K, k, Kpa, Fya, Fyb, Jka, Jkb, M, N, S, s, P1, Lea, Leb, DI")
        neg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        z = input();
        def pheno(yVal, xVal):
            n = 0
            for count, ele in enumerate(yVal):
                n = n+1
                if yVal[count] == xVal[count]:
                    print ("ABT", n);
        pheno(neg, z)
    PhenoNegControl()
    PhenoNegControl()
    PhenoNegControl()
    PhenoNegControl()
    PhenoNegControl()
###############################################
print ("input 101 for phenotyping 2 to proceed with the code")
Ui = input ()
if Ui == 101:
    phenotyping()
else:
    print ("Welcome to Transfusion Lab")
    Y = []
    print ("enter cell 1")
    f = input()
    Y.append(f)
    print ("enter cell 2")
    f = input()
    Y.append(f)
    print ("enter cell 3")
    f = input()
    Y.append(f)
    print ("enter cell 4")
    f = input()
    Y.append(f)
    print ("enter cell 5")
    f = input()
    Y.append(f)
    print ("enter cell 6")
    f = input()
    Y.append(f)
    print ("enter cell 7")
    f = input()
    Y.append(f)
    print ("enter cell 8")
    f = input()
    Y.append(f)
    print ("enter cell 9")
    f = input()
    Y.append(f)
    print ("enter cell 10")
    f = input()
    Y.append(f)
    print ("enter cell 11")
    f = input()
    Y.append(f)

    compare = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    def ret(yVal, xVal):
        for count, ele in enumerate(yVal):
            if yVal[count] > xVal[count]: yVal[count] = xVal[count] = 1
    ret(Y, compare)
    print ("The Test value", Y)
################################################


################################################
#Exact match and crossing of on negative results
################################################
print ("D")
def exact(yVal, xVal):
    n = 0
    for count, ele in enumerate(yVal):
        if yVal[count] == xVal[count]:
            n = n+1
    Q = n/11
    precent = Q * 100
    print ("Match precentage", precent)
exact(Y, D)
print ("C")
exact(Y, C)
print ("E")
exact(Y, E)
#print ("c"), you can add stroke above
print ("c¯")
exact(Y, c)
print ("e")
exact(Y, e)
print ("Cw")
exact(Y, Cw)
print ("K")
exact(Y, K)
#print ("k"), you can add stroke above
print ("k¯")
exact(Y, k)
print ("Kp^a")
exact(Y, Kpa)
print ("Fy^a")
exact(Y, Fya)
print ("Fy^b")
exact(Y, Fyb)
print ("JK^a")
exact(Y, Jka)
print ("JK^b")
exact(Y, Jkb)
print ("M")
exact(Y, M)
print ("N")
exact(Y, N)
print ("S")
exact(Y, S)
print ("s")
exact(Y, s)
print ("P1")
exact(Y, P1)
print ("Le^a")
exact(Y, Lea)
print ("Le^b")
exact(Y, Leb)
print ("DI")
exact(Y, DI)
heterozygotes(S, s)
heterozygotes(M, N)
heterozygotes(Jka, Jkb)
heterozygotes(Fya, Fyb)
heterozygotes(K, k)
heterozygotes(E, e)
heterozygotes(C, c)

print ("___________________________")
print ("Di")
def excluder(yVal, xVal):
    for count, ele in enumerate(yVal):
        #print("Current Y list value in this loop cycle:" + str(ele))
        if yVal[count] < xVal[count]:
            print(str(xVal[count]), "Excluded");

excluder(Y, DI)
print ("Le^b")
excluder(Y, Leb)
print ("Le^a")
excluder(Y, Lea)
print ("P1")
excluder(Y, P1)
print ("s")
excluder(Y, s)
print ("S")
excluder(Y, S)
print ("N")
excluder(Y, N)
print ("M")
excluder(Y, M)
print ("JK^b")
excluder(Y, Jkb)
print ("JK^a")
excluder(Y, Jka)
print ("Fy^b")
excluder(Y, Fyb)
print ("Fy^a")
excluder(Y, Fya)
print ("Kp^a")
excluder(Y, Kpa)
print ("k¯")
excluder(Y, k)
print ("K")
excluder(Y, K)
print ("Cw")
excluder(Y, Cw)
print ("e")
excluder(Y, e)
print ("c¯")
excluder(Y, c)
print ("E")
excluder(Y, E)
print ("C")
excluder(Y, C)
print ("D")
excluder(Y, D)

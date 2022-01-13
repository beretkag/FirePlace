import csv
from os import system

system('cls')


file =open("otos.csv")
elso=True
data_array=[]
for row in file.readlines():
    if elso:
        elso=not elso
        continue
    data=[]
    data.append(int(row.split(';')[11]))
    data.append(int(row.split(';')[12]))
    data.append(int(row.split(';')[13]))
    data.append(int(row.split(';')[14]))
    data.append(int(row.split(';')[15]))
 
    data_array.append(data)


lehet_sor = []
for i in range(5):
    lehet_sor.append(0)

for i in range(len(data_array)):
    for j in range(5):
        lehet_sor[j] = data_array[i][j]
    for k in range(len(data_array)):
        x = 0
        y = 0
        for l in range(5):
            if lehet_sor[l] in data_array[k]:
                x+=1
            elif lehet_sor[l]-2 in data_array[k] or lehet_sor[l]+2 in data_array[k]:
                if not(lehet_sor[l]-2 in lehet_sor) and not(lehet_sor[l]+2 in lehet_sor):
                    y+=1
        if x == 4 and y == 1:
            print(f"{k+2} és {i+2}: ")
            for m in range(5):
                print(f"{data_array[k][m]} ", end="")
            print(" és  ", end="")
            for m in range(5):
                print(f"{lehet_sor[m]} ", end="")
            print()

print("Itt a vége!")


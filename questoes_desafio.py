
# Q1
indice = 13
soma = 0
k = 0
while k < indice:
    k = k + 1
    soma = soma + k
print(soma) #91


# Q2
def fibonnaci(num):
    f1, f2 = 1, 1
    
    if num == f1:
        print(num, 'in fibonnaci')
    else:
        count = f1
        while (count < num):
            f1, f2 = f2, f1 + f2
            count = f1
            
            if (count == num):
                print("in fibonnaci")
                break
        
        if (num != count):
            print("not fibonnaci")


entrada = int(input())
fibonnaci(entrada)

# Q3


a) 1, 3, 5, 7, 9  

b) 2, 4, 8, 16, 32, 64, 128  

c) 0, 1, 4, 9, 16, 25, 36, 49  

d) 4, 16, 36, 64, 100  

e) 1, 1, 2, 3, 5, 8, 13  

f) 2,10, 12, 16, 17, 18, 19, 20

# Q4

a)
0 + 110 x km/h = 100 - 80 x km/h
190 x km = 100
x = 0,53

Como o caminhão esta fazendo o percurso de Franca para Ribeirão, após o instante 0,53 horas,
o caminhão estara mais perto


b) Adicionando o equivalente a 10 min ao percurso do caminhão, temos que 13,6 + 100, logo:

    110x=113,6 - 80x
    190x=113,6
    x = 0,6

O caminhão estará mais proximo de ribeirão após 0,6 horas


# Q5

def inverter(entrada):
    tamanho = len(entrada)
    out = ""
    for i in range(1, tamanho + 1):
        out += entrada[tamanho - i]
    
    return out
entrada = input()
print(inverter(entrada))


letras = "abcdefghijklmnopqrstuvwxyz"
operacoes = {"AND":"and","OR":"or","XOR":"^","Xor":"^","NOT":"not"}

def evalu(s, corres):
    t = s
    for j in range(0, len(corres[0])):
        t = t.replace(corres[1][j], str(corres[0][j]))


    for key in operacoes:
        t = t.replace(key, operacoes[key])


    answer = {True:1, False:0,1:1,0:0}
    return(corres[0], answer[eval(t)])

while True:
    try:
        expre = input("--> ")
        print("\n")
        variaveis = []
        
        for letter in expre:
            if letter in letras and letter not in variaveis:
                variaveis.append(letter)

        variaveis = sorted(variaveis)
        quantia = len(variaveis)

        for vari in variaveis:
            print(vari," ", end="")
        print("SAÍDA: ")

        for i in range(0, 2**quantia):
            j = i
            answer = [0 for i in range(0, quantia)]

            pos = 0
            while j != 0:
                answer[pos] = (int(j%2))
                j = j//2 
                pos += 1
            resposta = evalu(expre, [answer, variaveis])
            
            for num in resposta[0]:
                print(num, " " ,end="")
            print(resposta[1])
        print("\n")
    except:
        print("escreva certo, piranha.")
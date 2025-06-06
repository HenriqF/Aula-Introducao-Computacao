
v = ""
with open("tabela.txt", "r") as t:
    v = t.read()

foundTerms = False
terms = []

expressions = []
current = []
for char in v:
    if char == "\n":
        if foundTerms:
            expressions.append(current)
            current = []
        foundTerms = True
    elif char != " " and not foundTerms:
        terms.append(char)
    elif char == "1" or char == "0":
        current.append(char)  
expressions.append(current)
current = ""

resposta = []
for exp in expressions:
    if exp[-1] == "1":
        for i in range(len(exp)-1):
            char = exp[i]
            if char == "1":
                current += (str(terms[i]))
            else:
                current += (str("!"+terms[i]))
            current += "*"
            pass
        resposta.append(current[:-1])
        current = ""

processed = ""
for res in resposta:
    processed += "(" + res + ")"
    processed += " + "


print("\n\n" + processed[:-3] + f" = {terms[-1]}" + "\n\n")

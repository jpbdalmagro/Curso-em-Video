parentese_a = parentese_f = 0
expressao = str(input("Digite uma expressão: ")).strip()

for e in expressao:
    if e == '(':
        parentese_a += 1
    if e == ')':
        parentese_f += 1
        if parentese_a == 0:
            break

if parentese_f == parentese_a:
    print(f"A expressão {expressao} é válida.")
else:
    print(f"A expressão {expressao} não é válida.")

from random import choice
lista_alunos = []
aluno = input('Nome do primeiro aluno: ')
lista_alunos.append(aluno)
aluno = input('Nome do segundo aluno: ')
lista_alunos.append(aluno)
aluno = input('Nome do terceiro aluno: ')
lista_alunos.append(aluno)
aluno = input('Nome do quarto aluno: ')
lista_alunos.append(aluno)

aluno_sorteado = choice(lista_alunos)
print('O aluno escolhido foi {}.'.format(aluno_sorteado))
from random import shuffle
lista_alunos = []
aluno = input('Nome do primeiro aluno: ')
lista_alunos.append(aluno)
aluno = input('Nome do segundo aluno: ')
lista_alunos.append(aluno)
aluno = input('Nome do terceiro aluno: ')
lista_alunos.append(aluno)
aluno = input('Nome do quarto aluno: ')
lista_alunos.append(aluno)
shuffle(lista_alunos)

print('A ordem de apresentação será {}'.format(lista_alunos))
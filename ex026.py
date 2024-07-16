frase = str(input('Digite uma frase: ')).strip().lower()
print('Na sua frase a letra "A" aparece {} vezes.'.format(frase.count('a')))
print('A primeira vez que o a aparece é na {} letra.'.format(frase.find('a') + 1))
print('A ultima vez que a letra "A" aparece é na {} letra.'.format(frase.lower().rfind('a') - frase.count(' ') + 1))

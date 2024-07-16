from datetime import date

ano_nasc = int(input('Que ano o atleta nasceu? '))
idade = date.today().year - ano_nasc
print(idade)
if idade <= 9:
    print('O atleta se caracteriza como \033[36mMIRIM\033[m.')
elif idade <= 14:
    print('O atleta se classifica como \033[36mINFANTIL\033[m.')
elif idade <= 19:
    print('O atleta se classifica como \033[36mJUNIOR\033[m.')
elif idade <= 25:
    print('O atleta se classifica como \033[36mSENIOR\033[m.')
else:
    print('O atleta se classifica como \033[36mMASTER\033[m.')

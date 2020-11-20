from math import log10
#Percentual de Gordura

print('\033[34m=\033[m' * 35)
print('\033[33m          Digite Seus Dados\033[m')
print('\033[34m=\033[m' * 35 )

altura = float(input('Altura: '))
peso = float(input('Peso: '))
idade = int(input('Idade: '))
abdomen = float(input('Abdômen: '))
pescoco = float(input('Pescoço: '))
totalgordura = 495 / ( 1.0324 - 0.19077 * log10( abdomen - pescoco) + 0.15456 * log10( altura ) ) - 450

print('\033[34m=\033[m' * 35)
print('\033[33m   Percentual de Gordura Corporal\033[m')
print('\033[34m=\033[m' * 35 )

print ('Percentual de gordura é \033[33m {:.2f}% \033[m'.format(totalgordura))

gorda = peso * (totalgordura / 100)
print('Massa Gorda = {:.2f}kg'.format(gorda))
magra = peso - gorda
print('Massa Magra = {:.2f}kg'.format(magra))

if totalgordura >= 27:
	print('\033[31mPrecisa se cuidar, você está obeso.\033[m')
elif totalgordura >= 22 < 27:
	print('\033[33m Você está com sobrepeso. \033[m ')
elif totalgordura >=18 < 22:
	print('\033[32m Você é uma pessoa saudável! \033[m')
elif totalgordura >= 12 < 18:
	print('\033[34m Está na Busca do Six pack. \033[m')
elif totalgordura < 12:
	print('\033[32m Tem um baixo Percentual de gordura.\033[m\n \033[33m Se você não for Atleta procure um médico.')

#Ingestão de Água
print('\033[34m=\033[m' * 35)
print('\033[33m    Água Necessidade Diária\033[m')
print('\033[34m=\033[m' * 35 )

agua = peso * 32
print('Beba {} ml de água por dia'.format(agua))

#Taxa Metabolica Basal
print('\033[34m=\033[m' * 35)
print('\033[33m    Taxa Metabolica Basal TMB\033[m')
print('\033[34m=\033[m' * 35 )

tmb = (13.75 * peso) + (5 * altura) - (6.76 * idade) + 66.5 

print ('Manter Peso = {:.1f} kcal dia'.format(tmb))
ganhar = tmb + 500
print ('Ganhar Massa = {:.1f} kcal dia'.format(ganhar))
eliminar = tmb - 500
print ('Emagrecer = {:.1f} kcal dia'.format(eliminar))


import random
import string

tamanho = int(input('Digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-+=;:.,\/<>?'

rnd = random.SystemRandom()

print('Nova Senha Gerada com Sucesso! A nova Senha é: ' + ''.join(rnd.choice(chars) for i in range(tamanho)))
import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O Arquivo: {arquivo1} é diferente do Arquivo: {arquivo2} ')
    print('o hash do arquivo a.txt é: ', hash1.hexdigest())
    print('o hash do arquivo b.txt é: ', hash2.hexdigest())

else:
    print(f'O Arquivo: {arquivo1} é igual ao Arquivo: {arquivo2} ')
    print('o hash do arquivo a.txt é: ', hash1.hexdigest())
    print('o hash do arquivo b.txt é: ', hash2.hexdigest())
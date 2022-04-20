import ctypes

pasta = input('Digite o caminho da Pasta a ser ocultada. EX:(C:/pasta): ')

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print('Arquivo foi Ocultado')
else:
    print('Arquivo não foi Ocultado')
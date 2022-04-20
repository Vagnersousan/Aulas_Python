import os ##importa o módulo ou biblioteca OS (integra os programas e recursos do S.O)

print('#' * 60) ##Imprimindo #60 vezes

ip_ou_host = input('Digite o IP ou Host a ser Verificado: ')
##criamos uma variável que vai receber do usuário um IP
print('-' * 60) ##Imprimindo - 60 vezes
os.system('ping -n 6 {}' .format(ip_ou_host)) ##Chamando System da Biblioteca OS - Comando PING (-n : num de pacotes
# que serão 6 {})
print('-' * 60) ##Imprimindo - 60 vezes

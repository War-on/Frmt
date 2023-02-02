import os
from time import sleep
os.system('clear')

# cores
vm = '\033[31m' # vermelho
vd = '\033[32m' # verde 
a = '\033[33m' # amarelo
az = '\033[34m' # azul
r = '\033[35m' # roxo
cn = '\033[36m' #ciano
t = '\033[m' # final cor

print(f'''
                 {az}______________________
                |                      |
                |{vd}$ Modo de atualização{az} |
                |______________________|
                |                      |
                |{vd}$ ᵉQ⃟ᵘⁱᵖᵉ ⁱⁿᵛᵃˢᵒʳᵉˢ{az}    |
                |______________________|{t}
                
''')

while True:
    print(f'   >>{a}${t}<< {az}Baixando nova versão...{t}')
    sleep(3)
    os.system('cd ~/Frmt;git clone https://github.com/War-on/Frmt &> /dev/null')
    if os.path.exists('/data/data/com.termux/files/home/Frmt/Frmt') == False:
        print(f'{vm}[x] ERROR não foi possível baixar nova versão.{t} \n{a}[!] Verifique sua conexão com a internet ou se o git esta instalado e tente novamente{t}.')
        sleep(5)
        break
    print(f'   >>{a}${t}<< {az}Removendo versão antiga...{t}')
    os.system('rm -rf ~/Frmt/Frmt.py;rm -rf ~/Frmt/vidfn.py')
    sleep(3)
    os.system('mv ~/Frmt/Frmt/Frmt.py ~/Frmt;mv ~/Frmt/Frmt/vidfn.py ~/Frmt')
    print(f'   >>{a}${t}<< {az}Adicionando permissão...{t}')
    sleep(3)
    os.system('cd ~/Frmt;chmod 777 *')
    if os.path.exists('/data/data/com.termux/files/home/Frmt/Frmt.py') == True:
        print(f'\n>>{vd}[✔]{t}<< {vd}Atualização concluida.{t}')
        sleep(3)
        print(f'>>{vd}[*]{t}<< {vd}Abrindo ferramenta...{t}')
        sleep(5)
        os.system('cd ~/Frmt;python Frmt.py')
        break
    else:
        print(f'\n   {vm}[x] ERROR: não foi possível atualizar!{t}')
        sleep(3)
        break
 
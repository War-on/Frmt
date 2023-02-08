import os
from time import sleep
import subprocess

def atualizar_Frmt():
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
                |{vm}$ ᵉQ⃟ᵘⁱᵖᵉ ⁱⁿᵛᵃˢᵒʳᵉˢ{az}     |
                |______________________|{t}
''')

    while True:
        print(f'   >>{a}${t}<< {az}Removendo versão antiga...{t}')
        sleep(3)
        os.system('rm -rf ~/Frmt')

        print(f'   >>{a}${t}<< {az}Baixando nova versão...{t}')
        sleep(3)
        subprocess.run('cd ~/;git clone https://github.com/War-on/Frmt /dev/null', shell=True)
        if os.path.exists('/data/data/com.termux/files/home/Frmt/') == False:
            print(f'{vm}[x] ERROR não foi possível baixar nova versão.{t} \n{a}[!] Verifique sua conexão com a internet ou se o git esta instalado e tente novamente{t}.')
            sleep(5)
            break
        else:
            print(f'   >>{a}${t}<< {az}Adicionando permissão...{t}')
            sleep(3)
            os.system('cd ~/Frmt;chmod +x *')
            print(f'\n>>{vd}[✔]{t}<< {vd}Atualização concluida.{t}')
            sleep(3)
            break

 
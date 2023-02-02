from time import sleep
import os, sys
import subprocess

# Modulos internos

from config import vidfn

# cores
vm = '\033[31m' # vermelho
vd = '\033[32m' # verde
a = '\033[33m' # amarelo
az = '\033[34m' # azul
r = '\033[35m' # roxo
cn = '\033[36m' #ciano
t = '\033[m' # final cor

def animacao():
      frase = f'{cn}###########################{t}\n'
      for i in list(frase):
            print(i, end='')
            sys.stdout.flush()
            sleep(0.1)

os.system('clear')
print(f'{cn}Verificando permissão...{t}')
sleep(3)
if os.path.exists('/data/data/com.termux/files/home/storage') == False:
      os.system('termux-setup-storage')
      sleep(10)
else:
      print(f'{vd}[✔] Permissão...........[Ok]{t}')
      sleep(1)
os.system('clear')

# Abrir programa de atualização

if os.path.exists('/data/data/com.termux/files/home/Frmt/config/upgradeArquivos.py') == True:
      from config import upgradeArquivos
      upgradeArquivos.atualizacao_arquivos()
      os.system('clear')
      os.system('rm -rf /data/data/com.termux/files/home/Frmt/config/upgradeArquivos.py')

# Abrir verificador de recursos?

while True:
      os.system('clear')
      rpt = str(input(f'{a}[!] Deseja fazer uma verificação de recursos? \n\nWaring:{t} Se caso seja a primeira vez, é recomendado fazer a verificação. \n\n[Y/n]: ')).lower().strip()

      if rpt == 'y':
            vidfn.recursos()
            break
      elif rpt == 'n':
            break
      elif rpt == '':
            vidfn.recursos()
            break
      elif rpt not in 'yn':
            print(f'{vm}[x] Opção invalida.{t}')
            sleep(2)
os.system('clear')
os.system('apt install python2 -y;apt install python3 -y')
while True:
      if os.path.exists('/data/data/com.termux/files/home/storage') == False:
            print(f'{vm}[x] ERROR: A permissão foi NEGADA! \n{a}[!] Aperte em permitir para continuar.{t}')
            break
      result = subprocess.run(['termux-info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

      if result.returncode == 0:
            version = None
            for line in result.stdout.decode().split("\n"):
                  if line.startswith("TERMUX_VERSION"):
                        version = line.split("=")[1]
                        break
            if version:
                  if version != '0.118.0':
                        print(f"{vm}[X] A versão do Termux é antiga{t}")
                        break
      os.system('clear')
      print(f'''
 {az} _____  {vm} ____   {a} __  __  {vd} _____ {t} 
 {az}|  ___| {vm}|  _ \  {a}|  \/  | {vd}|_   _|{t}
 {az}| |_    {vm}| |_) | {a}| |\/| | {vd}  | |  {t}
 {az}|  _|   {vm}|  _ <  {a}| |  | | {vd}  | | {vm}ᵉQ⃟ᵘⁱᵖᵉ ⁱⁿᵛᵃˢᵒʳᵉˢ{t}
 {az}|_|     {vm}|_| \_\ {a}|_|  |_| {vd}  |_|  {t}

''')
      print(f'''
[{r}01{t}] {a}ngrok{t}           [{r}06{t}] {a}Clownters.c{t}
[{r}02{t}] {a}sherlock{t}        [{r}07{t}] {a}Facebook-BruteForce{t}
[{r}03{t}] {a}toutatis{t}        [{r}08{t}] {a}zphisher{t}
[{r}04{t}] {a}wifite2(root){t}   [{r}09{t}] {a}nmap (sqlmap){t}
[{r}05{t}] {a}Kiny-painel{t}     [{r}10{t}] {a}m-wiz (para instalar metasploit){t}

[{vm}98{t}] {a}Atualizar (Frmt){t}
[{vm}99{t}] {a}link do grupo (WhatsApp){t}
[{vm}00{t}] {a}SAIR{t}
''')
      
      print(f'{cn}#{t}'*27)
      nm = str(input(f'{vd}[?] {az}select option --> {r}')).strip()
      if nm == '1' or nm == '01':
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}ngrok{t}]...')
            animacao()
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}ngrok{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/termux-ngrok') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/Marcel0Sousa/termux-ngrok')
            frase3 = f'{cn}###########################{t}\n'
            for i3 in list(frase3):
                  print(i3,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/termux-ngrok') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [ngrok]. {a}\n[!] Verifique se o [git] está instalado corretamente ou se está conectado a internet!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...{t}')
                  sleep(3)
                  os.system('cd ~/termux-ngrok;chmod 777 *')
                  frase4 = f'{cn}###########################{t}\n'
                  for i4 in list(frase4):
                        print(i4,end='')
                        sys.stdout.flush()
                        sleep(0.1)
                  os.system('cd ~/termux-ngrok;bash termux-ngrok.sh')
                  print(f'{vd}[*] Instalação concluida!{t}')
      elif nm == '2' or nm == '02':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}sherlock{t}]...')
            frase2 = f'{cn}###########################{t}\n'
            for i2 in list(frase2):
                  print(i2,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} baixando ferramenta{t} [{a}sherlock{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/sherlock') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/sherlock-project/sherlock.git')
            frase6 = f'{cn}###########################{t}\n'
            for i6 in list(frase6):
                  print(i6,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/sherlock') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [sherlock]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Preparando para instalar{t} [{a}requirements.txt{t}]...')
                  sleep(7)
                  os.system('cd ~/sherlock;python3 -m pip install -r requirements.txt')
                  frase8 = f'{cn}###########################{t}\n'
                  for i8 in list(frase8):
                        print(i8,end='')
                        sys.stdout.flush()
                        sleep(0.1)
                  print(f'{vd}[*] Instalação concluida!{t}')
                  frase9 = f'{cn}###########################{t}\n'
                  for i9 in list(frase9):
                        print(i9,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            while True:
                  ab = str(input(f'{vd}[?] {az}Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        nome = str(input(f'{vd}[?] {az}Ecreva um nome de alguma pessoa:{vd} '))
                        frase = f'{cn}###########################{t}\n'
                        for i in list(frase):
                              print(i,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        frase1 = f'{cn}###########################{t}\n'
                        for i1 in list(frase1):
                              print(i1,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        os.system('cd ~/;cd sherlock;python3 sherlock {}'.format(nome))
                        break
                  elif ab == 'n':
                        break
                  elif ab == '':
                        print(f'{cn}#{t}'*27)
                        print(f'{a}[!] Nada digitado!{t}')
                        sleep(1)
                  else:
                       print(f'{cn}#{t}'*27)
                       print(f'{vm}[x] Opcao invalida!{t}')
                       sleep(1)
            break
      elif nm == '3' or nm == '03':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}toutatis{t}]...')
            frase2 = f'{cn}###########################{t}\n'
            for i2 in list(frase2):
                  print(i2,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} instalando{t} [{a}pip install toutatis{t}]...')
            sleep(3)
            os.system('cd ~/;pip install toutatis')
            frase4 = f'{cn}###########################{t}\n'
            for i4 in list(frase4):
                  print(i4,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} baixando ferramenta{t} [{a}toutatis{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/toutatis') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/megadose/toutatis.git')
            frase5 = f'{cn}###########################{t}\n'
            for i5 in list(frase5):
                  print(i5,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/toutatis') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [toutatis]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*] Instalação concluida!{t}')
                  frase6 = f'{cn}###########################{t}'
                  for i6 in list(frase6):
                        print(i6,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'\n{a}[!]MODO DE USO: [toutatis -u (username) -s (instagramsessionid)]{t}')
            break
      elif nm == '00':
            break
      elif nm == '98':
            print(f'{cn}#{t}'*27)
            print(f'{vd}[*] Abrindo arquivos para upgrade da Ferramenta...{t}')
            sleep(2)
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            os.system('cd ~/Frmt;python upgradeFrmt.py')
      elif nm == '':
            print(f'\n   {a}[!] Nada foi digitado!{t}')
            sleep(1.3)
      elif nm == '99':
            print(f'{cn}#{t}'*27)
            print(f'{vd}[+] Abrindo link...{t}')
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            os.system('termux-open-url https://chat.whatsapp.com/DErbgi6cxVzByz9sCR1ITX')
      elif nm == '4' or nm == '04':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}wifite2{t}]...')
            frase1 = f'{cn}###########################{t}\n'
            for i1 in list(frase1):
                  print(i1,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}wifite2{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/wifite2') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/derv82/wifite2.git')
            frase3 = f'{cn}###########################{t}\n'
            for i3 in list(frase3):
                  print(i3,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/wifite2') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [wifite2]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/wifite2;chmod +x Wifite.py')
                  frase4 = f'{cn}###########################{t}\n'
                  for i4 in list(frase4):
                        print(i4,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'{vd}[*]{a} Instalando{t} [{a}wifite{t}]...')
            sleep(5)
            os.system('cd ~/;cd wifite2;python setup.py install')
            frase6 = f'{cn}###########################{t}\n'
            for i6 in list(frase6):
                  print(i6,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*] Instalação concluida!{t}')
            frase7 = f'{cn}###########################{t}\n'
            for i7 in list(frase7):
                  print(i7,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            break
      elif nm == '5' or nm == '05':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}Kiny-painel{t}]...')
            frase1 = f'{cn}###########################{t}\n'
            for i1 in list(frase1):
                  print(i1,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}Kiny-painel{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/Kinypainel') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/Kiny-Kiny/Kinypainel')
            frase3 = f'{cn}###########################{t}\n'
            for i3 in list(frase3):
                  print(i3,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/Kinypainel') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [Kinypainel]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/Kinypainel;chmod +x *')
                  frase4 = f'{cn}###########################{t}\n'
                  for i4 in list(frase4):
                        print(i4,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'{vd}[*] Instalação concluida!')
            frase5 = f'{cn}###########################{t}\n'
            for i5 in list(frase5):
                  print(i5,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{a}[!] Basta usar o comando [cd;cd Kinypainel] depois o comando [python3 main.py] para usar. \n{cn}####################{t} \n{az}USERNAME: {vd}YATO ou KING \n{az}PASSWORD:{vd} VirtualInsanity{t}')
            while True:
                  print(f'{cn}#{t}'*27)
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        frase = f'{cn}###########################{t}'
                        for i in list(frase):
                              print(i,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        os.system('cd ~/Kinypainel;python3 main.py')
                        break
                  elif ab == 'n':
                        break
                  elif ab == '':
                        print(f'{a}[!] Nada digitado!{t}')
                        sleep(1)
                  else:
                       print(f'{cn}#{t}'*27)
                       print(f'{vm}[x] Opção inválida!{t}')
                       sleep(1)
            break
      elif nm == '6' or nm == '06':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}Clownters.c{t}]...')
            frase1 = f'{cn}###########################{t}\n'
            for i1 in list(frase1):
                  print(i1,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}Clownters.c{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/Clownters.c') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/mike90s15/Clownters.c')
            frase3 = f'{cn}###########################{t}\n'
            for i3 in list(frase3):
                  print(i3,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/Clownters.c') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [Clownters.c]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...{t}')
                  sleep(3)
                  os.system('cd ~/Clownters.c;chmod +x *')
                  frase4 = f'{cn}###########################{t}\n'
                  for i4 in list(frase4):
                        print(i4,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'{vd}[*] Instalação concluida!')
            frase5 = f'{cn}###########################{t}\n'
            for i5 in list(frase5):
                  print(i5,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{a}[!] Para usar basta colocar o comando [cd;cd Clownters.c], depois o comando [./A1.sh].{t}')
            print(f'{cn}###########################{t}\n{az}username: {vd}342992a1{t} \n{az}password: {vd}MiKe{t}')
            while True:
                  print(f'{cn}#{t}'*27)
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        frase = f'{cn}###########################{t}'
                        for i in list(frase):
                              print(i,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        os.system('cd ~/Clownters.c;bash A1.sh')
                        break
                  elif ab == 'n':
                        break
                  elif ab == '':
                        print(f'{a}[!] Nada digitado!{t}')
                        sleep(1)
                  else:
                       print(f'{cn}#{t}'*27)
                       print(f'{vm}[x] Opcao invalida!{t}')
                       sleep(1)
            break
      elif nm == '7' or nm == '07':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}Facebook-BruteForce{t}]...')
            frase1 = f'{cn}###########################{t}\n'
            for i1 in list(frase1):
                  print(i1,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Baixando Ferramenta{t} [{a}Facebook-BruteForce{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/Facebook-BruteForce') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/IAmBlackHacker/Facebook-BruteForce')
            frase4 = f'{cn}###########################{t}\n'
            for i4 in list(frase4):
                  print(i4,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/Facebook-BruteForce') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [Facebook-BruteForce]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Instalando requisitos da ferramenta...{t}')
                  sleep(3)
                  os.system('cd ~/Facebook-BruteForce;python3 -m pip install requests bs4')
                  os.system('cd ~/Facebook-BruteForce;python3 -m pip install mechanize')
                  frase6 = f'{cn}###########################{t}\n'
                  for i6 in list(frase6):
                        print(i6,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'{vd}[*]{a} adicionando permissão...')
            sleep(3)
            os.system('cd ~/Facebook-BruteForce;chmod +x *')
            frase7 = f'{cn}###########################{t}\n'
            for i7 in list(frase4):
                  print(i7,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*] Instalação concluida!{t}')
            frase8 = f'{cn}###########################{t}\n'
            for i8 in list(frase8):
                  print(i8,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{a}[!] Para usar basta colocar o comando [cd;cd Facebook-BruteForce], depois o comando [python3 fb.py ou python fb2.py].{t}')
            while True:
                  print(f'{cn}#{t}'*27)
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        frase = f'{cn}###########################{t}'
                        for i in list(frase):
                              print(i,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        os.system('cd ~/Facebook-BruteForce;python fb.py')
                        break
                  elif ab == 'n':
                        break
                  elif ab == '':
                        print(f'{a}[!] Nada digitado!{t}')
                        sleep(1)
                  else:
                       print(f'{cn}#{t}'*27)
                       print(f'{vm}[x] Opcao invalida!{t}')
                       sleep(1)
            break
      elif nm == '8' or nm == '08':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*] {a}Preparando para instalar{t} [{a}zphisher{t}]...')
            frase1 = f'{cn}###########################{t}\n'
            for i1 in list(frase1):
                  print(i1,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}zphisher{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/zphisher') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/htr-tech/zphisher.git')
            frase3 = f'{cn}###########################{t}\n'
            for i3 in list(frase3):
                  print(i3,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/zphisher') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [zphisher]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:   
                  print(f'{vd}[*]{a} adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/zphisher;chmod +x *')
                  frase4 = f'{cn}###########################{t}\n'
                  for i4 in list(frase4):
                        print(i4,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'{vd}[*] Instalação concluida!')
            frase5 = f'{cn}###########################{t}\n'
            for i5 in list(frase5):
                  print(i5,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            while True:
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        frase = f'{cn}###########################{t}'
                        for i in list(frase):
                              print(i,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        os.system('cd ~/zphisher;./zphisher.sh')
                        break
                  elif ab == 'n':
                        break
                  elif ab == '':
                        print(f'{a}[!] Nada digitado!{t}')
                        sleep(1)
                        print(f'{cn}#{t}'*27)
                  else:
                       print(f'{cn}#{t}'*27)
                       print(f'{vm}[x] Opcao invalida!{t}')
                       sleep(2)
            break
      elif nm == '9' or nm == '09':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}nmap{t}]...')
            frase1 = f'{cn}###########################{t}\n'
            for i1 in list(frase1):
                  print(i1,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}nmap{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/sqlmap') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/sqlmapproject/sqlmap')
            frase4 = f'{cn}###########################{t}\n'
            for i4 in list(frase4):
                  print(i4,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/sqlmap') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [sqlmap]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/sqlmap;chmod +x *')
                  frase5 = f'{cn}###########################{t}\n'
                  for i5 in list(frase5):
                        print(i5,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'{vd}[*] Instalação concluida!')
            frase6 = f'{cn}###########################{t}\n'
            for i6 in list(frase6):
                  print(i6,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            while True:
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        frase = f'{cn}###########################{t}\n'
                        for i in list(frase):
                              print(i,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        url = str(input(f'{vd}[?]{a} Cole a [URL/LINK] aqui:{cn} '))
                        os.system('cd ~/sqlmap;python sqlmap.py -u {} --batch'.format(url))
                        break
                  elif ab == 'n':
                        break
                  elif ab == '':
                        print(f'{a}[!] Nada digitado!{t}')
                        sleep(1)
                        print(f'{cn}#{t}'*27)
                  else:
                       print(f'{cn}#{t}'*27)
                       print(f'{vm}[x] Opcao invalida!{t}')
                       sleep(1)
            break
      elif nm == '10':
            frase = f'{cn}###########################{t}\n'
            for i in list(frase):
                  print(i,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}m-wiz{t}]...')
            frase1 = f'{cn}###########################{t}\n'
            for i1 in list(frase1):
                  print(i1,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Instalando{t} [{a}pip lolcat{t}]...')
            sleep(3)
            os.system('cd ~/;pip install lolcat')
            frase7 = f'{cn}###########################{t}\n'
            for i7 in list(frase7):
                  print(i7,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}m-wiz{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/m-wiz') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/noob-hackers/m-wiz')
            frase3 = f'{cn}###########################{t}\n'
            for i3 in list(frase3):
                  print(i3,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            if os.path.exists('/data/data/com.termux/files/home/m-wiz') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [m-wiz]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break      
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/m-wiz;chmod +x *')
                  frase4 = f'{cn}###########################{t}\n'
                  for i4 in list(frase4):
                        print(i4,end='')
                        sys.stdout.flush()
                        sleep(0.1)
            print(f'{vd}[*] Instalação concluida!')
            frase5 = f'{cn}###########################{t}\n'
            for i5 in list(frase5):
                  print(i5,end='')
                  sys.stdout.flush()
                  sleep(0.1)
            while True:
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()[0]
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        frase = f'{cn}###########################{t}'
                        for i in list(frase):
                              print(i,end='')
                              sys.stdout.flush()
                              sleep(0.1)
                        os.system('cd ~/m-wiz;./m-wiz.sh')
                        break
                  elif ab == 'n':
                        break
                  elif ab == '':
                        print(f'{a}[!] Nada digitado!{t}')
                        sleep(1)
                        print(f'{cn}#{t}'*27)
                  else:
                       print(f'{cn}#{t}'*27)
                       print(f'{vm}[x] Opcao invalida!{t}')
                       sleep(1)
            break
      else:
            print(f'\n    {vm}[x] Opção inválida!{t}')
            sleep(1.3)
print(f'''\n    {a}bye :){t}''')
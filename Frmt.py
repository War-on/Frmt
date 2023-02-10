from time import sleep
import os, sys
import subprocess

# Modulos internos
from config import vidfn
from config import menu
from config import upgradeFrmt
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
            print(f'{vm}\n  [x] Opção invalida.{t}')
            sleep(2)

while True:
      if os.path.exists('/data/data/com.termux/files/home/Frmt/config/vcs_version.py') == True:
            from config import vcs_version
            os.system('clear')
            print(f'{vd}[*] Verifcando a versão...\n{t}')
            sleep(3)
            if vcs_version.version != '0.118.0':
                  print(f"{vm}\n[X] ERROR: A versão do Termux está desatualizado.{t}")
                  print(f'{a}\n[!] Acesse este link ({az}https://f-droid.org/repo/com.termux_118.apk{t}) {a}para baixar a versao mais atualizada do termux e continuar usando a ferramenta.{t}')
                  break
            elif vcs_version.version == '0.118.0':
                  print(f'{vd}\n[*] ---Versão ok---{t}')
                  sleep(3)
            else:
                  print(f"{vm}\n[X] ERROR: A versão do Termux está desatualizado.{t}")
                  print(f'{a}\n[!] Acesse este link ({az}https://f-droid.org/repo/com.termux_118.apk{t}) {a}para baixar a versao mais atualizada do termux e continuar usando a ferramenta.{t}')
                  break
      subprocess.run('rm -rf ~/Frmt/config/vcs_version.py',shell=True)
      if os.path.exists('/data/data/com.termux/files/home/storage') == False:
            print(f'{vm}[x] ERROR: A permissão foi NEGADA! \n{a}[!] Aperte em permitir para continuar.{t}')
            break
      os.system('clear')
      menu.menu()
      print(f'{cn}#{t}'*27)
      nm = str(input(f'{vd}[?] {az}select option --> {r}')).strip()
      if nm == '1' or nm == '01':
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}ngrok{t}]...')
            animacao()
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}ngrok{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/termux-ngrok') == True:
                  print(f'{vd}\n[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/Marcel0Sousa/termux-ngrok')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/termux-ngrok') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [ngrok]. {a}\n[!] Verifique se o [git] está instalado corretamente ou se está conectado a internet!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...{t}')
                  sleep(3)
                  os.system('cd ~/termux-ngrok;chmod 777 *')
                  animacao()
                  os.system('cd ~/termux-ngrok;bash termux-ngrok.sh')
                  if os.path.exists('/data/data/com.termux/files/usr/bin/ngrok') == True:
                        print(f'{vd}\n  [*] Instalação concluida!{t}')
                        sleep(5)
                  else:
                        print(f'{a}\n  [!] A instalação foi cancelada.{t}')
                        sleep(5)
      elif nm == '2' or nm == '02':
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}sherlock{t}]...')
            animacao()
            print(f'{vd}[*]{a} baixando ferramenta{t} [{a}sherlock{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/sherlock') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/sherlock-project/sherlock.git')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/sherlock') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [sherlock]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Instalando {t}[{a}requirements.txt{t}]...')

                  msg_error = subprocess.run('cd ~/sherlock;python3 -m pip install -r requirements.txt',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                  if msg_error.returncode == 0:
                        msg = None
                        for line in result.stdout.decode().split("\n"):
                              if line.startswith(" error"):
                                    msg = line.split(":")[1]
                                    break
                        if msg == "subprocess-exited-with-error":
                              animacao()
                              print(f'{a}[!] Instalação concluida com error!{t}')
                              break
                        else:
                              animacao()
                              print(f'{vd}[*] Instalação concluida.{t}')
                              break

                  else:
                        animacao()
                        print(f"{vm}[x] ERROR ao instalar {t}[{a}requirements.txt{t}]")
                        break


      elif nm == '3' or nm == '03':
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}toutatis{t}]...')
            animacao()
            print(f'{vd}[*]{a} instalando{t} [{a}pip install toutatis{t}]...')
            sleep(3)
            os.system('cd ~/;pip install toutatis')
            animacao()
            print(f'{vd}[*]{a} baixando ferramenta{t} [{a}toutatis{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/toutatis') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/megadose/toutatis.git')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/toutatis') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [toutatis]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*] Instalação concluida!{t}')
                  animacao()
            print(f'\n{a}[!]MODO DE USO: [toutatis -u (username) -s (instagramsessionid)]{t}')
            break
      elif nm == '00':
            break
      elif nm == '98':
            print(f'{cn}#{t}'*27)
            print(f'{a}[!] Verificando rede wi-fi...{t}')
            sleep(3)

            result = subprocess.run(['ping','-c','1','google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                  ping = None
                  for line in result.stdout.decode().split("\n"):
                        if line.startswith("ping"):
                              ping = line.split(":")[1]
                              break
                  if ping != 'unknown':
                        print(f'{vd}\n  [*] Abrindo arquivo para atualizar Ferramenta...{t}')
                        sleep(2)
                        upgradeFrmt.atualizar_Frmt()
                  else:
                        print(f'{vm}\n[x] ERROR: conect a uma rede wi-fi para atualizar a ferramenta.{t}')
                        sleep(5)
            else:
                  print(f'{vm}\n[x] ERROR: conect a uma rede wi-fi para atualizar a ferramenta.{t}')
                  sleep(5)

      elif nm == '':
            print(f'\n   {a}[!] Nada foi digitado!{t}')
            sleep(1.3)
      elif nm == '99':
            print(f'{cn}#{t}'*27)
            print(f'{vd}[+] Abrindo link...{t}')
            animacao()
            os.system('termux-open-url https://chat.whatsapp.com/DErbgi6cxVzByz9sCR1ITX')
      elif nm == '4' or nm == '04':
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}wifite2{t}]...')
            animacao()
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}wifite2{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/wifite2') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/derv82/wifite2.git')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/wifite2') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [wifite2]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/wifite2;chmod +x Wifite.py')
                  animacao()
                  print(f'{vd}[*] Instalação concluida!{t}')
                  animacao()
                  break
      elif nm == '5' or nm == '05':
            animacao()
            print(f'{vd}Iniciando modo de personalização...')
            sleep(5)
            animacao()
            subprocess.run('cd $HOME/Frmt/config;bash T-style.sh')
            break
      elif nm == '6' or nm == '06':
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}Clownters.c{t}]...')
            animacao()
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}Clownters.c{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/Clownters.c') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/mike90s15/Clownters.c')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/Clownters.c') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [Clownters.c]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...{t}')
                  sleep(3)
                  os.system('cd ~/Clownters.c;chmod +x *')
                  animacao()
            print(f'{vd}[*] Instalação concluida!')
            animacao()
            print(f'{a}[!] Para usar basta colocar o comando [cd;cd Clownters.c], depois o comando [./A1.sh].{t}')
            print(f'{cn}###########################{t}\n{az}username: {vd}342992a1{t} \n{az}password: {vd}MiKe{t}')
            while True:
                  print(f'{cn}#{t}'*27)
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [y/n]{t}')).strip().lower()
                  if ab == 'y':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        animacao()
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
      elif nm == '7' or nm == '07':
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}Facebook-BruteForce{t}]...')
            animacao()
            print(f'{vd}[*]{a} Baixando Ferramenta{t} [{a}Facebook-BruteForce{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/Facebook-BruteForce') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/IAmBlackHacker/Facebook-BruteForce')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/Facebook-BruteForce') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [Facebook-BruteForce]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Instalando requisitos da ferramenta...{t}')
                  sleep(3)
                  os.system('cd ~/Facebook-BruteForce;python3 -m pip install requests bs4')
                  os.system('cd ~/Facebook-BruteForce;python3 -m pip install mechanize')
                  animacao()
            print(f'{vd}[*]{a} adicionando permissão...')
            sleep(3)
            os.system('cd ~/Facebook-BruteForce;chmod +x *')
            animacao()
            print(f'{vd}[*] Instalação concluida!{t}')
            animacao()
            print(f'{a}[!] Para usar basta colocar o comando [cd;cd Facebook-BruteForce], depois o comando [python3 fb.py ou python fb2.py].{t}')
            while True:
                  print(f'{cn}#{t}'*27)
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        animacao()
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
            animacao()
            print(f'{vd}[*] {a}Preparando para instalar{t} [{a}zphisher{t}]...')
            animacao()
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}zphisher{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/zphisher') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/htr-tech/zphisher.git')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/zphisher') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [zphisher]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:   
                  print(f'{vd}[*]{a} adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/zphisher;chmod +x *')
                  animacao()
            print(f'{vd}[*] Instalação concluida!')
            animacao()
            while True:
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        animacao()
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
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}nmap{t}]...')
            animacao()
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}nmap{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/sqlmap') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/sqlmapproject/sqlmap')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/sqlmap') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [sqlmap]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/sqlmap;chmod +x *')
                  animacao()
            print(f'{vd}[*] Instalação concluida!')
            animacao()
            while True:
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        animacao()
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
            animacao()
            print(f'{vd}[*]{a} Preparando para instalar{t} [{a}m-wiz{t}]...')
            animacao()
            print(f'{vd}[*]{a} Instalando{t} [{a}pip lolcat{t}]...')
            sleep(3)
            os.system('cd ~/;pip install lolcat')
            animacao()
            print(f'{vd}[*]{a} Baixando ferramenta{t} [{a}m-wiz{t}]...')
            sleep(3)
            if os.path.exists('/data/data/com.termux/files/home/m-wiz') == True:
                  print(f'{vd}[*] Esta ferramenta já está Baixada!{t}')
                  break
            os.system('cd ~/;git clone https://github.com/noob-hackers/m-wiz')
            animacao()
            if os.path.exists('/data/data/com.termux/files/home/m-wiz') == False:
                  print(f'{vm}[x] ERROR: Não foi possível baixar [m-wiz]. {a}\n[!] Verifique se o [git] está instalado corretamente!{t}')
                  break      
            else:
                  print(f'{vd}[*]{a} Adicionando permissão...')
                  sleep(3)
                  os.system('cd ~/m-wiz;chmod +x *')
                  animacao()
            print(f'{vd}[*] Instalação concluida!')
            animacao()
            while True:
                  ab = str(input(f'{vd}[?]{az} Deseja abrir essa ferramenta agora? [s/n]{t}')).strip().lower()[0]
                  if ab == 's':
                        print(f'{cn}#{t}'*27)
                        print(f'{vd}[*] Abrindo ferramenta...{t}')
                        sleep(5)
                        animacao()
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
            print(f'\n    {vm}[x] {t}[{r}{nm}{t}]{vm} Não é uma opção inválida!{t}')
            sleep(3)
print(f'''\n    {a}bye :){t}''')
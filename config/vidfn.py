def recursos():

    from time import sleep
    import os

    # cores
    vm = '\033[31m' # vermelho
    vd = '\033[32m' # verde
    cn = '\033[36m' #ciano
    t = '\033[m' # final cor

    img = f'''{vm}
                     ______
                  .-"      "-.
                 /            |
                |              |
                |,  .-.  .-.  ,|
                | )(_o/  \o_)( |
                |/     /\     \|
      (@_       (_     ^^     _) Installing...
 _     ) \_______\__|IIIIII|__/__________________________
(_)@8@8$3<________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------`

{t}\n'''
    print(img)
    print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)
    sleep(3)

    if os.path.exists('/data/data/com.termux/files/usr/bin/git') == True:
        print(f'>>{vd}${t}<< {cn}git...........[✔]{t}')
        sleep(2)

    else:
        print(f'\n   >>{vd}${t}<< {vm}git...........[x]{cn}')
        sleep(2)
        os.system('pkg install git -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/git') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar git!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)

    if os.path.exists('/data/data/com.termux/files/usr/bin/python') == True:
        print(f'>>{vd}${t}<< {cn}python........[✔]{t}')
        sleep(2)

    else:
        print(f'\n   >>{vd}${t}<< {vm}python........[x]{cn}')
        sleep(2)
        os.system('pkg install python -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/python') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar python!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)

    if os.path.exists('/data/data/com.termux/files/usr/bin/python2') == True:
        print(f'>>{vd}${t}<< {cn}python2.......[✔]{t}')
        sleep(2)

    else:
        print(f'\n   >>{vd}${t}<< {vm}python2.......[x]{cn}')
        sleep(2)
        os.system('pkg install python2 -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/python2') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar python2!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)
    
    if os.path.exists('/data/data/com.termux/files/usr/bin/python3') == True:
        print(f'>>{vd}${t}<< {cn}python3.......[✔]{t}')
        sleep(2)
    else:
        print(f'\n   >>{vd}${t}<< {vm}python3.......[x]{cn}')
        sleep(2)
        os.system('pkg install python3 -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/python3') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar python3!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)

    if os.path.exists('/data/data/com.termux/files/usr/bin/curl') == True:
        print(f'>>{vd}${t}<< {cn}curl..........[✔]{t}')
        sleep(2)
    else:
        print(f'\n   >>{vd}${t}<< {vm}python3.......[x]{cn}')
        sleep(2)
        os.system('pkg install curl -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/curl') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar curl!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)
    
    if os.path.exists('/data/data/com.termux/files/usr/bin/vim') == True:
        print(f'>>{vd}${t}<< {cn}vim...........[✔]{t}')
        sleep(2)
    else:
        print(f'\n   >>{vd}${t}<< {vm}vim...........[x]{cn}')
        sleep(2)
        os.system('pkg install vim -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/vim') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar vim!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)
    
    if os.path.exists('/data/data/com.termux/files/usr/bin/php') == True:
        print(f'>>{vd}${t}<< {cn}php...........[✔]{t}')
        sleep(2)
    else:
        print(f'\n   >>{vd}${t}<< {vm}php...........[x]{cn}')
        sleep(2)
        os.system('pkg install php -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/php') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar php!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)
    
    if os.path.exists('/data/data/com.termux/files/usr/bin/git') == True:
        print(f'>>{vd}${t}<< {cn}wget..........[✔]{t}')
        sleep(2)
    else:
        print(f'\n   >>{vd}${t}<< {vm}wget..........[x]{cn}')
        sleep(2)
        os.system('pkg install php -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/wget') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar wget!{t}')
            sleep(5)
        os.system('clear')
        print(img)
        print(f'{cn}={t}'*10,'Verificando requisitos',f'{cn}={t}'*10)

    if os.path.exists('/data/data/com.termux/files/usr/bin/nano') == True:
        print(f'>>{vd}${t}<< {cn}nano..........[✔]{t}')
        sleep(2)
    else:
        print(f'\n   >>{vd}${t}<< {vm}nano..........[x]{cn}')
        sleep(2)
        os.system('pkg install nano -y')
        if os.path.exists('/data/data/com.termux/files/usr/bin/nano') == False:
            print(f'\n{vm}[x] Error: Não foi possível instalar nano{t}')
            sleep(5)


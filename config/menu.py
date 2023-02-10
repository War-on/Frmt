def menu():
    # cores
    vm = '\033[31m'  # vermelho
    vd = '\033[32m'  # verde
    a = '\033[33m'  # amarelo
    az = '\033[34m'  # azul
    r = '\033[35m'  # roxo
    t = '\033[m'  # final cor

    print(f'''
{az} _____  {vm} ____   {a} __  __  {vd} _____ {t} 
{az}|  ___| {vm}|  _ \  {a}|  \/  | {vd}|_   _|{t}
{az}| |_    {vm}| |_) | {a}| |\/| | {vd}  | |  {t}
{az}|  _|   {vm}|  _ <  {a}| |  | | {vd}  | | {vm}ᵉQ⃟ᵘⁱᵖᵉ ⁱⁿᵛᵃˢᵒʳᵉˢ{t}
{az}|_|     {vm}|_| \_\ {a}|_|  |_| {vd}  |_|  {t}

            {az}--------{t}[ {az}F{vm}R{a}M{vd}T {a}v1.2{t} ]{az}--------{t}

[{r}01{t}] {a}ngrok{t}               [{r}06{t}] {a}Clownters.c{t}
[{r}02{t}] {a}sherlock{t}            [{r}07{t}] {a}Facebook-BruteForce{t}
[{r}03{t}] {a}toutatis{t}            [{r}08{t}] {a}zphisher{t}
[{r}04{t}] {a}wifite2(root){t}       [{r}09{t}] {a}nmap (sqlmap){t}
[{r}05{t}] {a}Personalizar Termux{t} [{r}10{t}] {a}m-wiz (para instalar metasploit){t}

[{vm}98{t}] {a}Atualizar (Frmt){t}
[{vm}99{t}] {a}link do grupo (WhatsApp){t}
[{vm}00{t}] {a}SAIR{t}''')
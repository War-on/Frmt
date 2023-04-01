import subprocess
# cores
vm = '\033[31m' # vermelho
vd = '\033[32m' # verde
a = '\033[33m' # amarelo
az = '\033[34m' # azul
r = '\033[35m' # roxo
cn = '\033[36m' #ciano
t = '\033[m' # final cor
result = subprocess.run(['termux-info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    version = None
    for line in result.stdout.decode().split("\n"):
        if line.startswith("TERMUX_VERSION"):
            version = line.split("=")[1]
            break

def atualizacao_arquivos():
    import os
    from time import sleep
    print('\033[36mAtualizando arquivos...\033[m')
    sleep(3)
    os.system('apt update -y;apt upgrade -y')
import pyautogui as pag
import pyperclip
import time
import os
import sys

pag.PAUSE = 0.001

pag.alert(text="Atenção! Nunca clique, mexa o mouse, troque de tela ou interfira de alguma forma enquando o programa está no processo de escrever mensagens. Evite acidentes", title="Spam Tool v2.0")

# -----------------------------

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
 
mode = pag.confirm(text="Escolha o modo:\nSequencial: escreve várias mensagens sem apertar enter para enviar\nSeparado: envia várias mensagens uma de cada vez, apertando enter", buttons=['Sequencial', 'Separado'], title="Spam Tool v2.0")
if mode is None:
    exit()

msg = pag.prompt(text="Insira a mensagem", title=mode)
if msg is None:
    exit()

qtd = pag.prompt(text="Insira a quantidade", title=mode)
if qtd is None:
    exit()

inter = pag.prompt(text="Insira o intervalo entre cada mensagem (padrão = 0.1\nmínimo = 0.001)", title=mode)
if inter is None:
    exit()

inter = float(inter)
qtd = int(qtd)

pyperclip.copy(msg)

confirmar = pag.confirm(text="Clique em OK quando estiver pronto (espere um delay de 3 segundos)", title=mode, buttons=['OK', 'Cancelar'])
if confirmar is None:
    exit()
elif confirmar == "Cancelar":
    exit()

pag.sleep(3)


if mode == "Separado":
    tempoIni = time.time()

    for i in range(qtd):
        pag.hotkey(['ctrl', 'v'])
        pag.press('enter')
        pag.sleep(inter) 
    
    tempoFim = time.time()

elif mode == "Sequencial":
    tempoIni = time.time()

    for i in range(qtd):
        pag.hotkey(['ctrl', 'v'])
        pag.sleep(inter)

    tempoFim = time.time()

tempo = tempoFim - tempoIni



Fim = pag.confirm(f"Sucesso!\nMensagens escritas: {qtd}\nTempo total: {tempo:.2f} segundo(s)\n\nDeseja executar o programa novamente?", title="Spam Tool v2.0", buttons=['Sim', "Não"])
if Fim == 'Não':
    exit()
elif Fim is None:
    exit()
elif Fim == 'Sim':
    restart()

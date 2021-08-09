import pyautogui
import docx
import clipboard
'''
#ABRIR SISTEMA PROCESSUAL
pyautogui.moveTo(270,893,0.5)
pyautogui.click()
pyautogui.PAUSE = 2
pyautogui.hotkey('alt','tab')
pyautogui.moveTo(947,411,0.5)
pyautogui.click()
pyautogui.typewrite('pi100035', interval=0.02)
pyautogui.press('tab')
pyautogui.typewrite('tere20', interval=0.02)
pyautogui.moveTo(659,476,0.5)
pyautogui.click()
pyautogui.moveTo(795,606,0.5)
pyautogui.click()
pyautogui.moveTo(652,423,0.5)
pyautogui.click()

#ACESSAR ROTINA DE PUBLICAÇÃO
pyautogui.moveTo(507,35,0.5)
pyautogui.click()
pyautogui.moveTo(507,60,0.5)
pyautogui.click()
pyautogui.moveTo(723,513,0.5)
pyautogui.click()
'''

def alimentarOraclePublicacao():
    #EXCLUIR PRIMEIRO REGISTRO DA ROTINA DE PUBLICAÇÃO DO SISTEMA PROCESSUAL
    pyautogui.moveTo(176,157,0.5)
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(264,67,0.5)
    pyautogui.click()
    pyautogui.moveTo(71,67,0.5)
    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('2')
    pyautogui.press('tab')
    pyautogui.press('tab')

    #COPIA DADOS DO ARQUIVO

    from docx import Document

    input = Document('arquivo_base.docx')

    paragraphs = []

    for para in input.paragraphs:
        p = para.text
        if p != "":
            paragraphs.append(p)

    pyautogui.moveTo(691,437,0.5)
    pyautogui.click()

    #INCLUSÃO DO PRIMEIRO REGISTRO

    #colar texto
    clipboard.copy(paragraphs[1])
    pyautogui.hotkey('ctrl','v')

    pyautogui.moveTo(239,444,0.5) #clicar no botão processo
    pyautogui.click()
    pyautogui.moveTo(30,319,0.5) #clicar no checkbox usar nova localização física
    pyautogui.click()
    pyautogui.moveTo(475,254,0.5) #clicar no campo processo
    pyautogui.click()

    #colar num processo
    clipboard.copy(paragraphs[0])
    pyautogui.hotkey('ctrl','v')

    pyautogui.moveTo(613,254,0.5) #desmarca incluir movimentação
    pyautogui.click()
    pyautogui.moveTo(688,450,0.5) #clica no botão gravar/voltar
    pyautogui.click()
    pyautogui.moveTo(720,508,0.5) #botão ok
    pyautogui.click()
    pyautogui.moveTo(157,274,0.5) #clicar no sequencial do registro
    pyautogui.click()
    pyautogui.moveTo(236,68,0.5) #clicar no botão "+"
    pyautogui.click()
    pyautogui.press('tab')

    #INCLUSÃO DOS DEMAIS REGISTROS

    i = 2

    while i+1 < len(paragraphs):
        #colar texto
        clipboard.copy(paragraphs[i+1])
        pyautogui.hotkey('ctrl','v')

        pyautogui.moveTo(239,444,0.5) #clicar no botão processo
        pyautogui.click()
        #pyautogui.moveTo(30,319,1) #clicar no checkbox usar nova localização física
        #pyautogui.click()
        pyautogui.moveTo(475,254,0.5) #clicar no campo processo
        pyautogui.click()

        #colar num processo
        clipboard.copy(paragraphs[i])
        pyautogui.hotkey('ctrl','v')
        i = i+2
        
        pyautogui.moveTo(613,254,0.5) #desmarca incluir movimentação
        pyautogui.click()
        pyautogui.moveTo(688,450,0.5) #clica no botão gravar/voltar
        pyautogui.click()
        pyautogui.moveTo(720,508,0.5) #botão ok
        pyautogui.click()
        pyautogui.moveTo(157,274,0.5) #clicar no sequencial do registro
        pyautogui.click()
        pyautogui.moveTo(236,68,0.5) #clicar no botão "+"
        pyautogui.click()
        pyautogui.press('tab')

def main():
    alimentarOraclePublicacao()

if __name__ == '__main__':
    main()

















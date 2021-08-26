# Copyright (C) 2021  FRANCINALDO CARVALHO <francinaldo@protonmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

# -*- coding: utf-8 -*-


import pyautogui
import docx
import clipboard
from docx import Document

from caps import getCapsState

def alimentarOraclePublicacao():

    #Excluir registro existente
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

    #copia dados do arquivo:
    #alterar esta rotina para que o arquivo seja gravado em processos.txt
    #fazer alteração na macro do Word

    
    input = Document('arquivo_base.docx')

    paragraphs = []

    for para in input.paragraphs:
        p = para.text
        if p != "":
            paragraphs.append(p)

    pyautogui.moveTo(691,437,0.5)
    pyautogui.click()

    #Inclsão do primeiro registro, onde se deve desmarcar a caixa de seleção
    #da escolha de utilizar nova localização no processos a serem inseridos

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

    #Inclusão dos demais registros

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
    if getCapsState():
        pyautogui.hotkey('capslock')

    alimentarOraclePublicacao()

if __name__ == '__main__':
    main()

















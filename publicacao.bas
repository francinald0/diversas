Attribute VB_Name = "publicacao"
'# Copyright (C) 2021  FRANCINALDO CARVALHO <francinaldo@protonmail.com>
'#
'# This program is free software; you can redistribute it and/or modify
'# it under the terms of the GNU General Public License as published by
'# the Free Software Foundation; either version 2 of the License, or
'# (at your option) any later version.
'#
'# This program is distributed in the hope that it will be useful,
'# but WITHOUT ANY WARRANTY; without even the implied warranty of
'# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
'# GNU General Public License for more details.
'#
'# You should have received a copy of the GNU General Public License
'# along with this program; if not, write to the Free Software
'# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

Option Explicit

Public processos As String
Public numProcessos As Integer
Public tipoAto As String
Public numBoletim As String
Public dtPublicacao As Date
Public rngProcessos As Range
Public Const LOCAL_CERTIDAO_NUMERA = "D:\certid�o - inser��o e publica��o.doc"
Public Const LOCAL_ARQ_CERTIDAO As String = "W:\FRANCINALDO\publica��o\certid�o - inser��o e publica��o.doc"
Public Const LOCAL_ARQ_PLAQUETA As String = "W:\FRANCINALDO\publica��o\plaqueta - lista de processos do boletim.doc"

'chamada das rotinas implementadas neste m�dulo
Sub imprimeCertidoesEPlaqueta()
    
   Call isolaNumeros
   Call excluiClasse
   Call imprimeCertidoes
   Call imprimePlaqueta
    
End Sub

Sub excluiClasse()
'rotina atualizada. Renomear rotina, e refazer a descri��o
' <---------melhorar reda��o:--------->
' contexto: Quando os n�meros de processos s�o delimitados no arquivo gerado pelo
' Sistema Oracle, as descri��o da classe permanece ao lado do n�mero do processo.
' Esta rotina exclui a descri��o da classe, e permanece somente a indica��o do n�mero de processo.

Dim rngParagrafo As Range
Dim i As Integer
Dim count As Integer

i = 1
Do While i <= ActiveDocument.Paragraphs.count - 1
    Set rngParagrafo = ActiveDocument.Paragraphs(i).Range
    
'    For count = 1 To Len(rngParagrafo.Text)
'        If Mid(rngParagrafo.Text, count, 1) = " " Then
'            ActiveDocument.Paragraphs(i).Range.Text = Left(rngParagrafo.Text, count) & Chr(13)
'            Exit For
    ActiveDocument.Paragraphs(i).Range.Text = Mid(ActiveDocument.Paragraphs(i).Range.Text, 18)
        'End If
    'Next count
    i = i + 1
Loop

'Call salvarArquivoProcessos 'salva conte�do no arquivo d:\processos.docx

End Sub
Sub salvarArquivoProcessos()

'ActiveDocument.SaveAs2 ("d:\processos.docx")
'ActiveDocument.SaveAs "processos.docx"
'MsgBox ("arquivo d:\processos.docx salvo")

End Sub
' Isola os n�meros dos processos do restante das informa��es e acrescenta a sua quantidade ao final do documento
Sub isolaNumeros()

Dim paragrafo As Paragraph
Dim tabela As Table
Const strPalavraChave As String = "Numera��o"
Dim strInicio As String, strParagrafo As String
Dim rngParagrafo As Range
Dim i As Integer
Dim pula As Boolean
Dim ultima_linha As Variant

'define o tipo de ato e armazena na vari�vel global
tipoAto = defineTipoAto()
numBoletim = defineNumBoletim()

'exclui todas as tabelas
For Each tabela In ActiveDocument.Tables
    tabela.Delete
Next tabela

pula = False

'apaga as linhas que n�o tenham as palavras "numera��o �nica" no in�cio da linha
For Each paragrafo In ActiveDocument.Paragraphs
    Set rngParagrafo = paragrafo.Range
    strInicio = Left(rngParagrafo.Text, 9)
    If strInicio <> strPalavraChave And Not pula Then
        paragrafo.Range.Delete
    ElseIf strInicio = strPalavraChave Then
      ' paragrafo.Range.Delete
      ' pula = True
    Else
        pula = False
    End If
Next paragrafo

'Call excluiClasse

'acrescenta a quantidade de processos
numProcessos = ActiveDocument.Paragraphs.count
ultima_linha = "(" & (CStr(numProcessos)) & " processos)"
ActiveDocument.Paragraphs.Add
ActiveDocument.Paragraphs.Last.Range.Text = ultima_linha

'atribui todo o conte�do do arquivo, que possui os n�meros isolados para uma vari�vel global range
' usada na rotina imprimePlaqueta
'Set rngProcessos = ActiveDocument.Content
'Dim Processos As String
processos = ActiveDocument.Range.Text


End Sub

Sub imprimeCertidoes()
Dim mensagem As String
Dim intDiaDaSemana As Integer

'a data de publica��o dever� identificar os s�bados e domingos
dtPublicacao = Date + 2
If Weekday(dtPublicacao) = 7 Then '  = 7 --> s�bado
    dtPublicacao = dtPublicacao + 2
ElseIf Weekday(dtPublicacao) = 1 Then ' = 1 --> domingo
    dtPublicacao = dtPublicacao + 2
End If

' preenche os dados do formul�rio
With frmCertidoes
.txtDtPublicacao.Value = dtPublicacao
.txtNumProcessos.Value = numProcessos
.txtBoletim.Value = numBoletim
.txtAto.Value = tipoAto
End With

frmCertidoes.Show

End Sub

Sub imprimePlaqueta()

Const pal_chave As String = "<processos> "

Dim i As Integer
Dim docPlaqueta As Document
Dim rngParagrafo As Range
Dim resposta As Integer

' abrir arquivo de certid�es
Set docPlaqueta = New Document
Set docPlaqueta = Documents.Open(LOCAL_ARQ_PLAQUETA)

'adicionar as informa��es no arquivo

'docPlaqueta.Activate

'substitui o "texto marcador" pelo ato
' <ato> por tipoAto
With docPlaqueta.Content.Find
 .Text = "<ato>"
 .ClearFormatting
 .Replacement.ClearFormatting
 .Forward = True
 .Replacement.Text = tipoAto
 .Execute Replace:=wdReplaceAll
 
End With

' Substitui o "texto marcador" <boletim> pelo valor armazenado em numeroBoletim
With docPlaqueta.Content.Find
 .Text = "<boletim>"
 .ClearFormatting
 .Replacement.ClearFormatting
 .Forward = True
 .Replacement.Text = numBoletim
 .Execute Replace:=wdReplaceAll
End With

With docPlaqueta.Content.Find
 .Text = "<data_publicacao>"
 .ClearFormatting
 .Replacement.ClearFormatting
 .Forward = True
 .Replacement.Text = dtPublicacao
 .Execute Replace:=wdReplaceAll
End With


i = 1
Do While i <= docPlaqueta.Paragraphs.count - 1
    Set rngParagrafo = docPlaqueta.Paragraphs(i).Range
    If Len(rngParagrafo.Text) = Len(pal_chave) Then
        rngParagrafo.Text = processos
        Exit Do
    End If
    i = i + 1
Loop

'imprimir o arquivo
resposta = MsgBox(Prompt:="deseja imprimir a lista de processos?", Buttons:=vbYesNo)

If resposta = 6 Then
    docPlaqueta.PrintOut
End If

' Fecha o arquivo sem salv�-lo
docPlaqueta.Close SaveChanges:=wdDoNotSaveChanges

End Sub

Function defineTipoAto()
' busca a palavra DESPACHO, DECIS�O, SENTEN�A ou ATO ORDINAT�RIO no arquivo gerado pelo sistema
Dim paragrafo As Paragraph
Const strPalavraChave As String = "AUTOS COM" 'Texto a ser retirado do in�cio do par�grafo
Dim strInicio, strParagrafo As String
Dim rngParagrafo As Range
Dim i As Integer 'counter
Dim ato As String

i = 1
Do While i <= ActiveDocument.Paragraphs.count - 1
    Set rngParagrafo = ActiveDocument.Paragraphs(i).Range
    'MsgBox (Left(rngParagrafo.Text, 9) & " = " & strPalavraChave)
    If Left(rngParagrafo.Text, 9) = strPalavraChave Then
        'MsgBox (Left(rngParagrafo.Text, 9) & " = " & strPalavraChave)
        ato = Mid(rngParagrafo.Text, 11)
        ' MsgBox (ato)
        'por algum motivo a vari�vel est� agregada de um par�grafo ao seu final
        'a linha abaixo retira o �ltimo caractere e atribui a palavra sem o par�grafo
        defineTipoAto = Left(ato, Len(ato) - 1)
        Exit Do
    End If

    i = i + 1
Loop

End Function

Function defineNumBoletim()
' busca o n�mero do boletim no arquivo gerado pelo sistema

Dim paragrafo As Paragraph
Const strPalavraChave As String = "BOLETIM " 'Texto base para copiar o restante do par�grafo
Dim strInicio, strParagrafo As String
Dim rngParagrafo As Range
Dim i As Integer 'counter
Dim numBoletim As String

i = 1
Do While i <= ActiveDocument.Paragraphs.count - 1
    Set rngParagrafo = ActiveDocument.Paragraphs(i).Range
    'MsgBox (Left(rngParagrafo.Text, 9) & " = " & strPalavraChave)
    If Left(rngParagrafo.Text, 8) = strPalavraChave Then
        'MsgBox (Left(rngParagrafo.Text, 9) & " = " & strPalavraChave)
        numBoletim = Mid(rngParagrafo.Text, 9)
        'MsgBox (numBoletim)
        defineNumBoletim = Left(numBoletim, Len(numBoletim) - 1)
        Exit Do
    End If

    i = i + 1
Loop

End Function

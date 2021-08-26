Attribute VB_Name = "teste"
Sub removerParagrafos()
    
Dim rngParag As Paragraph
Dim novoParagrafo As Range
Dim i As Integer
Dim cadeia_de_caracteres As String
Dim strComparar As String

i = 0
    For Each rngParag In ActiveDocument.Range.Paragraphs
       If Len(rngParag.Range.Text) <> 1 Then
            novoParagrafo.Text = novoParagrafo.Text & " " & rngParag.Range
            rngParag.Range.Delete
       Else
            ActiveDocument.Paragraphs.Add (novoParagrafo)
            novoParagrafo = ""
       End If
    Next rngParag

End Sub

'rotina não finalizada para copiar número dos processos do arquivo aberto para o processual
'implementada em python
Sub insereDadosNoProcessual()

Dim ReturnValue
Dim processos() As String
Dim index As Integer
Dim dtObject As New dataObject
Dim rngParagrafo As Range
Dim i As Integer
Dim count As Integer

ReDim numProcesso(ActiveDocument.Paragraphs.count - 1)

i = 1
Do While i <= ActiveDocument.Paragraphs.count - 1
    Set rngParagrafo = ActiveDocument.Paragraphs(i).Range
    
    For count = 1 To Len(rngParagrafo.Text)
        If Mid(rngParagrafo.Text, count, 1) = " " Then
            numProcesso(i - 1) = Left(rngParagrafo.Text, count - 1)
            Exit For
        End If
    Next count
    i = i + 1
Loop

ReturnValue = Shell("Ifrun60.EXE")
AppActivate ReturnValue
 If excluiDescricaoClasse(processos) = 1 Then ' o valor de processos é preenchido com a chamada da função
    For i = 1 To ActiveDocument.Paragraphs.count - 1
        dtObject.SetText processos(i)
        dtObject.PutInClipboard
        SendKeys "^v"
        SendKeys "{ENTER}"
        SendKeys "{ENTER}"
    Next i
End If

End Sub

Sub inverteFrase()

Dim i As Integer
Dim r As Range
Dim c(10) As String

Set r = ActiveDocument.Range(Start:=0, End:=9)
For i = 0 To r.Characters.count
    Debug.Print r.Characters(i)

    Debug.Print i
Next i

End Sub

Sub EachLine()

    Const SEARCH_STRING As String = "SearchThis"
    Dim Filename As String
    
    Filename = "C:\Users\Default\Desktop\test.csv"
    
    Dim file As Integer
    file = FreeFile
    Open Filename For Input As #file
    Dim rowNumber As Long
    rowNumber = 0
    Dim match As String
    Do Until EOF(file)
        rowNumber = rowNumber + 1
        Dim line As String
        Line Input #file, line
        If InStr(line, SEARCH_STRING) > 0 Then
        match = line
    Exit Do
        End If
    Loop
    Close #file
    
    If match <> vbNullString Then
    MsgBox "Found '" & SEARCH_STRING & "' in line #" & rowNumber & ": " & match, vbInformation, "Result"
    
    Else: MsgBox "Did not find '" & SEARCH_STRING & "'", vbInformation, "Result"
    End If
End Sub

End Sub

Public gCertProcesso() As clsCertidao
Public gIntNumProcesso As Integer
Public Const LOCAL_PROCESSOS = "D:\processos.docx"
Public Const LOCAL_CERTIDAO_PUBLICACAO = "D:\certidão - publicação.doc"

Public Function OpenFileDialog() As String
    Dim Filter As String, Title As String
    Dim FilterIndex As Integer
    Dim Filename As Variant
    ' Define o filtro de procura dos arquivos
    Filter = "Arquivos Wave (*.wav),*.wav,"
    ' O filtro padrão é *.*
    FilterIndex = 3
    ' Define o Título (Caption) da Tela
    Title = "Selecione um arquivo"
    ' Define o disco de procura
    ChDrive ("C")
    ChDir ("C:\")
    With Application
        ' Abre a caixa de diálogo para seleção do arquivo com os parâmetros
        Filename = .GetOpenFilename(Filter, FilterIndex, Title)
        ' Reseta o Path
        ChDrive (Left(.DefaultFilePath, 1))
        ChDir (.DefaultFilePath)
    End With
    ' Abandona ao Cancelar
    If Filename = False Then
        MsgBox "Nenhum arquivo foi selecionado."
        Exit Function
    End If
    ' Retorna o caminho do arquivo
    OpenFileDialog = Filename
End Function


Public Sub imprimeFolhasProcessos()

Dim i As Integer
Dim docCertidaoFolha As Document
Dim docProcessos As Document
Dim rngParagrafoProcesso As Range
Dim resposta As Integer
Dim pArray() As Paragraph
Dim n As Integer ' número de processos
Dim intFls As Integer
Dim intFlsAto As Variant
Dim strProcesso As String
Dim intItem As Integer


' buscar os números dos processos no arquivo "processos.docx"

Set docProcessos = New Document
Set docProcessos = Documents.Open(LOCAL_PROCESSOS)

ReDim pArray(1)

For i = 1 To docProcessos.Paragraphs.count
    'MsgBox docProcessos.Paragraphs(i).Range.Text
    Set pArray(i) = docProcessos.Paragraphs(i)
    'Debug.Print pArray(i).Range.Text
    ReDim pArray(i + 1)
Next i

numProcessos = i

frmFlsCertidao.Show

' abrir arquivo de certidões
'Set docCertidaoFolha = New Document
'Set docCertidaoFolha = Documents.Open(LOCAL_CERTIDAO_PUBLICACAO)

docProcessos.Close

'adicionar as informações no arquivo

'docPlaqueta.Activate

'substitui o "texto marcador" pelo ato
' <ato> por tipoAto
'With docPlaqueta.Content.Find
' .Text = "<ato>"
' .ClearFormatting
' .Replacement.ClearFormatting
' .Forward = True
' .Replacement.Text = tipoAto
' .Execute Replace:=wdReplaceAll
 
'End With
'
'' Substitui o "texto marcador" <boletim> pelo valor armazenado em numeroBoletim
'With docPlaqueta.Content.Find
' .Text = "<boletim>"
' .ClearFormatting
' .Replacement.ClearFormatting
' .Forward = True
' .Replacement.Text = numBoletim
' .Execute Replace:=wdReplaceAll
'End With
'
'With docPlaqueta.Content.Find
' .Text = "<data_publicacao>"
' .ClearFormatting
' .Replacement.ClearFormatting
' .Forward = True
' .Replacement.Text = dtPublicacao
' .Execute Replace:=wdReplaceAll
'End With
'
'
'
''o bloco abaixo deu erro
''With docPlaqueta.Content.Find
'' .Text = "<processos>"
'' .Forward = True
'' .Replacement.Text = Processos
'' .Execute Replace:=wdReplaceAll
''End With
''retira determinados caracteres do início dos parágrafos
'
'i = 1
'Do While i <= docPlaqueta.Paragraphs.count - 1
'    Set rngParagrafo = docPlaqueta.Paragraphs(i).Range
'    If Len(rngParagrafo.Text) = Len(pal_chave) Then
'        rngParagrafo.Text = processos
'        Exit Do
'    End If
'    i = i + 1
'Loop
'
''docPlaqueta.Activate
'
''imprimir o arquivo
'resposta = MsgBox(Prompt:="deseja imprimir a lista de processos?", Buttons:=vbYesNo)
'
'If resposta = 6 Then
'    docPlaqueta.PrintOut
'End If
'
'' Fecha o arquivo sem salvá-lo
'docPlaqueta.Close SaveChanges:=wdDoNotSaveChanges


End Sub

Private Sub usoDoMsgBox()

Dim resposta As String

resposta = MsgBox(Prompt:="deseja imprimir a lista de processos?", Buttons:=vbYesNo)

Debug.Print resposta

End Sub
Function defineProxData()

Dim dataExemplo As Date

dataExemplo = Date
    
MsgBox (Month(dataExemplo))

End Function


Sub testa_substituicao()

Const TEXTO As String = "caju "

Dim docTeste As Document
Dim rngParagrafo As Range
Dim i As Integer
Dim Paragrafos As String
Dim para As Paragraph

Set docTeste = Documents.Open("d:\teste_substituicao.doc.rtf")

Paragrafos = docTeste.Content.Text


For Each para In docTeste.Paragraphs

    If Len(para.Range.Text) = Len(TEXTO) Then
        MsgBox ("OK")
    End If
    'para.Range.Text = "teste"

Next para

'i = 1
'Do While i <= docTeste.Paragraphs.Count - 1
'    Set rngParagrafo = docTeste.Paragraphs(i).Range
'    MsgBox (Len(rngParagrafo.Text) & " = " & Len(TEXTO))
'    If StrComp(rngParagrafo.Text, TEXTO, vbTextCompare) = 0 Then
'        rngParagrafo.Text = Paragrafos
'
    'Else
    '    rngParagrafo.Text = "diferente"
'    End If
'    i = i + 1
'Loop

docTeste.Activate



End Sub

Public Sub wrap_words()

    Dim para_index As Paragraph
    Dim para_index_numchars, char_index, para_index_start As Long
    
    'set the max line length constraint
    Const line_max As Byte = 50
    
    'loop through each paragraph
    For Each para_index In ActiveDocument.Paragraphs
        
        'find number of characters
        para_index_numchars = para_index.Range.Characters.count
        
        'find the paragraph starting point
        para_index_start = para_index.Range.Start
        
        'if the paragraph has more than the predetermined amount of characters,
        If para_index_numchars > line_max Then
        
        'loop through each character starting with line_max position
        'and stepping by line_max position, to the end of the paragraph
            For char_index = (para_index_start + line_max) To _
            (para_index_start + para_index_numchars) Step line_max
                
                'if there is not a word in this position...
                If ActiveDocument.Range(char_index).Text = " " Or _
                ActiveDocument.Range(char_index).Text = "-" Then
                
                '...just insert new line mark
                    ActiveDocument.Range(char_index, char_index).InsertAfter Chr(13)
                Else
                    
                    '... if there is a word, or a hyphenated word that 'can be split, move to the beginnng of word or the
                    'end of the hyphenated section.
                    ActiveDocument.Range(char_index, char_index).Select
                    Selection.MoveLeft unit:=wdWord, count:=1
                    
                    'insert newline at the beginning
                    Selection.InsertBefore Chr(13)
                    
                    'since a new paragraph created before the word,
                    'the previous paragraph structure has changed.
                    'change char_index to reflect that change.
                    char_index = Selection.Start
                End If
            Next
        End If
    Next
End Sub


Sub TextoAntesEDepois()

Dim oPara As Word.Paragraph
Dim rng As Range

For Each oPara In ActiveDocument.Paragraphs
    'or Selection.Paragraphs
    Set rng = oPara.Range
    With rng
        If .ListFormat.ListType = WdListType.wdListBullet Then
            .Style = ActiveDocument.Styles(wdStyleNormal)
            .InsertBefore " * "
            .Collapse wdCollapseEnd
            .Move wdCharacter, -1
            .InsertAfter "&&&"
        End If
    End With
Next

End Sub



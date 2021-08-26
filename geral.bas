Attribute VB_Name = "geral"
Sub transfereConteudo()

Const ARQUIVO_DESTINO As String = "D:\processos.docx"

Dim i As Integer
Dim docProcessos As Document
Dim rngParagrafo As Range
Dim resposta As Integer

Set docProcessos = New Document
Set docProcessos = Documents.Open(ARQUIVO_DESTINO)

docProcessos.Range.Delete


docProcessos.Range = Documents(2).Range
'imprimir o arquivo
MsgBox ("conteúdo copiado para o arquivo 'd:\processos.docx'")

' Fecha o arquivo sem salvá-lo
docProcessos.Save
docProcessos.Close

End Sub

Sub excluiQuebraDeLinha()
Attribute excluiQuebraDeLinha.VB_ProcData.VB_Invoke_Func = "Normal.NewMacros.excluiParagrafos"
'
' excluiParagrafos Macro
'
    Selection.Find.ClearFormatting
    Selection.Find.Replacement.ClearFormatting
    With Selection.Find
        .Text = "^p"
        .Replacement.Text = " "
        .Forward = True
        .Wrap = wdFindAsk
        .Format = False
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
    End With
    Selection.Find.Execute Replace:=wdReplaceAll
End Sub
Sub preparaArquivoProcessos()
'abre arquivo "processos.docx" e copia para ele os processos do arquivo atual

Dim docProcessos As Document
Dim rngParagrafo As Range
Dim i As Integer
Dim Paragrafos As String
Dim para As Paragraph
Dim count As Integer
Dim strPaste As String
Set docProcessos = Documents.Open("d:\processos.docx")

ActiveDocument.Content.Copy
'docProcessos.Content = ActiveDocument.Content

Dim DataObj As MSForms.dataObject
Set DataObj = New MSForms.dataObject
DataObj.GetFromClipboard

strPaste = DataObj.GetText(1)

docProcessos.Content.Text = strPaste

i = 1
Do While i <= docProcessos.Paragraphs.count - 1
    Set rngParagrafo = docProcessos.Paragraphs(i).Range
    For count = 1 To Len(rngParagrafo.Text)
        If Mid(rngParagrafo.Text, count, 1) = " " Then
            docProcessos.Paragraphs(i).Range.Text = Left(rngParagrafo.Text, count - 1)
            Exit For
        End If
    Next count
    'numProcesso(i) = rngParagrafo.Words.Item(1)
    'MsgBox (numProcesso(i))
    i = i + 1
Loop
MsgBox ("arquivo pronto")
docProcessos.Close ' SaveChanges:=False

End Sub

Sub excluiDescricaoClasse()

'Const strPalavraChave As String = "Numeração única:" 'Texto a ser retirado do início do parágrafo
Dim rngParagrafo As Range
Dim i As Integer
Dim count As Integer
'Dim numProcesso() As String

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
    'numProcesso(i) = rngParagrafo.Words.Item(1)
    'MsgBox (numProcesso(i))
    i = i + 1
Loop

excluiDescricaoClasse = 1

End Sub

'retira determinados caracteres do início dos parágrafos
Sub retiraInicio()

Dim paragrafo As Paragraph
Const strPalavraChave As String = "Numeração única:" 'Texto a ser retirado do início do parágrafo
Dim strInicio, strParagrafo As String
Dim rngParagrafo As Range
Dim i As Integer 'counter

i = 1
Do While i <= 12
    Set rngParagrafo = ActiveDocument.Paragraphs(i).Range
    rngParagrafo.Text = Right(rngParagrafo.Text, 24)
    i = i + 1
Loop

End Sub

from tkinter import *
import tkinter as tk
# tabuada
def tabuada():  # multiplicação
    numero = primeiro_valor.get()  # comando para coletar a informação da caixa de texto
    numero2 = segundo_valor.get()
    valor1 = float(numero)
    valor2 = float(numero2)
    resultado_final = valor1 * valor2
    texto_botao["text"] = resultado_final
def divisao():  # divisão
    numero = primeiro_valor.get()  # comando para coletar a informação da caixa de texto
    numero2 = segundo_valor.get()
    valor1 = float(numero)
    valor2 = float(numero2)
    resultado_final = valor1 / valor2
    texto_botao["text"] = resultado_final
def subtração():  # subtracão
    numero = primeiro_valor.get()  # comando para coletar a informação da caixa de texto
    numero2 = segundo_valor.get()
    valor1 = float(numero)
    valor2 = float(numero2)
    resultado_final = valor1 - valor2
    texto_botao["text"] = resultado_final
def adição():  # adição
    numero = primeiro_valor.get()  # comando para coletar a informação da caixa de texto
    numero2 = segundo_valor.get()
    valor1 = float(numero)
    valor2 = float(numero2)
    resultado_final = valor1 + valor2
    texto_botao["text"] = resultado_final
def porcentagem():  # porcentagem
    numero = primeiro_valor.get()  # comando para coletar a informação da caixa de texto
    numero2 = segundo_valor.get()
    valor1 = float(numero)
    valor2 = float(numero2)
    resultado = valor2/100
    resultado_final = valor1 * resultado
    texto_botao["text"] = resultado_final
def exponenciação():  # exponenciação
    cospley_de_janela_flamegente_purpura_corantiano_original = primeiro_valor.get()
    Num2 = segundo_valor.get()

    valor1 = float(cospley_de_janela_flamegente_purpura_corantiano_original)
    valor2 = float(Num2)

    Resultado = valor1 ** valor2
    texto_botao["text"] = Resultado
def openNewWindow():  # janela da tabuada
    janela2 = Toplevel(janela1)
    # comando para mudar o titulo da janela do TKinter
    janela2.title("calculadora")
    # comando para mudar as dimenções da janela do TKinter
    janela2.geometry("220x280")
    # comando para mudar a cor de fundo da janela do TKinter
    janela2.configure(bg='yellow')

    global primeiro_valor
    global segundo_valor
    global texto_botao

    texto_orientacao2 = Label(janela2, text=('coloque o primeiro numero'))
    # comando para conficar a linha e coluna
    texto_orientacao2.grid(column=2, row=4)

    primeiro_valor = Entry(janela2)  # comando para enserir uma caixa de texto
    primeiro_valor.grid(column=2, row=5)

    texto_orientacao2 = Label(janela2, text=('coloque o segundo numero'))
    texto_orientacao2.grid(column=2, row=6)

    segundo_valor = Entry(janela2)
    segundo_valor.grid(column=2, row=7)

    botao_gerar_tabuada = Button(
        janela2, text="Clique aqui para multiplicar", command=tabuada)
    botao_gerar_tabuada.grid(column=2, row=11)

    textinfo = Label(janela2, text="resultado:")
    textinfo.grid(column=2, row=9)

    texto_botao = Label(janela2, text="")
    texto_botao.grid(column=2, row=10)

    botao_divisao = Button(
        janela2, text='clique aqui para dividir ', command=divisao)
    botao_divisao.grid(column=2, row=12)

    botao_adição = Button(
        janela2, text='clique aqui para somar ', command=adição)
    botao_adição.grid(column=2, row=13)

    botao_divisao = Button(
        janela2, text='clique aqui para subtrair ', command=subtração)
    botao_divisao.grid(column=2, row=14)

    botao_divisao = Button(
        janela2, text='clique aqui para meidr a porcentagem', command=porcentagem)
    botao_divisao.grid(column=2, row=15)

    botao_divisao = Button(
        janela2, text='clique aqui para fazer a exponenciação', command=exponenciação)
    botao_divisao.grid(column=2, row=16)
# ordem cresente
def cresente():
    ordem = []

    primeiro_numero1 = primeiro_numero.get()
    segundo_numero1 = segundo_numero.get()
    terceiro_numero1 = terceiro_numero.get()
    quarto_numero1 = quarto_numero.get()
    quinto_numero1 = quinto_numero.get()
    sexto_numero1 = sexto_numero.get()
    setimo_numero1 = setimo_numero.get()
    oitavo_numero1 = oitavo_numero.get()
    nono_numero1 = nono_numero.get()

    primeiro_numero2 = float(primeiro_numero1)
    segundo_numero2 = float(segundo_numero1)
    terceiro_numero2 = float(terceiro_numero1)
    quarto_numero2 = float(quarto_numero1)
    quinto_numero2 = float(quinto_numero1)
    sexto_numero2 = float(sexto_numero1)
    setimo_numero2 = float(setimo_numero1)
    oitavo_numero2 = float(oitavo_numero1)
    nono_numero2 = float(nono_numero1)

    ordem.append(primeiro_numero2)
    ordem.append(segundo_numero2)
    ordem.append(terceiro_numero2)
    ordem.append(quarto_numero2)
    ordem.append(quinto_numero2)
    ordem.append(sexto_numero2)
    ordem.append(setimo_numero2)
    ordem.append(oitavo_numero2)
    ordem.append(nono_numero2)
    ordem.sort()
    text_cresente["text"] = ordem
def abrir_janela_cresente():
    janela_cresente = Toplevel(janela1)
    # comando para mudar o titulo da janela do TKinter
    janela_cresente.title("ordem cresente")
    # comando para mudar as dimenções da janela do TKinter
    janela_cresente.geometry("325x250")
    janela_cresente.configure(bg='purple')

    global primeiro_numero
    global segundo_numero
    global terceiro_numero
    global quarto_numero
    global quinto_numero
    global sexto_numero
    global setimo_numero
    global oitavo_numero
    global nono_numero
    global text_cresente

    texto_instrução = Label(
        janela_cresente, text='coloque os numeros para ficar na ordem cresente  abaixo ')
    texto_instrução.grid(column=2, row=1)

    primeiro_numero = Entry(janela_cresente)
    primeiro_numero.grid(column=2, row=3)

    segundo_numero = Entry(janela_cresente)
    segundo_numero.grid(column=2, row=4)

    terceiro_numero = Entry(janela_cresente)
    terceiro_numero.grid(column=2, row=6)

    quarto_numero = Entry(janela_cresente)
    quarto_numero.grid(column=2, row=7)

    quinto_numero = Entry(janela_cresente)
    quinto_numero.grid(column=2, row=8)

    sexto_numero = Entry(janela_cresente)
    sexto_numero.grid(column=2, row=9)

    setimo_numero = Entry(janela_cresente)
    setimo_numero.grid(column=2, row=10)

    oitavo_numero = Entry(janela_cresente)
    oitavo_numero.grid(column=2, row=11)

    nono_numero = Entry(janela_cresente)
    nono_numero.grid(column=2, row=12)

    text_cresente = Label(janela_cresente, text="")
    text_cresente.grid(column=2, row=14)

    botao_gerar_cresente = Button(
        janela_cresente, text='clique aqui', command=cresente)
    botao_gerar_cresente.grid(column=2, row=15)
# area
def triangulo():  # area do triangulo
    altura = altura_triangulo.get()
    base = base_triangulo.get()

    base1 = float(base)
    altura1 = float(altura)
    area = altura1 * base1 / 2

    texto_botao1["text"] = area
def quadrado():  # area do quadrado
    altura = altura_triangulo.get()
    base = base_triangulo.get()

    base1 = float(altura)
    base2 = float(base)

    if base1 == base2:
        resultado = base1 * base2
        texto_botao1["text"] = resultado
    else:
        erro = 'Isso não é um quadrado'
        texto_botao1["text"] = erro
def retangulo():  # area do retangulo
    altura = altura_triangulo.get()
    base = base_triangulo.get()

    altura1 = float(altura)
    base1 = float(base)

    if altura1 == base1:
        erro = 'Isso não é um retangulo'
        texto_botao1["text"] = erro

    else:
        resultado = altura1 * base1
        texto_botao1["text"] = resultado
def abrir_janela_Triangulo():  # janela do calculo das areas
    global base_triangulo
    global altura_triangulo
    global texto_botao1

    janela_triangulo = Toplevel(janela1)
    # comando para mudar o titulo da janela do TKinter
    janela_triangulo.title("area")
    # comando para mudar as dimenções da janela do TKinter
    janela_triangulo.geometry("250x250")
    janela_triangulo.configure(bg='red')

    textarea = Label(janela_triangulo, text="altura:")
    textarea.grid(column=0, row=0)

    altura_triangulo = Entry(janela_triangulo)
    altura_triangulo.grid(column=0, row=1)

    textbase = Label(janela_triangulo, text="base:")
    textbase.grid(column=0, row=2)

    base_triangulo = Entry(janela_triangulo)
    base_triangulo.grid(column=0, row=3)

    textinfo = Label(janela_triangulo, text="area igual a:")
    textinfo.grid(column=0, row=4)

    texto_botao1 = Label(janela_triangulo, text="")
    texto_botao1.grid(column=0, row=5)

    botao_gerar_area = Button(
        janela_triangulo, text="Clique aqui para calcular a area do triangulo", command=triangulo)
    botao_gerar_area.grid(column=0, row=6)

    botao_gerar_area = Button(
        janela_triangulo, text="Clique aqui para calcular a area do quadrado", command=quadrado)
    botao_gerar_area.grid(column=0, row=7)

    botao_gerar_area = Button(
        janela_triangulo, text="Clique aqui para calcular a area do retangulo", command=retangulo)
    botao_gerar_area.grid(column=0, row=8)
# medidor de temperaturas
def graus():  # medidas
    graus = valor_graus.get()
    graus1 = float(graus)
    fahrenheit = (9 * graus1 + 160) / 5

    valor2 = float(graus)

    kelvins = valor2 + 273, 15

    text_fahrenheit["text"] = fahrenheit
    text_kelvins["text"] = kelvins
    text_graus["text"] = graus
def abrir_janela_graus():  # janela das medidas de temeratua
    janela_graus = Toplevel(janela1)
    # comando para mudar o titulo da janela do TKinter
    janela_graus.title("teperatura")
    # comando para mudar as dimenções da janela do TKinter
    janela_graus.geometry("130x200")
    janela_graus.configure(bg='grey')

    global valor_graus
    global text_fahrenheit
    global text_graus
    global text_kelvins

    textograus = Label(janela_graus, text='graus')
    textograus.grid(column=2, row=2)

    valor_graus = Entry(janela_graus)
    valor_graus.grid(column=2, row=3)

    texto_fahrenheit = Label(janela_graus, text='valor em fahrenheit ')
    texto_fahrenheit.grid(column=2, row=4)

    text_fahrenheit = Label(janela_graus, text="")
    text_fahrenheit.grid(column=2, row=5)

    texto_kelvins = Label(janela_graus, text='valor em kelvins ')
    texto_kelvins.grid(column=2, row=6)

    text_kelvins = Label(janela_graus, text="")
    text_kelvins.grid(column=2, row=7)

    texto_graus = Label(janela_graus, text='valor em graus ')
    texto_graus.grid(column=2, row=8)

    text_graus = Label(janela_graus, text="")
    text_graus.grid(column=2, row=9)

    botao_gerar_graus = Button(janela_graus, text='clique aqui', command=graus)
    botao_gerar_graus.grid(column=2, row=10)
# sorteio
def sorteio():  # sorteio
    import random

    alunos = []
    pessoa1 = valor_primeiro.get()
    pessoa2 = valor_segundo.get()
    pessoa3 = valor_terceiro.get()
    pessoa4 = valor_quarto.get()
    pessoa5 = valor_quinto.get()

    alunos.append(pessoa1)
    alunos.append(pessoa2)
    alunos.append(pessoa3)
    alunos.append(pessoa4)
    alunos.append(pessoa5)

    random.shuffle(alunos)

    texto_info3["text"] = alunos
def abrir_janela_sorteio():  # janela soreteio
    janela_sorteio = Toplevel(janela1)
    janela_sorteio.title("sorteio")
    janela_sorteio.geometry("200x200")
    janela_sorteio.configure(bg='pink')

    global valor_primeiro
    global valor_segundo
    global valor_terceiro
    global valor_quarto
    global valor_quinto
    global texto_info3

    texto_info = Label(
        janela_sorteio, text='coloque os nomes das pessas abaixo')
    texto_info.grid(column=2, row=1)

    valor_primeiro = Entry(janela_sorteio)
    valor_primeiro.grid(column=2, row=2)

    valor_segundo = Entry(janela_sorteio)
    valor_segundo.grid(column=2, row=3)

    valor_terceiro = Entry(janela_sorteio)
    valor_terceiro.grid(column=2, row=4)

    valor_quarto = Entry(janela_sorteio)
    valor_quarto.grid(column=2, row=5)

    valor_quinto = Entry(janela_sorteio)
    valor_quinto.grid(column=2, row=6)

    texto_info2 = Label(janela_sorteio, text='a ordem sorteada foi')
    texto_info2.grid(column=2, row=7)

    texto_info3 = Label(janela_sorteio, text="")
    texto_info3.grid(column=2, row=8)

    botao_gerar_sorteio = Button(
        janela_sorteio, text='clique aqui', command=sorteio)
    botao_gerar_sorteio.grid(column=2, row=9)
# gerador de senha
def gerador_de_senha():  # senhas de 8 digitos
    from lib2to3.pygram import Symbols
    import random

    caractersM= ''
    minuscula = ''
    numeros = ''
    simbolos = ''
   
    minuscula = minuscula_SouN.get()#resultado da caixa de texto das letras minusculas
    if minuscula == 'sim':
        caractersM = 'abcdefghijklmnopqrstuwxyz'
        senha = caractersM + minuscula + simbolos + numeros
    elif minuscula =='nao':
        minuscula = ''
        senha = caractersM + simbolos + numeros

    numeros = numeros_SouN.get()
    if numeros == 'sim':
        numeros = '1234567890'
        senha = caractersM + minuscula + simbolos + numeros
    elif numeros == 'nao':
        numeros = ''
        senha = minuscula + caractersM + simbolos

    simbolos = simbolos_SouN.get()
    if simbolos == 'sim':
        simbolos = '!@#$%¨&*'
        senha = caractersM + minuscula + simbolos + numeros
    elif simbolos == 'nao':
        simbolos = ''
        senha = minuscula + caractersM + numeros

    maiscula = maiuscula_SouN.get()#resultado da caixa de texto das letras maisculas
    if maiscula == 'nao':
        caractersM = ''
        senha = minuscula + simbolos + numeros
    elif maiscula == 'sim':
        caractersM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        senha = caractersM + minuscula + simbolos + numeros

    tam = tamanho_da_senha1.get()
    tamanho = int(tam)
    tamanho_da_senha = tamanho

    if tamanho_da_senha > 6 < 15:
        senha_final = "".join(random.sample(senha, tamanho_da_senha))

        text_senha["text"] = senha_final

    else:
        text_senha["text"] = 'coloque um tamanho valido'
def abrir_janela_gerador_senha():  # janela do gerador de senhas

    janela_senha = Toplevel(janela1)
    janela_senha.title("sorteio")
    janela_senha.geometry("500x500")
    janela_senha.configure(bg='light green')

    global text_senha
    global tamanho_da_senha1
    global maiuscula_SouN
    global minuscula_SouN
    global numeros_SouN
    global simbolos_SouN

    texto_inicial = Label(janela_senha, text='a senha gerada foi ')#parte de cima do resultado final
    texto_inicial.grid(column=2, row=11)

    text_senha = Label(janela_senha, text="")#resultado final
    text_senha.grid(column=2, row=12)

    tamanho_da_senha1 = Entry(janela_senha)#caixa de texto para definir o tamanho da senha
    tamanho_da_senha1.grid(column=2, row=2)

    botao_gerar_senha = Button( janela_senha, text='gerar senha', command=gerador_de_senha)#botao para gerar a senha 
    botao_gerar_senha.grid(column=2, row=13)

    inf = Label(janela_senha, text='definir o tamanho da senha (responda com um numero entre 6 e 15)')#indicar a caixa de texto para definir o tamanho da senha 
    inf.grid(column=2, row=1)

    inf1 = Label(janela_senha, text='adicionar letras maiusculas(responda com sim ou nao)')
    inf1.grid(column= 2, row =3)

    maiuscula_SouN = Entry(janela_senha)#caixa de texto para selecionar letras maiusculas 
    maiuscula_SouN.grid(column=2, row=4)

    inf2 = Label(janela_senha, text='adicionar letras minusculas(responda com sim ou nao)')
    inf2.grid(column= 2, row= 5)

    minuscula_SouN = Entry(janela_senha)#caixa de texto para selecionar letras minuscula
    minuscula_SouN.grid(column= 2, row=6)

    inf3 = Label(janela_senha, text='adicionar numeros(responda com sim ou nao)')
    inf3.grid(column= 2, row= 7)   

    numeros_SouN = Entry(janela_senha)#caixa de texto para selecioanr numeros
    numeros_SouN.grid(column= 2, row= 8)

    inf2 = Label(janela_senha, text='adicionar letras simbolos(responda com sim ou nao)')
    inf2.grid(column= 2, row= 9)

    simbolos_SouN = Entry(janela_senha)#caixa de texto para selecionar simbolos
    simbolos_SouN.grid(column= 2, row= 10)
# calculo de IMC
def abrir_janela_IMC():  # janela do calculo de IMC
    janela_imc = Toplevel(janela1)
    janela_imc.title("IMC")
    janela_imc.geometry("100x170")
    janela_imc.configure(bg='light blue')
    pesoinfo = Label(janela_imc, text='Peso')
    global peso
    global altura
    global texto_botao
    pesoinfo.grid(column=0, row=0)
    peso = Entry(janela_imc)
    peso.grid(column=0, row=1)

    alturainfo = Label(janela_imc, text="Altura")
    alturainfo.grid(column=0, row=2)
    altura = Entry(janela_imc)
    altura.grid(column=0, row=4)

    botaoimc = Button(janela_imc, text="Clique aqui", command=imc)
    botaoimc.grid(column=0, row=5)
    textinfo = Label(janela_imc, text="Seu imc é:")
    textinfo.grid(column=0, row=6)
    texto_botao = Label(janela_imc, text="")
    texto_botao.grid(column=0, row=7)
def imc():  # codigo que calcula o IMC
    pesonum = peso.get()
    alturanum = altura.get()
    pesofloat = float(pesonum)
    alturafloat = float(alturanum)
    calcfinal = pesofloat/alturafloat**2
    texto_botao["text"] = calcfinal
# jogos
def janela_pedra():  # jogo do pedra papel e tesoura
    janela_pedra1 = Toplevel(janela1)
    janela_pedra1.title("IMC")
    janela_pedra1.geometry("200x200")
    janela_pedra1.configure(bg='Navy blue')
    global pergunta
    global computador_escolha
    global resultado

    texto_introdutorio = Label(
        janela_pedra1, text='Escolha uma opcao para se jogar:')
    texto_introdutorio.grid(column=1, row=1)
    texto_introdutorio1 = Label(janela_pedra1, text='[0] = Pedra')
    texto_introdutorio1.grid(column=1, row=2)
    texto_introdutorio2 = Label(janela_pedra1, text='[1] = Papel')
    texto_introdutorio2.grid(column=1, row=3)
    texto_introdutorio3 = Label(janela_pedra1, text='[2] = Tesoura')
    texto_introdutorio3.grid(column=1, row=4)

    texto_guia = Label(janela_pedra1, text='sua escolha')
    texto_guia.grid(column=1, row=5)

    pergunta = Entry(janela_pedra1)
    pergunta.grid(column=1, row=6)

    computador_escolha = Label(janela_pedra1, text="")
    computador_escolha.grid(column=1, row=7)

    resultado = Label(janela_pedra1, text="")
    resultado.grid(column=1, row=8)

    botao = Button(janela_pedra1, text='jogar', command=pedra_papel_tessoura)
    botao.grid(column=1, row=9)
def pedra_papel_tessoura():
    import random
    pergunta1 = pergunta.get()
    perguntar = int(pergunta1)
    computador = random.randint(0, 2)

    if computador == 0:
        computador_escolha["text"] = "o computador escolheu pedra"
        if perguntar == 0:
            resultado["text"] = "empate"
        elif perguntar == 1:
            resultado["text"] = "Você Venceu"
        elif perguntar == 2:
            resultado["text"] = "você perdeu"
    elif computador == 1:
        computador_escolha["text"] = "o computador escolheu papel"
        if perguntar == 0:
            resultado["text"] = "Você perdeu"
        elif perguntar == 1:
            resultado["text"] = "empate"
        elif perguntar == 2:
            resultado["text"] = "Voce venceu"
    elif computador == 2:
        computador_escolha["text"] = "o computador escolheu Tesoura"
        if perguntar == 0:
            resultado["text"] = "voce Venceu"
        elif perguntar == 1:
            resultado["text"] = "voce perdeu"
        elif perguntar == 2:
            resultado["text"] = "empate"
    else:
        print("Operacao invalida")
# janela inicial
janela1 = Tk()
janela1.title('menu')
janela1.geometry('225x250')
janela1.configure(bg='brown')  # definr cor

botaotabuada = Button(janela1,  text="calculadora",  command=openNewWindow)
botaotabuada.grid(column=2, row=1)  # botao para abrir a cauculadora

botaotabuada = Button(janela1,  text="calculos de area ",command=abrir_janela_Triangulo)
botaotabuada.grid(column=2, row=2)  # botao para abrir o calculador de area

botaograus = Button(janela1, text='converter graus em fahrenheit e kelvins', command=abrir_janela_graus)
botaograus.grid(column=2, row=3)  # botao para abrir o calculo de graus

botaoCresente = Button(janela1,  text='gerar ordem cresente', command=abrir_janela_cresente)
botaoCresente.grid(column=2, row=7)  # janela q deixa numeros na ordem cresente

botaosorteio = Button(janela1, text='fazer um sorteio entre 5 pessoas', command=abrir_janela_sorteio)
botaosorteio.grid(column=2, row=9)  # abrir janela do sorteio

botao_senha = Button(janela1, text='gerar uma senha', command=abrir_janela_gerador_senha)
botao_senha.grid(column=2, row=10)  # janela do gerador de senhas

botao_imc = Button(janela1, text='calcular IMC', command=abrir_janela_IMC)
botao_imc.grid(column=2, row=11)  # janela do calculo de IMC

botao_padra = Button(janela1, text='jogar padra papel e tesoura', command=janela_pedra)
botao_padra.grid(column=2, row=12)

janela1.mainloop()
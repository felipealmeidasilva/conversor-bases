from tkinter import *
from tkinter import ttk

valores = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G":"16", "H": "17", "I": "18", "J":"19", "K": "20",
           "L": "21", "M":"22", "N": "23", "O": "24", "P": "25", "Q":"26", "R": "27", "S": "28", "T": "29", "U":"30", "V":"31", "W":"32",
           "X":"33" ,"Y":"34", "Z": "35"}

def converter_base(*args):
    ## Recebendo os valores digitados
    try:
        valor = str(numero.get())
        valor_inicial = valor
        valor_listado = []
        
        ## Converte o valor digitado para lista
        for i in range(len(valor)):
            valor_listado.append(valor[i])

        for i in range(len(valor_listado)):
            if valor_listado[i] in valores:
                valor_listado[i]=str(valores[valor_listado[i]])
        
        base_origem = str(opcoesvar.get())
        base_origem = int(base_origem[5:7])

        base_destino = str(opcoesvar_destino.get())
        base_destino = int(base_destino[5:7])

        
    except ValueError:
        pass
    
    
    def converter_para_base10(num, base_ori):
        if base_ori == 10:
            acumulador = ''
            for i in range(len(num)):
                acumulador += num[i]
            return acumulador
        else:

            num_invertido = num[::-1]
            
            if "." in num_invertido:
                for i in range(len(num_invertido)):
                    if num_invertido[i] == ".":
                        valor_limite = i
                real = num_invertido[0:valor_limite]
                inteiro = num_invertido[valor_limite+1:]
            else:
                real = "0"
                inteiro = num_invertido[0:]
            
            acumulador = 0
            for i in range(len(inteiro)):
                acumulador += int(inteiro[i])*(base_ori**i)
            
            acumulador_real = 0
            if real != "0":
                real_invertido = real[::-1]
                for i in range(len(real_invertido)):
                    acumulador_real += int(real_invertido[i])*(base_ori)**(-(i+1))
            
            acumulador = acumulador + acumulador_real
            return acumulador
        
    def converter_da_base10(numero, base_destino):
        numero = str(numero)
        if base_destino == 10:
            return numero
        else:
            if "." in numero:
                numero = str(numero).split(".")
                numero_inteiro = numero[0]
                numero_float = numero[1]
            else:
                numero_inteiro=numero
                numero_float = 0

            result_lista = []
            result = int(numero_inteiro)
            div = result
            while(div>0):
                result = div % base_destino
                div = div//base_destino
                result_lista.append(result)
            result_lista_att = []
            for i in range(len(result_lista)):
                if int(result_lista[i])>9:
                    for k, v in valores.items():
                        if str(result_lista[i]) == v:
                            result_lista_att.append(k)
                else:
                    result_lista_att.append(result_lista[i])
            result_lista_att = result_lista_att[::-1]

            template = ''
            for i in range(len(result_lista_att)):
                template += '' + str(result_lista_att[i])
            

            if base_destino == 2:
                resultado_float_att = []
                count = 0
                #print(numero_float)
                resultado = int(numero_float)
                while(count!=3):
                    resultado *= base_destino
                    #print(resultado)
                    if resultado<1000:
                        resultado_float_att.append(0)
                        count += 1
                    elif resultado>1000:
                        resultado_float_att.append(1)
                        resultado = resultado-1000
                        count += 1
                    elif resultado==1000:
                        resultado_float_att.append(1)
                        break
                #print(resultado_float)
            else:
                resultado_float = []
                result = int(numero_float)
                div = result
                while(div>0):
                    result = div % base_destino
                    div = div//base_destino
                    resultado_float.append(result)
                resultado_float_att = []
                for i in range(len(resultado_float)):
                    if int(resultado_float[i])>9:
                        for k, v in valores.items():
                            if str(resultado_float[i]) == v:
                                resultado_float_att.append(k)
                    else:
                        resultado_float_att.append(resultado_float[i])
                resultado_float_att = resultado_float_att[::-1]
            
            template_float = ','
            for i in range(len(resultado_float_att)):
                template_float += '' + str(resultado_float_att[i])

            template = template + template_float
            return template     
            

    resultado = converter_da_base10(converter_para_base10(valor_listado, base_origem), base_destino)
    #calculo.set(str(resultado))
    calculo.config(text=f"{valor_inicial} (Base {base_origem}) = {resultado} (Base {base_destino})")
    


root = Tk()
root.title("Conversor de Bases")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

numero = StringVar()
numero_entry = ttk.Entry(mainframe, width=7, textvariable=numero)
numero_entry.grid(column=2, row=1, sticky=(W, E))



calculo = ttk.Label(mainframe, text="")
calculo.grid(column=1, row=4, sticky=E)

opcoesvar = StringVar()
opcoes = ttk.Combobox(mainframe, textvariable=opcoesvar, values=["Base 2 (Binário)", 
    "Base 3 (Ternário)", "Base 4 (Quaternário)", "Base 5 (Quinário)", "Base 6 (Senário)", 
    "Base 7 (Septenário)", "Base 8 (Octal)", "Base 9 (Nonário)", "Base 10 (Decimal)", "Base 11", 
    "Base 12 (Duodecimal)", "Base 13", "Base 14", "Base 15", "Base 16 (Hexadecimal)", "Base 17", 
    "Base 18", "Base 19", "Base 20", "Base 21", "Base 22", "Base 23", "Base 24", "Base 25", "Base 26",
    "Base 27", "Base 28", "Base 29", "Base 30", "Base 31", "Base 32", "Base 33", "Base 34", "Base 35", "Base 36"]).grid(column=3, row=1, sticky=(W, E))

opcoesvar_destino = StringVar()
opcoes_destino = ttk.Combobox(mainframe, textvariable=opcoesvar_destino, values=["Base 2 (Binário)", 
    "Base 3 (Ternário)", "Base 4 (Quaternário)", "Base 5 (Quinário)", "Base 6 (Senário)", 
    "Base 7 (Septenário)", "Base 8 (Octal)", "Base 9 (Nonário)", "Base 10 (Decimal)", "Base 11", 
    "Base 12 (Duodecimal)", "Base 13", "Base 14", "Base 15", "Base 16 (Hexadecimal)", "Base 17", 
    "Base 18", "Base 19", "Base 20", "Base 21", "Base 22", "Base 23", "Base 24", "Base 25", "Base 26",
    "Base 27", "Base 28", "Base 29", "Base 30", "Base 31", "Base 32", "Base 33", "Base 34", "Base 35", "Base 36"]).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Converter", command=converter_base).grid(column=3, row=5, sticky=W)


ttk.Label(mainframe, text="Digite um número e sua base (Ex: 0000.0000)").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Selecione a Base de Destino").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

numero_entry.focus()
root.bind("<Return>", converter_base)

root.mainloop()
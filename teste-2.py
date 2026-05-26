import tkinter as tk
from tkinter import messagebox

# --------- PALETA DE CORES MODERNAS ---------
COR_FUNDO = "#121212"       
COR_BOTAO = "#00C853"       
COR_TEXTO = "#FFFFFF"      
COR_ENTRADA = "#1E1E1E"     

# --------- FUNÇÃO PARA CALCULAR ---------
def calcular(operacao):
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        
        if operacao == 'SOMA': res = x + y
        elif operacao == 'SUBTRACAO': res = x - y
        elif operacao == 'MULTIPLICACAO': res = x * y
        elif operacao == 'DIVISAO':
            if y != 0: 
                res = x / y
            else:
                messagebox.showerror("Erro", "Divisão por zero!")
                return

        label_resultado.config(text=f"RESULTADO: {res}")
        
    except ValueError:
        messagebox.showerror("Erro de Digitação", "Por favor, digite apenas números!")

# --------- CONFIGURAÇÃO DA JANELA ---------
janela = tk.Tk()
janela.title("Calculadora Moderna")
janela.geometry("380x480")
janela.configure(bg=COR_FUNDO) 
janela.resizable(False, False) 

# Fontes
fonte_titulo = ("Segoe UI", 12, "bold")
fonte_input = ("Segoe UI", 16)
fonte_botao = ("Segoe UI", 10, "bold")

# --------- INTERFACE VISUAL ---------


tk.Label(janela, text="PRIMEIRO VALOR", bg=COR_FUNDO, fg=COR_BOTAO, font=fonte_titulo).pack(pady=(25, 5))
entry_x = tk.Entry(janela, font=fonte_input, bg=COR_ENTRADA, fg=COR_TEXTO, 
                   insertbackground=COR_BOTAO, relief="flat", justify="center")
entry_x.pack(ipady=8, pady=5, padx=40, fill="x")


tk.Label(janela, text="SEGUNDO VALOR", bg=COR_FUNDO, fg=COR_BOTAO, font=fonte_titulo).pack(pady=(15, 5))
entry_y = tk.Entry(janela, font=fonte_input, bg=COR_ENTRADA, fg=COR_TEXTO, 
                   insertbackground=COR_BOTAO, relief="flat", justify="center")
entry_y.pack(ipady=8, pady=5, padx=40, fill="x")


tk.Label(janela, text="ESCOLHA A OPERAÇÃO", bg=COR_FUNDO, fg=COR_TEXTO, font=fonte_titulo).pack(pady=(25, 10))

frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack()

def criar_botao(texto, op):
    return tk.Button(frame_botoes, text=texto, bg=COR_BOTAO, fg=COR_FUNDO, font=fonte_botao, 
                     relief="flat", cursor="hand2", 
                     activebackground="#00E676", activeforeground=COR_FUNDO,
                     command=lambda: calcular(op), width=14)

btn_soma = criar_botao("+ SOMA", "SOMA")
btn_soma.grid(row=0, column=0, padx=5, pady=5, ipady=8)

btn_sub = criar_botao("- SUBTRAÇÃO", "SUBTRACAO")
btn_sub.grid(row=0, column=1, padx=5, pady=5, ipady=8)

btn_mult = criar_botao("× MULTIPLICAR", "MULTIPLICACAO")
btn_mult.grid(row=1, column=0, padx=5, pady=5, ipady=8)

btn_div = criar_botao("÷ DIVIDIR", "DIVISAO")
btn_div.grid(row=1, column=1, padx=5, pady=5, ipady=8)


label_resultado = tk.Label(janela, text="RESULTADO: ---", bg=COR_FUNDO, fg=COR_BOTAO, font=("Segoe UI", 18, "bold"))
label_resultado.pack(pady=30)


janela.mainloop()
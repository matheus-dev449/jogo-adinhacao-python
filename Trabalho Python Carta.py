import tkinter as tk
import random


#  CORES
BG = "#1e1e2f"
BTN = "#3a3a5c"
HOVER = "#505080"
TEXT = "#ffffff"
SUCCESS = "#4CAF50"
ERROR = "#E53935"


pontuacao = 0
tentativas = 0


janela = tk.Tk()
janela.title("🎴 Carta Coringa")
janela.geometry("400x400")
janela.config(bg=BG)




def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()




#  MENU
def menu():
    limpar_tela()


    titulo = tk.Label(
        janela,
        text="🎴 Carta Coringa",
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=TEXT
    )
    titulo.pack(pady=30)


    jogar_btn = tk.Button(
        janela,
        text="Jogar",
        font=("Arial", 14),
        bg=BTN,
        fg=TEXT,
        width=15,
        command=jogar
    )
    jogar_btn.pack(pady=10)


    sair_btn = tk.Button(
        janela,
        text="Sair",
        font=("Arial", 14),
        bg=BTN,
        fg=TEXT,
        width=15,
        command=janela.quit
    )
    sair_btn.pack(pady=10)




#  GERAR CORINGA
def gerar_numero():
    return random.randint(1, 3)




#  VERIFICAR RESULTADO
def verificar_resultado(escolha, coringa):
    global pontuacao, tentativas
    tentativas += 1


    limpar_tela()


    if escolha == coringa:
        pontuacao += 1
        cor = SUCCESS
        texto = "🎉 Você acertou!"
    else:
        cor = ERROR
        texto = f"❌ Errou! Era a carta {coringa}"


    resultado = tk.Label(
        janela,
        text=texto,
        font=("Arial", 18, "bold"),
        fg=cor,
        bg=BG
    )
    resultado.pack(pady=20)


    placar_label = tk.Label(
        janela,
        text=f"Pontuação: {pontuacao} | Tentativas: {tentativas}",
        font=("Arial", 12),
        fg=TEXT,
        bg=BG
    )
    placar_label.pack(pady=10)


    tk.Button(
        janela,
        text="Jogar novamente",
        bg=BTN,
        fg=TEXT,
        width=18,
        command=jogar
    ).pack(pady=5)


    tk.Button(
        janela,
        text="Menu",
        bg=BTN,
        fg=TEXT,
        width=18,
        command=menu
    ).pack(pady=5)




#  JOGAR
def jogar():
    limpar_tela()
    coringa = gerar_numero()


    texto = tk.Label(
        janela,
        text="Escolha uma carta",
        font=("Arial", 16),
        fg=TEXT,
        bg=BG
    )
    texto.pack(pady=20)


    frame_cartas = tk.Frame(janela, bg=BG)
    frame_cartas.pack(pady=20)


    # Criando cartas grandes
    for i in range(1, 4):
        btn = tk.Button(
            frame_cartas,
            text="🂠",
            font=("Arial", 30),
            bg=BTN,
            fg=TEXT,
            width=3,
            height=1,
            command=lambda escolha=i: verificar_resultado(escolha, coringa)
        )
        btn.grid(row=0, column=i, padx=10)




#  INICIO
menu()
janela.mainloop()
import tkinter as tk
import random
import math
from tkinter import messagebox

def jogar_roleta():
    root.withdraw()  # Oculta a janela inicial

    def girar_seta():
        duracao_total = 3000  # Duração total da animação (ms)
        passos_iniciais = 10  # Menor intervalo entre passos (ms)
        voltas = 8  # Número de voltas completas antes de desacelerar

        # Definir números e probabilidades
        numeros = list(range(1, 21))
        probabilidades = (
            [30] * 4 +  # 1 a 6: 30%
            [37] * 9 +  # 7 a 14: 37%
            [20] * 5 +  # 15 a 18: 20%
            [13] * 2    # 19 e 20: 13%
        )

        # Escolher o número vencedor
        numero_vencedor = random.choices(numeros, weights=probabilidades, k=1)[0]

        # Determinar o setor e calcular o ângulo de destino
        setor_vencedor = setores_embaralhados.index(numero_vencedor)
        angulo_central = setor_vencedor * angulo_por_setor + angulo_por_setor / 2
        angulo_deslocado = random.uniform(-5, 5)  # Pequeno ajuste para evitar exatidão
        angulo_final = angulo_central + angulo_deslocado

        angulo_total = voltas * 360 + angulo_final
        passo_atual = 0

        def animar_giro():
            nonlocal passo_atual
            if passo_atual <= passos_totais:
                if not canvas.winfo_exists():
                    return
                # Calcular o ângulo atual e o intervalo do passo
                angulo_atual = (angulo_total / passos_totais) * passo_atual
                intervalo = max(passos_iniciais, int(duracao_total / passos_totais * (1 + passo_atual / passos_totais)))
                atualiza_seta(angulo_atual)
                roleta.update()
                roleta.after(intervalo, animar_giro)
                passo_atual += 1
            else:
                print(f"Resultado: {numero_vencedor} M&Ms")
                mostrar_pontuacao(numero_vencedor)

        passos_totais = 300  # Total de passos para suavizar a animação
        animar_giro()

    def atualiza_seta(angulo_atual):
        """Atualiza a posição da seta ao redor da roleta."""
        canvas.delete("seta")  # Remove a seta antiga
        angulo_radianos = math.radians(angulo_atual)
        ponta_x = 200 + 150 * math.cos(angulo_radianos)  # Ponta mais próxima da roleta
        ponta_y = 200 - 150 * math.sin(angulo_radianos)
        base1_x = 200 + 180 * math.cos(angulo_radianos + math.radians(10))
        base1_y = 200 - 180 * math.sin(angulo_radianos + math.radians(10))
        base2_x = 200 + 180 * math.cos(angulo_radianos - math.radians(10))
        base2_y = 200 - 180 * math.sin(angulo_radianos - math.radians(10))
        canvas.create_polygon(
            ponta_x, ponta_y, base1_x, base1_y, base2_x, base2_y,
            fill="red", outline="black", tags="seta"
        )

    def mostrar_pontuacao(numero_ganho):
        """Exibe o resultado e fecha a janela."""
        messagebox.showinfo("Resultado", f"Você ganhou {numero_ganho} M&Ms!")
        roleta.destroy()
        root.destroy()

    # Configuração da janela principal da roleta
    roleta = tk.Toplevel(root)
    roleta.title("Roleta de M&Ms")

    # Canvas para desenhar a roleta e a seta
    canvas = tk.Canvas(roleta, width=400, height=400, bg="white")
    canvas.pack()

    # Configuração dos setores da roleta
    setores = 20
    angulo_por_setor = 360 / setores
    cores = ["#ff6347", "#32cd32", "#ffcc00", "#4682b4"] * (setores // 4)

    # Criação dos números embaralhados
    setores_embaralhados = list(range(1, 21))
    random.shuffle(setores_embaralhados)

    def desenhar_roleta():
        """Desenha a roleta fixa no centro do canvas."""
        for i in range(setores):
            angulo_inicio = i * angulo_por_setor
            canvas.create_arc(
                50, 50, 350, 350,
                start=angulo_inicio, extent=angulo_por_setor,
                fill=cores[i], outline="black"
            )

            # Determina a posição do texto no setor
            angulo_medio = math.radians(angulo_inicio + angulo_por_setor / 2)
            texto_x = 200 + 120 * math.cos(angulo_medio)
            texto_y = 200 - 120 * math.sin(angulo_medio)
            canvas.create_text(
                texto_x, texto_y, text=str(setores_embaralhados[i]),
                font=("Arial", 10, "bold"), fill="black"
            )

    # Desenha a roleta e a seta inicial
    desenhar_roleta()
    atualiza_seta(0)  # Mostra a seta estática inicialmente

    # Botão para iniciar o giro
    tk.Button(roleta, text="Girar Seta", command=girar_seta).pack(pady=20)

    roleta.mainloop()

# Inicializa a aplicação
root = tk.Tk()
root.title("Roleta")
root.geometry("0x0")  # Oculta a janela principal
jogar_roleta()

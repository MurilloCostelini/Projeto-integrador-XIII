import tkinter as tk
import random
import math
from tkinter import messagebox

def jogar_roleta(root, callback=None):
    # Não é mais necessário ocultar a janela principal
    # root.withdraw()  # Isso não será necessário agora

    def girar_seta():
        duracao_total = 3000  # Duração total da animação (ms)
        passos_iniciais = 10  # Menor intervalo entre passos (ms)
        voltas = 8  # Número de voltas completas antes de desacelerar

        # Definir números e probabilidades
        numeros = list(range(1, 21))
        probabilidades = [1] * 20  # Probabilidades iguais para números de 1 a 20

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
                angulo_atual = (angulo_total / passos_totais) * passo_atual
                intervalo = max(passos_iniciais, int(duracao_total / passos_totais * (1 + passo_atual / passos_totais)))
                atualiza_seta(angulo_atual)
                roleta.update()
                roleta.after(intervalo, animar_giro)
                passo_atual += 1
            else:
                # Quando a roleta parar de girar, chama a função callback com o resultado
                quantidades = gerar_comando(numero_vencedor)
                if callback:
                    callback(quantidades)  # Passa as quantidades para a função callback

        passos_totais = 300  # Total de passos para suavizar a animação
        animar_giro()

    def gerar_comando(numero_total):
        """Gera as quantidades de M&Ms para cada cor."""
        motores = ["LARANJA", "VERMELHO", "AMARELO", "AZUL", "VERDE"]
        base = numero_total // 5  # Quantidade base para cada motor
        restante = numero_total % 5  # Restante para distribuir

        # Distribuição uniforme dos M&Ms entre os motores
        resultado = {motor: base for motor in motores}
        for i in range(restante):
            resultado[motores[i]] += 1

        # Retorna as quantidades das cores (sem os nomes das cores)
        return list(resultado.values())

    def atualiza_seta(angulo_atual):
        """Atualiza a posição da seta ao redor da roleta."""
        canvas.delete("seta")  # Remove a seta antiga
        angulo_radianos = math.radians(angulo_atual)
        ponta_x = 200 + 150 * math.cos(angulo_radianos)
        ponta_y = 200 - 150 * math.sin(angulo_radianos)
        base1_x = 200 + 180 * math.cos(angulo_radianos + math.radians(10))
        base1_y = 200 - 180 * math.sin(angulo_radianos + math.radians(10))
        base2_x = 200 + 180 * math.cos(angulo_radianos - math.radians(10))
        base2_y = 200 - 180 * math.sin(angulo_radianos - math.radians(10))
        canvas.create_polygon(
            ponta_x, ponta_y, base1_x, base1_y, base2_x, base2_y,
            fill="red", outline="black", tags="seta"
        )

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

    setores_embaralhados = list(range(1, 21))
    random.shuffle(setores_embaralhados)

    def desenhar_roleta():
        """Desenha a roleta no canvas."""
        for i in range(setores):
            angulo_inicio = i * angulo_por_setor
            canvas.create_arc(
                50, 50, 350, 350,
                start=angulo_inicio, extent=angulo_por_setor,
                fill=cores[i], outline="black"
            )
            angulo_medio = math.radians(angulo_inicio + angulo_por_setor / 2)
            texto_x = 200 + 120 * math.cos(angulo_medio)
            texto_y = 200 - 120 * math.sin(angulo_medio)
            canvas.create_text(
                texto_x, texto_y, text=str(setores_embaralhados[i]),
                font=("Arial", 10, "bold"), fill="black"
            )

    desenhar_roleta()
    atualiza_seta(0)

    tk.Button(roleta, text="Girar Seta", command=girar_seta).pack(pady=20)
    roleta.mainloop()

if __name__ == "__main__":
    resultado = jogar_roleta()  # Agora retorna o resultado ao invés de exibir

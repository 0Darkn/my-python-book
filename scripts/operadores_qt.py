# pip install pyqt5
# operadores_qt.py
# Demonstração dos tipos de operadores em Python com uma interface Qt (PyQt5).
# Comentários e texto em português europeu, explicando passo a passo.

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox
)


class JanelaOperadores(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Título da janela
        self.setWindowTitle("Tipos de Operadores em Python — Demo com Qt")

        # Layout principal vertical
        vbox = QVBoxLayout()

        # Linha para escolher o tipo de operador
        hbox_tipo = QHBoxLayout()
        hbox_tipo.addWidget(QLabel("Seleciona tipo de operador:"))
        self.combo_tipo = QComboBox()
        # Adicionamos as categorias de operadores
        self.combo_tipo.addItems([
            "Aritméticos",
            "Atribuição",
            "Comparação",
            "Lógicos",
            "Bitwise (bit a bit)",
            "Pertença (in / not in)",
            "Identidade (is / is not)",
            "Ternário"
        ])
        hbox_tipo.addWidget(self.combo_tipo)
        vbox.addLayout(hbox_tipo)

        # Entradas para operandos (usar como a e b)
        entradas_h = QHBoxLayout()
        entradas_h.addWidget(QLabel("a:"))
        self.input_a = QLineEdit()
        self.input_a.setPlaceholderText("Ex.: 10 ou 'olá' ou [1,2]")
        entradas_h.addWidget(self.input_a)

        entradas_h.addWidget(QLabel("b:"))
        self.input_b = QLineEdit()
        self.input_b.setPlaceholderText("Ex.: 3 ou 'mundo' ou 2")
        entradas_h.addWidget(self.input_b)

        vbox.addLayout(entradas_h)

        # Botões: Executar e Mostrar exemplos predefinidos
        botoes_h = QHBoxLayout()

        self.btn_executar = QPushButton("Executar exemplo")
        self.btn_executar.clicked.connect(self.executar_exemplo)
        botoes_h.addWidget(self.btn_executar)

        # Botão para carregar exemplos típicos para cada categoria
        self.btn_exemplo_predef = QPushButton("Carregar exemplo predefinido")
        self.btn_exemplo_predef.clicked.connect(self.carregar_predefinido)
        botoes_h.addWidget(self.btn_exemplo_predef)

        vbox.addLayout(botoes_h)

        # Área de texto para mostrar resultado e explicação
        self.texto_saida = QTextEdit()
        self.texto_saida.setReadOnly(True)
        vbox.addWidget(self.texto_saida)

        # Iniciar com um exemplo predefinido
        self.setLayout(vbox)
        self.carregar_predefinido()

    def carregar_predefinido(self):
        """Carrega valores de exemplo úteis conforme a categoria escolhida."""
        tipo = self.combo_tipo.currentText()

        # Valores predefinidos que fazem sentido para cada tipo de operador
        if tipo == "Aritméticos":
            self.input_a.setText("10")
            self.input_b.setText("3")
        elif tipo == "Atribuição":
            # para atribuição, mostramos alteração de variável
            self.input_a.setText("x = 5")
            self.input_b.setText("x += 2")
        elif tipo == "Comparação":
            self.input_a.setText("10")
            self.input_b.setText("3")
        elif tipo == "Lógicos":
            self.input_a.setText("True")
            self.input_b.setText("False")
        elif tipo == "Bitwise (bit a bit)":
            self.input_a.setText("6")   # 0b110
            self.input_b.setText("3")   # 0b011
        elif tipo == "Pertença (in / not in)":
            self.input_a.setText("'a'")    # elemento
            self.input_b.setText("'banana'")# sequência/container
        elif tipo == "Identidade (is / is not)":
            # mostraremos duas variáveis que podem ser iguais ou não
            self.input_a.setText("a = [1,2]")
            self.input_b.setText("b = [1,2]")
        elif tipo == "Ternário":
            self.input_a.setText("10")
            self.input_b.setText("5")
        else:
            self.input_a.setText("")
            self.input_b.setText("")
        # Limpar saída
        self.texto_saida.clear()
        self.texto_saida.append("Exemplo predefinido carregado. Clica em 'Executar exemplo'.")

    def executar_exemplo(self):
        """Interpreta os inputs conforme a categoria e mostra resultado + explicação."""
        tipo = self.combo_tipo.currentText()
        a_raw = self.input_a.text().strip()
        b_raw = self.input_b.text().strip()

        # Para segurança e simplicidade vamos avaliar de forma limitada:
        # permitimos literais Python simples (números, strings, listas, tuplas, dicts, booleans)
        # e expressões pequenas. Usamos eval com um ambiente restrito.
        permitido = {"True": True, "False": False, "None": None}
        contexto_restrito = {"__builtins__": {}}
        contexto_restrito.update(permitido)

        def safe_eval(expr):
            """Avalia literais Python de forma relativamente segura."""
            if expr == "":
                return None
            # Se o utilizador inseriu algo do tipo 'a = [1,2]' devolvemos a string bruta
            # para tratar operações especiais (atribuição e identidade com nomes).
            if "=" in expr and not expr.strip().startswith("'") and not expr.strip().startswith('"'):
                return expr  # tratamos fora do eval
            try:
                return eval(expr, contexto_restrito)
            except Exception:
                # Se falhar, retornamos a string literal para evitar crash
                return expr

        a = safe_eval(a_raw)
        b = safe_eval(b_raw)

        # Construímos a resposta dependendo do tipo de operador
        resultado_texto = ""

        try:
            if tipo == "Aritméticos":
                # Exemplos: +, -, *, /, //, %, ** (potência)
                # Convertemos para floats/int conforme necessário, mas mantemos tal como o Python faria
                resultado_texto += "Operadores aritméticos:\n"
                resultado_texto += f"a = {a!r}, b = {b!r}\n\n"
                try:
                    resultado_texto += f"a + b = {a + b}\n"
                except Exception as e:
                    resultado_texto += f"a + b -> erro: {e}\n"
                try:
                    resultado_texto += f"a - b = {a - b}\n"
                except Exception as e:
                    resultado_texto += f"a - b -> erro: {e}\n"
                try:
                    resultado_texto += f"a * b = {a * b}\n"
                except Exception as e:
                    resultado_texto += f"a * b -> erro: {e}\n"
                try:
                    resultado_texto += f"a / b = {a / b}\n"
                except Exception as e:
                    resultado_texto += f"a / b -> erro: {e}\n"
                try:
                    resultado_texto += f"a // b (divisão inteira) = {a // b}\n"
                except Exception as e:
                    resultado_texto += f"a // b -> erro: {e}\n"
                try:
                    resultado_texto += f"a % b (resto) = {a % b}\n"
                except Exception as e:
                    resultado_texto += f"a % b -> erro: {e}\n"
                try:
                    resultado_texto += f"a ** b (potência) = {a ** b}\n"
                except Exception as e:
                    resultado_texto += f"a ** b -> erro: {e}\n"

                resultado_texto += ("\nNota: operadores aritméticos aplicam-se a números. "
                                    "O operador + também concatena strings e listas quando apropriado.")

            elif tipo == "Atribuição":
                # Demonstração de operadores de atribuição compostos: =, +=, -=, *=, /=, //=, **=, %=
                resultado_texto += "Operadores de atribuição:\n"
                # Se utilizador forneceu 'x = 5' e 'x += 2', vamos demonstrar
                if isinstance(a, str) and "=" in a:
                    # Interpretar string do tipo "x = 5"
                    # Simples parsing: separar nome e expressão
                    nome, expr = a.split("=", 1)
                    nome = nome.strip()
                    expr = expr.strip()
                    # Avaliar valor
                    valor_inicial = safe_eval(expr)
                    # Agora aplicar segunda expressão (b)
                    if isinstance(b, str) and "+=" in b or "-=" in b or "*=" in b or "/=" in b or "%=" in b or "//=" in b or "**=" in b:
                        # exemplo: "x += 2"
                        op_split = b.split("=", 1)
                        op = op_split[0].strip()  # ex: "x +"
                        # determinar operador composto
                        if "+=" in b:
                            novo = valor_inicial + safe_eval(b.split("+=")[1])
                            resultado_texto += f"Inicial: {nome} = {valor_inicial!r}\n"
                            resultado_texto += f"Após '{b}': {nome} = {novo!r}\n"
                        elif "-=" in b:
                            novo = valor_inicial - safe_eval(b.split("-=")[1])
                            resultado_texto += f"Inicial: {nome} = {valor_inicial!r}\n"
                            resultado_texto += f"Após '{b}': {nome} = {novo!r}\n"
                        elif "*=" in b:
                            novo = valor_inicial * safe_eval(b.split("*=")[1])
                            resultado_texto += f"Inicial: {nome} = {valor_inicial!r}\n"
                            resultado_texto += f"Após '{b}': {nome} = {novo!r}\n"
                        elif "/=" in b:
                            novo = valor_inicial / safe_eval(b.split("/=")[1])
                            resultado_texto += f"Inicial: {nome} = {valor_inicial!r}\n"
                            resultado_texto += f"Após '{b}': {nome} = {novo!r}\n"
                        elif "//=" in b:
                            novo = valor_inicial // safe_eval(b.split("//=")[1])
                            resultado_texto += f"Inicial: {nome} = {valor_inicial!r}\n"
                            resultado_texto += f"Após '{b}': {nome} = {novo!r}\n"
                        elif "**=" in b:
                            novo = valor_inicial ** safe_eval(b.split("**=")[1])
                            resultado_texto += f"Inicial: {nome} = {valor_inicial!r}\n"
                            resultado_texto += f"Após '{b}': {nome} = {novo!r}\n"
                        elif "%=" in b:
                            novo = valor_inicial % safe_eval(b.split("%=")[1])
                            resultado_texto += f"Inicial: {nome} = {valor_inicial!r}\n"
                            resultado_texto += f"Após '{b}': {nome} = {novo!r}\n"
                        else:
                            resultado_texto += "Operador de atribuição composto não reconhecido.\n"
                    else:
                        resultado_texto += "Formato esperado para o segundo campo: operador composto (ex.: 'x += 2').\n"
                else:
                    # Caso geral: mostrar exemplos programáticos
                    x = 5
                    resultado_texto += "Exemplo programático:\n"
                    resultado_texto += f"x = {x}\n"
                    x += 3
                    resultado_texto += f"após x += 3 -> x = {x}\n"
                    x *= 2
                    resultado_texto += f"após x *= 2 -> x = {x}\n"
                    x -= 1
                    resultado_texto += f"após x -= 1 -> x = {x}\n"
                    resultado_texto += "\nNota: os operadores de atribuição combinam operação e atribuição."

            elif tipo == "Comparação":
                # Operadores: ==, !=, >, <, >=, <=
                resultado_texto += "Operadores de comparação:\n"
                resultado_texto += f"a = {a!r}, b = {b!r}\n\n"
                resultado_texto += f"a == b -> {a == b}\n"
                resultado_texto += f"a != b -> {a != b}\n"
                try:
                    resultado_texto += f"a > b -> {a > b}\n"
                except Exception:
                    resultado_texto += "a > b -> não aplicável (tipos incompatíveis)\n"
                try:
                    resultado_texto += f"a < b -> {a < b}\n"
                except Exception:
                    resultado_texto += "a < b -> não aplicável (tipos incompatíveis)\n"
                try:
                    resultado_texto += f"a >= b -> {a >= b}\n"
                except Exception:
                    resultado_texto += "a >= b -> não aplicável (tipos incompatíveis)\n"
                try:
                    resultado_texto += f"a <= b -> {a <= b}\n"
                except Exception:
                    resultado_texto += "a <= b -> não aplicável (tipos incompatíveis)\n"

            elif tipo == "Lógicos":
                # Operadores: and, or, not
                resultado_texto += "Operadores lógicos:\n"
                resultado_texto += f"a = {a!r}, b = {b!r}\n\n"
                # Mostramos exemplos típicos com avaliação booleana
                resultado_texto += f"a and b -> {a and b}\n"
                resultado_texto += f"a or b  -> {a or b}\n"
                resultado_texto += f"not a   -> {not a}\n"
                resultado_texto += ("\nNota: em Python, 'and' e 'or' devolvem o último valor avaliado, "
                                    "não apenas True/False — isto é útil com valores não booleanos.")

            elif tipo == "Bitwise (bit a bit)":
                # Operadores: &, |, ^, ~, <<, >>
                resultado_texto += "Operadores bit a bit (bitwise):\n"
                resultado_texto += f"a = {a!r}, b = {b!r}\n\n"
                try:
                    resultado_texto += f"a & b -> {a & b}\n"
                except Exception as e:
                    resultado_texto += f"a & b -> erro: {e}\n"
                try:
                    resultado_texto += f"a | b -> {a | b}\n"
                except Exception as e:
                    resultado_texto += f"a | b -> erro: {e}\n"
                try:
                    resultado_texto += f"a ^ b -> {a ^ b}\n"
                except Exception as e:
                    resultado_texto += f"a ^ b -> erro: {e}\n"
                try:
                    resultado_texto += f"~a -> {~a}\n"
                except Exception as e:
                    resultado_texto += f"~a -> erro: {e}\n"
                try:
                    resultado_texto += f"a << b -> {a << b}\n"
                except Exception as e:
                    resultado_texto += f"a << b -> erro: {e}\n"
                try:
                    resultado_texto += f"a >> b -> {a >> b}\n"
                except Exception as e:
                    resultado_texto += f"a >> b -> erro: {e}\n"

                resultado_texto += ("\nNota: aplicam-se tipicamente a inteiros. "
                                    "Ex.: 6 (0b110) & 3 (0b011) = 2 (0b010).")

            elif tipo == "Pertença (in / not in)":
                # Verificar se um elemento (a) está em um container (b)
                resultado_texto += "Operadores de pertença:\n"
                resultado_texto += f"a = {a!r}, container b = {b!r}\n\n"
                try:
                    resultado_texto += f"a in b -> {a in b}\n"
                    resultado_texto += f"a not in b -> {a not in b}\n"
                except Exception as e:
                    resultado_texto += f"Operação de pertença -> erro: {e}\n"
                resultado_texto += ("\nNota: 'in' verifica se um elemento pertence a sequências, listas, tuplas, dicionários (chaves), etc.")

            elif tipo == "Identidade (is / is not)":
                # is compara identidade de objetos (mesmo objecto em memória)
                resultado_texto += "Operadores de identidade:\n"
                # Se o utilizador inseriu 'a = [1,2]' e 'b = [1,2]', tratamos isso
                if isinstance(a, str) and "=" in a and isinstance(b, str) and "=" in b:
                    # criar variáveis distintas com mesmo conteúdo
                    # parse simples: ignoramos nomes e apenas criamos duas listas iguais
                    # Avaliar o conteúdo entre '='
                    _, expr_a = a.split("=", 1)
                    _, expr_b = b.split("=", 1)
                    val_a = safe_eval(expr_a)
                    val_b = safe_eval(expr_b)
                    resultado_texto += f"valor A = {val_a!r} (objeto A em memória: {id(val_a)})\n"
                    resultado_texto += f"valor B = {val_b!r} (objeto B em memória: {id(val_b)})\n\n"
                    resultado_texto += f"A is B -> {val_a is val_b}\n"
                    resultado_texto += f"A is not B -> {val_a is not val_b}\n"
                    resultado_texto += ("\nNota: duas listas com o mesmo conteúdo normalmente NÃO são o mesmo objecto em memória; "
                                        "usar 'is' só quando queres comparar identidade, não igualdade de conteúdo.")
                else:
                    resultado_texto += f"a = {a!r} (id={id(a)}), b = {b!r} (id={id(b)})\n\n"
                    resultado_texto += f"a is b -> {a is b}\n"
                    resultado_texto += f"a is not b -> {a is not b}\n"
                    resultado_texto += ("\nNota: '==' compara igualdade de valor; 'is' compara se são exactamente o mesmo objecto.")

            elif tipo == "Ternário":
                # Expressão condicional: x if cond else y
                resultado_texto += "Operador ternário (expressão condicional):\n"
                resultado_texto += f"a = {a!r}, b = {b!r}\n\n"
                # Exemplo prático: escolher o maior
                try:
                    maior = a if a > b else b
                    resultado_texto += f"Exemplo: maior = a if a > b else b  -> {maior}\n"
                    resultado_texto += "Isto equivale a:\nif a > b:\n    maior = a\nelse:\n    maior = b\n"
                except Exception:
                    resultado_texto += ("Não foi possível calcular a > b (tipos incompatíveis). "
                                        "Ainda assim a sintaxe é: <valor1> if <condição> else <valor2>.\n")
            else:
                resultado_texto += "Categoria não reconhecida.\n"

        except Exception as e:
            resultado_texto += f"\nErro inesperado durante a execução: {e}\n"

        # Apresentar o resultado na área de texto
        self.texto_saida.clear()
        self.texto_saida.append(resultado_texto)
        # Acrescentar dicas de aprendizagem
        self.texto_saida.append("\nDica: modifica os valores de 'a' e 'b' e experimenta combinações diferentes.")
        self.texto_saida.append("Ex.: para strings usa 'hello' (com aspas simples ou duplas). Para listas usa [1,2,3].")

def main():
    app = QApplication(sys.argv)
    janela = JanelaOperadores()
    janela.resize(700, 450)
    janela.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

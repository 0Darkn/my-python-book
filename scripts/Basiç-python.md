# ==========================================
# Script Python Básico
# Autor: Tu 🙂
# Descrição: Exemplo simples com variáveis,
# entrada do utilizador, condições e ciclos
# ==========================================

# --- 1. Mostrar mensagem no ecrã ---
print("Olá! Bem-vindo ao script Python básico.")

# --- 2. Pedir dados ao utilizador ---
nome = input("Qual é o teu nome? ")
idade = input("Qual é a tua idade? ")

# Converter idade (string) para número inteiro
idade = int(idade)

# --- 3. Trabalhar com variáveis ---
ano_atual = 2026
ano_nascimento = ano_atual - idade

# Mostrar resultado
print("Olá", nome)
print("Nasceste aproximadamente em", ano_nascimento)

# --- 4. Estrutura condicional (if/else) ---
if idade >= 18:
    print("És maior de idade.")
else:
    print("És menor de idade.")

# --- 5. Ciclo (loop) ---
print("Vamos contar até 5:")

for i in range(1, 6):
    print("Número:", i)

# --- 6. Função simples ---
def saudacao(nome):
    """
    Esta função recebe um nome e devolve
    uma mensagem personalizada.
    """
    return "Olá, " + nome + "! Bem-vindo ao Python."

# Chamar a função
mensagem = saudacao(nome)
print(mensagem)

# --- 7. Lista e iteração ---
frutas = ["maçã", "banana", "laranja"]

print("Lista de frutas:")
for fruta in frutas:
    print("-", fruta)

# --- 8. Fim do programa ---
print("Programa terminado.")

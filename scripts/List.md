**gerenciador de lista de tarefas (To-Do List)** que roda direto no terminal.
Ele usa loops, funções e manipulação de listas, o que é ótimo para praticar.
### Código do Script (lista_tarefas.py)
```python
def exibir_menu():
    print("\n" + "="*20)
    print("  LISTA DE TAREFAS")
    print("="*20)
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")
    print("="*20)

def Executar():
    tarefas = []
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            if not tarefas:
                print("\n[!] Sua lista está vazia.")
            else:
                print("\n--- Suas Tarefas ---")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
                    
        elif opcao == "2":
            nova_tarefa = input("\nDigite a nova tarefa: ")
            if nova_tarefa.strip():
                tarefas.append(nova_tarefa)
                print(f"[+] '{nova_tarefa}' adicionada com sucesso!")
            else:
                print("[!] A tarefa não pode ser vazia.")
                
        elif opcao == "3":
            if not tarefas:
                print("\n[!] Não há tarefas para remover.")
            else:
                print("\n--- Remover Tarefa ---")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
                
                try:
                    indice = int(input("\nDigite o número da tarefa que deseja remover: ")) - 1
                    if 0 <= indice < len(tarefas):
                        removida = tarefas.pop(indice)
                        print(f"[-] '{removida}' foi removida.")
                    else:
                        print("[!] Número inválido.")
                except ValueError:
                    print("[!] Por favor, digite um número válido.")
                    
        elif opcao == "4":
            print("\nSaindo... Até logo!")
            break
        else:
            print("[!] Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    Executar()

```
### Como testar no seu computador:
 1. **Copie o código** acima.
 2. Abra um editor de texto (como o Bloco de Notas, VS Code ou IDLE do Python) e cole o código.
 3. Salve o arquivo com o nome **lista_tarefas.py**.
 4. Abra o terminal ou prompt de comando na pasta onde salvou o arquivo e digite:
   ```bash
   python lista_tarefas.py
   
   ```

import sys
import os

# Importando as classes para o modo interativo
from Exercicio1 import TreeMap
from Exercicio2 import AVLTreeMap
from Exercicio3 import RedBlackTreeMap

# Importando os scripts de resolução dos exercícios específicos
import Exercicio4
import Exercicio5
import Exercicio6
import Exercicio7

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_cabecalho():
    print("="*50)
    print("      TRABALHO 3 - ESTRUTURA DE DADOS")
    print("      Árvores de Busca, AVL e Rubro-Negras")
    print("="*50)

def menu_principal():
    while True:
        imprimir_cabecalho()
        print("\nEscolha uma opção para executar:")
        print("1. Executar Exercício 4 (Inserção em BST)")
        print("2. Executar Exercício 5 (Inserção em AVL - Caso da Fig 11.14b)")
        print("3. Executar Exercício 6 (Remoção em AVL - Caso da Fig 11.14b)")
        print("4. Executar Exercício 7 (Inserção em Rubro-Negra)")
        print("-" * 30)
        print("5. Modo Playground (Criar e testar suas próprias árvores)")
        print("-" * 30)
        print("0. Sair")
        
        opcao = input("\nOpção: ")

        if opcao == '1':
            limpar_tela()
            Exercicio4.run_exercise_4()
            input("\nPressione Enter para voltar...")
            limpar_tela()
        elif opcao == '2':
            limpar_tela()
            Exercicio5.run_exercise_5()
            input("\nPressione Enter para voltar...")
            limpar_tela()
        elif opcao == '3':
            limpar_tela()
            Exercicio6.run_exercise_6()
            input("\nPressione Enter para voltar...")
            limpar_tela()
        elif opcao == '4':
            limpar_tela()
            Exercicio7.run_exercise_7()
            input("\nPressione Enter para voltar...")
            limpar_tela()
        elif opcao == '5':
            limpar_tela()
            modo_playground()
        elif opcao == '0':
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida!")
            input("Pressione Enter para tentar novamente...")
            limpar_tela()

def modo_playground():
    print("\n--- MODO PLAYGROUND ---")
    print("Teste as implementações dos Exercícios 1, 2 e 3.")
    print("Qual tipo de árvore deseja criar?")
    print("1. TreeMap (Árvore Binária de Busca Padrão)")
    print("2. AVLTreeMap (Árvore AVL)")
    print("3. RedBlackTreeMap (Árvore Rubro-Negra)")
    
    tipo = input("Escolha: ")
    tree = None
    nome_arvore = ""

    if tipo == '1':
        tree = TreeMap()
        nome_arvore = "BST Padrão"
    elif tipo == '2':
        tree = AVLTreeMap()
        nome_arvore = "AVL"
    elif tipo == '3':
        tree = RedBlackTreeMap()
        nome_arvore = "Rubro-Negra"
    else:
        print("Tipo inválido. Voltando ao menu.")
        return

    print(f"\nÁrvore {nome_arvore} criada com sucesso!")
    
    while True:
        print(f"\n--- Operações em {nome_arvore} ---")
        print("1. Inserir chave")
        print("2. Remover chave")
        print("3. Buscar chave")
        print("4. Visualizar Árvore")
        print("0. Voltar ao Menu Principal")
        
        op = input("Opção: ")
        
        try:
            if op == '1':
                val = int(input("Digite um número inteiro para inserir: "))
                tree[val] = f"Valor-{val}" # Valor genérico
                print(f"Chave {val} inserida.")
            
            elif op == '2':
                val = int(input("Digite a chave para remover: "))
                del tree[val]
                print(f"Chave {val} removida.")
            
            elif op == '3':
                val = int(input("Digite a chave para buscar: "))
                res = tree.get(val) # Usa o get do MapBase/Python dict
                if res:
                    print(f"Encontrado! Valor associado: {res}")
                else:
                    print("Chave não encontrada.")
            
            elif op == '4':
                print("\nEstrutura Atual:")
                if tree.is_empty():
                    print("(Árvore Vazia)")
                else:
                    # Se for Rubro-Negra, usamos uma visualização especial para ver as cores
                    if isinstance(tree, RedBlackTreeMap):
                        visualizar_rb(tree, tree.root())
                    else:
                        tree.print_tree()
            
            elif op == '0':
                limpar_tela()
                break
            
            else:
                print("Opção inválida.")
        
        except KeyError:
            print("Erro: Chave não encontrada para remoção.")
        except ValueError:
            print("Erro: Digite um número válido.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def visualizar_rb(tree, p, depth=0):
    """Auxiliar para imprimir árvore Rubro-Negra com as cores"""
    if p is None: return
    
    color = "RED" if tree._is_red(p) else "BLACK"
    print("  " * depth + f"{p.key()} [{color}]")
    
    if tree.left(p):
        visualizar_rb(tree, tree.left(p), depth + 1)
    elif tree.right(p): # Se tem filho direito mas não esquerdo, imprime placeholder para visualização
        print("  " * (depth + 1) + "(None)")

    if tree.right(p):
        visualizar_rb(tree, tree.right(p), depth + 1)
    elif tree.left(p):
        print("  " * (depth + 1) + "(None)")

if __name__ == "__main__":
    menu_principal()
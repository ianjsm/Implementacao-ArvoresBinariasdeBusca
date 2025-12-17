import sys
import os
from Exercicio1 import MapaArvore
from Exercicio2 import MapaArvoreAVL
from Exercicio3 import MapaArvoreRubroNegra
import Exercicio4
import Exercicio5
import Exercicio6
import Exercicio7

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        print("Escolha uma opção para executar:")
        print("1. Exercício 4")
        print("2.Exercício 5")
        print("3.Exercício 6")
        print("4.Exercício 7")
        print("0. Sair")
        
        opcao = input("sua opcao: ")

        if opcao == '1':
            limpar_tela()
            Exercicio4.executar_exercicio_4()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
        elif opcao == '2':
            limpar_tela()
            Exercicio5.executar_exercicio_5()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
        elif opcao == '3':
            limpar_tela()
            Exercicio6.executar_exercicio_6()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
        elif opcao == '4':
            limpar_tela()
            Exercicio7.executar_exercicio_7()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
        elif opcao == '5':
            limpar_tela()
            modo_playground()
        elif opcao == '0':
            print("Encerrando o programa...")
            sys.exit()
        else:
            print("Opção inválida!")
            input("Pressione Enter para tentar novamente...")
            limpar_tela()

def modo_playground():
    print("Escolha o tipo de estrutura para testar:")
    print("1. Mapa com Árvore Binária Simples")
    print("2. Mapa com Árvore AVL")
    print("3. Mapa com Árvore Rubro-Negra")
    
    tipo = input("Escolha: ")
    arvore = None
    nome_arvore = ""

    if tipo == '1':
        arvore = MapaArvore()
        nome_arvore = "Busca Binária Simples"
    elif tipo == '2':
        arvore = MapaArvoreAVL()
        nome_arvore = "AVL"
    elif tipo == '3':
        arvore = MapaArvoreRubroNegra()
        nome_arvore = "Rubro-Negra"
    else:
        print("Tipo inválido. Retornando ao menu.")
        return

    print(f"\nSucesso: {nome_arvore} pronta para uso!")
    
    while True:
        print(f"\n--- Operações em {nome_arvore} ---")
        print("1. Inserir chave")
        print("2. Remover chave")
        print("3. Buscar chave")
        print("4. Visualizar Estrutura")
        print("0. Sair do Playground")
        
        op = input("Opção: ")
        
        try:
            if op == '1':
                chave = int(input("Digite um número (chave): "))
                arvore[chave] = f"Dado-{chave}"
                print(f"Chave {chave} inserida com sucesso.")
            
            elif op == '2':
                chave = int(input("Digite a chave para remover: "))
                del arvore[chave]
                print(f"Chave {chave} removida.")
            
            elif op == '3':
                chave = int(input("Digite a chave para buscar: "))
                resultado = arvore.get(chave)
                if resultado:
                    print(f"Sucesso! Valor encontrado: {resultado}")
                else:
                    print("Aviso: Chave não encontrada.")
            
            elif op == '4':
                print("\nVisualização da Estrutura Atual:")
                if arvore.esta_vazia():
                    print("(A árvore está vazia)")
                else:
                    if isinstance(arvore, MapaArvoreRubroNegra):
                        visualizar_cores_rn(arvore, arvore.raiz())
                    else:
                        arvore.imprimir_arvore()
            
            elif op == '0':
                limpar_tela()
                break
            
            else:
                print("Opção inválida.")
        
        except KeyError:
            print("Erro: Esta chave não existe na árvore.")
        except ValueError:
            print("Erro: Por favor, insira apenas números inteiros.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def visualizar_cores_rn(arvore, pos, nivel=0):
    if pos is None: return
    
    cor = "VERMELHO" if arvore._eh_vermelho(pos) else "PRETO"
    print("  " * nivel + f"{pos.chave()} [{cor}]")
    
    if arvore.esquerdo(pos):
        visualizar_cores_rn(arvore, arvore.esquerdo(pos), nivel + 1)
    elif arvore.direito(pos):
        print("  " * (nivel + 1) + "(Vazio)")

    if arvore.direito(pos):
        visualizar_cores_rn(arvore, arvore.direito(pos), nivel + 1)
    elif arvore.esquerdo(pos):
        print("  " * (nivel + 1) + "(Vazio)")

if __name__ == "__main__":
    menu_principal()
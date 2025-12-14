# Exercicio5.py
from Exercicio2 import AVLTreeMap

def run_exercise_5():
    print("--- Exercício 5 ---")
    print("Construindo a árvore AVL da Figura 11.14b...")
    
    tree = AVLTreeMap()
    # Ordem de inserção para recriar a estrutura da Figura 11.14b (antes da inserção do 52)
    # Estrutura baseada nas chaves visíveis: 44 (root), 17, 62, 50, 78, 48, 54, 88
    initial_keys = [44, 17, 62, 50, 78, 48, 54, 88]
    
    for k in initial_keys:
        tree[k] = None
    
    print("Árvore Inicial (Fig 11.14b):")
    tree.print_tree()
    
    print("\nInserindo chave 52...")
    tree[52] = None
    
    print("Árvore Resultante (AVL):")
    tree.print_tree()

if __name__ == "__main__":
    run_exercise_5()
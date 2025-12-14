# Exercicio6.py
from Exercicio2 import AVLTreeMap

def run_exercise_6():
    print("--- Exercício 6 ---")
    print("Construindo a árvore AVL da Figura 11.14b...")
    
    tree = AVLTreeMap()
    # Mesma árvore inicial do Ex 5
    initial_keys = [44, 17, 62, 50, 78, 48, 54, 88]
    
    for k in initial_keys:
        tree[k] = None
        
    print("Árvore Inicial (Fig 11.14b):")
    tree.print_tree()
    
    print("\nRemovendo chave 62...")
    del tree[62]
    
    print("Árvore Resultante após remoção (AVL):")
    tree.print_tree()

if __name__ == "__main__":
    run_exercise_6()
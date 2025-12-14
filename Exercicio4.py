# Exercicio4.py
from Exercicio1 import TreeMap

def run_exercise_4():
    print("--- Exercício 4 ---")
    keys = [30, 40, 24, 58, 48, 26, 11, 13]
    tree = TreeMap()
    
    for k in keys:
        print(f"\nInserindo {k}:")
        tree[k] = None # Valor arbitrário
        tree.print_tree()

if __name__ == "__main__":
    run_exercise_4()
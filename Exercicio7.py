# Exercicio7.py
from Exercicio3 import RedBlackTreeMap

def run_exercise_7():
    print("--- Exercício 7 ---")
    keys = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    tree = RedBlackTreeMap()
    
    print(f"Inserindo sequência: {keys}")
    for k in keys:
        tree[k] = None
        
    print("\nÁrvore Rubro-Negra Resultante:")
    # Nota: A visualização simples print_tree mostra a estrutura,
    # mas não mostra as cores (Vermelho/Preto).
    # Para verificar as cores, acessamos o nó interno.
    
    def print_rb_tree(p, depth=0):
        color = "RED" if tree._is_red(p) else "BLACK"
        print("  " * depth + f"{p.key()} ({color})")
        if tree.left(p):
            print_rb_tree(tree.left(p), depth + 1)
        if tree.right(p):
            print_rb_tree(tree.right(p), depth + 1)

    if not tree.is_empty():
        print_rb_tree(tree.root())
    else:
        print("Árvore vazia.")

if __name__ == "__main__":
    run_exercise_7()
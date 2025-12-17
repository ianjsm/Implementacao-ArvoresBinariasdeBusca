from Exercicio2 import MapaArvoreAVL

def executar_exercicio_5():
    print("--- Exercício 5 ---")
    print("Construindo a árvore AVL da Figura 11.14b...")
    
    arvore = MapaArvoreAVL()
    # Chaves para recriar a estrutura da Figura 11.14b
    chaves_iniciais = [44, 17, 62, 50, 78, 48, 54, 88]
    
    for k in chaves_iniciais:
        arvore[k] = None
    
    print("Árvore Inicial (Fig 11.14b):")
    arvore.imprimir_arvore()
    
    print("\nInserindo chave 52...")
    arvore[52] = None
    
    print("Árvore Resultante (AVL com rebalanceamento):")
    arvore.imprimir_arvore()

if __name__ == "__main__":
    executar_exercicio_5()
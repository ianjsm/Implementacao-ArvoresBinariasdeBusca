from Exercicio2 import MapaArvoreAVL

def executar_exercicio_5():
    print("construindo a arvore AVL")
    
    arvore = MapaArvoreAVL()
    chaves_iniciais = [44, 17, 62, 50, 78, 48, 54, 88]
    
    for k in chaves_iniciais:
        arvore[k] = None
    
    print("arvore inicial:")
    arvore.imprimir_arvore()
    
    print("\ninserindo chave 52...")
    arvore[52] = None
    
    print("arvore resultante:")
    arvore.imprimir_arvore()

if __name__ == "__main__":
    executar_exercicio_5()
from Exercicio1 import MapaArvore

def executar_exercicio_4():
    print("--- Exercício 4 ---")
    chaves = [30, 40, 24, 58, 48, 26, 11, 13]
    arvore = MapaArvore()
    
    for k in chaves:
        print(f"\nInserindo {k}:")
        arvore[k] = None 
        arvore.imprimir_arvore()

if __name__ == "__main__":
    executar_exercicio_4()
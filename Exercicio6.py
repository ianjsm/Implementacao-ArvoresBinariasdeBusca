from Exercicio2 import MapaArvoreAVL

def executar_exercicio_6():    
    arvore = MapaArvoreAVL()
    chaves_iniciais = [44, 17, 62, 50, 78, 48, 54, 88]
    
    for k in chaves_iniciais:
        arvore[k] = None
        
    print("arvore inicial:")
    arvore.imprimir_arvore()
    
    print("removendo chave 62...")
    del arvore[62]
    
    print("arvore resultante:")
    arvore.imprimir_arvore()

if __name__ == "__main__":
    executar_exercicio_6()
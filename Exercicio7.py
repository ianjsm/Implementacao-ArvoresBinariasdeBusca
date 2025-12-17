from Exercicio3 import MapaArvoreRubroNegra

def executar_exercicio_7():
    chaves = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    arvore = MapaArvoreRubroNegra()
    
    print(f"inserindo sequencia: {chaves}")
    for k in chaves:
        arvore[k] = None
        
    print("arvore rubro negra:")
    
    def imprimir_arvore_rubro_negra(pos, nivel=0):
        cor = "VERMELHO" if arvore._eh_vermelho(pos) else "PRETO"
        print("  " * nivel + f"{pos.chave()} ({cor})")
        
        if arvore.esquerdo(pos):
            imprimir_arvore_rubro_negra(arvore.esquerdo(pos), nivel + 1)
        if arvore.direito(pos):
            imprimir_arvore_rubro_negra(arvore.direito(pos), nivel + 1)

    if not arvore.esta_vazia():
        imprimir_arvore_rubro_negra(arvore.raiz())
    else:
        print("arvore vazia")

if __name__ == "__main__":
    executar_exercicio_7()
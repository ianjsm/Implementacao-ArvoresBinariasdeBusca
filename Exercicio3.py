from Exercicio1 import MapaArvore

class MapaArvoreRubroNegra(MapaArvore):
    
    class _No(MapaArvore._No):
        __slots__ = '_eh_vermelho'
        
        def __init__(self, elemento, pai=None, esquerdo=None, direito=None):
            super().__init__(elemento, pai, esquerdo, direito)
            self._eh_vermelho = True

    def _definir_vermelho(self, pos): pos._no._eh_vermelho = True
    def _definir_preto(self, pos): pos._no._eh_vermelho = False
    def _definir_cor(self, pos, tornar_vermelho): pos._no._eh_vermelho = tornar_vermelho
    
    def _eh_vermelho(self, pos): return pos is not None and pos._no._eh_vermelho
    def _eh_folha_vermelha(self, pos): return self._eh_vermelho(pos) and self.eh_folha(pos)

    def _obter_filho_vermelho(self, pos):
        for filho in (self.esquerdo(pos), self.direito(pos)):
            if self._eh_vermelho(filho):
                return filho
        return None

    def irmao(self, pos):
        pai_pos = self.pai(pos)
        if pai_pos is None:
            return None
        if pos == self.esquerdo(pai_pos):
            return self.direito(pai_pos)
        else:
            return self.esquerdo(pai_pos)

    def filhos(self, pos):
        if self.esquerdo(pos): yield self.esquerdo(pos)
        if self.direito(pos): yield self.direito(pos)

    def _rebalancear_insercao(self, pos):
        self._resolver_vermelho(pos)

    def _resolver_vermelho(self, pos):
        if self.is_root(pos):
            self._definir_preto(pos)
        else:
            pai_pos = self.pai(pos)
            if self._eh_vermelho(pai_pos):
                tio = self.irmao(pai_pos)
                if not self._eh_vermelho(tio):
                    meio = self._reestruturar(pos)
                    self._definir_preto(meio)
                    self._definir_vermelho(self.esquerdo(meio))
                    self._definir_vermelho(self.direito(meio))
                else:
                    avo = self.pai(pai_pos)
                    self._definir_vermelho(avo)
                    self._definir_preto(self.esquerdo(avo))
                    self._definir_preto(self.direito(avo))
                    self._resolver_vermelho(avo)

    def _rebalancear_delecao(self, pos):
        if len(self) == 1:
            self._definir_preto(self.raiz())
        elif pos is not None:
            n = self.num_children(pos)
            if n == 1:
                filho = next(self.filhos(pos))
                if not self._eh_folha_vermelha(filho):
                    self._corrigir_deficit(pos, filho)
            elif n == 2:
                if self._eh_folha_vermelha(self.esquerdo(pos)):
                    self._definir_preto(self.esquerdo(pos))
                else:
                    self._definir_preto(self.direito(pos))

    def _corrigir_deficit(self, z, y):
        if not self._eh_vermelho(y):
            x = self._obter_filho_vermelho(y)
            if x is not None:
                cor_antiga_z = self._eh_vermelho(z)
                meio = self._reestruturar(x)
                self._definir_cor(meio, cor_antiga_z)
                self._definir_preto(self.esquerdo(meio))
                self._definir_preto(self.direito(meio))
            else:
                self._definir_vermelho(y)
                if self._eh_vermelho(z):
                    self._definir_preto(z)
                elif not self.is_root(z):
                    self._corrigir_deficit(self.pai(z), self.irmao(z))
        else:
            self._rotacionar(y)
            self._definir_preto(y)
            self._definir_vermelho(z)
            if z == self.direito(y):
                self._corrigir_deficit(z, self.esquerdo(z))
            else:
                self._corrigir_deficit(z, self.direito(z))
from Dados import Dado

class RotinaXilol:
    def __init__(self, dado):
        self._nome_banho = []
        self._temperatura_banho = []
        self._tempo_banho = []
        self._ganho_proporcional = []
        self._dado = dado

    def iniciar(self, formol_eh_ativado=True):
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_1A2:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('XILOL1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

            self.set_nome_banho('XILOL2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_3A4:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('XILOL1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

            self.set_nome_banho('XILOL2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)
        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL1')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)

                self.set_nome_banho('FORMOL2')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('XILOL1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

            self.set_nome_banho('XILOL2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)


    def set_nome_banho(self, nome):
        self._nome_banho.append(nome)

    def set_temperatura_banho(self, temperatura):
        self._temperatura_banho.append(temperatura)
        
    def set_tempo_banho(self, tempo):
        self._tempo_banho.append(tempo)

    def set_ganho_proporcional(self, ganho):
        self._ganho_proporcional.append(ganho)

    @property
    def nome_banho(self):
        return self._nome_banho

    @property
    def temperatura_banho(self):
        return self._temperatura_banho

    @property
    def tempo_banho(self):
        return self._tempo_banho

    @property
    def ganho_proporcional(self):
        return self._ganho_proporcional

#Classe para testar valores diferentes
""" class RotinaXilol:
    def __init__(self, dado):
        self._nome_banho = []
        self._temperatura_banho = []
        self._tempo_banho = []
        self._ganho_proporcional = []
        self._dado = dado

    def iniciar(self, formol_eh_ativado=True):
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_1A2:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(30)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('XILOL1')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

            self.set_nome_banho('XILOL2')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_3A4:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(30)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('XILOL1')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

            self.set_nome_banho('XILOL2')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)
        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL1')
                self.set_temperatura_banho(30)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)

                self.set_nome_banho('FORMOL2')
                self.set_temperatura_banho(30)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('XILOL1')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)

            self.set_nome_banho('XILOL2')
            self.set_temperatura_banho(30)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_XILOL)


    def set_nome_banho(self, nome):
        self._nome_banho.append(nome)

    def set_temperatura_banho(self, temperatura):
        self._temperatura_banho.append(temperatura)
        
    def set_tempo_banho(self, tempo):
        self._tempo_banho.append(tempo)

    def set_ganho_proporcional(self, ganho):
        self._ganho_proporcional.append(ganho)

    @property
    def nome_banho(self):
        return self._nome_banho

    @property
    def temperatura_banho(self):
        return self._temperatura_banho

    @property
    def tempo_banho(self):
        return self._tempo_banho

    @property
    def ganho_proporcional(self):
        return self._ganho_proporcional """

class RotinaIsopropanol:
    def __init__(self, dado):
        self._nome_banho = []
        self._temperatura_banho = []
        self._tempo_banho = []
        self._ganho_proporcional = []
        self._dado = dado

    def iniciar(self, formol_eh_ativado=True):
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_1A2:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ISOPROPANOL1')
            self.set_temperatura_banho(58)
            self.set_tempo_banho(10)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ISOPROPANOL)

            self.set_nome_banho('ISOPROPANOL2')
            self.set_temperatura_banho(58)
            self.set_tempo_banho(10)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ISOPROPANOL)

        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_3A4:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ISOSPROPANOL1')
            self.set_temperatura_banho(58)
            self.set_tempo_banho(10)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ISOPROPANOL)

            self.set_nome_banho('ISOSPROPANOL2')
            self.set_temperatura_banho(58)
            self.set_tempo_banho(10)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ISOPROPANOL)
        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL1')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)

                self.set_nome_banho('FORMOL2')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ISOPROPANOL1')
            self.set_temperatura_banho(58)
            self.set_tempo_banho(8)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ISOPROPANOL)

            self.set_nome_banho('ISOPROPANOL2')
            self.set_temperatura_banho(58)
            self.set_tempo_banho(8)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ISOPROPANOL)

            self.set_nome_banho('ISOPROPANOL3')
            self.set_temperatura_banho(58)
            self.set_tempo_banho(8)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ISOPROPANOL)


    def set_nome_banho(self, nome):
        self._nome_banho.append(nome)

    def set_temperatura_banho(self, temperatura):
        self._temperatura_banho.append(temperatura)
        
    def set_tempo_banho(self, tempo):
        self._tempo_banho.append(tempo)

    def set_ganho_proporcional(self, ganho):
        self._ganho_proporcional.append(ganho)

    @property
    def nome_banho(self):
        return self._nome_banho

    @property
    def temperatura_banho(self):
        return self._temperatura_banho

    @property
    def tempo_banho(self):
        return self._tempo_banho

    @property
    def ganho_proporcional(self):
        return self._ganho_proporcional

class RotinaWitclear:
    def __init__(self, dado):
        self._nome_banho = []
        self._temperatura_banho = []
        self._tempo_banho = []
        self._ganho_proporcional = []
        self._dado = dado

    def iniciar(self, formol_eh_ativado=True):
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_1A2:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(50)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('WITCLEAR1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_WITCLEAR)

            self.set_nome_banho('WITCLEAR2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(5)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_WITCLEAR)

        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_3A4:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('WITCLEAR1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_WITCLEAR)

            self.set_nome_banho('WITCLEAR2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_WITCLEAR)
        elif self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
            if formol_eh_ativado ==True:
                self.set_nome_banho('FORMOL1')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)

                self.set_nome_banho('FORMOL2')
                self.set_temperatura_banho(60)
                self.set_tempo_banho(30)
                self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_FORMOL)
            self.set_nome_banho('ALCOOL1')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL2')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL3')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL4')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('ALCOOL5')
            self.set_temperatura_banho(60)
            self.set_tempo_banho(7)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_ALCOOL)

            self.set_nome_banho('WITCLEAR1')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_WITCLEAR)

            self.set_nome_banho('WITCLEAR2')
            self.set_temperatura_banho(55)
            self.set_tempo_banho(6)
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_WITCLEAR)

class RotinaPersonalizada:
    def __init__(self, dado):
        self._nome_banho = []
        self._temperatura_banho = []
        self._tempo_banho = []
        self._ganho_proporcional = []
        self._dado = dado

    def iniciar(self, formol_eh_ativado=True):
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_NENHUM:
            
            self.set_nome_banho('ROTINA PERSONALIZADA')
            self.set_temperatura_banho(int(self._dado.texto_valor_temperatura))
            self.set_tempo_banho(int(self._dado.texto_valor_tempo))
            self.set_ganho_proporcional(self._dado.GANHO_PROPORCIONAL_PESONALIZADO)


    def set_nome_banho(self, nome):
        self._nome_banho.append(nome)

    def set_temperatura_banho(self, temperatura):
        self._temperatura_banho.append(temperatura)
        
    def set_tempo_banho(self, tempo):
        self._tempo_banho.append(tempo)

    def set_ganho_proporcional(self, ganho):
        self._ganho_proporcional.append(ganho)

    @property
    def nome_banho(self):
        return self._nome_banho

    @property
    def temperatura_banho(self):
        return self._temperatura_banho

    @property
    def tempo_banho(self):
        return self._tempo_banho

    @property
    def ganho_proporcional(self):
        return self._ganho_proporcional

class RotinaExecutada:
    def __init__(self, dado):
        self._dado = dado
        self._banho = None

        if self._dado.reagente == self._dado.REAGENTE_XILOL:
            self._banho = RotinaXilol(self._dado)
            self._banho.iniciar( formol_eh_ativado = self._dado.formol_esta_ativado )
            self._dado._ativa_execucao = True
        elif self._dado.reagente == self._dado.REAGENTE_ISOPROPANOL:
            self._banho = RotinaIsopropanol(self._dado)
            self._banho.iniciar( formol_eh_ativado = self._dado.formol_esta_ativado )
            self._dado._ativa_execucao = True
        elif self._dado.reagente == self._dado.REAGENTE_WITCLEAR:
            self._banho = RotinaXilol(self._dado)
            self._banho.iniciar( formol_eh_ativado = self._dado.formol_esta_ativado )
            self._dado._ativa_execucao = True
        elif self._dado.reagente == self._dado.REAGENTE_NENHUM:
            self._banho = RotinaPersonalizada(self._dado)
            self._banho.iniciar()
            self._dado._ativa_execucao = True

    @property
    def banho(self):
        return self._banho


if __name__ == "__main__":
    dado = Dado()
    dado.set_tamanho_da_amostra(dado.TAMANHO_1A2)

    banho = RotinaIsopropanol(dado)
    banho.iniciar(formol_eh_ativado=dado.formol_esta_ativado)

    print(banho.nome_banho[0])
    print(banho.temperatura_banho[0])
    print(banho.tempo_banho[0])
    print(banho.ganho_proporcional[0])
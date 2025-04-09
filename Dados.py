class Dado:
    def __init__(self):
        self.TELA_PRINCIPAL = 0
        self.TELA_PROCESSO_PADRAO = 1
        self.TELA_PROCESSO_PERSONALIZADO = 2
        self.TELA_TEC_TEMPO = 3
        self.TELA_TEC_TEMPERATURA = 4
        self.TELA_ESCOLHE_TAMANHO = 5
        self.TELA_ESCOLHE_REAGENTE = 6
        self.TELA_COMPLETA_PARAMETROS = 7
        self.TELA_PORCESSANDO = 8
        self.TELA_TROCA_BANHO = 9
        self.TELA_CONFIRMA_CANCELAMENTO = 10
        self.TELA_FINAL_PROCESSO = 11

        self.TAMANHO_1A2 = 0
        self.TAMANHO_3A4 = 1
        self.TAMANHO_ESPECIAL = 2
        self.TAMANHO_NENHUM = 3

        self.REAGENTE_XILOL = 0
        self.REAGENTE_ISOPROPANOL = 1
        self.REAGENTE_WITCLEAR = 2
        self.REAGENTE_NENHUM = 3


        self.GANHO_PROPORCIONAL_FORMOL = 3
        self.GANHO_PROPORCIONAL_ALCOOL = 3
        self.GANHO_PROPORCIONAL_ISOPROPANOL = 3
        self.GANHO_PROPORCIONAL_XILOL = 4
        self.GANHO_PROPORCIONAL_WITCLEAR = 4
        self.GANHO_PROPORCIONAL_PESONALIZADO = 3
        self.PERIODO_PWM = 2
        self.MLX90614_ERRO = -273.15
        self.FATOR_TEMPER_MAX = 1.35

        self._tamanho_da_amostra = self.TAMANHO_NENHUM
        self._reagente = self.REAGENTE_NENHUM
        
        self.tela_ativa = self.TELA_PRINCIPAL
        self.aciona_buzzer = True
        self.controle_estah_acionado = False
        self.beep_fim_processo = False

        self._temperatura_sistema = 0
        self._temperatura_set_point = 0
        self._ganho_poporcional_sistema = 0
        self.index_banho = 0

        self._formol_esta_ativado = False
        self._texto_formol_ativado = "FIXAÇÃO: DESATIVADO"
        self._texto_tamanho_amostra = "TAMANHO AMOSTRA"
        self._texto_reagente = "REAGENTE"

        self._texto_nome_do_processo = "NOME DO PROCESSO"
        self._texto_percento_progresso_banho = "0%"
        self._cor_indicacao_processo = "#505050"
        
        #self._cursor = 'cross'
        self._cursor = 'none'
        self._nome_programa = 'Histo V6'
        self._texto_iniciar_pausar = 'INICIAR'
        self._nome_proximo_reagente = 'AlCOOL'

        self._texto_valor_tempo = "05"
        self._texto_valor_temperatura = "55"
        self.posicao_digito_tempo = 0
        self.posicao_digito_temperatura = 0
        
        self._black = '#000000'
        self._white = '#FFFFFF'
        self._brighted = '#C4C4C4'
        self._grey = '#E5E5E5'
        self._grey_dark = "#505050"
        self._red = '#FF0000'
        self._green = '#2CCA28'
        self._window_w = 480
        self._window_h = 320
        
    @property
    def cursor(self):
        return self._cursor
    
    @property
    def nome_programa(self):
        return self._nome_programa

    @property
    def tamanho_da_amostra(self):
        return self._tamanho_da_amostra

    @property
    def reagente(self):
        return self._reagente
    
    @property
    def black(self):
        return self._black
    
    @property
    def white(self):
        return self._white
    
    @property
    def brighted(self):
        return self._brighted
    
    @property
    def grey(self):
        return self._grey
    
    @property
    def red(self):
        return self._red
    
    @property
    def green(self):
        return self._green
    
    @property
    def window_w(self):
        return self._window_w
    
    @property
    def window_h(self):
        return self._window_h

    @property
    def formol_esta_ativado(self):
        return self._formol_esta_ativado

    @property
    def texto_formol_ativado(self):
        return self._texto_formol_ativado

    @property
    def texto_tamanho_amostra(self):
        return self._texto_tamanho_amostra

    @property
    def texto_reagente(self):
        return self._texto_reagente

    @property
    def texto_nome_do_processo(self):
        return self._texto_nome_do_processo

    @property
    def texto_percento_progresso_banho(self):
        return self._texto_percento_progresso_banho

    @property
    def cor_indicacao_processo(self):
        return self._cor_indicacao_processo

    @property
    def texto_iniciar_pausar(self):
        return self._texto_iniciar_pausar

    @property
    def nome_proximo_reagente(self):
        return self._nome_proximo_reagente

    @property
    def temperatura_sistema(self):
        return self._temperatura_sistema

    @property
    def temperatura_set_point(self):
        return self._temperatura_set_point

    @property
    def ganho_poporcional_sistema(self):
        return self._ganho_poporcional_sistema

    @property
    def texto_valor_tempo(self):
        return self._texto_valor_tempo

    @property
    def texto_valor_temperatura(self):
        return self._texto_valor_temperatura


    def set_temperatura_sistema(self, temperatura_sistema):
        self._temperatura_sistema = temperatura_sistema

    def set_temperatura_set_point(self, temperatura_setpoint):
        self._temperatura_set_point = temperatura_setpoint

    def set_ganho_poporcional_sistema(self, ganho_proporcional):
        self._ganho_poporcional_sistema = ganho_proporcional


    def set_tamanho_da_amostra(self, tamanho_amostra):
        self._tamanho_da_amostra = tamanho_amostra
        self.set_texto_tamanho_amostra()

    def set_reagente(self, reagente):
        self._reagente = reagente
        self.set_texto_reagente()

    def set_texto_tamanho_amostra(self):
        if self.tamanho_da_amostra == self.TAMANHO_1A2:
            self._texto_tamanho_amostra = "1 A 2mm"
        if self.tamanho_da_amostra == self.TAMANHO_3A4:
            self._texto_tamanho_amostra = "3 A 4mm"
        if self.tamanho_da_amostra == self.TAMANHO_ESPECIAL:
            self._texto_tamanho_amostra = "MATERIAIS ESPECIAIS"
        if self.tamanho_da_amostra == self.TAMANHO_NENHUM:
            self._texto_tamanho_amostra = "TAMANHO AMOSTRA"

    def set_texto_reagente(self):
        if self.reagente == self.REAGENTE_XILOL:
            self._texto_reagente = "XILOL"
        if self.reagente == self.REAGENTE_ISOPROPANOL:
            self._texto_reagente = "ISOPROPANOL"
        if self.reagente == self.REAGENTE_WITCLEAR:
            self._texto_reagente = "WITCLEAR"
        if self.reagente == self.REAGENTE_NENHUM:
            self._texto_reagente = "REAGENTE"

    def set_texto_iniciar_pausar(self, texto):
        self._texto_iniciar_pausar = texto
        

    def set_formol_ativado(self, estado):
        if estado == True:
            self._texto_formol_ativado = "FIXAÇÃO: ATIVADO"
        else:
            self._texto_formol_ativado = "FIXAÇÃO: DESATIVADO"
        self._formol_esta_ativado = estado

    def set_texto_nome_processo(self, nome_processo):
        self._texto_nome_do_processo = nome_processo

    def set_texto_percento_progresso_banho(self, texto_num):
        valor = ("%02d%%" %(int(texto_num)))
        self._texto_percento_progresso_banho = valor

    def set_nome_proximo_reagente(self, nome_reagente):
        self._nome_proximo_reagente = nome_reagente

    def set_texto_valor_tempo(self, valor):
        self._texto_valor_tempo = "{:02d}".format(int(valor))

    def set_texto_valor_temperatura(self, valor):
        self._texto_valor_temperatura = "{:02d}".format(int(valor))

import threading
import time
from turtle import color
from Saidas import Saidas

class Execucao(threading.Thread):
    def __init__(self, dado, tela, rotina):
        threading.Thread.__init__(self)
        self._dado = dado
        self._tela = tela
        self._rotina = rotina
        self._toggle = True
        self._io = Saidas()
        
        self.OFFSET_TEMPERATURA = 0.94

        self._tempo_corrente_banho = 0
        
    def run(self):
        if self._dado.index_banho < len(self._rotina.banho.nome_banho):
            self.config_ganho_proporcional()
            self.config_setpoint()
            self.config_nome_banho()
            self.config_display_banhos()


        while self._dado.controle_estah_acionado:
            if self._dado.index_banho < len(self._rotina.banho.nome_banho):
                self.toggle_banho(self._dado.index_banho)

                if self._dado.temperatura_sistema > (self._rotina.banho.temperatura_banho[self._dado.index_banho])*self.OFFSET_TEMPERATURA:
                    if self._tempo_corrente_banho >= (self._rotina.banho.tempo_banho[self._dado.index_banho]*60):
                        self._tempo_corrente_banho = 0
                        self.proximo_banho()
                    else:
                        self._tempo_corrente_banho += 1
                self.atualiza_progresso()
            if self._io.porta_in == 1:
                self._dado.set_texto_iniciar_pausar("INICIAR")
                self._dado.controle_estah_acionado = False
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.bt_iniciar_TelaProcessando.objText, text=self._dado.texto_iniciar_pausar)
            if self._dado.temperatura_sistema == self._dado.MLX90614_ERRO or (self._dado.temperatura_sistema >= (self._rotina.banho.temperatura_banho[self._dado.index_banho]*self._dado.FATOR_TEMPER_MAX) ):
                self._dado.controle_estah_acionado = False
                self._tela.iniciaTelaAvisoErro()
                self._tela.destroy_TelaProcessando()
                self._io.magmetron(0)
                time.sleep(1)
                self._io.magmetron(0)
                time.sleep(1)
            time.sleep(1)

    def atualiza_progresso(self):
        valor = (self._tempo_corrente_banho * 100)/(self._rotina.banho.tempo_banho[self._dado.index_banho]*60)
        self._dado.set_texto_percento_progresso_banho(valor)
        self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_progresso_banho_TelaProcessando.objText, text= self._dado.texto_percento_progresso_banho)

    def proximo_banho(self):
        if self._dado.index_banho < len(self._rotina.banho.nome_banho):
            self._dado.index_banho += 1
            if self._dado.index_banho < len(self._rotina.banho.nome_banho):
                self._dado.tela_ativa = self._dado.TELA_TROCA_BANHO
                self._dado.controle_estah_acionado = False
                self._dado.set_nome_proximo_reagente(self._rotina.banho.nome_banho[self._dado.index_banho])
                self._dado.beep_fim_processo = True
                self._tela.iniciaTelaTrocaBanho()
                self._tela.destroy_TelaProcessando()

            else:
                self._dado.tela_ativa = self._dado.TELA_FINAL_PROCESSO
                self._dado.index_banho = 0
                self.config_display_banhos()

                self._dado.set_tamanho_da_amostra(self._dado.TAMANHO_NENHUM)
                self._dado.set_reagente(self._dado.REAGENTE_NENHUM)
                self._dado.set_formol_ativado(False)
                self._dado.controle_estah_acionado = False
                self._dado.beep_fim_processo = True

                self._tela.inicia_TelaFinalProcesso()
                self._tela.destroy_TelaProcessando() 

    def config_ganho_proporcional(self):
        self._dado.set_ganho_poporcional_sistema(self._rotina.banho.ganho_proporcional[self._dado.index_banho])
    
    def config_setpoint(self):
        self._dado.set_temperatura_set_point(self._rotina.banho.temperatura_banho[self._dado.index_banho])

    def config_nome_banho(self):
        self._dado.set_texto_nome_processo(self._rotina.banho.nome_banho[self._dado.index_banho])
        self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_nome_processo_TelaProcessando.objText, text=self._dado.texto_nome_do_processo)

    def config_display_banhos_(self):
        if self._dado.formol_esta_ativado == True:
            if self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            else:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)

        else:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)

        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_1A2:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
        
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_3A4:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
        
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            
            if self._dado.reagente == self._dado.REAGENTE_XILOL or self._dado.reagente == self._dado.REAGENTE_WITCLEAR:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
            else:
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_NENHUM:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_fixacao_TelaProcessando.objText, text= "")
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_desidratacao_TelaProcessando.objText, text= "STATUS-BANHO")
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.bttx_clarificacao_TelaProcessando.objText, text= "")

            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)

            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.grey)
            

            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec, fill= self._dado.grey)

    def config_display_banhos(self):
        self.config_display_banhos_()
        if self._dado.formol_esta_ativado == True:
            if self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
                if self._dado.index_banho == 0:
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                elif self._dado.index_banho == 1:
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                elif self._dado.index_banho > 1:
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.green)
                self._completa_banho(2)


            else:
                if self._dado.index_banho == 0:
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.cor_indicacao_processo)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)
                elif self._dado.index_banho > 0:
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)
                self._completa_banho(1)

        else:
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_fixacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_fixacao_TelaProcessando.objRec, fill= self._dado.grey)
            self._completa_banho(0)


    def _completa_banho(self, ofset):
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_1A2:
            if self._dado.index_banho == (1+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (2+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (3+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (4+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.green)
            
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_3A4:
            if self._dado.index_banho == (1+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (2+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (3+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (4+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (5+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (6+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.green)

            
        if self._dado.tamanho_da_amostra == self._dado.TAMANHO_ESPECIAL:
            if self._dado.index_banho == (1+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (2+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (3+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (4+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            elif self._dado.index_banho == (5+ofset):
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
            
            if self._dado.reagente == self._dado.REAGENTE_XILOL or self._dado.reagente == self._dado.REAGENTE_WITCLEAR:
                if self._dado.index_banho == (6+ofset):
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.green)

            else:
                if self._dado.index_banho == (6+ofset):
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.green)
                elif self._dado.index_banho == (7+ofset):
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec, fill= self._dado.green)
                    self._tela.canvas_TelaProcessando.itemconfig(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec, fill= self._dado.green)

    def toggle_banho(self, index):
    
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "FORMOL" or self._rotina.banho.nome_banho[self._dado.index_banho] == "FORMOL1":
            self.toggle_color(self._tela.btind_primeira_fixacao_TelaProcessando.objRec)

        if self._rotina.banho.nome_banho[self._dado.index_banho] == "FORMOL2":
            self.toggle_color(self._tela.btind_segunda_fixacao_TelaProcessando.objRec)

        if self._rotina.banho.nome_banho[self._dado.index_banho] == "ALCOOL1":
            self.toggle_color(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "ALCOOL2":
            self.toggle_color(self._tela.btind_segunda_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "ALCOOL3":
            self.toggle_color(self._tela.btind_terceira_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "ALCOOL4":
            self.toggle_color(self._tela.btind_quarta_desidratacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "ALCOOL5":
            self.toggle_color(self._tela.btind_quinta_desidratacao_TelaProcessando.objRec)

        if self._rotina.banho.nome_banho[self._dado.index_banho] == "XILOL1" or self._rotina.banho.nome_banho[self._dado.index_banho] == "ISOPROPANOL1" or self._rotina.banho.nome_banho[self._dado.index_banho] == "WITCLEAR1":
            self.toggle_color(self._tela.btind_primeira_clarificacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "XILOL2" or self._rotina.banho.nome_banho[self._dado.index_banho] == "ISOPROPANOL2" or self._rotina.banho.nome_banho[self._dado.index_banho] == "WITCLEAR2":
            self.toggle_color(self._tela.btind_segunda_clarificacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "XILOL3" or self._rotina.banho.nome_banho[self._dado.index_banho] == "ISOPROPANOL3" or self._rotina.banho.nome_banho[self._dado.index_banho] == "WITCLEAR3":
            self.toggle_color(self._tela.btind_terceira_clarificacao_TelaProcessando.objRec)
        
        if self._rotina.banho.nome_banho[self._dado.index_banho] == "ROTINA PERSONALIZADA":
            self.toggle_color(self._tela.btind_primeira_desidratacao_TelaProcessando.objRec)
        
        

    def toggle_color(self, obj):

        if self._toggle == True:
            self._tela.canvas_TelaProcessando.itemconfig(obj, fill= self._dado.green)
        else:
            self._tela.canvas_TelaProcessando.itemconfig(obj, fill= self._dado.cor_indicacao_processo)

        self._toggle = not self._toggle


    

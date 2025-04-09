import tkinter as tk

#from sqlalchemy import null
from Saidas import Saidas
from Watchdog import Watchdog
from SensorMlx90614 import MlX90614
from ControleProporcional import ControleProporcional
from Dados import Dado
from Buzzer import Beep
from Rotinas import RotinaExecutada
from Execucao import Execucao

import Telas

import time

class Main(Telas.TelaPrincipal, Telas.TelaProcessoPadrao, Telas.TelaPersonalizado,
           Telas.TelaTecTempo, Telas.TelaTecTemperatura, Telas.TelaEscolheTamanho,
           Telas.TelaEscolheReagente, Telas.TelaCompletaParametros, 
           Telas.TelaProcessando, Telas.TelaTrocaBanho, Telas.TelaConfirmaCancelamento,
           Telas.TelaFinalProcesso, Telas.TelaAvisoErro ):
    def __init__(self):
        self.out = Saidas()
        self.wtd = Watchdog()
        self.dado = Dado()
        self.sensor = MlX90614(arredondamento=1, dado=self.dado)
        self.buzzer = Beep(self.dado)
        self.controle_proporcional = ControleProporcional(self.dado, self.out)
        self.execucao = None
        
        
        self.buzzer.start()
        self.sensor.start()
        self.controle_proporcional.start()
        self.out.magnetron(1)
        self.out.ventilador(1)
        time.sleep(1)
        self.out.magnetron(0)
        self.out.ventilador(0)
        self.wtd.start()

        self.root = tk.Tk()

        Telas.TelaPrincipal.__init__(self, tk_inter_TelaPrincipal=self.root, dado_TelaPrincipal=self.dado)
        Telas.TelaProcessoPadrao.__init__(self, tk_inter_ProcessoPadrao=self.root, dado_ProcessoPadrao=self.dado)
        Telas.TelaPersonalizado.__init__(self, tk_inter_TelaPersonalizado=self.root, dado_TelaPersonalizado=self.dado)
        Telas.TelaTecTempo.__init__(self, tk_inter_TelaTecTempo=self.root, dado_TelaTecTempo=self.dado)
        Telas.TelaTecTemperatura.__init__(self, tk_inter_TelaTecTemperatura=self.root, dado_TelaTecTemperatura=self.dado)
        Telas.TelaEscolheTamanho.__init__(self, tk_inter_TelaEscolheTamanho=self.root, dado_TelaEscolheTamanho=self.dado)
        Telas.TelaEscolheReagente.__init__(self, tk_inter_TelaEscolheReagente=self.root, dado_TelaEscolheReagente=self.dado)
        Telas.TelaCompletaParametros.__init__(self, tk_inter_TelaCompletaParametros=self.root, dado_TelaCompletaParametros=self.dado)
        Telas.TelaProcessando.__init__(self, tk_inter_TelaProcessando=self.root, dado_TelaProcessando=self.dado)
        Telas.TelaTrocaBanho.__init__(self, tk_inter_TelaTrocaBanho=self.root, dado_TelaTrocaBanho=self.dado)
        Telas.TelaConfirmaCancelamento.__init__(self, tk_inter_TelaConfirmaCancelamento=self.root, dado_TelaConfirmaCancelamento=self.dado)
        Telas.TelaFinalProcesso.__init__(self, tk_inter_TelaFinalProcesso=self.root, dado_TelaFinalProcesso=self.dado)
        Telas.TelaAvisoErro.__init__(self, tk_inter_TelaAvisoErro=self.root, dado_TelaAvisoErro=self.dado)

    """ 
    Metodos reescritos das classes herdadas:
    """
    #TelaPrincipal
    def onBotaoPadrao_TelaPrincipal(self, event):
        super().onBotaoPadrao_TelaPrincipal(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.iniciaPadrao()
        self.destroyPrincipal()
        
    def onBotaoPersonalizado_TelaPrincipal(self, event):
        super().onBotaoPersonalizado_TelaPrincipal(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PERSONALIZADO
        self.iniciaTelaPersonalizado()
        self.destroyPrincipal()
    #-----------------------------------------------------------------
    #TelaProcessoPadrao
    def onBotaoVoltar_TelaProcessoPadrao(self, event):
        super().onBotaoVoltar_TelaProcessoPadrao(event)
        self.dado.tela_ativa = self.dado.TELA_PRINCIPAL
        self.iniciaPrincipal()
        self.destroyProcessoPadrao()

    def onBotaoFixacao_TelaProcessoPadrao(self, event):
        super().onBotaoFixacao_TelaProcessoPadrao(event)
        self.dado.set_formol_ativado(estado = not self.dado.formol_esta_ativado )

        self.canvas_ProcessoPadrao.itemconfig(self.bt_fixacaoProcessoPadrao.objText, text=self.dado.texto_formol_ativado)

    def onBotaoReagente_TelaProcessoPadrao(self, event):
        super().onBotaoReagente_TelaProcessoPadrao(event)
        self.dado.tela_ativa = self.dado.TELA_ESCOLHE_REAGENTE
        self.iniciaTelaEscolheReagente()
        self.destroyProcessoPadrao()

    def onBotaoTamanhoAmostra_TelaProcessoPadrao(self, event):
        super().onBotaoTamanhoAmostra_TelaProcessoPadrao(event)
        self.dado.tela_ativa = self.dado.TELA_ESCOLHE_TAMANHO
        self.iniciaTelaEscolheTamanho()
        self.destroyProcessoPadrao()

    def onBotaoIniciar_TelaProcessoPadrao(self, event):
        super().onBotaoIniciar_TelaProcessoPadrao(event)

        if self.dado.tamanho_da_amostra != self.dado.TAMANHO_NENHUM and self.dado.reagente != self.dado.REAGENTE_NENHUM:
            self.dado.tela_ativa = self.dado.TELA_PORCESSANDO

            #self.dado.controle_estah_acionado = True

            rotina = RotinaExecutada(self.dado)
            self.execucao = Execucao(self.dado, self, rotina)
        
            self.iniciaTelaProcessando()
            self.execucao.start()
            self.destroyProcessoPadrao()

        else:
            self.dado.tela_ativa = self.dado.TELA_COMPLETA_PARAMETROS
            self.iniciaTelaCompletaParametros()
            self.destroyProcessoPadrao()
        
        

    #-----------------------------------------------------------------
    #TelaPersonalizado
    def onBotaoVoltar_TelaPersonalizado(self, event):
        super().onBotaoVoltar_TelaPersonalizado(event)
        self.dado.tela_ativa = self.dado.TELA_PRINCIPAL
        self.iniciaPrincipal()
        self.destroy_TelaPersonalizado()

    def onBotaoTemperatura_TelaPersonalizado(self, event):
        super().onBotaoTemperatura_TelaPersonalizado(event)
        self.dado.tela_ativa = self.dado.TELA_TEC_TEMPERATURA
        self.iniciaTelaTecTemperatura()
        self.destroy_TelaPersonalizado()

    def onBotaoTempo_TelaPersonalizado(self, event):
        super().onBotaoTempo_TelaPersonalizado(event)
        self.dado.tela_ativa = self.dado.TELA_TEC_TEMPO
        self.iniciaTelaTecTempo()
        self.destroy_TelaPersonalizado()

    def onBotaoIniciar_TelaPersonalizado(self, event):
        super().onBotaoIniciar_TelaPersonalizado(event)
        if self.dado.tamanho_da_amostra == self.dado.TAMANHO_NENHUM and self.dado.reagente == self.dado.REAGENTE_NENHUM:
            self.dado.tela_ativa = self.dado.TELA_PORCESSANDO

            rotina = RotinaExecutada(self.dado)
            self.execucao = Execucao(self.dado, self, rotina)
        
            self.iniciaTelaProcessando()
            self.execucao.start()
            self.destroy_TelaPersonalizado()

    #-----------------------------------------------------------------
    #TelaTecTempo
    def onBotaoTempo_TelaTecTempo(self, event):
        super().onBotaoTempo_TelaTecTempo(event)

    def onBotaoValorTempo_TelaTecTempo(self, event):
        super().onBotaoValorTempo_TelaTecTempo(event)

    def onBotaoTeclaZero_TelaTecTempo(self, event):
        super().onBotaoTeclaZero_TelaTecTempo(event)
        self.preenche_digito(0)

    def onBotaoTeclaUm_TelaTecTempo(self, event):
        super().onBotaoTeclaUm_TelaTecTempo(event)
        self.preenche_digito(1)

    def onBotaoTeclaDois_TelaTecTempo(self, event):
        super().onBotaoTeclaDois_TelaTecTempo(event)
        self.preenche_digito(2)

    def onBotaoTeclaTres_TelaTecTempo(self, event):
        super().onBotaoTeclaTres_TelaTecTempo(event)
        self.preenche_digito(3)

    def onBotaoTeclaQuatro_TelaTecTempo(self, event):
        super().onBotaoTeclaQuatro_TelaTecTempo(event)
        self.preenche_digito(4)

    def onBotaoTeclaCinco_TelaTecTempo(self, event):
        super().onBotaoTeclaCinco_TelaTecTempo(event)
        self.preenche_digito(5)

    def onBotaoTeclaSeis_TelaTecTempo(self, event):
        super().onBotaoTeclaSeis_TelaTecTempo(event)
        self.preenche_digito(6)

    def onBotaoTeclaSete_TelaTecTempo(self, event):
        super().onBotaoTeclaSete_TelaTecTempo(event)
        self.preenche_digito(7)

    def onBotaoTeclaOito_TelaTecTempo(self, event):
        super().onBotaoTeclaOito_TelaTecTempo(event)
        self.preenche_digito(8)

    def onBotaoTeclaNove_TelaTecTempo(self, event):
        super().onBotaoTeclaNove_TelaTecTempo(event)
        self.preenche_digito(9)

    def onBotaoTeclaSeta_TelaTecTempo(self, event):
        super().onBotaoTeclaSeta_TelaTecTempo(event)
        self.dado_TelaTecTempo.posicao_digito_tempo
        self.dado_TelaTecTempo.set_texto_valor_tempo(0)
        self.canvas_TelaTecTempo.itemconfig(self.bt_valor_tempo_TelaTecTempo.objText, text=self.dado_TelaTecTempo.texto_valor_tempo)
            

    def preenche_digito(self, digito):
        if self.dado_TelaTecTempo.posicao_digito_tempo == 0:
            self.dado_TelaTecTempo.set_texto_valor_tempo(digito)
            self.canvas_TelaTecTempo.itemconfig(self.bt_valor_tempo_TelaTecTempo.objText, text=self.dado_TelaTecTempo.texto_valor_tempo)
            self.dado_TelaTecTempo.posicao_digito_tempo += 1
        elif self.dado_TelaTecTempo.posicao_digito_tempo >= 1:
            self.dado_TelaTecTempo.posicao_digito_tempo = 0
            valor = int(self.dado_TelaTecTempo.texto_valor_tempo)
            valor = valor*10 + digito
            self.dado_TelaTecTempo.set_texto_valor_tempo(valor)
            self.canvas_TelaTecTempo.itemconfig(self.bt_valor_tempo_TelaTecTempo.objText, text=self.dado_TelaTecTempo.texto_valor_tempo)



    def onBotaoTeclaOk_TelaTecTempo(self, event):
        super().onBotaoTeclaOk_TelaTecTempo(event)
        self.dado_TelaTecTempo.posicao_digito_tempo = 0
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PERSONALIZADO
        self.iniciaTelaPersonalizado()
        self.destroy_TelaTecTempo()

    #-----------------------------------------------------------------
    #TelaTecTempertura
    def onBotaoTeclaOk_TelaTecTemperatura(self, event):
        super().onBotaoTeclaOk_TelaTecTemperatura(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PERSONALIZADO
        self.iniciaTelaPersonalizado()
        self.destroy_TelaTecTemperatura()

    def onBotaoTeclaZero_TelaTecTemperatura(self, event):
        super().onBotaoTeclaZero_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(0)

    def onBotaoTeclaUm_TelaTecTemperatura(self, event):
        super().onBotaoTeclaUm_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(1)

    def onBotaoTeclaDois_TelaTecTemperatura(self, event):
        super().onBotaoTeclaDois_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(2)

    def onBotaoTeclaTres_TelaTecTemperatura(self, event):
        super().onBotaoTeclaTres_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(3)

    def onBotaoTeclaQuatro_TelaTecTemperatura(self, event):
        super().onBotaoTeclaQuatro_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(4)

    def onBotaoTeclaCinco_TelaTecTemperatura(self, event):
        super().onBotaoTeclaCinco_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(5)

    def onBotaoTeclaSeis_TelaTecTemperatura(self, event):
        super().onBotaoTeclaSeis_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(6)

    def onBotaoTeclaSete_TelaTecTemperatura(self, event):
        super().onBotaoTeclaSete_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(7)

    def onBotaoTeclaOito_TelaTecTemperatura(self, event):
        super().onBotaoTeclaOito_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(8)

    def onBotaoTeclaNove_TelaTecTemperatura(self, event):
        super().onBotaoTeclaNove_TelaTecTemperatura(event)
        self.preenche_digito_temperatura(9)

    def onBotaoTeclaSeta_TelaTecTemperatura(self, event):
        super().onBotaoTeclaSeta_TelaTecTemperatura(event)
        self.dado_TelaTecTemperatura.posicao_digito_temperatura = 0
        self.dado_TelaTecTemperatura.set_texto_valor_temperatura(0)
        self.canvas_TelaTecTemperatura.itemconfig(self.bt_valor_tempo_TelaTecTempo.objText, text=self.dado_TelaTecTemperatura.texto_valor_temperatura)


    

    def preenche_digito_temperatura(self, digito):
        if self.dado_TelaTecTemperatura.posicao_digito_temperatura == 0:
            self.dado_TelaTecTemperatura.set_texto_valor_temperatura(digito)
            self.canvas_TelaTecTemperatura.itemconfig(self.bt_valor_tempo_TelaTecTempo.objText, text=self.dado_TelaTecTemperatura.texto_valor_temperatura)
            self.dado_TelaTecTemperatura.posicao_digito_temperatura += 1
        elif self.dado_TelaTecTemperatura.posicao_digito_temperatura >= 1:
            self.dado_TelaTecTemperatura.posicao_digito_temperatura = 0
            valor = int(self.dado_TelaTecTemperatura.texto_valor_temperatura)
            valor = valor*10 + digito
            self.dado_TelaTecTemperatura.set_texto_valor_temperatura(valor)
            self.canvas_TelaTecTemperatura.itemconfig(self.bt_valor_tempo_TelaTecTemperatura.objText, text=self.dado_TelaTecTemperatura.texto_valor_temperatura)


    #-----------------------------------------------------------------
    #TelaEscolheTamanho
    def onBotao1A2_TelaEscolheTamanho(self, event):
        super().onBotao1A2_TelaEscolheTamanho(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.dado.set_tamanho_da_amostra(self.dado.TAMANHO_1A2)
        self.iniciaPadrao()
        self.destroy_TelaEscolheTamanho()

    def onBotao3A4_TelaEscolheTamanho(self, event):
        super().onBotao3A4_TelaEscolheTamanho(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.dado.set_tamanho_da_amostra(self.dado.TAMANHO_3A4)
        self.iniciaPadrao()
        self.destroy_TelaEscolheTamanho()

    def onBotaoMaterialEspecial_TelaEscolheTamanho(self, event):
        super().onBotaoMaterialEspecial_TelaEscolheTamanho(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.dado.set_tamanho_da_amostra(self.dado.TAMANHO_ESPECIAL)
        self.iniciaPadrao()
        self.destroy_TelaEscolheTamanho()
    #-----------------------------------------------------------------
    #TelaEscolheReagente
    def onBotaoXilol_TelaEscolheReagente(self, event):
        super().onBotaoXilol_TelaEscolheReagente(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.dado.set_reagente(self.dado.REAGENTE_XILOL)
        self.iniciaPadrao()
        self.destroy_TelaEscolheReagente()

    def onBotaoIsopropanol_TelaEscolheReagente(self, event):
        super().onBotaoIsopropanol_TelaEscolheReagente(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.dado.set_reagente(self.dado.REAGENTE_ISOPROPANOL)
        self.iniciaPadrao()
        self.destroy_TelaEscolheReagente()

    def onBotaoWitclear_TelaEscolheReagente(self, event):
        super().onBotaoWitclear_TelaEscolheReagente(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.dado.set_reagente(self.dado.REAGENTE_WITCLEAR)
        self.iniciaPadrao()
        self.destroy_TelaEscolheReagente()
    #-----------------------------------------------------------------
    #TelaCompletaParametros
    def onBotaoVoltar_TelaCompletaParametros(self, event):
        super().onBotaoVoltar_TelaCompletaParametros(event)
        self.dado.tela_ativa = self.dado.TELA_PROCESSO_PADRAO
        self.iniciaPadrao()
        self.destroy_TelaCompletaParametros()
    #-----------------------------------------------------------------
    #TelaProcessando
    def onBotaoCancelar_TelaProcessando(self, event):
        super().onBotaoCancelar_TelaProcessando(event)
        self.dado.tela_ativa = self.dado.TELA_CONFIRMA_CANCELAMENTO
        self.dado.controle_estah_acionado = False
        self.inicia_TelaConfirmaCancelamento()
        self.destroy_TelaProcessando()

    def onBotaoInicar_TelaProcessando(self, event):
        super().onBotaoInicar_TelaProcessando(event)
        self.dado.controle_estah_acionado = not self.dado.controle_estah_acionado
        if self.dado.controle_estah_acionado == True:
            self.dado.set_texto_iniciar_pausar("PAUSAR")
            rotina = RotinaExecutada(self.dado)
            self.execucao = Execucao(self.dado, self, rotina)
            self.execucao.start()
        else:
            self.dado.set_texto_iniciar_pausar("INICIAR")
        self.canvas_TelaProcessando.itemconfig(self.bt_iniciar_TelaProcessando.objText, text=self.dado.texto_iniciar_pausar) 

    #-----------------------------------------------------------------
    #TelaTrocaBanho
    def onBotaoOk_TelaTrocaBanho(self, event):
        super().onBotaoOk_TelaTrocaBanho(event)
        

        self.dado.tela_ativa = self.dado.TELA_PORCESSANDO
        self.dado.beep_fim_processo = False

        if self.dado.controle_estah_acionado == True:
            self.dado.set_texto_iniciar_pausar("PAUSAR")
        else:
            self.dado.set_texto_iniciar_pausar("INICIAR")

        rotina = RotinaExecutada(self.dado)
        self.execucao = Execucao(self.dado, self, rotina)
    
        self.iniciaTelaProcessando()
        self.execucao.start()
        self.destroy_TelaTrocaBanho()

    #-----------------------------------------------------------------
    #TelaConfirmaCancelamento
    def onBotaoSim_TelaConfirmaCancelamento(self, event):
        super().onBotaoSim_TelaConfirmaCancelamento(event)
        self.dado.tela_ativa = self.dado.TELA_PRINCIPAL
        self.dado.set_tamanho_da_amostra(self.dado.TAMANHO_NENHUM)
        self.dado.set_reagente(self.dado.REAGENTE_NENHUM)
        self.dado.set_formol_ativado(False)
        self.dado.controle_estah_acionado = False
        self.dado.set_texto_iniciar_pausar("INICIAR")
        self.iniciaPrincipal()
        self.destroy_TelaConfirmaCancelamento()

    def onBotaoNao_TelaConfirmaCancelamento(self, event):
        super().onBotaoNao_TelaConfirmaCancelamento(event)
        self.dado.tela_ativa = self.dado.TELA_PORCESSANDO
        #self.dado.controle_estah_acionado = True
        self.dado.set_texto_iniciar_pausar("INICIAR")

        rotina = RotinaExecutada(self.dado)
        self.execucao = Execucao(self.dado, self, rotina)

        self.iniciaTelaProcessando()
        self.execucao.start()
        self.destroy_TelaConfirmaCancelamento()
    #-----------------------------------------------------------------
    #TelaFinalProcesso
    def onBotaoOk_TelaFinalProcesso(self, event):
        super().onBotaoOk_TelaFinalProcesso(event)
        self.dado.tela_ativa = self.dado.TELA_PRINCIPAL
        self.dado.set_tamanho_da_amostra(self.dado.TAMANHO_NENHUM)
        self.dado.set_reagente(self.dado.REAGENTE_NENHUM)
        self.dado.set_formol_ativado(False)
        self.dado.controle_estah_acionado = False
        self.dado.beep_fim_processo = False
        self.dado.set_texto_iniciar_pausar("INICIAR")
        self.iniciaPrincipal()
        self.destroy_TelaFinalProcesso()
    
    """ 
    Metodos dessa classe
    """

try:
    if __name__ == '__main__':
       main = Main()
       main.iniciaPrincipal()
       main.root.mainloop()
finally:
    print('Erro de sistema!')


import tkinter as tk

class TelaPrincipal:
    def __init__(self, tk_inter_TelaPrincipal, dado_TelaPrincipal):

        self.tk_inter_TelaPrincipal = tk_inter_TelaPrincipal
        self.frame_TelaPrincipal = 0
        self.dado_TelaPrincipal = dado_TelaPrincipal
        #self.imagemTelaPrincipal = tk.PhotoImage(file="/home/pi/Histo_V6/img/Intro_back.png")
        #self.imagemTelaPrincipal = tk.PhotoImage(file="img/Intro_back.png")

        self.canvas_TelaPrincipal = 0

        self.bt_padraoTelaPrincipal = 0
        self.bt_personalizadoTelaPrincipal = 0
        
        self.tk_inter_TelaPrincipal.title('Histo_V6')
        self.tk_inter_TelaPrincipal.config(cursor = self.dado_TelaPrincipal.cursor)
        self.tk_inter_TelaPrincipal.geometry("{0}x{1}+0+0".format(self.dado_TelaPrincipal.window_w, self.dado_TelaPrincipal.window_h))
        self.tk_inter_TelaPrincipal.overrideredirect(True)
        
    def iniciaPrincipal(self):
        self.frame_TelaPrincipal = tk.Frame(self.tk_inter_TelaPrincipal)
        #self.dado_TelaPrincipal.aciona_buzzer = True

        #adiciona área para desenho
        self.canvas_TelaPrincipal = tk.Canvas(self.tk_inter_TelaPrincipal, width=self.dado_TelaPrincipal.window_w, height=self.dado_TelaPrincipal.window_h, background=self.dado_TelaPrincipal.grey)
        #self.canvas_TelaPrincipal.create_image(0,0,image=self.imagemTelaPrincipal, anchor='nw')
        
        self.bt_padraoTelaPrincipal = CriaBotao('PADRÃO',25 , 400, 60, 40, 61, self.dado_TelaPrincipal.green,self.canvas_TelaPrincipal, self.tk_inter_TelaPrincipal)
        self.bt_personalizadoTelaPrincipal = CriaBotao('PERSONALIZADO',25 , 400, 60, 40, 151, self.dado_TelaPrincipal.green,self.canvas_TelaPrincipal, self.tk_inter_TelaPrincipal)
        
        #Associa o método no envento click
        self.canvas_TelaPrincipal.tag_bind(self.bt_padraoTelaPrincipal.objRec, '<ButtonPress-1>', self.onBotaoPadrao_TelaPrincipal)
        self.canvas_TelaPrincipal.tag_bind(self.bt_padraoTelaPrincipal.objText, '<ButtonPress-1>', self.onBotaoPadrao_TelaPrincipal)
        
        self.canvas_TelaPrincipal.tag_bind(self.bt_personalizadoTelaPrincipal.objRec, '<ButtonPress-1>', self.onBotaoPersonalizado_TelaPrincipal)
        self.canvas_TelaPrincipal.tag_bind(self.bt_personalizadoTelaPrincipal.objText, '<ButtonPress-1>', self.onBotaoPersonalizado_TelaPrincipal)
        
        self.canvas_TelaPrincipal.pack()
        self.frame_TelaPrincipal.pack()
        
    def onBotaoPadrao_TelaPrincipal(self, event):
        self.dado_TelaPrincipal.aciona_buzzer = True
        #self.dado_TelaPrincipal.tela_ativa = self.dado_TelaPrincipal.TELA_PROCESSO_PADRAO
        
        #self.telaProcessoPadrao = tk.Toplevel(self.tk_inter_TelaPrincipal)
        #self.app = TelaProcessoPadrao(self.telaProcessoPadrao, self.dado_TelaPrincipal)
        #self.destroy()
        
    def onBotaoPersonalizado_TelaPrincipal(self, event):
        self.dado_TelaPrincipal.aciona_buzzer = True
        # self.dado_TelaPrincipal.tela_ativa = self.dado_TelaPrincipal.TELA_PROCESSO_PERSONALIZADO
        # print('Clicou no Botão PERSONALIZADO: ', self.dado_TelaPrincipal.tela_ativa )
        
        # self.telaPersonalizado = tk.Toplevel(self.tk_inter_TelaPrincipal)
        # self.app = TelaPersonalizado(self.telaPersonalizado, self.dado_TelaPrincipal)
        # self.destroy(self.frame_TelaPrincipal, self.canvas_TelaPrincipal)
        
    def destroyPrincipal(self):
        self.frame_TelaPrincipal.destroy()
        self.canvas_TelaPrincipal.destroy()
        
class TelaProcessoPadrao:
    def __init__(self, tk_inter_ProcessoPadrao, dado_ProcessoPadrao):
        self.tk_inter_ProcessoPadrao = tk_inter_ProcessoPadrao
        self.frame_ProcessoPadrao = 0
        self.dado_ProcessoPadrao = dado_ProcessoPadrao
        self.canvas_ProcessoPadrao = 0
        #self.imagemProcessoPadrao = tk.PhotoImage(file="/home/pi/Histo_V6/img/Intro_back.png")
        #self.imagemProcessoPadrao = tk.PhotoImage(file="img/Intro_back.png")

        self.bt_fixacaoProcessoPadrao = 0
        self.bt_tamanho_amostraProcessoPadrao = 0
        self.bt_reagenteProcessoPadrao = 0
        self.bt_voltarProcessoPadrao = 0
        self.bt_iniciarProcessoPadrao = 0
        
        self.tk_inter_ProcessoPadrao.title('Histo_V6')
        self.tk_inter_ProcessoPadrao.config(cursor=self.dado_ProcessoPadrao.cursor)
        self.tk_inter_ProcessoPadrao.geometry("{0}x{1}+0+0".format(self.dado_ProcessoPadrao.window_w, self.dado_ProcessoPadrao.window_h))
        self.tk_inter_ProcessoPadrao.overrideredirect(True)
        
    def iniciaPadrao(self):
        self.frame_ProcessoPadrao = tk.Frame(self.tk_inter_ProcessoPadrao)

        #adiciona área para desenho
        self.canvas_ProcessoPadrao = tk.Canvas(self.tk_inter_ProcessoPadrao, width=self.dado_ProcessoPadrao.window_w, height=self.dado_ProcessoPadrao.window_h, background=self.dado_ProcessoPadrao.grey)
        #self.canvas_ProcessoPadrao.create_image(0,0,image=self.imagemProcessoPadrao, anchor='nw')

        self.bt_fixacaoProcessoPadrao = CriaBotao(self.dado_ProcessoPadrao.texto_formol_ativado , 25, 400, 44, 40, 18, self.dado_ProcessoPadrao.green,self.canvas_ProcessoPadrao, self.tk_inter_ProcessoPadrao)
        self.bt_tamanho_amostraProcessoPadrao = CriaBotao(self.dado_ProcessoPadrao.texto_tamanho_amostra,25 , 400, 44, 40, 73, self.dado_ProcessoPadrao.green,self.canvas_ProcessoPadrao, self.tk_inter_ProcessoPadrao)
        self.bt_reagenteProcessoPadrao = CriaBotao(self.dado_ProcessoPadrao.texto_reagente,25 , 400, 44, 40, 129, self.dado_ProcessoPadrao.green,self.canvas_ProcessoPadrao, self.tk_inter_ProcessoPadrao)
        self.bt_voltarProcessoPadrao = CriaBotao('VOLTAR',16 , 110, 70, 40, 185, self.dado_ProcessoPadrao.green,self.canvas_ProcessoPadrao, self.tk_inter_ProcessoPadrao)
        self.bt_iniciarProcessoPadrao = CriaBotao('INICIAR',16 , 110, 70, 330, 185, self.dado_ProcessoPadrao.green,self.canvas_ProcessoPadrao, self.tk_inter_ProcessoPadrao)
        
        #Associa o método no envento click
        self.canvas_ProcessoPadrao.tag_bind(self.bt_fixacaoProcessoPadrao.objRec, '<ButtonPress-1>', self.onBotaoFixacao_TelaProcessoPadrao)
        self.canvas_ProcessoPadrao.tag_bind(self.bt_fixacaoProcessoPadrao.objText, '<ButtonPress-1>', self.onBotaoFixacao_TelaProcessoPadrao)
        
        self.canvas_ProcessoPadrao.tag_bind(self.bt_tamanho_amostraProcessoPadrao.objRec, '<ButtonPress-1>', self.onBotaoTamanhoAmostra_TelaProcessoPadrao)
        self.canvas_ProcessoPadrao.tag_bind(self.bt_tamanho_amostraProcessoPadrao.objText, '<ButtonPress-1>', self.onBotaoTamanhoAmostra_TelaProcessoPadrao)
        
        self.canvas_ProcessoPadrao.tag_bind(self.bt_reagenteProcessoPadrao.objRec, '<ButtonPress-1>', self.onBotaoReagente_TelaProcessoPadrao)
        self.canvas_ProcessoPadrao.tag_bind(self.bt_reagenteProcessoPadrao.objText, '<ButtonPress-1>', self.onBotaoReagente_TelaProcessoPadrao)
        
        self.canvas_ProcessoPadrao.tag_bind(self.bt_voltarProcessoPadrao.objRec, '<ButtonPress-1>', self.onBotaoVoltar_TelaProcessoPadrao)
        self.canvas_ProcessoPadrao.tag_bind(self.bt_voltarProcessoPadrao.objText, '<ButtonPress-1>', self.onBotaoVoltar_TelaProcessoPadrao)
        
        self.canvas_ProcessoPadrao.tag_bind(self.bt_iniciarProcessoPadrao.objRec, '<ButtonPress-1>', self.onBotaoIniciar_TelaProcessoPadrao)
        self.canvas_ProcessoPadrao.tag_bind(self.bt_iniciarProcessoPadrao.objText, '<ButtonPress-1>', self.onBotaoIniciar_TelaProcessoPadrao)
        
        self.canvas_ProcessoPadrao.pack()
        self.frame_ProcessoPadrao.pack()
        
    def onBotaoFixacao_TelaProcessoPadrao(self, event):
        self.dado_ProcessoPadrao.aciona_buzzer = True
        
    def onBotaoTamanhoAmostra_TelaProcessoPadrao(self, event):
        self.dado_ProcessoPadrao.aciona_buzzer = True
        
    def onBotaoReagente_TelaProcessoPadrao(self, event):
        self.dado_ProcessoPadrao.aciona_buzzer = True
        
    def onBotaoVoltar_TelaProcessoPadrao(self, event):
        self.dado_ProcessoPadrao.aciona_buzzer = True
        
    def onBotaoIniciar_TelaProcessoPadrao(self, event):
        self.dado_ProcessoPadrao.aciona_buzzer = True
        
    def destroyProcessoPadrao(self):
        self.frame_ProcessoPadrao.destroy()
        self.canvas_ProcessoPadrao.destroy()
        
class TelaPersonalizado:
    def __init__(self, tk_inter_TelaPersonalizado, dado_TelaPersonalizado):
        self.tk_inter_TelaPersonalizado = tk_inter_TelaPersonalizado
        self.frame_TelaPersonalizado = 0
        self.dado_TelaPersonalizado = dado_TelaPersonalizado
        self.canvas_TelaPersonalizado = 0
        #self.imagem_TelaPersonalizado = tk.PhotoImage(file="img/Intro_back.png")

        self.bt_tempo_TelaPersonalizado = 0
        self.bt_temperatura_TelaPersonalizado = 0
        self.bt_voltar_TelaPersonalizado = 0
        self.bt_iniciar_TelaPersonalizado = 0

        self.tk_inter_TelaPersonalizado.title('Histo_V6')
        self.tk_inter_TelaPersonalizado.config(cursor=self.dado_TelaPersonalizado.cursor)
        self.tk_inter_TelaPersonalizado.geometry("{0}x{1}+0+0".format(self.dado_TelaPersonalizado.window_w, self.dado_TelaPersonalizado.window_h))
        self.tk_inter_TelaPersonalizado.overrideredirect(True)
        
    def iniciaTelaPersonalizado(self):
        self.frame_TelaPersonalizado = tk.Frame(self.tk_inter_TelaPersonalizado)
        self.dado_TelaPersonalizado.set_texto_valor_tempo(self.dado_TelaPersonalizado.texto_valor_tempo)
        self.dado_TelaPersonalizado.set_texto_valor_temperatura(self.dado_TelaPersonalizado.texto_valor_temperatura)

        #adiciona área para desenho
        self.canvas_TelaPersonalizado = tk.Canvas(self.tk_inter_TelaPersonalizado, width=self.dado_TelaPersonalizado.window_w, height=self.dado_TelaPersonalizado.window_h, background=self.dado_TelaPersonalizado.grey)
        #self.canvas_TelaPersonalizado.create_image(0,0,image=self.imagem_TelaPersonalizado, anchor='nw')
        
        self.bt_tempo_TelaPersonalizado = CriaBotao('TEMPO: {} min.'.format(self.dado_TelaPersonalizado.texto_valor_tempo) ,25 , 400, 60, 40, 35, self.dado_TelaPersonalizado.green,self.canvas_TelaPersonalizado, self.tk_inter_TelaPersonalizado)
        self.bt_temperatura_TelaPersonalizado = CriaBotao('TEMPERATURA: {} °C.'.format(self.dado_TelaPersonalizado.texto_valor_temperatura),25 , 400, 60, 40, 109, self.dado_TelaPersonalizado.green,self.canvas_TelaPersonalizado, self.tk_inter_TelaPersonalizado)
        self.bt_voltar_TelaPersonalizado = CriaBotao('VOLTAR',16 , 110, 70, 40, 183, self.dado_TelaPersonalizado.green,self.canvas_TelaPersonalizado, self.tk_inter_TelaPersonalizado)
        self.bt_iniciar_TelaPersonalizado = CriaBotao('INICIAR',16 , 110, 70, 330, 183, self.dado_TelaPersonalizado.green,self.canvas_TelaPersonalizado, self.tk_inter_TelaPersonalizado)
        
        #Associa o método no envento click
        self.canvas_TelaPersonalizado.tag_bind(self.bt_tempo_TelaPersonalizado.objRec, '<ButtonPress-1>', self.onBotaoTempo_TelaPersonalizado)
        self.canvas_TelaPersonalizado.tag_bind(self.bt_tempo_TelaPersonalizado.objText, '<ButtonPress-1>', self.onBotaoTempo_TelaPersonalizado)
        
        self.canvas_TelaPersonalizado.tag_bind(self.bt_temperatura_TelaPersonalizado.objRec, '<ButtonPress-1>', self.onBotaoTemperatura_TelaPersonalizado)
        self.canvas_TelaPersonalizado.tag_bind(self.bt_temperatura_TelaPersonalizado.objText, '<ButtonPress-1>', self.onBotaoTemperatura_TelaPersonalizado)
        
        self.canvas_TelaPersonalizado.tag_bind(self.bt_voltar_TelaPersonalizado.objRec, '<ButtonPress-1>', self.onBotaoVoltar_TelaPersonalizado)
        self.canvas_TelaPersonalizado.tag_bind(self.bt_voltar_TelaPersonalizado.objText, '<ButtonPress-1>', self.onBotaoVoltar_TelaPersonalizado)
        
        self.canvas_TelaPersonalizado.tag_bind(self.bt_iniciar_TelaPersonalizado.objRec, '<ButtonPress-1>', self.onBotaoIniciar_TelaPersonalizado)
        self.canvas_TelaPersonalizado.tag_bind(self.bt_iniciar_TelaPersonalizado.objText, '<ButtonPress-1>', self.onBotaoIniciar_TelaPersonalizado)
        
        self.canvas_TelaPersonalizado.pack()
        self.frame_TelaPersonalizado.pack()

    def onBotaoTempo_TelaPersonalizado(self, event):
        self.dado_TelaPersonalizado.aciona_buzzer = True
        
    def onBotaoTemperatura_TelaPersonalizado(self, event):
        self.dado_TelaPersonalizado.aciona_buzzer = True
        
    def onBotaoVoltar_TelaPersonalizado(self, event):
        self.dado_TelaPersonalizado.aciona_buzzer = True
        
    def onBotaoIniciar_TelaPersonalizado(self, event):
        self.dado_TelaPersonalizado.aciona_buzzer = True
        
    def destroy_TelaPersonalizado(self):
        self.frame_TelaPersonalizado.destroy()
        self.canvas_TelaPersonalizado.destroy()

class TelaTecTempo:
    def __init__(self, tk_inter_TelaTecTempo, dado_TelaTecTempo):
        self.tk_inter_TelaTecTempo = tk_inter_TelaTecTempo
        self.frame_TelaTecTempo = 0
        self.dado_TelaTecTempo = dado_TelaTecTempo
        self.canvas_TelaTecTempo = 0
        #self.imagem_TelaTecTempo = tk.PhotoImage(file="img/Intro_back.png")

        self.bttx_tempo_TelaTecTempo = 0
        self.bt_valor_tempo_TelaTecTempo = 0

        self.bt_tecla_zero_TelaTecTempo = 0
        self.bt_tecla_um_TelaTecTempo = 0
        self.bt_tecla_dois_TelaTecTempo = 0
        self.bt_tecla_tres_TelaTecTempo = 0
        self.bt_tecla_quatro_TelaTecTempo = 0
        self.bt_tecla_cinco_TelaTecTempo = 0
        self.bt_tecla_seis_TelaTecTempo = 0
        self.bt_tecla_sete_TelaTecTempo = 0
        self.bt_tecla_oito_TelaTecTempo = 0
        self.bt_tecla_nove_TelaTecTempo = 0
        self.bt_tecla_seta_TelaTecTempo = 0
        self.bt_tecla_ok_TelaTecTempo = 0

        self.tk_inter_TelaTecTempo.title('Histo_V6')
        self.tk_inter_TelaTecTempo.config(cursor=self.dado_TelaTecTempo.cursor)
        self.tk_inter_TelaTecTempo.geometry("{0}x{1}+0+0".format(self.dado_TelaTecTempo.window_w, self.dado_TelaTecTempo.window_h))
        self.tk_inter_TelaTecTempo.overrideredirect(True)
        
    def iniciaTelaTecTempo(self):
        self.frame_TelaTecTempo = tk.Frame(self.tk_inter_TelaTecTempo)

        #adiciona área para desenho
        self.canvas_TelaTecTempo = tk.Canvas(self.tk_inter_TelaTecTempo, width=self.dado_TelaTecTempo.window_w, height=self.dado_TelaTecTempo.window_h, background=self.dado_TelaTecTempo.grey)
        #self.canvas_TelaPersonalizado.create_image(0,0,image=self.imagem_TelaPersonalizado, anchor='nw')
        
        self.bttx_tempo_TelaTecTempo = CriaBotao('TEMPO(min)',22 , 170, 60, 32, 38, self.dado_TelaTecTempo.grey,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_valor_tempo_TelaTecTempo = CriaBotao(self.dado_TelaTecTempo.texto_valor_tempo,25 , 200, 60, 247, 38, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        
        self.bt_tecla_zero_TelaTecTempo = CriaBotao('0',25 , 60, 60, 32, 117, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_um_TelaTecTempo = CriaBotao('1',25 , 60, 60, 103, 117, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_dois_TelaTecTempo = CriaBotao('2',25 , 60, 60, 174, 117, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_tres_TelaTecTempo = CriaBotao('3',25 , 60, 60, 245, 117, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_quatro_TelaTecTempo = CriaBotao('4',25 , 60, 60, 316, 117, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_cinco_TelaTecTempo = CriaBotao('5',25 , 60, 60, 384, 117, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_seis_TelaTecTempo = CriaBotao('6',25 , 60, 60, 32, 185, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_sete_TelaTecTempo = CriaBotao('7',25 , 60, 60, 103, 185, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_oito_TelaTecTempo = CriaBotao('8',25 , 60, 60, 174, 185, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_nove_TelaTecTempo = CriaBotao('9',25 , 60, 60, 245, 185, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_seta_TelaTecTempo = CriaBotao('<-',25 , 60, 60, 316, 185, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        self.bt_tecla_ok_TelaTecTempo = CriaBotao('OK',25 , 60, 60, 384, 184, self.dado_TelaTecTempo.green,self.canvas_TelaTecTempo, self.tk_inter_TelaTecTempo)
        
        #Associa o método no envento click
        self.canvas_TelaTecTempo.tag_bind(self.bttx_tempo_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTempo_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bttx_tempo_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTempo_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_valor_tempo_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoValorTempo_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_valor_tempo_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoValorTempo_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_zero_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaZero_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_zero_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaZero_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_um_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaUm_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_um_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaUm_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_dois_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaDois_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_dois_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaDois_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_tres_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaTres_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_tres_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaTres_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_quatro_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaQuatro_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_quatro_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaQuatro_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_cinco_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaCinco_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_cinco_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaCinco_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_seis_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaSeis_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_seis_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaSeis_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_sete_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaSete_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_sete_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaSete_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_oito_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaOito_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_oito_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaOito_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_nove_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaNove_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_nove_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaNove_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_seta_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaSeta_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_seta_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaSeta_TelaTecTempo)
        
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_ok_TelaTecTempo.objRec, '<ButtonPress-1>', self.onBotaoTeclaOk_TelaTecTempo)
        self.canvas_TelaTecTempo.tag_bind(self.bt_tecla_ok_TelaTecTempo.objText, '<ButtonPress-1>', self.onBotaoTeclaOk_TelaTecTempo)
              
        self.canvas_TelaTecTempo.pack()
        self.frame_TelaTecTempo.pack()

    def onBotaoTempo_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoValorTempo_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaZero_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaUm_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaDois_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaTres_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaQuatro_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaCinco_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaSeis_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaSete_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaOito_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaNove_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaSeta_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def onBotaoTeclaOk_TelaTecTempo(self, event):
        self.dado_TelaTecTempo.aciona_buzzer = True

    def destroy_TelaTecTempo(self):
        self.frame_TelaTecTempo.destroy()
        self.canvas_TelaTecTempo.destroy()

class TelaTecTemperatura:
    def __init__(self, tk_inter_TelaTecTemperatura, dado_TelaTecTemperatura):
        self.tk_inter_TelaTecTemperatura = tk_inter_TelaTecTemperatura
        self.frame_TelaTecTemperatura = 0
        self.dado_TelaTecTemperatura = dado_TelaTecTemperatura
        self.canvas_TelaTecTemperatura = 0
        #self.imagem_TelaTecTemperatura = tk.PhotoImage(file="img/Intro_back.png")

        self.bttx_tempo_TelaTecTemperatura = 0
        self.bt_valor_tempo_TelaTecTemperatura = 0

        self.bt_tecla_zero_TelaTecTemperatura = 0
        self.bt_tecla_um_TelaTecTemperatura = 0
        self.bt_tecla_dois_TelaTecTemperatura = 0
        self.bt_tecla_tres_TelaTecTemperatura = 0
        self.bt_tecla_quatro_TelaTecTemperatura = 0
        self.bt_tecla_cinco_TelaTecTemperatura = 0
        self.bt_tecla_seis_TelaTecTemperatura = 0
        self.bt_tecla_sete_TelaTecTemperatura = 0
        self.bt_tecla_oito_TelaTecTemperatura = 0
        self.bt_tecla_nove_TelaTecTemperatura = 0
        self.bt_tecla_seta_TelaTecTemperatura = 0
        self.bt_tecla_ok_TelaTecTemperatura = 0

        self.tk_inter_TelaTecTemperatura.title('Histo_V6')
        self.tk_inter_TelaTecTemperatura.config(cursor=self.dado_TelaTecTemperatura.cursor)
        self.tk_inter_TelaTecTemperatura.geometry("{0}x{1}+0+0".format(self.dado_TelaTecTemperatura.window_w, self.dado_TelaTecTemperatura.window_h))
        self.tk_inter_TelaTecTemperatura.overrideredirect(True)
        
    def iniciaTelaTecTemperatura(self):
        self.frame_TelaTecTemperatura = tk.Frame(self.tk_inter_TelaTecTemperatura)

        #adiciona área para desenho
        self.canvas_TelaTecTemperatura = tk.Canvas(self.tk_inter_TelaTecTemperatura, width=self.dado_TelaTecTemperatura.window_w, height=self.dado_TelaTecTemperatura.window_h, background=self.dado_TelaTecTemperatura.grey)
        #self.canvas_TelaPersonalizado.create_image(0,0,image=self.imagem_TelaPersonalizado, anchor='nw')
        
        self.bttx_tempo_TelaTecTemperatura = CriaBotao('TEMPERATURA',25 , 275, 60, 32, 38, self.dado_TelaTecTemperatura.grey,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_valor_tempo_TelaTecTemperatura = CriaBotao(self.dado_TelaTecTemperatura.texto_valor_temperatura,25 , 130, 60, 316, 38, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        
        self.bt_tecla_zero_TelaTecTemperatura = CriaBotao('0',25 , 60, 60, 32, 117, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_um_TelaTecTemperatura = CriaBotao('1',25 , 60, 60, 103, 117, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_dois_TelaTecTemperatura = CriaBotao('2',25 , 60, 60, 174, 117, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_tres_TelaTecTemperatura = CriaBotao('3',25 , 60, 60, 245, 117, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_quatro_TelaTecTemperatura = CriaBotao('4',25 , 60, 60, 316, 117, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_cinco_TelaTecTemperatura = CriaBotao('5',25 , 60, 60, 384, 117, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_seis_TelaTecTemperatura = CriaBotao('6',25 , 60, 60, 32, 185, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_sete_TelaTecTemperatura = CriaBotao('7',25 , 60, 60, 103, 185, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_oito_TelaTecTemperatura = CriaBotao('8',25 , 60, 60, 174, 185, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_nove_TelaTecTemperatura = CriaBotao('9',25 , 60, 60, 245, 185, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_seta_TelaTecTemperatura = CriaBotao('<-',25 , 60, 60, 316, 185, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        self.bt_tecla_ok_TelaTecTemperatura = CriaBotao('OK',25 , 60, 60, 384, 184, self.dado_TelaTecTemperatura.green,self.canvas_TelaTecTemperatura, self.tk_inter_TelaTecTemperatura)
        
        #Associa o método no envento click
        self.canvas_TelaTecTemperatura.tag_bind(self.bttx_tempo_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTempo_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bttx_tempo_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTempo_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_valor_tempo_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoValorTempo_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_valor_tempo_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoValorTempo_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_zero_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaZero_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_zero_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaZero_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_um_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaUm_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_um_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaUm_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_dois_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaDois_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_dois_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaDois_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_tres_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaTres_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_tres_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaTres_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_quatro_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaQuatro_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_quatro_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaQuatro_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_cinco_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaCinco_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_cinco_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaCinco_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_seis_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaSeis_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_seis_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaSeis_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_sete_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaSete_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_sete_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaSete_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_oito_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaOito_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_oito_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaOito_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_nove_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaNove_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_nove_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaNove_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_seta_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaSeta_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_seta_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaSeta_TelaTecTemperatura)
        
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_ok_TelaTecTemperatura.objRec, '<ButtonPress-1>', self.onBotaoTeclaOk_TelaTecTemperatura)
        self.canvas_TelaTecTemperatura.tag_bind(self.bt_tecla_ok_TelaTecTemperatura.objText, '<ButtonPress-1>', self.onBotaoTeclaOk_TelaTecTemperatura)
              
        self.canvas_TelaTecTemperatura.pack()
        self.frame_TelaTecTemperatura.pack()

    def onBotaoTempo_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoValorTempo_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaZero_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaUm_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaDois_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaTres_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaQuatro_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaCinco_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaSeis_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaSete_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaOito_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaNove_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaSeta_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def onBotaoTeclaOk_TelaTecTemperatura(self, event):
        self.dado_TelaTecTemperatura.aciona_buzzer = True

    def destroy_TelaTecTemperatura(self):
        self.frame_TelaTecTemperatura.destroy()
        self.canvas_TelaTecTemperatura.destroy()

class TelaEscolheTamanho:
    def __init__(self, tk_inter_TelaEscolheTamanho, dado_TelaEscolheTamanho):
        self.tk_inter_TelaEscolheTamanho = tk_inter_TelaEscolheTamanho
        self.frame_TelaEscolheTamanho = 0
        self.dado_TelaEscolheTamanho = dado_TelaEscolheTamanho
        self.canvas_TelaEscolheTamanho = 0
        #self.imagem_TelaEscolheTamanho = tk.PhotoImage(file="img/Intro_back.png")

        self.bt_1A2_mm_TelaEscolheTamanho = 0
        self.bt_3A4_mm_TelaEscolheTamanho = 0
        self.bt_material_especial_TelaEscolheTamanho = 0

        self.tk_inter_TelaEscolheTamanho.title('Histo_V6')
        self.tk_inter_TelaEscolheTamanho.config(cursor=self.dado_TelaEscolheTamanho.cursor)
        self.tk_inter_TelaEscolheTamanho.geometry("{0}x{1}+0+0".format(self.dado_TelaEscolheTamanho.window_w, self.dado_TelaEscolheTamanho.window_h))
        self.tk_inter_TelaEscolheTamanho.overrideredirect(True)
        
    def iniciaTelaEscolheTamanho(self):
        self.frame_TelaEscolheTamanho = tk.Frame(self.tk_inter_TelaEscolheTamanho)

        #adiciona área para desenho
        self.canvas_TelaEscolheTamanho = tk.Canvas(self.tk_inter_TelaEscolheTamanho, width=self.dado_TelaEscolheTamanho.window_w, height=self.dado_TelaEscolheTamanho.window_h, background=self.dado_TelaEscolheTamanho.grey)
        #self.canvas_TelaPersonalizado.create_image(0,0,image=self.imagem_TelaPersonalizado, anchor='nw')
        
        self.bt_1A2_mm_TelaEscolheTamanho = CriaBotao('1 A 2mm',25 , 400, 72, 40, 16, self.dado_TelaEscolheTamanho.green,self.canvas_TelaEscolheTamanho, self.tk_inter_TelaEscolheTamanho)
        self.bt_3A4_mm_TelaEscolheTamanho = CriaBotao('3 A 4mm',25 , 400, 72, 40, 100, self.dado_TelaEscolheTamanho.green,self.canvas_TelaEscolheTamanho, self.tk_inter_TelaEscolheTamanho)
        self.bt_material_especial_TelaEscolheTamanho = CriaBotao('MATERIAIS ESPECIAIS',25 , 400, 72, 40, 184, self.dado_TelaEscolheTamanho.green,self.canvas_TelaEscolheTamanho, self.tk_inter_TelaEscolheTamanho)
        
        #Associa o método no envento click
        self.canvas_TelaEscolheTamanho.tag_bind(self.bt_1A2_mm_TelaEscolheTamanho.objRec, '<ButtonPress-1>', self.onBotao1A2_TelaEscolheTamanho)
        self.canvas_TelaEscolheTamanho.tag_bind(self.bt_1A2_mm_TelaEscolheTamanho.objText, '<ButtonPress-1>', self.onBotao1A2_TelaEscolheTamanho)
        
        self.canvas_TelaEscolheTamanho.tag_bind(self.bt_3A4_mm_TelaEscolheTamanho.objRec, '<ButtonPress-1>', self.onBotao3A4_TelaEscolheTamanho)
        self.canvas_TelaEscolheTamanho.tag_bind(self.bt_3A4_mm_TelaEscolheTamanho.objText, '<ButtonPress-1>', self.onBotao3A4_TelaEscolheTamanho)
        
        self.canvas_TelaEscolheTamanho.tag_bind(self.bt_material_especial_TelaEscolheTamanho.objRec, '<ButtonPress-1>', self.onBotaoMaterialEspecial_TelaEscolheTamanho)
        self.canvas_TelaEscolheTamanho.tag_bind(self.bt_material_especial_TelaEscolheTamanho.objText, '<ButtonPress-1>', self.onBotaoMaterialEspecial_TelaEscolheTamanho)
        
        self.canvas_TelaEscolheTamanho.pack()
        self.frame_TelaEscolheTamanho.pack()

    def onBotao1A2_TelaEscolheTamanho(self, event):
        self.dado_TelaEscolheTamanho.aciona_buzzer = True

    def onBotao3A4_TelaEscolheTamanho(self, event):
        self.dado_TelaEscolheTamanho.aciona_buzzer = True

    def onBotaoMaterialEspecial_TelaEscolheTamanho(self, event):
        self.dado_TelaEscolheTamanho.aciona_buzzer = True

    def destroy_TelaEscolheTamanho(self):
        self.frame_TelaEscolheTamanho.destroy()
        self.canvas_TelaEscolheTamanho.destroy()

class TelaEscolheReagente:
    def __init__(self, tk_inter_TelaEscolheReagente, dado_TelaEscolheReagente):
        self.tk_inter_TelaEscolheReagente = tk_inter_TelaEscolheReagente
        self.frame_TelaEscolheReagente = 0
        self.dado_TelaEscolheReagente = dado_TelaEscolheReagente
        self.canvas_TelaEscolheReagente = 0
        #self.imagem_TelaEscolheReagente = tk.PhotoImage(file="img/Intro_back.png")

        self.bt_xilolTelaEscolheReagente = 0
        self.bt_isopropanolTelaEscolheReagente = 0
        self.bt_witclearTelaEscolheReagente = 0

        self.tk_inter_TelaEscolheReagente.title('Histo_V6')
        self.tk_inter_TelaEscolheReagente.config(cursor=self.dado_TelaEscolheReagente.cursor)
        self.tk_inter_TelaEscolheReagente.geometry("{0}x{1}+0+0".format(self.dado_TelaEscolheReagente.window_w, self.dado_TelaEscolheReagente.window_h))
        self.tk_inter_TelaEscolheReagente.overrideredirect(True)
        
    def iniciaTelaEscolheReagente(self):
        self.frame_TelaEscolheReagente = tk.Frame(self.tk_inter_TelaEscolheReagente)

        #adiciona área para desenho
        self.canvas_TelaEscolheReagente = tk.Canvas(self.tk_inter_TelaEscolheReagente, width=self.dado_TelaEscolheReagente.window_w, height=self.dado_TelaEscolheReagente.window_h, background=self.dado_TelaEscolheReagente.grey)
        #self.canvas_TelaPersonalizado.create_image(0,0,image=self.imagem_TelaPersonalizado, anchor='nw')
        
        self.bt_xilolTelaEscolheReagente = CriaBotao('XILOL',25 , 400, 72, 40, 16, self.dado_TelaEscolheReagente.green,self.canvas_TelaEscolheReagente, self.tk_inter_TelaEscolheReagente)
        self.bt_isopropanolTelaEscolheReagente = CriaBotao('ISOPROPANOL',25 , 400, 72, 40, 100, self.dado_TelaEscolheReagente.green,self.canvas_TelaEscolheReagente, self.tk_inter_TelaEscolheReagente)
        self.bt_witclearTelaEscolheReagente = CriaBotao('WITCLEAR',25 , 400, 72, 40, 184, self.dado_TelaEscolheReagente.green,self.canvas_TelaEscolheReagente, self.tk_inter_TelaEscolheReagente)
        
        #Associa o método no envento click
        self.canvas_TelaEscolheReagente.tag_bind(self.bt_xilolTelaEscolheReagente.objRec, '<ButtonPress-1>', self.onBotaoXilol_TelaEscolheReagente)
        self.canvas_TelaEscolheReagente.tag_bind(self.bt_xilolTelaEscolheReagente.objText, '<ButtonPress-1>', self.onBotaoXilol_TelaEscolheReagente)
        
        self.canvas_TelaEscolheReagente.tag_bind(self.bt_isopropanolTelaEscolheReagente.objRec, '<ButtonPress-1>', self.onBotaoIsopropanol_TelaEscolheReagente)
        self.canvas_TelaEscolheReagente.tag_bind(self.bt_isopropanolTelaEscolheReagente.objText, '<ButtonPress-1>', self.onBotaoIsopropanol_TelaEscolheReagente)
        
        self.canvas_TelaEscolheReagente.tag_bind(self.bt_witclearTelaEscolheReagente.objRec, '<ButtonPress-1>', self.onBotaoWitclear_TelaEscolheReagente)
        self.canvas_TelaEscolheReagente.tag_bind(self.bt_witclearTelaEscolheReagente.objText, '<ButtonPress-1>', self.onBotaoWitclear_TelaEscolheReagente)
        
        self.canvas_TelaEscolheReagente.pack()
        self.frame_TelaEscolheReagente.pack()

    def onBotaoXilol_TelaEscolheReagente(self, event):
        self.dado_TelaEscolheReagente.aciona_buzzer = True

    def onBotaoIsopropanol_TelaEscolheReagente(self, event):
        self.dado_TelaEscolheReagente.aciona_buzzer = True

    def onBotaoWitclear_TelaEscolheReagente(self, event):
        self.dado_TelaEscolheReagente.aciona_buzzer = True

    def destroy_TelaEscolheReagente(self):
        self.frame_TelaEscolheReagente.destroy()
        self.canvas_TelaEscolheReagente.destroy()

class TelaCompletaParametros:
    def __init__(self, tk_inter_TelaCompletaParametros, dado_TelaCompletaParametros):
        self.tk_inter_TelaCompletaParametros = tk_inter_TelaCompletaParametros
        self.frame_TelaCompletaParametros = 0
        self.dado_TelaCompletaParametros = dado_TelaCompletaParametros
        self.canvas_TelaCompletaParametros = 0
        #self.imagem_TelaCompletaParametros = tk.PhotoImage(file="img/Intro_back.png")

        self.bttx_erroTelaCompletaParametros = 0
        self.bttx_complete_todosTelaCompletaParametros = 0
        self.bttx_os_parametrosTelaCompletaParametros = 0
        self.bt_voltaTelaCompletaParametros = 0

        self.tk_inter_TelaCompletaParametros.title('Histo_V6')
        self.tk_inter_TelaCompletaParametros.config(cursor=self.dado_TelaCompletaParametros.cursor)
        self.tk_inter_TelaCompletaParametros.geometry("{0}x{1}+0+0".format(self.dado_TelaCompletaParametros.window_w, self.dado_TelaCompletaParametros.window_h))
        self.tk_inter_TelaCompletaParametros.overrideredirect(True)
        
    def iniciaTelaCompletaParametros(self):
        self.frame_TelaCompletaParametros = tk.Frame(self.tk_inter_TelaCompletaParametros)

        #adiciona área para desenho
        self.canvas_TelaCompletaParametros = tk.Canvas(self.tk_inter_TelaCompletaParametros, width=self.dado_TelaCompletaParametros.window_w, height=self.dado_TelaCompletaParametros.window_h, background=self.dado_TelaCompletaParametros.grey)
        #self.canvas_TelaPersonalizado.create_image(0,0,image=self.imagem_TelaPersonalizado, anchor='nw')
        
        self.bttx_erroTelaCompletaParametros = CriaBotao('ERRO!',25 , 400, 60, 40, 13, self.dado_TelaCompletaParametros.grey,self.canvas_TelaCompletaParametros, self.tk_inter_TelaCompletaParametros)
        self.bttx_complete_todosTelaCompletaParametros = CriaBotao('COMPLETE TODOS',25 , 400, 60, 40, 73, self.dado_TelaCompletaParametros.grey,self.canvas_TelaCompletaParametros, self.tk_inter_TelaCompletaParametros)
        self.bttx_os_parametrosTelaCompletaParametros = CriaBotao('OS PARAMETROS',25 , 400, 60, 40, 133, self.dado_TelaCompletaParametros.grey,self.canvas_TelaCompletaParametros, self.tk_inter_TelaCompletaParametros)
        self.bt_voltaTelaCompletaParametros = CriaBotao('<-',25 , 70, 60, 398, 200, self.dado_TelaCompletaParametros.green,self.canvas_TelaCompletaParametros, self.tk_inter_TelaCompletaParametros)
        
        #Associa o método no envento click
        self.canvas_TelaCompletaParametros.tag_bind(self.bt_voltaTelaCompletaParametros.objRec, '<ButtonPress-1>', self.onBotaoVoltar_TelaCompletaParametros)
        self.canvas_TelaCompletaParametros.tag_bind(self.bt_voltaTelaCompletaParametros.objText, '<ButtonPress-1>', self.onBotaoVoltar_TelaCompletaParametros)
        
        self.canvas_TelaCompletaParametros.pack()
        self.frame_TelaCompletaParametros.pack()

    def onBotaoVoltar_TelaCompletaParametros(self, event):
        self.dado_TelaCompletaParametros.aciona_buzzer = True

    def destroy_TelaCompletaParametros(self):
        self.frame_TelaCompletaParametros.destroy()
        self.canvas_TelaCompletaParametros.destroy()

class TelaProcessando:
    def __init__(self, tk_inter_TelaProcessando, dado_TelaProcessando):
        self.tk_inter_TelaProcessando = tk_inter_TelaProcessando
        self.frame_TelaProcessando = 0
        self.dado_TelaProcessando = dado_TelaProcessando
        self.canvas_TelaProcessando = 0
        #self.imagem_TelaProcessando = tk.PhotoImage(file="img/Intro_back.png")

        self.bttx_nome_processo_TelaProcessando = 0
        self.bttx_progresso_banho_TelaProcessando = 0
        self.bttx_fixacao_TelaProcessando = 0
        self.bttx_desidratacao_TelaProcessando = 0
        self.bttx_clarificacao_TelaProcessando = 0

        self.btind_primeira_fixacao_TelaProcessando = 0
        self.btind_segunda_fixacao_TelaProcessando = 0
        self.btind_primeira_desidratacao_TelaProcessando = 0
        self.btind_segunda_desidratacao_TelaProcessando = 0
        self.btind_terceira_desidratacao_TelaProcessando = 0
        self.btind_quarta_desidratacao_TelaProcessando = 0
        self.btind_quinta_desidratacao_TelaProcessando = 0
        self.btind_primeira_clarificacao_TelaProcessando = 0
        self.btind_segunda_clarificacao_TelaProcessando = 0
        self.btind_terceira_clarificacao_TelaProcessando = 0

        self.bt_cancelar_TelaProcessando = 0
        self.bt_iniciar_TelaProcessando = 0

        self.tk_inter_TelaProcessando.title('Histo_V6')
        self.tk_inter_TelaProcessando.config(cursor=self.dado_TelaProcessando.cursor)
        self.tk_inter_TelaProcessando.geometry("{0}x{1}+0+0".format(self.dado_TelaProcessando.window_w, self.dado_TelaProcessando.window_h))
        self.tk_inter_TelaProcessando.overrideredirect(True)
        
    def iniciaTelaProcessando(self):
        self.frame_TelaProcessando = tk.Frame(self.tk_inter_TelaProcessando)

        #adiciona área para desenho
        self.canvas_TelaProcessando = tk.Canvas(self.tk_inter_TelaProcessando, width=self.dado_TelaProcessando.window_w, height=self.dado_TelaProcessando.window_h, background=self.dado_TelaProcessando.grey)
        
        self.bttx_nome_processo_TelaProcessando = CriaBotao(self.dado_TelaProcessando.texto_nome_do_processo,25 , 432, 42, 24, 13, self.dado_TelaProcessando.grey,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.bttx_progresso_banho_TelaProcessando = CriaBotao(self.dado_TelaProcessando.texto_percento_progresso_banho,25 , 432, 42, 24, 59, self.dado_TelaProcessando.grey,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.bttx_fixacao_TelaProcessando = CriaBotao("FIXAÇÃO",16 , 161, 22, 46, 113, self.dado_TelaProcessando.grey,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.bttx_desidratacao_TelaProcessando = CriaBotao("DESIDRATAÇÃO",16 , 161, 22, 46, 140, self.dado_TelaProcessando.grey,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.bttx_clarificacao_TelaProcessando = CriaBotao("CLARIFICAÇÃO",16 , 161, 22, 46, 167, self.dado_TelaProcessando.grey,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)

        self.btind_primeira_fixacao_TelaProcessando =       CriaBotao("",16 , 16, 16, 240, 116, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_segunda_fixacao_TelaProcessando =        CriaBotao("",16 , 16, 16, 265, 116, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_primeira_desidratacao_TelaProcessando =  CriaBotao("",16 , 16, 16, 240, 143, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_segunda_desidratacao_TelaProcessando =   CriaBotao("",16 , 16, 16, 265, 143, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_terceira_desidratacao_TelaProcessando =  CriaBotao("",16 , 16, 16, 290, 143, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_quarta_desidratacao_TelaProcessando =    CriaBotao("",16 , 16, 16, 315, 143, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_quinta_desidratacao_TelaProcessando =    CriaBotao("",16 , 16, 16, 341, 143, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_primeira_clarificacao_TelaProcessando =  CriaBotao("",16 , 16, 16, 240, 170, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_segunda_clarificacao_TelaProcessando =   CriaBotao("",16 , 16, 16, 265, 170, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.btind_terceira_clarificacao_TelaProcessando =  CriaBotao("",16 , 16, 16, 290, 170, self.dado_TelaProcessando.cor_indicacao_processo,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        
        self.bt_cancelar_TelaProcessando = CriaBotao("CANCELAR",16 , 145, 60, 13, 203, self.dado_TelaProcessando.green,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        self.bt_iniciar_TelaProcessando =  CriaBotao(self.dado_TelaProcessando.texto_iniciar_pausar,16 , 145, 60, 323, 203, self.dado_TelaProcessando.green,self.canvas_TelaProcessando, self.tk_inter_TelaProcessando)
        
        #Associa o método no envento click
        self.canvas_TelaProcessando.tag_bind(self.bt_cancelar_TelaProcessando.objRec, '<ButtonPress-1>', self.onBotaoCancelar_TelaProcessando)
        self.canvas_TelaProcessando.tag_bind(self.bt_cancelar_TelaProcessando.objText, '<ButtonPress-1>', self.onBotaoCancelar_TelaProcessando)
        
        self.canvas_TelaProcessando.tag_bind(self.bt_iniciar_TelaProcessando.objRec, '<ButtonPress-1>', self.onBotaoInicar_TelaProcessando)
        self.canvas_TelaProcessando.tag_bind(self.bt_iniciar_TelaProcessando.objText, '<ButtonPress-1>', self.onBotaoInicar_TelaProcessando)
        
        self.canvas_TelaProcessando.pack()
        self.frame_TelaProcessando.pack()

    def onBotaoCancelar_TelaProcessando(self, event):
        self.dado_TelaProcessando.aciona_buzzer = True

    def onBotaoInicar_TelaProcessando(self, event):
        self.dado_TelaProcessando.aciona_buzzer = True

    def destroy_TelaProcessando(self):
        self.frame_TelaProcessando.destroy()
        self.canvas_TelaProcessando.destroy()

class TelaTrocaBanho:
    def __init__(self, tk_inter_TelaTrocaBanho, dado_TelaTrocaBanho):
        self.tk_inter_TelaTrocaBanho = tk_inter_TelaTrocaBanho
        self.frame_TelaTrocaBanho = 0
        self.dado_TelaTrocaBanho = dado_TelaTrocaBanho
        self.canvas_TelaTrocaBanho = 0
        #self.imagem_TelaTrocaBanho = tk.PhotoImage(file="img/Intro_back.png")

        self.bttx_insira_mateiral_TelaTrocaBanho = 0
        self.bttx_contendo_reagente_TelaTrocaBanho = 0
        self.bttx_pressione_ok_TelaTrocaBanho = 0
        self.bttx_reagente_TelaTrocaBanho = 0
        self.bt_ok_TelaTrocaBanho = 0

        self.tk_inter_TelaTrocaBanho.title('Histo_V6')
        self.tk_inter_TelaTrocaBanho.config(cursor=self.dado_TelaTrocaBanho.cursor)
        self.tk_inter_TelaTrocaBanho.geometry("{0}x{1}+0+0".format(self.dado_TelaTrocaBanho.window_w, self.dado_TelaTrocaBanho.window_h))
        self.tk_inter_TelaTrocaBanho.overrideredirect(True)
        
    def iniciaTelaTrocaBanho(self):
        self.frame_TelaTrocaBanho = tk.Frame(self.tk_inter_TelaTrocaBanho)

        #adiciona área para desenho
        self.canvas_TelaTrocaBanho = tk.Canvas(self.tk_inter_TelaTrocaBanho, width=self.dado_TelaTrocaBanho.window_w, height=self.dado_TelaTrocaBanho.window_h, background=self.dado_TelaTrocaBanho.grey)
        
        self.bttx_insira_mateiral_TelaTrocaBanho =   CriaBotao('INSIRA O MATERIAL',16 , 200, 20, 140, 18, self.dado_TelaTrocaBanho.grey,self.canvas_TelaTrocaBanho, self.tk_inter_TelaTrocaBanho)
        self.bttx_contendo_reagente_TelaTrocaBanho = CriaBotao('CONTENDO O REAGENTE',16 , 200, 20, 140, 46, self.dado_TelaTrocaBanho.grey,self.canvas_TelaTrocaBanho, self.tk_inter_TelaTrocaBanho)
        self.bttx_pressione_ok_TelaTrocaBanho =      CriaBotao('E PRESSIONE OK',16 , 200, 20, 140, 74, self.dado_TelaTrocaBanho.grey,self.canvas_TelaTrocaBanho, self.tk_inter_TelaTrocaBanho)
        self.bttx_reagente_TelaTrocaBanho =          CriaBotao(self.dado_TelaTrocaBanho.nome_proximo_reagente,36 , 300, 42, 90, 115, self.dado_TelaTrocaBanho.grey,self.canvas_TelaTrocaBanho, self.tk_inter_TelaTrocaBanho)
        self.bt_ok_TelaTrocaBanho = CriaBotao('OK',36 , 145, 60, 167, 186, self.dado_TelaTrocaBanho.green,self.canvas_TelaTrocaBanho, self.tk_inter_TelaTrocaBanho)

        #Associa o método no envento click
        self.canvas_TelaTrocaBanho.tag_bind(self.bt_ok_TelaTrocaBanho.objRec, '<ButtonPress-1>', self.onBotaoOk_TelaTrocaBanho)
        self.canvas_TelaTrocaBanho.tag_bind(self.bt_ok_TelaTrocaBanho.objText, '<ButtonPress-1>', self.onBotaoOk_TelaTrocaBanho)
        
        self.canvas_TelaTrocaBanho.pack()
        self.frame_TelaTrocaBanho.pack()
    
    def onBotaoOk_TelaTrocaBanho(self, event):
        self.dado_TelaTrocaBanho.aciona_buzzer = True

    def destroy_TelaTrocaBanho(self):
        self.frame_TelaTrocaBanho.destroy()
        self.canvas_TelaTrocaBanho.destroy()

class TelaConfirmaCancelamento:
    def __init__(self, tk_inter_TelaConfirmaCancelamento, dado_TelaConfirmaCancelamento):
        self.tk_inter_TelaConfirmaCancelamento= tk_inter_TelaConfirmaCancelamento
        self.frame_TelaConfirmaCancelamento= 0
        self.dado_TelaConfirmaCancelamento= dado_TelaConfirmaCancelamento
        self.canvas_TelaConfirmaCancelamento= 0
        #self.imagem_TelaConfirmaCancelamento= tk.PhotoImage(file="img/Intro_back.png")

        self.bttx_tem_certeza_TelaConfirmaCancelamento= 0
        self.bttx_deseja_cancelar_TelaConfirmaCancelamento= 0
        self.bt_sim_TelaConfirmaCancelamento= 0
        self.bt_nao_TelaConfirmaCancelamento= 0

        self.tk_inter_TelaConfirmaCancelamento.title('Histo_V6')
        self.tk_inter_TelaConfirmaCancelamento.config(cursor=self.dado_TelaConfirmaCancelamento.cursor)
        self.tk_inter_TelaConfirmaCancelamento.geometry("{0}x{1}+0+0".format(self.dado_TelaConfirmaCancelamento.window_w, self.dado_TelaConfirmaCancelamento.window_h))
        self.tk_inter_TelaConfirmaCancelamento.overrideredirect(True)
        
    def inicia_TelaConfirmaCancelamento(self):
        self.frame_TelaConfirmaCancelamento= tk.Frame(self.tk_inter_TelaConfirmaCancelamento)

        #adiciona área para desenho
        self.canvas_TelaConfirmaCancelamento= tk.Canvas(self.tk_inter_TelaConfirmaCancelamento, width=self.dado_TelaConfirmaCancelamento.window_w, height=self.dado_TelaConfirmaCancelamento.window_h, background=self.dado_TelaConfirmaCancelamento.grey)
        
        self.bttx_tem_certeza_TelaConfirmaCancelamento= CriaBotao('TEM CERTEZA',24 , 350, 40, 65, 19, self.dado_TelaConfirmaCancelamento.grey,self.canvas_TelaConfirmaCancelamento, self.tk_inter_TelaConfirmaCancelamento)
        self.bttx_deseja_cancelar_TelaConfirmaCancelamento= CriaBotao('QUE DESEJA CANCELAR?',24 , 350, 40, 65, 75, self.dado_TelaConfirmaCancelamento.grey,self.canvas_TelaConfirmaCancelamento, self.tk_inter_TelaConfirmaCancelamento)
        self.bt_sim_TelaConfirmaCancelamento= CriaBotao('SIM',24 , 145, 60, 18, 165, self.dado_TelaConfirmaCancelamento.green,self.canvas_TelaConfirmaCancelamento, self.tk_inter_TelaConfirmaCancelamento)
        self.bt_nao_TelaConfirmaCancelamento= CriaBotao('NÃO',24 , 145, 60, 322, 165, self.dado_TelaConfirmaCancelamento.green,self.canvas_TelaConfirmaCancelamento, self.tk_inter_TelaConfirmaCancelamento)

        #Associa o método no envento click
        self.canvas_TelaConfirmaCancelamento.tag_bind(self.bt_sim_TelaConfirmaCancelamento.objRec, '<ButtonPress-1>', self.onBotaoSim_TelaConfirmaCancelamento)
        self.canvas_TelaConfirmaCancelamento.tag_bind(self.bt_sim_TelaConfirmaCancelamento.objText, '<ButtonPress-1>', self.onBotaoSim_TelaConfirmaCancelamento)
        
        self.canvas_TelaConfirmaCancelamento.tag_bind(self.bt_nao_TelaConfirmaCancelamento.objRec, '<ButtonPress-1>', self.onBotaoNao_TelaConfirmaCancelamento)
        self.canvas_TelaConfirmaCancelamento.tag_bind(self.bt_nao_TelaConfirmaCancelamento.objText, '<ButtonPress-1>', self.onBotaoNao_TelaConfirmaCancelamento)
        
        self.canvas_TelaConfirmaCancelamento.pack()
        self.frame_TelaConfirmaCancelamento.pack()

    def destroy_TelaConfirmaCancelamento(self):
        self.frame_TelaConfirmaCancelamento.destroy()
        self.canvas_TelaConfirmaCancelamento.destroy()

    def onBotaoSim_TelaConfirmaCancelamento(self, event):
        self.dado_TelaConfirmaCancelamento.aciona_buzzer = True

    def onBotaoNao_TelaConfirmaCancelamento(self, event):
        self.dado_TelaConfirmaCancelamento.aciona_buzzer = True

class TelaAvisoErro:
    def __init__(self, tk_inter_TelaAvisoErro, dado_TelaAvisoErro):
        self.tk_inter_TelaAvisoErro = tk_inter_TelaAvisoErro
        self.frame_TelaAvisoErro = 0
        self.dado_TelaAvisoErro = dado_TelaAvisoErro
        self.canvas_TelaAvisoErro = 0

        self.bttx_texto_linha1_TelaAvisoErro = 0
        self.bttx_texto_linha2_TelaAvisoErro = 0
        self.bttx_texto_linha3_TelaAvisoErro = 0
        self.bttx_texto_linha4_TelaAvisoErro = 0

        self.tk_inter_TelaAvisoErro.title('Histo_V6')
        self.tk_inter_TelaAvisoErro.config(cursor=self.dado_TelaAvisoErro.cursor)
        self.tk_inter_TelaAvisoErro.geometry("{0}x{1}+0+0".format(self.dado_TelaAvisoErro.window_w, self.dado_TelaAvisoErro.window_h))
        self.tk_inter_TelaAvisoErro.overrideredirect(True)
        
    def iniciaTelaAvisoErro(self):
        self.frame_TelaAvisoErro = tk.Frame(self.tk_inter_TelaAvisoErro)

        #adiciona área para desenho
        self.canvas_TelaAvisoErro = tk.Canvas(self.tk_inter_TelaAvisoErro, width=self.dado_TelaAvisoErro.window_w, height=self.dado_TelaAvisoErro.window_h, background=self.dado_TelaAvisoErro.grey)
        
        self.bttx_texto_linha1_TelaAvisoErro = CriaBotao('ERRO SISTEMA!',16 , 200, 20, 140, 18, self.dado_TelaAvisoErro.grey,self.canvas_TelaAvisoErro, self.tk_inter_TelaAvisoErro)
        self.bttx_texto_linha2_TelaAvisoErro = CriaBotao('DESLIGAR POR',16 , 200, 20, 140, 46, self.dado_TelaAvisoErro.grey,self.canvas_TelaAvisoErro, self.tk_inter_TelaAvisoErro)
        self.bttx_texto_linha3_TelaAvisoErro = CriaBotao('10 SEGUNDOS',16 , 200, 20, 140, 74, self.dado_TelaAvisoErro.grey,self.canvas_TelaAvisoErro, self.tk_inter_TelaAvisoErro)
        self.bttx_texto_linha4_TelaAvisoErro = CriaBotao('E RELIGAR EQUIPAMENTO.',16 , 300, 42, 90, 115, self.dado_TelaAvisoErro.grey,self.canvas_TelaAvisoErro, self.tk_inter_TelaAvisoErro)
        
        
        self.canvas_TelaAvisoErro.pack()
        self.frame_TelaAvisoErro.pack()

    def destroy_TelaAvisoErro(self):
        self.frame_TelaAvisoErro.destroy()
        self.canvas_TelaAvisoErro.destroy()

class TelaFinalProcesso:
    def __init__(self, tk_inter_TelaFinalProcesso, dado_TelaFinalProcesso):
        self.tk_inter_TelaFinalProcesso= tk_inter_TelaFinalProcesso
        self.frame_TelaFinalProcesso= 0
        self.dado_TelaFinalProcesso= dado_TelaFinalProcesso
        self.canvas_TelaFinalProcesso= 0
        #self.imagem_TelaFinalProcesso= tk.PhotoImage(file="img/Intro_back.png")

        self.bttx_processamento_TelaFinalProcesso= 0
        self.bttx_finalizado_TelaFinalProcesso= 0
        self.bt_ok_TelaFinalProcesso= 0

        self.tk_inter_TelaFinalProcesso.title('Histo_V6')
        self.tk_inter_TelaFinalProcesso.config(cursor=self.dado_TelaFinalProcesso.cursor)
        self.tk_inter_TelaFinalProcesso.geometry("{0}x{1}+0+0".format(self.dado_TelaFinalProcesso.window_w, self.dado_TelaFinalProcesso.window_h))
        self.tk_inter_TelaFinalProcesso.overrideredirect(True)
        
    def inicia_TelaFinalProcesso(self):
        self.frame_TelaFinalProcesso= tk.Frame(self.tk_inter_TelaFinalProcesso)

        #adiciona área para desenho
        self.canvas_TelaFinalProcesso= tk.Canvas(self.tk_inter_TelaFinalProcesso, width=self.dado_TelaFinalProcesso.window_w, height=self.dado_TelaFinalProcesso.window_h, background=self.dado_TelaFinalProcesso.grey)
        
        self.bttx_processamento_TelaFinalProcesso= CriaBotao('PROCESSAMENTO',36 , 377, 44, 51, 10, self.dado_TelaFinalProcesso.grey,self.canvas_TelaFinalProcesso, self.tk_inter_TelaFinalProcesso)
        self.bttx_finalizado_TelaFinalProcesso= CriaBotao('FINALIZADO',36 , 377, 44, 51, 63, self.dado_TelaFinalProcesso.grey,self.canvas_TelaFinalProcesso, self.tk_inter_TelaFinalProcesso)
        self.bt_ok_TelaFinalProcesso= CriaBotao('OK',24 , 145, 60, 167, 165, self.dado_TelaFinalProcesso.green,self.canvas_TelaFinalProcesso, self.tk_inter_TelaFinalProcesso)
        
        #Associa o método no envento click
        self.canvas_TelaFinalProcesso.tag_bind(self.bt_ok_TelaFinalProcesso.objRec, '<ButtonPress-1>', self.onBotaoOk_TelaFinalProcesso)
        self.canvas_TelaFinalProcesso.tag_bind(self.bt_ok_TelaFinalProcesso.objText, '<ButtonPress-1>', self.onBotaoOk_TelaFinalProcesso)
        
        self.canvas_TelaFinalProcesso.pack()
        self.frame_TelaFinalProcesso.pack()

    def destroy_TelaFinalProcesso(self):
        self.frame_TelaFinalProcesso.destroy()
        self.canvas_TelaFinalProcesso.destroy()

    def onBotaoOk_TelaFinalProcesso(self, event):
        self.dado_TelaFinalProcesso.aciona_buzzer = True

class CriaBotao:
    def __init__(self, texto, fonte, w_botao, h_botao, x_init, y_init, cor_botao, canvas, tk_inter):
        
        #Coordenadas de botões
        self.texto = texto
        self.fonte = fonte
        self.altura = h_botao
        self.largura = w_botao
        
        self.x_init = x_init
        self.y_init = y_init
        
        self.cor_botao = cor_botao
        self.canvas = canvas
        self.tk_inter = tk_inter
        
        self.x_fim = self.largura + self.x_init
        self.y_fim = self.altura + self.y_init
        
        self.texto_x = self.x_init + (self.largura/2)
        self.texto_y = self.y_init + (self.altura/2)
        
        self.objRec = 0
        self.objText = 0

        #Desenha Botão
        self.desenha_botao()
        
    def desenha_botao(self):
        self.objRec = self.canvas.create_rectangle(self.x_init, self.y_init, self.x_fim, self.y_fim, fill=self.cor_botao, width=0, tags='objt1Tag')
        self.objText = self.canvas.create_text(self.texto_x, self.texto_y, text=self.texto, fill='black', font=('Helvetica', self.fonte, 'bold') )
import tkinter as tk

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

    def onBotaoOk_TelaFinalProcesso(self):
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

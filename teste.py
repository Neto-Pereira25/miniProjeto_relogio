from modulos import *

import pyglet # Após baixar a biblioteca colocamos o código abaixo
pyglet.font.add_file("digital-7.ttf") # permite adicionar fontes extras no Tkinter

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR')
except:
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')


class Watch():
    def __init__(self):
        self.janela = Tk() # cria a janela
        self.tela()
        self.frames_tela()
        self.janela.mainloop()
        
    def tela(self):
        self.janela.title("Relógio Digital") # cria o título da janela
        self.janela.geometry("440x180") # diz as dimensões da janela
        self.janela.resizable(width = False, height = False) # impede a alteração das dimensões
        self.janela.configure(bg = cor1) # define a cor do fundo da janela

    def frames_tela(self):
        # Criando a label do relógio(hora) para definir a posição da hora na janela
        self.l1 = Label(self.janela, text = "", font = ("digital-7 100"), bg = fundo, fg = cor)
        self.l1.grid(row = 0, column = 0, sticky = NW, padx = 5)

        # Criando a label do dia da semana para definir a posição do Dia na janela
        self.l2 = Label(self.janela, text = "", font = ("digital-7 17"), bg = fundo, fg = cor)
        self.l2.grid(row = 1, column = 0, sticky = NW, padx = 5)

        self.relogio() # Chamada da função relógio para poder aparecer na janela com a hora da máquina

    def relogio(self):
        self.tempo = datetime.now() # criei uma variável para guardar o tempo da minha máquina

        self.hora = self.tempo.strftime("%H:%M:%S") # criei uma variável para obter a hora da minha máquina
        self.dia_semana = self.tempo.strftime("%A")# criei uma variável para obter o dia da semana (segunda, terça...)
        self.dia = self.tempo.day # criei uma variável para obter o dia do mês
        self.mes = self.tempo.strftime("%b") # criei uma variável para obter o mês
        self.ano = self.tempo.strftime("%Y") # criei uma variável para obter o ano
        
        self.l1.config(text=self.hora) # fazendo a hora da máquina sair na label l1 criada na janela
        self.l1.after(200, self.relogio) # aqui estamos passando o relógio de estático para dinâmico em que a cada 200 milesimos ele vai chamar a função novamente e executar
        self.l2.config(text=self.dia_semana + " " + str(self.dia) + "/" + str(self.mes) + "/" + str(self.ano)) # fazendo dia, mês e ano da máquina sairem na label l2 criada na janela


Watch()

from turtle import Turtle
FONT = ("Arial", 16, "normal")
ALIGN = "center"

class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.pontos = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.atualiza_tela()
        self.hideturtle()

    def ganha_ponto(self):
        self.pontos += 1
        self.atualiza_tela()

    def fim_de_jogo(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def atualiza_tela(self):
        self.clear()
        self.write(f"Pontos: {self.pontos}", align=ALIGN, font=FONT)

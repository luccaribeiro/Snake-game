from turtle import Turtle

POSICOES_INICIAIS = [(0,0), (-20,0), (-40,0)]
DISTANCIA_MOVIMENTO = 20
CIMA = 90
BAIXO = 270
DIREITA = 0
ESQUERDA = 180

class Snake:

    def __init__(self):
        self.posicoes = []
        self.create_snake()
        self.head = self.posicoes[0]

    def create_snake(self):
        for posicao in POSICOES_INICIAIS:
            self.add_posicao(posicao)

    def add_posicao(self, posicao):
        parte_cobra = Turtle("square")
        parte_cobra.color("white")
        parte_cobra.penup()
        parte_cobra.goto(posicao)
        self.posicoes.append(parte_cobra)

    def extend(self):
        self.add_posicao(self.posicoes[-1].position())

    def move(self):
        for segmento in range(len(self.posicoes)-1,0,-1):
            new_x = self.posicoes[segmento-1].xcor()
            new_y = self.posicoes[segmento-1].ycor()
            self.posicoes[segmento].goto(new_x,new_y)
        self.posicoes[0].forward(DISTANCIA_MOVIMENTO)

    def up(self):
        if self.head.heading() != BAIXO:
            self.head.setheading(CIMA)

    def down(self):
        if self.head.heading() != CIMA:
            self.head.setheading(BAIXO)

    def right(self):
        if self.head.heading() != ESQUERDA:
            self.head.setheading(DIREITA)

    def left(self):
        if self.head.heading() != DIREITA:
            self.head.setheading(ESQUERDA)

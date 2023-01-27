from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Placar

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Snake Game")
tela.tracer(0)

snake = Snake()
comida = Food()
placar = Placar()

tela.listen()
tela.onkey(snake.up, "Up")
tela.onkey(snake.down, "Down")
tela.onkey(snake.left, "Left")
tela.onkey(snake.right, "Right")


game = True
while game:
    tela.update()
    sleep(0.1)
    snake.move()

    # DETECTANDO COLISÃO COMIDA
    if snake.head.distance(comida) < 15:
        comida.atualiza()
        snake.extend()
        placar.ganha_ponto()

    # DETECTANDO COLISÃO PAREDE
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        placar.fim_de_jogo()

    # DETECTANDO COLISÃO CAUDA
    for posicao in snake.posicoes[1:]:
        if snake.head.distance(posicao) < 10:
            game = False
            placar.fim_de_jogo()


tela.exitonclick()

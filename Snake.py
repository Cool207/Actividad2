"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import random
lista=["purple", "orange", "blue", "gray", "green"]
s=random.choice(lista)
c=random.choice(lista)

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def dentro_pantalla(food):
    x = food.x
    y = food.y
    
    if -190 < x < 190 and -190 < y < 190:
        return True
    else:
        return False
    

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        
        #Verificar que la comida no se quede en el mismo lugar
        cambio_x = randrange(-1,2) * 10
        while cambio_x == 0:
            cambio_x = randrange(-1,2) * 10

        cambio_y = randrange(-1,2) * 10
        while cambio_y == 0:
            cambio_y = randrange(-1,2) * 10
        
        food.x = food.x + cambio_x 
        print (food.x)
        food.y = food.y + cambio_y
        print (food.y)
        
        # verificar que la comida esté dentro de la pantalla
        while (dentro_pantalla(food)) == False:
            food.x = food.x + randrange(-1,1) * 10
            food.y = food.y + randrange(-1,1) * 10
            
    else:
        snake.pop(0)

    clear()
    
    for body in snake:
        
        square(body.x, body.y, 9, s)

    square(food.x, food.y, 9, c)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()


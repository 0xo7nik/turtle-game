from turtle import *
from random import *
tsize = 20
s_width = 200
s_height = 180
class Sprite(Turtle):
    def __init__(self, x, y, step, shape, color):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

total_score = 0
player = Sprite(0, -100, 10, 'circle', 'orange')

enemy1 = Sprite(-s_width, 0, 15, 'square', 'red')
enemy1.set_move(-s_width, 0, s_width, 0)

enemy2 = Sprite(s_width, 70, 15, 'square', 'red')
enemy2.set_move(s_width, 70, -s_width, 70)

enemy3 = Sprite(-s_width, 130, 15, 'square', 'red')
enemy3.set_move(-s_width, 130, s_width, 130)

enemy4 = Sprite(s_width, 160, 15, 'square', 'red')
enemy4.set_move(s_width, 160, -s_width, 160)

enemy5 = Sprite(-s_width, 200, 15, 'square', 'red')
enemy5.set_move(-s_width, 200, s_width, 200)

t1 = Turtle()
t1.pensize(10)
t1.ht()

t2 = Turtle()
t2.pensize(10)
t2.ht()

t3 = Turtle()
t3.pensize(10)
t3.ht()

t4 = Turtle()
t4.pensize(10)
t4.color('brown')
t4.ht()

goal = Sprite(0, 120, 20, 'triangle', 'green')
goal.set_move(-s_width, 120, s_width, 120)

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')
a = 100
while total_score < 5:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    enemy4.make_step()
    enemy5.make_step()
    goal.make_step()
    t1.ht()
    t2.ht()
    
    if player.is_collide(goal):
        total_score += 1
        player.goto(0, -100)
        t3.color('purple')
        t3.penup()
        t3.goto(200, a)
        a -= 50
        t3.pendown()
        t3.write(total_score, font = ('Calibri', 28, 'bold'))
    if player.is_collide(enemy1) or player.is_collide(enemy2) or player.is_collide(enemy3) or player.is_collide(enemy4) or player.is_collide(enemy5):
        goal.ht()
        break

if total_score == 5:
    enemy1.ht()
    enemy2.ht()
    enemy3.ht()
    enemy4.ht()
    enemy5.ht()
    goal.ht()
    player.ht()
    t2.penup()
    t2.goto(-50, 0)
    t2.pendown()
    t2.color('green')
    t2.write('You win!', font = ('Calibri', 20, 'bold'))

if total_score != 5:
    enemy1.ht()
    enemy2.ht()
    enemy3.ht()
    enemy4.ht()
    enemy5.ht()
    goal.ht()
    player.ht()
    t1.penup()
    t1.goto(-50, 0)
    t1.pendown()
    t1.color('red')
    t4.write('You lose!', font = ('Calibri', 20, 'bold'))

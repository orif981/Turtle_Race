from turtle import Screen,Turtle
from random import randint

t1=Turtle()
t2=Turtle()
t3=Turtle()
t4=Turtle()
t5=Turtle()
t1.color("deep sky blue")
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
t2.color("red")
t3.color("spring green")
t4.color("slate blue")
t5.color("olive")
t1.pu()
t2.pu()
t3.pu()
t4.pu()
t5.pu()
screen=Screen()
screen.setup(1000,400)
t1.goto(-450,150)
t2.goto(-450,30)
t3.goto(-450,-90)
t4.goto(-450,90)
t5.goto(-450,-30)
bet=screen.textinput("Make a bet","Which turtle will win the race? enter a color(cyan/red/lime/purple/olive): ")\
    .lower()
if bet=="deep sky blue": bet="cyan"
if bet=="spring green": bet=='lime'
if bet=="slate blue":bet=='purple'
while t1.xcor()<480 or t2.xcor()<480 or t3.xcor()<480 or t4.xcor()<480 or t5.xcor()<480:
    t1.forward(randint(1,12))
    t2.forward(randint(1, 12))
    t3.forward(randint(1, 12))
    t4.forward(randint(1, 12))
    t5.forward(randint(1, 12))
    if t1.xcor()>470:
        winner='cyan'
        break
    if t2.xcor()>470:
        winner='red'
        break
    if t3.xcor()>470:
        winner='lime'
        break
    if t4.xcor()>470:
        winner='purple'
        break
    if t5.xcor()>470:
        winner='olive'
        break
t1.goto(500,150)
t2.goto(500,30)
t3.goto(500,-90)
t4.goto(500,90)
t5.goto(500,-30)
if winner==bet: print("You won!")
else: print(f"You lost.. The {winner} turtle is the winner.")

screen.exitonclick()

if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

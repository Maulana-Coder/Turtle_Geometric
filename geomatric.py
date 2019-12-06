import turtle


colors = ["red","orange","yellow","green","blue","purple"]

turtle.title("Geometric Shape - Maulana ID")
turtle.bgcolor("black")


a = turtle.Pen()
for x in range(360):
    a.pencolor(colors[x % 6])
    a.width(x/100+1)
    a.forward(x)
    a.left(61)


def credits():
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-580, 200)
    turtle.write("  Created\nBy Maulana ID", font=("Consolas", 10, "bold",))
    turtle.penup()
    turtle.hideturtle()
credits()

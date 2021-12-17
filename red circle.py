import turtle 

lotus = turtle.Turtle()
lotus.speed(1280)
lotus.pencolor("white")

for i in range(180):
    lotus.forward(100)
    lotus.right(30)
    lotus.forward(20)      
    lotus.left(60)
    lotus.forward(50)
    lotus.right(30)

    lotus.pencolor("red")
    
    lotus.penup()
    lotus.setposition(0, 0)
    lotus.pendown()
    
    lotus.right(2)
    
turtle.done()
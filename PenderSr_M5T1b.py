def main():
    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()
    
    t.pensize(4)            # increase pensize (takes integer)
    t.pencolor('blue')       # set pencolor (takes string)
    t.shape('turtle')

    # Drawing first initial "A"

    t.left (70)
    t.forward (100)
    t.right (140)
    t.forward (100)
    t.right (180)
    t.penup()
    t.forward (40)
    t.left (70)
    t.pendown()
    t.forward (40)
    t.penup()
    t.right (140)
    t.penup()
    t.forward (90)

    #Drawing last initial "P"

    t.right (130)
    t.pendown()
    t.forward (95)
    t.left (180)
    t.penup()
    t.forward (95)
    t.pendown()
    t.right (90)
    t.forward (40)

    for a in range(3):
        t.right (45)
        t.forward (20)

    t.right(45)
    t.forward(40)
    t.penup()
    t.left(45)
    
    

main()

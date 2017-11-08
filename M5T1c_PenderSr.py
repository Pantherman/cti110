def main():

    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()

    t.pensize(2)
    t.pencolor('lightblue')
    t.shape('turtle')

    t.penup()
    t.backward(100)
    t.pendown()

    for a in range(6):
        for b in range(3):
            t.forward(100)
            t.right(90)
        t.right(30)
    t.left(30)
    for c in range(6):
        t.forward(100)
        t.right(60)
        for d in range(8):
            t.backward(20)
            t.right(45)
            t.forward(10)
main()

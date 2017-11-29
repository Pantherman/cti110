def main():

    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.shape('turtle')

    t.penup()
    t.backward(100)
    t.pendown()
    
    for a in range(8):
        for b in range(3):
            t.forward(100)
            t.right(90)
        t.right(45)
    t.left(45)
    for c in range(8):
        t.forward(100)
        t.right(45)
        for d in range(8):
            t.backward(100)
            t.right(45)
            t.forward(50)
            
    
main()

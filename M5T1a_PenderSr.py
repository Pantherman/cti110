def main():

    
    import turtle          # import turtle           
    win = turtle.Screen()  # turtle playground
    t = turtle.Turtle()    # assign variable to t

    t.pensize(3)           # thickness of pen
    t.pencolor('red')      # color of pen
    t.shape('turtle')      # shape of pen

    
# Outline shape of square
    for x in range(4):
        t.forward(100)
        t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()
    
# Outline shape of triangle
    for x in range(2):
       t.right(120)
       t.forward(100)
        

main()
    

    

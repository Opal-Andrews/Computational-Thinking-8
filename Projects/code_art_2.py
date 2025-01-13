import turtle

t = turtle.Turtle ()
t.speed(90)

#random triangle




t.pendown ()
t.begin_fill()
t.end_fill()
 
#part when the shape is made
color = ["blue","pink","purple"]
for i in range (80):
    t.forward (30 + i)
    t.left (30)
    t.color( color [i%3])

for i in range (30):
    t.forward (30)
    t.left (30 + 1)

t.setheading(90)

t.goto(100,0)




#End
turtle.exitonclick()
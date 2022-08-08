#golden spiral

import turtle
pp=turtle.Turtle()
p=turtle.getscreen()
p.bgcolor('black')
for x in range (500):
    pp.speed(0)
    pp.color('gold')
    pp.left(135.9)
    pp.fd(4*x)

turtle.mainloop()

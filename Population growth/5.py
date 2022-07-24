import turtle
turtle.speed(100)
i=1
while i<=7:
    turtle.circle(20*i)
    i+=1

r=7.5
a=185
turtle.color('white')
turtle.circle(180,60)
turtle.color('black')

for circles in range(13):
    if circles<7:
        turtle.right(90)
        turtle.circle(r)
        turtle.circle(r,a)
        turtle.right(90)
        r = r+8
        a = a+5
    elif circles>7:
        r=r-8
        a=a-5
        turtle.right(90)
        turtle.circle(r)
        turtle.circle(r,a)
        turtle.right(90)
    else:
        r=r-16
        a = a-10
        turtle.right(90)
        turtle.circle(r)
        turtle.circle(r,a)
        turtle.right(90)

turtle.done()
# I mostly found the values through trial and error, that is why it might seem random
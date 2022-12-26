from turtle import * 
color("black","red")
speed(0)

begin_fill()
left(90)
for i in range(4):
    forward(6)
    right(90)
    forward(6)
    left(90)
    forward(6)
    right(90)
end_fill()

canvas = getcanvas()
k = 0 
for x in range(-100,100):
    for y in range(-100,100):
        item = canvas.find_overlapping(x,y,x,y)
        if len(item) == 1 and item[0] == 5:
            k +=1
print(k)
done()
exit() 
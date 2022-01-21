def logo(pen,points):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.color("#fab104")  # Light Yellow
    pen.begin_fill()

    for i in range(1, len(points)):
        x, y = points[i]
        pen.goto(x, y)

    pen.end_fill()

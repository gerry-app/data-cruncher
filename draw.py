def flood_fill(screen, start_xcor, start_ycor, new_value, empty_value):
    coordinates_to_fill = set()
    coordinates_to_fill.add((start_xcor, start_ycor))
    while coordinates_to_fill:
        xcor, ycor = coordinates_to_fill.pop()
        if not screen.contains(xcor, ycor) or (screen.contains(xcor, ycor) and screen.get(xcor, ycor) != empty_value):
            continue
        screen.plot(xcor, ycor, new_value=new_value)
        coordinates_to_fill.add((xcor - 1, ycor))
        coordinates_to_fill.add((xcor + 1, ycor))
        coordinates_to_fill.add((xcor, ycor - 1))
        coordinates_to_fill.add((xcor, ycor + 1))
    return


def draw_line(screen, x0, y0, x1, y1):
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0

    x = x0
    y = y0

    a = 2 * (y1 - y0)
    b = -2 * (x1 - x0)

    if abs(x1 - x0) >= abs(y1 - y0):
        if a > 0:
            d = a + b / 2
            while x < x1:
                screen.plot(x, y)
                if d > 0:
                    y += 1
                    d += b
                x += 1
                d += a
            screen.plot(x1, y1)
        else:
            d = a - b / 2
            while x < x1:
                screen.plot(x, y)
                if d < 0:
                    y -= 1
                    d -= b
                x += 1
                d += a
            screen.plot(x1, y1)
    else:
        if a > 0:
            d = a / 2 + b
            while y < y1:
                screen.plot(x, y)
                if d < 0:
                    x += 1
                    d += a
                y += 1
                d += b
            screen.plot(x1, y1)
        else:
            d = a / 2 - b
            while y > y1:
                screen.plot(x, y)
                if d > 0:
                    x += 1
                    d += a
                y -= 1
                d -= b
            screen.plot(x1, y1)

import turtle

turty = turtle.Turtle()
my_window = turtle.Screen()


def draw(myTurtle, line_length=100, degrees_to_left=90, length_diminution=10, degrees_diminution=0):
    if line_length > 0:
        myTurtle.forward(line_length)
        myTurtle.left(degrees_to_left)
        draw(myTurtle, line_length=line_length - length_diminution,
            degrees_to_left=degrees_to_left - degrees_diminution,
            length_diminution=length_diminution,
            degrees_diminution=degrees_diminution)


if __name__ == '__main__':
    draw(turty, 250, 90, 5, 1)
    my_window.exitonclick()

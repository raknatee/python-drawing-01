from turtle import Screen, Turtle
from ironman_helmet import logo
from points import ankur1, ankur2, ankur3

def main():


        screen = Screen()
        screen.setup(500,600)
        screen.title("I AM IRONMAN")
        screen.bgcolor("#ba161e")

        my_turtle = Turtle()
        my_turtle.hideturtle()

        logo(my_turtle, ankur1)
        logo(my_turtle, ankur2)
        logo(my_turtle, ankur3)

        screen.mainloop()


main()

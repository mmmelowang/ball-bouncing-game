from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5) #stretch the length and width of the turtle to 100 and 20
        self.color("white")
        self.penup()
        self.goto(position)

# def create_paddle(self):
# self.paddle = Turtle.shape("square")
# self.shapesize(stretch_len=1, stretch_wid=5) #stretch the length and width of the turtle
# self.color("white")
# self.penup()
# self.goto(position_r)
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
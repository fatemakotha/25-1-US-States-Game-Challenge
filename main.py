import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Game")

image = "blank_states_img - Copy.gif"

screen.addshape(image) #adding a shape to turtle
turtle.shape(image) #using that shape

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

content = pandas.read_csv("50_states - Copy.csv")

states_list = content["state"].to_list()
print(states_list) #prints a list of all states
x_list = content["x"].to_list()
print(x_list) #prints a list of all x coordinates
y_list = content["y"].to_list()
print(y_list) #prints a list of all y coordinates

coordinate_list = []
for each_state in range(len(states_list)):
    tuple_coordinate = (x_list[each_state], y_list[each_state])
    coordinate_list.append(tuple_coordinate)
print(coordinate_list)
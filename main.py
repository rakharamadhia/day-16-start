# from turtle import Turtle, Screen
#
# joni = Turtle()
# print(joni)
# joni.shape("turtle")
# joni.color("DarkGoldenrod2")
# joni.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon name", "Type"]
table.add_row(["Greninja", "Green"])
table.add_row(["Charizard", "Fire"])
table.add_row(["Scolipede", "Bug"])
table.add_row(["Haxorus", "Dragon"])
table.add_row(["Mewtwo", "Psychic"])
table.align = "l"

print(table)

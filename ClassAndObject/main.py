# from turtle import Turtle, Screen
#
# vivek = Turtle()
# vivek.shape('turtle')
# vivek.color('green',)
# vivek.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Chamander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)



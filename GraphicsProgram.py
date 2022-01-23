import turtle
from GraphicsCommandClasses import *

class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]
    
    def __iter__(self):
        for c in self.items:
            yield c
            
def main():
    filename = input("Enter a drawing filename: ")
    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, "r")
    graphicsCommands = PyList()
    
    command_ = file.readline().strip()
    
    while command_ != " ":
        if command_ == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)
        
        elif command_ == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().split()
            cmd = CircleCommand(radius, width, color)
            
        elif command_ == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)
            
        elif command_ == "endfill":
            cmd = EndFillCommand()
            
        elif command_ == "penup":
            cmd = PenUpCommand()
            
        elif command_ == "pendown":
            cmd = PenDownCommand()
        
        else:
            raise RuntimeError("Unknown command: " + command_)
        
        graphicsCommands.append(cmd)
        command_ = file.readline().strip()
        
    for cmd in graphicsCommands:
        cmd.draw(t)
    
    file.close()
    t.ht()
    screen.exitonclick()
    print("Program execution completed!!!")

if __name__ == "__main__":
    main()


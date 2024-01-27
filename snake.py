import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

#Game Window
WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

#Center the Window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#Initialize Game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) #Snake's Head
food = Tile(10*TILE_SIZE, 10*TILE_SIZE) #Food
velocityX = 0
velocityY = 0

def change_direction(e):
    global velocityX, velocityY

    if(e.keysym == "Up"):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down"):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left"):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right"):
        velocityX = 1
        velocityY = 0

def move():
    global snake

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE 

def draw():
    global snake
    move()

    canvas.delete("all")

    #Draw Snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green")

    #Draw Food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "red")

    window.after(100, draw) # Call draw function after every 100 milliseconds

draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()
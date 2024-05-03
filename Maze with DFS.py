import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("The Maze")
wn.setup(700, 700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        if (move_to_x, move_to_y) in winningCord:
            turtle.write('You won!')

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        if (move_to_x, move_to_y) in winningCord:
            turtle.write('You won!', font=("Arial", 18, "normal"))

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = self.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        if (move_to_x, move_to_y) in winningCord:
            turtle.write('You won!')

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = self.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        if (move_to_x, move_to_y) in winningCord:
            turtle.write('You won!')

def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == end:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 'X' and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [(nx, ny)]))
    
    return None

def draw_path(path):
    pen.color("blue")
    for x, y in path:
        screen_x = -288 + (y * 24)
        screen_y = 288 - (x * 24)
        pen.goto(screen_x, screen_y)
        pen.stamp()

levels = [""]
level_1 = [
    "XXXXXXXXXXXXXXXXX",
    "XPX    X X       X",
    "X   XX           X",
    "X X X   XXXXXXXXXX",
    "X XXXX XX XXX  X X",
    "X X X  XXXX  XXX X",
    "X XXXX  XXXXX    X",
    "X X   X XXX  XXXXX",
    "X X XXX XX       X",
    "X   X X   XX     X",
    "XXXXXXXXXOXXXXXXXX"
]
levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "O":
                winningCord.append((screen_x, screen_y))

pen = Pen()
player = Player()
walls = []
winningCord = []

setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)

start_position = (1, 0)
end_position = (10, 9)

path = dfs(level_1, start_position, end_position)
if path:
    draw_path(path)
else:
    print("No path from start to end.")

while True:
    wn.update()

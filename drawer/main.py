from turtle import Screen, Turtle

#--------------- Constants -----------------#

SCREEN_WIDTH = 1605
SCREEN_HEIGHT = 1000
X_COR_WIDTH = int(SCREEN_WIDTH / 2)
Y_COR_HEIGHT = int(SCREEN_HEIGHT / 2)
SLEEP_TIMER = 0.1

#--------------- UI -----------------#

# Setup screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Stephanie's Test Drawer")
screen.bgcolor("black")
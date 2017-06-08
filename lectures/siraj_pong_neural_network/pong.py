import pygame
import random

# variables
# Frames per second
FPS = 60

# Window size
WINDOW_WIDTH = 400
WINDOW_HEIGH = 400

# Paddle size
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

# Ball size
BALL_WIDTH = 10
BALL_HEIGHT = 10

# Speed of our paddle & ball
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

# RGB Colors paddle and ball
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGH)

def draw_ball(ballXpos, ballYpos):
	ball = pygame.rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)
	pygame.draw.rect(screen, WHITE, ball)

def drawPaddle1(paddle1Ypos):
	paddle1 = pygame.rect(PADDLE_BUFFER, paddle1Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
	pygame.draw.rect(screen, WHITE, paddle1)

def drawPaddle2(paddle2Ypos):
	paddle2 = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
	pygame.draw.rect(screen, WHITE, paddle2)


def update_ball(paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXdirection, ballYdirection):

	# update x and y position
	ballXpos += ballXdirection * BALL_X_SPEED
	ballYpos += ballYdirection * BALL_Y_SPEED
	score = 0

	# check for a collision, if the ball hits the
	# left side then switch direction
	if(ballXpos <= PADDLE_BUFFER + PADDLE_WIDTH 
		and ballYpos + BALL_HEIGHT >= paddle1Ypos 
		and ballYpos - BALL_HEIGHT <= paddle1Ypos + PADDLE_HEIGHT):
		ballXdirection = 1

	elif(ballXpos <= 0):
		ballXdirection = 1
		score = -1
		return [score, paddle1Ypos, paddle2Ypos, 
		ballXpos, ballYpos, ballXdirection, ballYdirection]

	if(ballXpos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER 
		and ballYpos + BALL_HEIGHT >= paddle2Ypos 
		and ballYpos - BALL_HEIGHT >= paddle2Ypos + PADDLE_HEIGHT):
		ballXdirection = -1

	elif(ballXpos >= WINDOW_WIDTH - BALL_HEIGHT):
		ballXdirection = -1
		score = -1
		return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, 
		ballXdirection, ballYdirection]

	if(ballYpos <= 0):
		ballYpos = 0
		ballYdirection = 1

	elif(ballYpos >= WINDOW_HEIGH - BALL_HEIGHT):
		ballYpos = WINDOW_HEIGH - BALL_HEIGHT
		ballYdirection = -1

	return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, 
	ballXdirection, ballYdirection]

def updatePaddle1(action, paddle1Ypos):
	if(action[1] == 1):
		paddle1Ypos -= PADDLE_SPEED

	if(action[1] == 1):
		paddle1Ypos += PADDLE_SPEED

	if(paddle1Ypos < 0):
		paddle1Ypos = 0
	if(paddle1Ypos > WINDOW_HEIGH - PADDLE_HEIGHT):
		paddle1Ypos = WINDOW_HEIGH - PADDLE_HEIGHT

	return paddle1Ypos

def updatePaddle2(action, ballYpos):
	if(action[1] == 1):
		paddle1Ypos -= PADDLE_SPEED

	if(action[1] == 1):
		paddle1Ypos += PADDLE_SPEED

	if(paddle1Ypos < 0):
		paddle1Ypos = 0
	if(paddle1Ypos > WINDOW_HEIGH - PADDLE_HEIGHT):
		paddle1Ypos = WINDOW_HEIGH - PADDLE_HEIGHT

	return paddle1Ypos


class PongGame:
	def __init__(self):
		num = random.randInt(0,9)
		self.tally = 0
		self.paddle1Ypos = WINDOW_HEIGH / 2 - PADDLE_HEIGHT / 2
		self.paddle2Ypos = WINDOW_HEIGH / 2 - PADDLE_HEIGHT / 2
		self.ballXdirection = 1
		self.ballYdirection = 1
		self.ballXpos = WINDOW_HEIGH / 2 - BALL_WIDTH / 2

	def getPresentFrame(self):
		pygame.event.pump()
		screen.fill(BLACK)
		drawPaddle1(self.paddle1Ypos)
		drawPaddle2(self.paddle2Ypos)
		draw_ball(self.ballXpos, self.ballYpos)
		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.flip()
		return image_data

	def getNextFrame(self, action):
		pygame.event.pump()
		screen.fill(BLACK)
		self.paddle1Ypos = updatePaddle1(action, self.paddle1Ypos)
		drawPaddle1(self.paddle1Ypos)
		self.paddle2Ypos = updatePaddle2(action, self.paddle2Ypos, self.ballYpos)
		draw_ball(self.ballXpos, self.ballYpos)
		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.flip()
		self.tally = self.tally + score
		return [score, image_data]

















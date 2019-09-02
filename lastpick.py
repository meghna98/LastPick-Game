import pygame
import random
import subprocess as sp
import time
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,200,0)
bgreen = (0,255,0)
width = 800
height = 600
 
gameDisplay = pygame.display.set_mode((width,height))

def text_objects(text,font):
	TextSurface = font.render(text,True,white)
	return TextSurface,TextSurface.get_rect()

def msg_display(text,w,h,fs):
	largeText = pygame.font.Font("freesansbold.ttf",fs)
	TextSurf, TextRect = text_objects(text,largeText)
	TextRect.center = ((w/2),(h/2))
	gameDisplay.blit(TextSurf,TextRect)

def button(msg,x,y,w,h,i,a,user_pick,ind):  # i = inactive color of button | a = active color of button
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if(x+w>mouse[0]>x and y+h>mouse[1]>y):
		pygame.draw.rect(gameDisplay,a,(x,y,w,h))
		if(click[0] == 1 and user_pick==0 ):
			user_pick = ind
	else:
		pygame.draw.rect(gameDisplay,i,(x,y,w,h))

	smallText = pygame.font.Font("freesansbold.ttf",20)

	TextSurf1,TextRect1 = text_objects(msg,smallText)
	TextRect1.center = ((x+w/2),(y+h/2))
	gameDisplay.blit(TextSurf1,TextRect1)
	return user_pick

def balls(num,start_num):
	gameDisplay.fill(black)
	k = 10*start_num
	x = 270-k
	l = x + 80
	flag = 0
	for i in range(num):
		
		if(x>700 or flag == 1):
			l = l + 50
			flag = 1
			pygame.draw.circle(gameDisplay,white,(l-50,300),20)
		else:
			x = x + 50
			pygame.draw.circle(gameDisplay,white,(x,200),20) 

def check_result(num,prst_plyr):
	if(num==0):
		time.sleep(0.5)
		gameDisplay.fill(black)
		if(prst_plyr==1):
			msg_display("Player 1 Wins !!!",width,height,40)
		else:
			msg_display("Computer Wins !!!",width,height,40)
		pygame.display.update()
		time.sleep(2)
		return 1
	return 0

def display(n,sn):

	balls(n,sn)
	
	user_pick = button('Pick 1',250,450,100,50,green,bgreen,0,1)
	user_pick = button('Pick 2',460,450,100,50,green,bgreen,user_pick,2)
	pygame.display.update()

def comp_turn(num,start_num,prst_plyr,user_pick):
	if(num-user_pick<0):
		return num,0
	num = num-user_pick
	
	display(num,start_num)
	msg_display("Computer's turn",750,75,20)
	pygame.display.update()
	time.sleep(1)

	result = check_result(num,prst_plyr)
	if(result==1):
		return num,1
	prst_plyr = 2

	if(num%3==0):
		num = num-user_pick
	elif((num-1)%3==0):
		num = num-1
	elif((num-2)%3==0):
		num = num-2
	else:
		num=num-1
	display(num,start_num)
	time.sleep(1)
	result = check_result(num,prst_plyr)
	if(result==1):
		return num,1;
	return num,0;


flag = 0
exit_flag = 0
while True:
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			pygame.quit()
			quit()
	gameDisplay.fill(black)
	msg_display("Welcome to \"PICK THE LASTBALL\"!!!",width,height,35)
	exit_flag = button('Play',250,450,100,50,green,bgreen,0,1)
	exit_flag = button('Quit',460,450,100,50,green,bgreen,exit_flag,2)
	exit_flag = exit_flag
	pygame.display.update()
	if(exit_flag==2):
		break

	elif(exit_flag==1):
		flag = 0
		
		num = random.randint(7,25)
		start_num = num = 25
		time.sleep(0.5)
		gameDisplay.fill(black)

		while flag==0:

			prst_plyr = 1
			user_pick = 0
			for event in pygame.event.get():
				if(event.type==pygame.QUIT):
					pygame.quit()
					quit()

			
			balls(num,start_num)
			msg_display("Player 1 turn",400,75,20)
			user_pick = button('Pick 1',250,450,100,50,green,bgreen,0,1)
			user_pick = button('Pick 2',460,450,100,50,green,bgreen,user_pick,2)
			pygame.display.update()

			if(user_pick != 0):
				num,flag=comp_turn(num,start_num,prst_plyr,user_pick)
			pygame.display.update()
			
pygame.quit()
quit()


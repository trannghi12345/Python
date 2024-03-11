try:
	import pygame
	import time
	import math
	pygame.init()

	screen = pygame.display.set_mode((500,600))

	WHITE = (255,255,255)
	BLACK = (0,0,0)
	GREY = (150,150,150)
	GREEN = (0,255,17)

	running = True
	font = pygame.font.SysFont('sans',50)
	text_1= font.render('+',True,BLACK)
	text_2= font.render('+',True,BLACK)
	text_3= font.render('Start',True,BLACK)
	text_4= font.render('Reset',True,BLACK)
	text_5= font.render('-',True,BLACK)
	text_6= font.render('-',True,BLACK)


	total_secs = 0
	start = False
	r = 90
	sound = pygame.mixer.music.load("timeoout.wav")
	runsound = False
	while running:
		screen.fill(GREY)

		mouse_x, mouse_y = pygame.mouse.get_pos()
		
		
		

		pygame.draw.rect(screen, WHITE, (100,50,50,50))
		pygame.draw.rect(screen, WHITE, (100,200,50,50))
		pygame.draw.rect(screen, WHITE, (200,50,50,50))
		pygame.draw.rect(screen, WHITE, (200,200,50,50))
		pygame.draw.rect(screen, WHITE,  (300,50,150,50))
		pygame.draw.rect(screen, WHITE, (300,150,150,50))

		pygame.draw.circle(screen, BLACK, (250,400),105)
		pygame.draw.circle(screen, WHITE, (250,400),100)
		pygame.draw.circle(screen, BLACK, (250,400),5)


		screen.blit(text_1,(100,50))
		screen.blit(text_5,(100,200))
		screen.blit(text_2,(200,50))
		screen.blit(text_6,(200,200))
		screen.blit(text_3,(300,50))
		screen.blit(text_4,(300,150))
		
		pygame.draw.rect(screen, BLACK, (50,520,400,50))
		pygame.draw.rect(screen, WHITE, (60,530,380,30))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if 100 <= mouse_x <= 150 and 50 <= mouse_y <= 100:
						total_secs += 60
						print("press + min")
						print(total_secs)
					elif 200 <= mouse_x <= 250 and 50 <= mouse_y <= 100:
						total_secs += 1
						print("press + sec")
						print(total_secs)
					elif 100 <= mouse_x <= 150 and 200 <= mouse_y <= 250:
						total_secs -= 60
						print("press - min")
						print(total_secs)
					elif 200 <= mouse_x <= 250 and 200 <= mouse_y <= 250:
						total_secs -= 1
						print("press - sec")
						print(total_secs)
					elif 300 <= mouse_x <= 450 and 50 <= mouse_y <= 100:
						start = True
						print("press start")
					elif 300 <= mouse_x <= 450 and 150 <= mouse_y <= 200:
						total_secs = 0
						print("press restet")
						print(total_secs)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if runsound == True:
						pygame.mixer.music.pause()
					
		total = total_secs

		if start:
			total_secs -= 1
			if total_secs == 0:
				runsound = True
				pygame.mixer.music.play()
				start = False
			time.sleep(0.05)

		if total_secs < 0:
			total_secs = 0

		mins = int(total_secs/60)
		secs = total_secs - mins*60
		time_now = str(mins) + " : " + str(secs)
		text_time= font.render(time_now,True,BLACK)
		screen.blit(text_time,(120,120))

		x_secs = 250 + 90*math.sin(6*secs*math.pi/180)
		y_secs = 400 - 90*math.cos(6*secs*math.pi/180)
		pygame.draw.line(screen,BLACK,(250,400),(x_secs,y_secs))

		x_mins = 250 + 50*math.sin(6*mins*math.pi/180)
		y_mins = 400 - 50*math.cos(6*mins*math.pi/180)
		pygame.draw.line(screen,BLACK,(250,400),(x_mins,y_mins))

		if total != 0:
			pygame.draw.rect(screen, GREEN, (60,530,int(380*(total_secs/total)),30))

		pygame.display.flip()
	pygame.quit()
# # except: Exception as bug:
# 	print(bug)
input()

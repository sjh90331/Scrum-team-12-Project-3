import pygal
import lxml
import api
import json
import pygame 
import sys 

# data = api.getAndPrint()
# jsonData =json.dumps(data)
# #print(type(jsonData))
# #print
# print(len(data))
# #print(jsonData)
# print(data)


  
  
# pygame.init() will initialize all 
# imported module 

listofQuestions = ['Enter the stock symbol for the company you want data for',
                   ]
pygame.init() 
  
clock = pygame.time.Clock() 
  
# it will display on screen 
screen = pygame.display.set_mode([980, 900]) 
  
# basic font for user typed 
base_font = pygame.font.Font(None, 32) 
user_text = '' 
  
question_text = listofQuestions[0]
# create rectangle 
input_rect = pygame.Rect(100, 50, 340, 32) 
button_rect = pygame.Rect(350,100,140,40)
quest_rect = pygame.Rect(10, 10, 340, 10) 
  

color_active = pygame.Color('lightskyblue3') 

color_light = (10,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
color_passive = pygame.Color('aquamarine4') 
color = color_passive 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
active = False

while True: 
    
    for event in pygame.event.get(): 
        mouse = pygame.mouse.get_pos() 
      # if user types QUIT then the screen will close 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
            #     print(user_text)
            if button_rect.collidepoint(event.pos):
                print(user_text)
                question_text = user_text
            if input_rect.collidepoint(event.pos): 
                active = True
            else: 
                active = False
  
        if event.type == pygame.KEYDOWN: 
  
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1] 
  
            # Unicode standard is used for string 
            # formation 
            else: 
                user_text += event.unicode
      
    # it will set background color of screen 
    screen.fill((255, 255, 255)) 
  
    if active: 
        color = color_active 
    else: 
        color = color_passive 
        
    #(100,10,140,40) left top height width
    if button_rect.collidepoint(mouse): 
        pygame.draw.rect(screen,color_light,button_rect) 
          
    else: 
        pygame.draw.rect(screen,color_dark,button_rect) 
    # draw rectangle and argument passed which should 
    # be on screen 
    pygame.draw.rect(screen, color, input_rect) 
    quest_text_surface = base_font.render(question_text, True, (0,0, 0)) 
      
    # render at position stated in arguments 
    screen.blit(quest_text_surface, (quest_rect.x+5, quest_rect.y+5)) 
    #pygame.display.flip() 
  
    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
      
    # render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    input_rect.w = max(100, text_surface.get_width()+10) 
    
    # display.flip() will update only a portion of the 
    # screen to updated, not full area 
    pygame.display.flip() 
      
    # clock.tick(60) means that for every second at most 
    # 60 frames should be passed. 
    clock.tick(60) 
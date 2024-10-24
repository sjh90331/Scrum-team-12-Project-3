import pygal
import lxml
import api
import json
import pygame 
import sys 
import stock_visualization
from datetime import datetime

class varaibles:
    listofQuestions = ['Enter the stock symbol for the company you would like',
                   'Enter chart type you would like (line/bar)',
                   'Enter the time series function desired (TIME_SERIES_DAILY, TIME_SERIES_WEEKLY, etc.)',
                   'Enter the beginning date in YYYY-MM-DD ',
                   'Enter the end date in YYYY-MM-DD format', 
                   'Processin'
                   ]
    question_text = listofQuestions[0]
    questionIndex = 0
    listOfInputs = []
    secretQuestion = "Enter an end date not below the begining date."
    errorText = ''
    stringStartDate = ''
    stringEndDate =''


# pygame.init() will initialize all 
# imported module 



pygame.init() 
  
clock = pygame.time.Clock() 
  
# it will display on screen 
screen = pygame.display.set_mode([980, 900]) 
  
# basic font for user typed 
base_font = pygame.font.Font(None, 32) 
user_text = '' 
  

# create rectangle 
input_rect = pygame.Rect(100, 50, 340, 32) 
button_rect = pygame.Rect(350,100,140,40)
quest_rect = pygame.Rect(10, 10, 340, 10) 
error_rect = pygame.Rect(20, 410, 340, 10) 
  

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
def saveInput():
    
    if varaibles.questionIndex == 0:   
        if 0 < len(varaibles.listOfInputs):
            if len(varaibles.listOfInputs[0]) > 5:
                varaibles.errorText = 'Hey thats not a vaild symbol'
                return
            else:
                varaibles.listOfInputs[0] = varaibles.listOfInputs[0].upper()
    varaibles.listOfInputs.append(user_text)
    #print("question index", varaibles.questionIndex)
    ###
    ### THIS PROCESSES THE QUESTIONARE TO THE NEXT QUESTION
    ###
    if varaibles.questionIndex < len(varaibles.listofQuestions)-1:
        
        varaibles.questionIndex+=1
        
    
    if varaibles.questionIndex == 1:   
        if 1 < len(varaibles.listOfInputs):
            if varaibles.listOfInputs[1].upper() != "LINE" or varaibles.listOfInputs[1].upper() != "BAR":
                varaibles.errorText = 'Hey thats not a vaild type of chart'
    if varaibles.questionIndex == 4:
        print(varaibles.listOfInputs[3])
        try:
            ## FIRST DATE
            varaibles.stringStartDate =varaibles.listOfInputs[3]
            varaibles.listOfInputs[3] = datetime.strptime(varaibles.listOfInputs[3], '%Y-%m-%d')
        except Exception as e:
            print(e, "FIRST DATE")
            varaibles.questionIndex-=1
            varaibles.listOfInputs.pop(3)
            varaibles.errorText = "Hey your input does not match format '%Y-%m-%d' try again"
    if varaibles.questionIndex== 5:
        
        try:
            ## END DATE
            
            varaibles.stringEndDate = varaibles.listOfInputs[4]
            varaibles.listOfInputs[4] = datetime.strptime(varaibles.listOfInputs[4], '%Y-%m-%d')
            if varaibles.listOfInputs[4] < varaibles.listOfInputs[3]:
                varaibles.errorText = varaibles.secretQuestion
                varaibles.listOfInputs.pop(4)
        except Exception as e:
            print(e, "END DATE")
            varaibles.questionIndex-=1
            varaibles.errorText = "Hey your input does not match format '%Y-%m-%d' try again"
            varaibles.listOfInputs.pop(4)
    if varaibles.questionIndex == 5:
        print(varaibles.listOfInputs[3],varaibles.listOfInputs[4], type(varaibles.listOfInputs[3]),type(varaibles.listOfInputs[4]))
        stock_visualization.stockMaker(varaibles.listOfInputs[0],varaibles.listOfInputs[1],varaibles.listOfInputs[2],
                                       varaibles.listOfInputs[3],varaibles.listOfInputs[4], varaibles.stringStartDate,varaibles.stringEndDate)
        print("END OF QUESTION")
    print(varaibles.questionIndex)
    questionAsker()
def questionAsker():
     # stock_symbol = input("Enter the stock symbol: ")
    # chart_type = input("Enter the chart type (line/bar): ")
    # function = input("Enter the time series function (TIME_SERIES_DAILY, TIME_SERIES_WEEKLY, etc.): ")
    
    # start_date = input("Enter the beginning date (YYYY-MM-DD): ")
    # end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    varaibles.question_text = varaibles.listofQuestions[varaibles.questionIndex]

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
                saveInput()
                #varaibles.question_text = user_text
                #listOfInputs.append(user_text)
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
    quest_text_surface = base_font.render(varaibles.question_text, True, (0,0, 0)) 
      
    # render at position stated in arguments 
    screen.blit(quest_text_surface, (quest_rect.x+5, quest_rect.y+5)) 
    #pygame.display.flip() 
  
  
  
  
  
    error_text_surface = base_font.render(varaibles.errorText, True, (255,0, 0)) 
      
    # # render at position stated in arguments 
    screen.blit(error_text_surface, (error_rect.x+5, error_rect.y+5)) 
  
  
  
  
  
  
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
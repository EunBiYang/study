
import pygame

pygame.init()#초기화 (반드시 필요)

#화면크기 설정
screen_width = 550
screen_higth = 640
screen = pygame.display.set_mode((screen_width,screen_higth))

#화면 타이틀 설정
pygame.display.set_caption('bibi Game')

#배경이미지 불러오기
background = pygame.image.load("D:\\workspace\\small-projects\\pygame_basic\\backgroung.png")

#캐릭터 불러오기(스프라이트)
character = pygame.image.load("D:\\workspace\\small-projects\\pygame_basic\\character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]     #캐릭터의 가로 크기
character_height = character_size[1]    #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width/2)     #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_higth - character_height        #화면 세로크기 가장 아래에 위치



#이벤트 루프
running = True #게임이 진행중인가 확인!
while running:
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:           #창이 닫히는 이벤트가 발생하였는가?
            running = False                 #게임이 진행중이 아님
    
    screen.blit(background, (0,0))      #배경그리기
    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update()  #게임화면을 계속해서 다시 그려주는 코드!!

#pygame 종료
pygame.quit()
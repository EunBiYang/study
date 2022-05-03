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

#이벤트 루프
running = True #게임이 진행중인가 확인!
while running:
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:           #창이 닫히는 이벤트가 발생하였는가?
            running = False                 #게임이 진행중이 아님
    
    #screen.fill((0,0,255))      #RGB를 fill로 바로 채워줄수도 있다.
    screen.blit(background, (0,0))      #배경그리기
    pygame.display.update()  #게임화면을 계속해서 다시 그려주는 코드!!

#pygame 종료
pygame.quit()
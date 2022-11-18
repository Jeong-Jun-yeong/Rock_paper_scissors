import turtle as t
from tkinter import *
import random


#기본 설정
scr = t.Screen()
scr.title("가위 바위 보 하나빼기~")
scr.setup(width=1300, height=950)
scr.bgpic("jp/z.gif")
scr.update()

#----------------------------------------------------

#가위 바위 보 코드----------------------------------------------------
hands = ["가위","바위","보"]

hand_right =  ""
hand_left =  ""

com_hand_right =  ""
com_hand_left =  ""

player_hand = ""
com_hand = ""

player_win = 0
com_win = 0


results = 0

#----------------------------------------------------





rock_gif = "jp/rock.gif"
scissors_gif = "jp/scissors.gif"
paper_gif = "jp/paper.gif"
rock2_gif = "jp/rock2.gif"
scissors2_gif = "jp/scissors2.gif"
paper2_gif = "jp/paper2.gif"


t.addshape(rock_gif)
t.addshape(rock2_gif)
t.addshape(scissors_gif)
t.addshape(scissors2_gif)
t.addshape(paper_gif)
t.addshape(paper2_gif)




user_score = 0
user_score2 = 0
com_score = 0
com_score2 = 0



#나의 선택 이미지(왼손)
user = t.Turtle()
user.up()
user.speed(0)
user.goto(-200, -360) #가위 바위 보 이미지
user.shape(rock_gif)


user_state = t.Turtle()
user_state.speed(0)
user_state.up()
user_state.goto(000, -100) #나의 선택
user_state.ht()
user_state.write("나의 선택", False, "center", ("", 30))


#나의 선택 이미지(오른손)
user2 = t.Turtle()
user2.up()
user2.speed(0)
user2.goto(200, -360) #가위 바위 보 이미지
user2.shape(rock_gif)


#컴퓨터 선택 이미지 (왼손)
com = t.Turtle()
com.up()
com.speed(0)
com.goto(-200, 370)  #가위 바위 보 이미지
com.shape(rock2_gif)

com_state = t.Turtle()
com_state.speed(0)
com_state .up()
com_state .goto(000, 100)  #컴퓨터의 선택
com_state.ht()
com_state .write("컴퓨터의 선택", False, "center", ("", 30))

#컴퓨터 선택 이미지 (오른손)
com2 = t.Turtle()
com2.speed(0)
com2.up()
com2.goto(200, 370)  #가위 바위 보 이미지
com2.shape(rock2_gif)


# 유저 점수 펜
user_pen = t.Turtle()
user_pen.speed(0)
user_pen.up()
user_pen.goto(000, -200) #유저의 점수 위치
user_pen.ht()
user_pen.write(user_score, False, "center", ("", 50))


# 컴퓨터 점수 펜
com_pen = t.Turtle()
com_pen.speed(0)
com_pen.ht()
com_pen.up()
com_pen.goto(000, 200)  #컴퓨터의 점수 위치
com_pen.write(com_score, False, "center", ("", 50)) 



#계속하기 버튼
continue_gif = "jp/c.gif"
scr.addshape(continue_gif)
cb1 = t.Turtle()
cb1.speed(0)
cb1.up()
cb1.goto(0,-250)
cb1.shape(continue_gif)
cb1.ht()

#가위 바위 보 코드----------------------------------------------------


def hand_shoot():

    global player_win
    global com_win
    global player_hand
    global com_hand
    global user_pen
    global com_pen
    global user_score
    global com_score
    global com_state
    global user_state

    w_p = 0
    c_p = 0
    print("현재 선택 플레이어 : ",player_hand,"컴퓨터",com_hand)
    if(player_hand=="가위" and com_hand!="바위" and player_hand!=com_hand):
        player_win+=1
        w_p = 1
    if(player_hand=="바위" and com_hand!="보" and player_hand!=com_hand):
        player_win+=1
        w_p = 1
    if(player_hand=="보" and com_hand!="가위" and player_hand!=com_hand):
        player_win+=1
        w_p = 1
    if(com_hand =="가위" and player_hand!="바위" and player_hand!=com_hand):
        com_win+=1
        c_p=1
    if(com_hand =="바위" and player_hand!="보" and player_hand!=com_hand):
        com_win+=1
        c_p=1
    if(com_hand =="보" and player_hand!="가위" and player_hand!=com_hand):
        com_win+=1
        c_p=1
    print("점수",player_win," : ",com_win)
    user_score = player_win
    com_score = com_win
    
    user_pen.clear()
    com_pen.clear()
    com_state.up()
    user_state.up()
    
    user_pen.write(user_score, False, "center", ("", 50))
    com_pen.write(com_score, False, "center", ("", 50))

    com_state.clear()
    user_state.clear()
    com_state.up()
    user_state.up()

    temp = ("컴퓨터의 선택 : "+com_hand + "\n"+"플레이어의 선택 : "+player_hand+"\n")
    if(w_p>0):
        temp2 = "결과 : 플레이어가 이겼습니다"
    if(c_p>0):
        temp2 = "결과 : 컴퓨터가 이겼습니다"
    if(w_p==c_p):
        temp2="결과 : 비겼습니다"
        
    game_over(temp,temp2)
    
     
def game_over(result,result2):
     global results
     results = 1
     print("결과")
     global user
     global user2
     global com
     global com2
     global user_pen
     global com_pen
     global button1
     global button2
     global button3
     global win_p
     global win_c
     global cb1
     user.ht()
     user2.ht()
     com.ht()
     com2.ht()
     com.clear()
     user.clear()
     user_pen.ht()
     com_pen.ht()
     com_pen.clear()
     user_pen.clear()
     user_pen.reset
     user_pen.goto(0,-100)
     user_pen.write((result + "\n"+result2+"\n"), False, "center", ("", 50))
     button1.clear()
     button2.clear()
     button3.clear()
     button1.ht()
     button2.ht()
     button3.ht()
    
     cb1.st()
     
def re_open():
        global user_pen
        global button1
        global button2
        global button3
        global user
        global user2
        global com
        global com2
        global com_pen

        if(player_win > 2 or com_win > 2):
            results = 0
            final_result()
        else:
            button2.ht()
            button3.ht()
            button1.st()
            user_pen.clear()
            user_pen.up()
            user_pen.goto(000, -200) 
            user_pen.ht()
            user_pen.write(user_score, False, "center", ("", 50))
            com_pen.ht()
            com_pen.up()
            com_pen.goto(000, 200)  
            com_pen.write(com_score, False, "center", ("", 50)) 
            user.shape(rock_gif)
            user2.shape(rock_gif)
            com.shape(rock2_gif)
            com2.shape(rock2_gif)
            user.st()
            com.st()
            user2.st()
            com2.st()
            cb1.ht()

def final_result():
        global cb1
        global player_win
        global com_win
        global user_pen
        cb1.ht()
        if(player_win > com_win):
           user_pen.clear()
           user_pen.reset
           user_pen.goto(0,0)
           user_pen.write(("플레이어 최종 승리!"), False, "center", ("", 50))
        else:
           user_pen.clear()
           user_pen.reset
           user_pen.goto(0,0)
           user_pen.write(("컴퓨터  최종 승리!"), False, "center", ("", 50))
        
#-------------------------버튼

def hand():
    global hand_right
    global hand_left
    global com_hand_right
    global com_hand_left
    global com
    global user
    global com_state
    global user_state
    print("가위 바위 보를 내었다!")
    hand_right =  hands[random.randrange(0,3)]
    hand_left = hands[random.randrange(0,3)]
    print("오른손 : ",hand_right)
    print("왼손 : ",hand_left)
    if(hand_right=="가위"):
        user2.shape(scissors_gif)
    if(hand_right=="바위"):
        user2.shape(rock_gif)
    if(hand_right=="보"):
        user2.shape(paper_gif)
    if(hand_left=="가위"):
        user.shape(scissors_gif)
    if(hand_left=="바위"):
        user.shape(rock_gif)
    if(hand_left=="보"):
        user.shape(paper_gif)
    user_state.clear()
    user_state.up()
    user_state.write(("플레이어 상태"+" 왼손: "+hand_left+" / 오른손: "+hand_right), False, "center", ("", 30))
    #컴퓨터의 손
    com_hand_right =  hands[random.randrange(0,3)]
    com_hand_left = hands[random.randrange(0,3)]
    print("컴퓨터의 오른손 : ", com_hand_right)
    print("컴퓨터의 왼손 : ",com_hand_left)
    if(com_hand_right=="가위"):
        com2.shape(scissors2_gif)
    if(com_hand_right=="바위"):
        com2.shape(rock2_gif)
    if(com_hand_right=="보"):
        com2.shape(paper2_gif)
    if(com_hand_left=="가위"):
        com.shape(scissors2_gif)
    if(com_hand_left=="바위"):
        com.shape(rock2_gif)
    if(com_hand_left=="보"):
        com.shape(paper2_gif)
    com_state.clear()
    com_state.up()
    com_state.write(("컴퓨터 상태"+" 왼손: "+com_hand_left+" / 오른손: "+com_hand_right), False, "center", ("", 30))
    button2.st()
    button3.st()
    
#가위 바위 보! 버튼
hand_gif = "jp/r.gif"
scr.addshape(hand_gif)
button1 = t.Turtle()
button1.up()
button1.speed(0)
button1.goto(-500, -350)
button1.shape(hand_gif)


def just():
    global player_hand
    global com_hand
    global hand_left
    global com_hand_left
    print("왼손 내었다!")
    player_hand = hand_left
    com_hand = com_hand_left
    hand_shoot()
    
# 왼손 버튼
continue_gif = "jp/q.gif"
scr.addshape(continue_gif)
button2 = t.Turtle()
button2.up()
button2.speed(0)
button2.goto(-500, 10)
button2.shape(continue_gif)
button2.ht()


def change():
    global player_hand
    global com_hand
    global hand_right
    global com_hand_right
    print("오른손을 내었다!")
    player_hand = hand_right
    com_hand = com_hand_right
    hand_shoot()
    
# 오른손 버튼
change_gif = "jp/e.gif"
scr.addshape(change_gif)
button3 = t.Turtle()
button3.up()
button3.speed(0)
button3.goto(500, 10)
button3.shape(change_gif)
button3.ht()


#----------------------------------------------

def clickLeft(x,y):
    global results
    global button1
    global button2
    global button3
    global tutorial
    global cb1
    print(x,y)
    
    if(x>-600 and x<-400 and y<-250 and y>-450): # 가위바위보 버튼
        hand()
        button1.ht()
    if(x>-600 and x<-400 and y<110 and y>-90):  # 왼손 버튼
        just()
        button2.ht()
        button3.ht()
        print("왼손 누름")
    if(x>400 and x<600 and y<100 and y>-90): # 오른손 버튼
        change()
        button2.ht()
        button3.ht()
        print("오른손 누름")
    if(x>-110 and x<89 and y<-146 and  y>-352):
        if(results==1):
            results = 0
            cb1.ht()
            re_open()
#-------------------------------------------


t.onscreenclick(clickLeft,1)

t.done()


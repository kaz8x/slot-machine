import play
from random import randint

global credit
credit = 100

block_1 =play.new_box(color = "light blue",x=200,y=0,width=110,height=170)
block_2 =play.new_box(color = "light blue",x=-200,y=-0,width=110,height=170)
block_3 = play.new_box(color = "light blue",x=0,y=0,width=110,height=170)

play.new_text("SLOT MACHINE",x=0,y=150,font="none",font_size=30,color="dark blue")
big_win = play.new_text(words="")
cr = play.new_text(words="",x=-350,y=270,font="none",color="dark blue",font_size=30)

num1 =play.new_text("",x=200,y=0,font="none",font_size=100,color="dark blue")
num2 =play.new_text("",x=0,y=0,font="none",font_size=100,color="dark blue")
num3 =play.new_text("",x=-200,y=0,font="none",font_size=90,color="dark blue")

@play.when_program_starts
def start():
    pass

@play.repeat_forever
def do():
    if play.key_is_pressed("s"):

        num1.words =randint(0,1)
        num2.words =randint(0,1)
        num3.words =randint(0,1)
        if num1.words == num2.words and num2.words == num3.words and num1.words == num3.words:

            big_win.words = ">>BIG WIN<<"
            big_win.y = -150
            big_win.color = "dark blue"

        else:
            big_win.words = ""



    #if play.key_is_pressed("w"):
        #player.y += 5
    #if play.key_is_pressed("d"):
        #player.x += 5
    #if play.key_is_pressed("a"):
        #player.x -=5



play.start_program()

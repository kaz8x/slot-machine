import play
from random import randint
from time import sleep

block_1 =play.new_box(color = "light blue",x=200,y=0,width=110,height=170)
block_2 =play.new_box(color = "light blue",x=-200,y=-0,width=110,height=170)
block_3 = play.new_box(color = "light blue",x=0,y=0,width=110,height=170)

play.new_text("SLOT MACHINE",x=0,y=150,font="none",font_size=30,color="dark blue")
big_win = play.new_text(words="")
cr = play.new_text(words="100",x=-350,y=270,font="none",color="dark blue",font_size=30)

num1 =play.new_text("",x=200,y=0,font="none",font_size=100,color="dark blue")
num2 =play.new_text("",x=0,y=0,font="none",font_size=100,color="dark blue")
num3 =play.new_text("",x=-200,y=0,font="none",font_size=90,color="dark blue")

@play.when_program_starts
def start():
    pass

@play.repeat_forever
def do():
    if play.key_is_pressed("s"):

        num1.words =randint(0,9)
        num2.words =randint(0,9)
        num3.words =randint(0,9)
        if num1.words == num2.words and num2.words == num3.words and num1.words == num3.words:

            big_win.words = ">>BIG WIN<<"
            big_win.y = -150
            big_win.color = "dark blue"
            cr.words = str(int(cr.words) + 50)

        else:
            big_win.words = ""
            cr.words = str(int(cr.words) - 2)

        sleep(0.5)
play.start_program()

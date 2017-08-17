import letters
import turtle

instuff = input('What would you like to print?').lower()
arra = []
el = 0
al=0
while el<len(instuff):
    arra.append(instuff[el])
    el += 1

turtle.color(1,1,1)
turtle.right(180)
turtle.forward(300)
turtle.color(0,0,0)
turtle.right(90)
turtle.width(2)

for al in range(0, len(instuff)):
    if arra[al] == 'a':
        letters.a()
    elif arra[al] == ' ':
        letters.space()
    elif arra[al] == 'b':
        letters.b()
    elif arra[al] == 'c':
        letters.c()
    elif arra[al] == 'i':
        letters.i()
    elif arra[al] == 'o':
        letters.o()
    elif arra[al] == 'u':
        letters.u()
    elif arra[al] == 'n':
        letters.n()
    elif arra[al] == 'd':
        letters.d()
    elif arra[al] == 'e':
        letters.e()
    elif arra[al] == 'f':
        letters.f()
    elif arra[al] == 'g':
        letters.g()
    elif arra[al] == 'h':
        letters.h()
    elif arra[al] == 'j':
        letters.j()
    elif arra[al] == 'k':
        letters.k()
    elif arra[al] == 'l':
        letters.l()
    elif arra[al] == 'm':
        letters.m()
    elif arra[al] == 'p':
        letters.p()
    elif arra[al] == 'q':
        letters.q()
    elif arra[al] == 'r':
        letters.r()
    elif arra[al] == 's':
        letters.s()
    elif arra[al] == 't':
        letters.t()
    elif arra[al] == 'v':
        letters.v()
    elif arra[al] == 'w':
        letters.w()
    elif arra[al] == 'x':
        letters.x()
    elif arra[al] == 'y':
        letters.y()
    elif arra[al] == 'z':
        letters.z()
    elif arra[al] == '0':
        letters.zero()
    elif arra[al] == '1':
        letters.uno()
    elif arra[al] == '2':
        letters.deux()
    elif arra[al] == '3':
        letters.trois()
    elif arra[al] == '4':
        letters.quatre()
    elif arra[al] == '5':
        letters.cinq()
    elif arra[al] == '6':
        letters.six()
    elif arra[al] == '7':
        letters.sept()
    elif arra[al] == '8':
        letters.huit()
    elif arra[al] == '9':
        letters.neuf()
    elif arra[al] == '\'':
        letters.apost()
    elif arra[al] == ',':
        letters.comma()
    elif arra[al] == '!':
        letters.bang()
    elif arra[al] == '.':
        letters.fullstop()
    else:
        letters.question()
    letters.endin()
    al =+ 1
#print(arra)
s = input('Press enter to exit')

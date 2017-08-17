import letters
import turtle

instuff = input('What would you like to print?')
arra = []
el = 0
al=0
while el<len(instuff):
    arra.append(instuff[el])
    el += 1

turtle.color(1,1,1)
turtle.right(180)
turtle.forward((len(instuff)*20)//2)
turtle.color(0,0,0)
turtle.right(90)
turtle.width(2)

for al in range(0, len(instuff)):
    letters.black()
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
    elif arra[al] == 'A':
        letters.capa()
    elif arra[al] == 'B':
        letters.capb()
    elif arra[al] == 'C':
        letters.capc()
    elif arra[al] == 'D':
        letters.capd()
    elif arra[al] == 'E':
        letters.cape()
    elif arra[al] == 'F':
        letters.capf()
    elif arra[al] == 'G':
        letters.capg()
    elif arra[al] == 'H':
        letters.caph()
    elif arra[al] == 'I':
        letters.capi()
    elif arra[al] == 'J':
        letters.capj()
    elif arra[al] == 'K':
        letters.capk()
    elif arra[al] == 'L':
        letters.capl()
    elif arra[al] == 'M':
        letters.capm()
    elif arra[al] == 'N':
        letters.capn()
    elif arra[al] == 'O':
        letters.capo()
    elif arra[al] == 'P':
        letters.capp()
    elif arra[al] == 'Q':
        letters.capq()
    elif arra[al] == 'R':
        letters.capr()
    elif arra[al] == 'S':
        letters.caps()
    elif arra[al] == 'T':
        letters.capt()
    elif arra[al] == 'U':
        letters.capu()
    elif arra[al] == 'V':
        letters.capv()
    elif arra[al] == 'W':
        letters.capw()
    elif arra[al] == 'X':
        letters.capx()
    elif arra[al] == 'Y':
        letters.capy()
    elif arra[al] == 'Z':
        letters.capz()
    else:
        letters.question()
    letters.endin()
    al =+ 1
s = input('Press enter to exit')

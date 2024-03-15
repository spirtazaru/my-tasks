import turtle as t

import random as r

import math as m

 

t.Screen().bgcolor('lightgrey')

t.tracer(10)

t.hideturtle()

game = True

number_of_bombs = 10

 

def rect_cirk(a,b,r):

    t.setheading(0)

    t.penup()

    t.forward(r)

    t.pendown()

    t.forward(a)

    t.circle(r,90)

    t.forward(b)

    t.circle(r,90)

    t.forward(a)

    t.circle(r,90)

    t.forward(b)

    t.circle(r,90)

 

def rules():    

    t.penup()

    t.goto(-80, 260)

    t.pendown()

    t.write('Игра "Сапёр"', font=('Arial', 17, 'bold'))

    t.penup()

    t.goto(-370, 230)

    t.pendown()

    t.write('На поле спрятано 10 бомб. Нажатие левой клавишей мыши открывает клетку. Если там бомба, то она взрывается.', font=('Arial', 10))

    t.penup()

    t.goto(-370, 200)

    t.pendown()

    t.write('Число показывает, сколько вокруг клетки бомб в клетках, соседних по стороне или углу.', font=('Arial', 10))

    t.penup()

    t.goto(-370, 170)

    t.pendown()

    t.write('Правой кнопкой мыши можно поставить или убрать флажок.', font=('Arial', 10))

    t.penup()

    t.goto(-80, - 170)

    t.pendown()

    t.write('Осталось бомб:', font=('Arial', 12, 'bold'))

    t.penup()

    t.goto(60, -170)

    t.pendown()

    t.write(number_of_bombs, font=('Arial', 12, 'bold'))

   

 

   

 

def rectangle(a,b):

    t.setheading(0)

    for _ in range(2):

        t.forward(a)

        t.left(90)

        t.forward(b)

        t.left(90)

 

def restart():

    t.penup()

    t.goto(-89, -305)

    t.pendown()

    t.pencolor('green')

    t.fillcolor('green')

    t.begin_fill()

    rect_cirk(150, 10, 20)

    t.end_fill()

    t.penup()

    t.goto(-50, -290)

    t.pencolor('white')

    t.pendown()

    t.write('Начать заново', font =('Arial', 12, 'bold'))

 

def table():

    t.penup()

    t.goto(-120, 90)    

    for i in range(1,9):

        for j in range(8):

            t.pendown()

            rectangle(30,30)

            t.forward(30)

        t.penup()

        t.goto(-120, 90 - i*30)

 

def map():

    a = [0]*64

    indexes_of_bombs = r.sample([i for i in range(64)], 10)

    for i in range(64):

        if i in indexes_of_bombs:

            a[i] = '*'

    matrix = []

    for i in range(8):

        row = []

        for j in range(8):

            row.append(a[i*8+j])

        matrix.append(row)

    if matrix[0][0]!='*':

        counter = 0

        if matrix[0][1] == '*':

            counter += 1

        if matrix[1][0] == '*':

            counter += 1

        if matrix[1][1] == '*':

            counter += 1

        matrix[0][0] = counter

    if matrix[7][7]!='*':

        counter = 0

        if matrix[7][6] == '*':

            counter += 1

        if matrix[6][6] == '*':

            counter += 1

        if matrix[6][7] == '*':

            counter += 1

        matrix[7][7] = counter

    if matrix[0][7]!= '*':

        counter = 0

        if matrix[0][6] == '*':

            counter += 1

        if matrix[1][7] == '*':

            counter += 1

        if matrix[1][6] == '*':

            counter += 1

        matrix[0][7] = counter

    if matrix[7][0] != '*':

        counter = 0

        if matrix[6][1] == '*':

            counter += 1

        if matrix[6][0] == '*':

            counter += 1

        if matrix[7][1] == '*':

            counter += 1

        matrix[7][0] = counter

 

    for j in range(1,7):

        if matrix[0][j]!='*':

            counter = 0

            if matrix[0][j-1] == '*':

                counter+=1

            if matrix[0][j+1] == '*':

                counter+=1

            if matrix[1][j-1] == '*':

                counter+=1

            if matrix[1][j] == '*':

                counter+=1

            if matrix[1][j+1] == '*':

                counter+=1

            matrix[0][j] = counter

 

    for j in range(1,7):

        if matrix[j][0]!='*':

            counter = 0

            if matrix[j-1][0] == '*':

                counter+=1

            if matrix[j+1][0] == '*':

                counter+=1

            if matrix[j-1][1] == '*':

                counter+=1

            if matrix[j][1] == '*':

                counter+=1

            if matrix[j+1][1] == '*':

                counter+=1

            matrix[j][0] = counter

 

    for j in range(1,7):

        if matrix[7][j]!='*':

            counter = 0

            if matrix[7][j-1] == '*':

                counter+=1

            if matrix[7][j+1] == '*':

                counter+=1

            if matrix[6][j-1] == '*':

                counter+=1

            if matrix[6][j] == '*':

                counter+=1

            if matrix[6][j+1] == '*':

                counter+=1

            matrix[7][j] = counter

 

    for j in range(1,7):

        if matrix[j][7]!='*':

            counter = 0

            if matrix[j-1][7] == '*':

                counter+=1

            if matrix[j+1][7] == '*':

                counter+=1

            if matrix[j-1][6] == '*':

                counter+=1

            if matrix[j][6] == '*':

                counter+=1

            if matrix[j+1][6] == '*':

                counter+=1

            matrix[j][7] = counter

 

    for i in range(1,7):

        for j in range(1,7):

            if matrix[i][j]!='*':

                counter = 0

                if matrix[i-1][j-1] == '*':

                    counter+=1

                if matrix[i-1][j] == '*':

                    counter+=1

                if matrix[i-1][j+1] == '*':

                    counter+=1

                if matrix[i][j-1] == '*':

                    counter+=1

                if matrix[i][j+1] == '*':

                    counter+=1

                if matrix[i+1][j-1] == '*':

                    counter+=1

                if matrix[i+1][j] == '*':

                    counter+=1

                if matrix[i+1][j+1] == '*':

                    counter+=1

                matrix[i][j] = counter

 

    return(matrix)

 

def bomb(x,y):      

    angle, side = [126,20]

    t.pencolor('red')

    t.fillcolor('orange')

    t.penup()

    t.goto(x, y)

    t.pendown()

    t.begin_fill()

    while True:

        t.forward(side)

        t.left(angle)

        if abs(t.pos()-(x,y)) < 1:

            break

    t.end_fill()

   

 

def win():    

    for i in range(8):

        for j in range(8):

            q = j*30 - 105

            p = -i*30 + 95

            if matrix[i][j]=='*':                

                t.penup()

                t.goto(q+1,p)

                t.setheading(0)

                t.pencolor('blue')

                t.fillcolor('blue')

                t.begin_fill()

                t.circle(10)

                t.end_fill()

            else:

                t.penup()

                t.goto(q-2,p-3)

                t.setheading(0)

                t.pencolor('blue')

                t.pendown()

                t.write(matrix[i][j], font=('Arial', 12, 'bold'))

    t.penup()

    t.goto(-220, -250)

    t.pencolor('green')

    t.pendown()

    t.write('Вы выиграли!', font =('Arial', 48, 'bold'))

    restart()

 

def loose():

    for i in range(8):

        for j in range(8):

            q = j*30 - 110

            p = -i*30 + 90

            if matrix[i][j]=='*':                

                t.penup()

                t.goto(q-5,p+5)

                t.setheading(0)

                bomb(q-5,p+10)

            else:

                t.penup()

                t.goto(q,p)

                t.setheading(0)

                t.pencolor('red')

                t.pendown()

                t.write(matrix[i][j], font=('Arial', 14, 'bold'))

    t.penup()

    t.goto(-230, -250)

    t.pencolor('red')

    t.pendown()

    t.write('Вы проиграли', font =('Arial', 48, 'bold'))

    restart()

 

def left_click(x,y):

    global game

    global matrix

    global list_of_bombs

    global number_of_bombs

    if game is True:

        if (-120 <= x < 120) and (-120 <= y < 120):

            a = -(m.floor(y - 120))//30

            b = m.floor(x + 120)//30

            if matrix[a][b] == '*':

                t.penup()

                loose()

                game = False

            else:

                q = b*30 - 110

                p = - a*30 + 95          

                t.penup()

                t.goto(q,p-3)

                t.setheading(0)

                t.pencolor('black')

                t.pendown()

                t.write(matrix[a][b], font=('Arial', 14, 'bold'))

    else:

        if (-70 <= x <= 80) and (-300 <= y <= -250):

            game = True

            number_of_bombs = 10

            t.penup()

            t.goto(-450, -350)

            t.setheading(0)

            t.pencolor('lightgrey')

            t.fillcolor('lightgrey')

            t.pendown()

            t.begin_fill()

            rectangle(900, 700)

            t.end_fill()

            t.pencolor('black')            

            table()

            rules()

            matrix = map()

            list_of_bombs = []

            for i in range(8):

                for j in range(8):

                    if matrix[i][j] == '*':

                        list_of_bombs.append([i,j])



 

flagki = []

def right_click(x,y):

    global flagki

    global game

    global number_of_bombs

    global list_of_bombs

    if game is True:

        if (-120 <= x < 120) and (-120 <= y < 120):

            a = -(int(y - 120))//30

            b = int(x + 120)//30

            q = b*30 - 120

            p = -a*30 + 90  

            if [a,b] not in flagki:

                t.penup()

                t.goto(q+15,p+13)

                t.pendown()

                t.color('green')

                t.shape('triangle')

                t.stamp()

                flagki.append([a,b])

                number_of_bombs -= 1

                t.penup()

                t.goto(58,-170)

                t.pencolor('lightgrey')

                t.fillcolor('lightgrey')

                t.begin_fill()

                t.setheading(0)

                rectangle(50, 20)

                t.end_fill()

                t.penup()

                t.goto(60,-170)

                t.pencolor('black')

                t.write(number_of_bombs, font=('Arial', 12, 'bold'))

                if number_of_bombs == 0:

                    if sorted(flagki) == sorted(list_of_bombs):

                        win()

                        game = False

 

            elif [a,b] in flagki:

                t.penup()

                t.goto(q+1,p+1)

                t.pendown()

                t.color('lightgrey')

                t.pencolor('lightgrey')

                t.fillcolor('lightgrey')

                t.begin_fill()

                t.setheading(0)

                rectangle(26,26)

                t.end_fill()

                flagki.remove([a,b])

                number_of_bombs += 1

                t.penup()

                t.goto(58,-170)

                t.pencolor('lightgrey')

                t.fillcolor('lightgrey')

                t.begin_fill()

                t.setheading(0)

                rectangle(50,20)

                t.end_fill()

                t.penup()

                t.goto(60,-170)

                t.pencolor('black')

                t.write(number_of_bombs, font=('Arial', 12, 'bold'))

                if number_of_bombs == 0:

                    if sorted(flagki) == sorted(list_of_bombs):

                        win()

                        game = False

    else:

        if (-70 <= x <= 80) and (-300 <= y <= -250):            

            number_of_bombs = 10

            t.penup()

            t.goto(-450, -350)

            t.setheading(0)

            t.pencolor('lightgrey')

            t.fillcolor('lightgrey')

            t.pendown()

            t.begin_fill()

            rectangle(900, 700)

            t.end_fill()

            t.pencolor('black')            

            table()

            rules()

            flagki = []

            game = True

            matrix = map()

            list_of_bombs = []

            for i in range(8):

                for j in range(8):

                    if matrix[i][j] == '*':

                        list_of_bombs.append([i,j])

       

 

 

table()

rules()

matrix = map()

list_of_bombs = []

for i in range(8):

    for j in range(8):

        if matrix[i][j] == '*':

            list_of_bombs.append([i,j])


 

t.Screen().onclick(left_click, btn=1)

t.Screen().listen()

t.Screen().onclick(right_click,btn=3)

t.Screen().listen()

t.done()
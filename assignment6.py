import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.title('Shapes')
s.setup(width=800, height=600)
s.tracer()

class shape:
    def __init__(self, length = 0) :
        self.length = length
    def info(self):
        print("Number of sides are: ", self.sides)

class polygon(shape):
    def definition(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")
    def show(self):
        for i in range(self.sides):
           t.forward(self.length)
           t.right(360//self.sides)

class triangle(polygon):
    def __init__(self, length):
        self.sides = 3
        self.length = length
    def definition(self):
        print('Octagon is defined as 3-sided polygon.')

class square(polygon):
    def __init__(self, length):
        self.sides = 4
        self.length = length
    def definition(self):
        print('Square is a plane figure with four equal straight sides and four right angles.')

class pentagon(polygon):
    def __init__(self, length):
        self.sides = 5
        self.length = length
    def definition(self):
        print('Octagon is defined as 5-sided polygon.')

class hexagon(polygon):
    def __init__(self, length):
        self.sides = 6
        self.length = length
    def definition(self):
        print('Octagon is defined as 6-sided polygon.')

class octagon(polygon):
    def __init__(self, length):
        self.sides = 8
        self.length = length
    def definition(self):
        print('Octagon is defined as 8-sided polygon.')

def triag():
    length = int(input("Enter length: "))
    t.clear()
    tr = triangle(length)
    tr.definition()
    tr.info()
    tr.show()

def sq():
    length = int(input("Enter length: "))
    t.clear()
    sq = square(length)
    sq.definition()
    sq.info()
    sq.show()

def penta():
    length = int(input("Enter length: "))
    t.clear()
    p = pentagon(length)
    p.definition()
    p.info()
    p.show()

def hex():
    length = int(input("Enter length: "))
    t.clear()
    hex1 = hexagon(length)
    hex1.definition()
    hex1.info()
    hex1.show()

def oct():
    length = int(input("Enter length: "))
    t.clear()
    oc = octagon(length)
    oc.definition()
    oc.info()
    oc.show()

def quit():
    global exit
    exit = 1

pen = turtle.Turtle()
pen.penup()
pen.goto(-350, 250)
pen.color('red')
pen.write('To draw Triangle Press: T',align='left',font=('Arial', 12,'normal'))
pen.goto(-350, 230)
pen.write('To draw Square Press: S',align='left',font=('Arial', 12,'normal'))
pen.goto(-350, 210)
pen.write('To draw Pentagon Press: P',align='left',font=('Arial', 12,'normal'))
pen.goto(-350, 190)
pen.write('To draw Hexagon Press: H',align='left',font=('Arial', 12,'normal'))
pen.goto(-350, 170)
pen.write('To draw Octagon Press: O',align='left',font=('Arial', 12,'normal'))
pen.goto(-350, 150)
pen.write('To EXIT Press: Q',align='left',font=('Arial', 12,'normal'))


pol = hexagon(150)
pol.show()
print(pol.sides)
print(pol.length)


#keyboard command
s.listen()
s.onkeypress(triag,'t')
s.onkeypress(sq,'s')
s.onkeypress(penta,'p')
s.onkeypress(hex,'h')
s.onkeypress(oct,'o')
s.onkeypress(quit,'q')
exit = 0;
while(not exit):
    s.update()



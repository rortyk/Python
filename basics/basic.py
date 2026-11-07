import colorsys
import math
import turtle

SPEED = 10         # 1 が一番遅い。全体で 252 個の円を描くので、遅くしすぎると数分かかる


def rainbow(i, total, sat=0.8):
    """i 番目 / total 個 の位置に応じた虹色を返す"""
    return colorsys.hsv_to_rgb((i / total) % 1.0, sat, 1.0)


def move_to(t, x, y, heading=0):
    """線を引かずに (x, y) へ移動し、向きをそろえる"""
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()


def circle_at(t, x, y, r):
    """(x, y) を中心とする半径 r の円"""
    move_to(t, x, y - r)          # 円の一番下から描き始めると中心が (x, y) になる
    t.circle(r)


def wave_rose(t, count, base, amp, waves):
    """中心: 半径が sin で波打つ円を回転させて重ねる"""
    move_to(t, 0, 0)
    for i in range(count):
        r = base + amp * math.sin(2 * math.pi * waves * i / count)
        t.pencolor(rainbow(i, count))
        t.circle(r)
        t.left(360 / count)


def flower(t, x, y, radius, petals, hue):
    """中間: (x, y) を起点に、左右交互の円で花を描く"""
    move_to(t, x, y)
    for i in range(petals):
        t.pencolor(colorsys.hsv_to_rgb((hue + 0.25 * i / petals) % 1.0, 0.8, 1.0))
        t.circle(radius if i % 2 == 0 else -radius)
        t.left(360 / petals)


def ring_of_circles(t, ring_r, n, small_r, layers):
    """外周: 半径 ring_r の円周上の n か所に、同心円を layers 重で置く"""
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = ring_r * math.cos(angle)
        y = ring_r * math.sin(angle)
        for k in range(layers):
            t.pencolor(rainbow(i, n, sat=1.0 - 0.25 * k))
            circle_at(t, x, y, small_r * (k + 1) / layers)


screen = turtle.Screen()
screen.setup(950, 950)
screen.title("円だけで描く複雑な模様")
screen.bgcolor("black")

t = turtle.Turtle()
t.shape("circle")
t.shapesize(0.3)       # タートル自体も小さな丸にして、動きを目で追いやすくする
t.speed(SPEED)
t.pensize(1)

# 1. 中心の波打つバラ
wave_rose(t, count=72, base=90, amp=50, waves=5)

# 2. 正六角形の頂点に 6 つの花
for j in range(6):
    angle = 2 * math.pi * j / 6
    flower(t, 290 * math.cos(angle), 290 * math.sin(angle),
           radius=35, petals=12, hue=j / 6)

# 3. 外周の同心円の輪
ring_of_circles(t, ring_r=410, n=36, small_r=18, layers=3)

t.hideturtle()
screen.mainloop()

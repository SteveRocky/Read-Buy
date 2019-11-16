from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

WIDTH = 60
HEIGHT = 30


# 产生四个随机的数字、大小写字母的组合
def create_num_char():
    num_char = ''
    for i in range(4):
        n1 = random.randint(1, 2)
        # 如果n为1产生数字， n为2产生字母
        if n1 == 1:
            num = random.randint(0, 9)
            num_char += str(num)
        else:
            n2 = random.randint(1, 2)
            # 如果n为1产生大写字母， n为2产生小写字母
            if n2 == 1:
                char = chr(random.randint(65, 90))
                num_char += char
            else:
                char = chr(random.randint(97, 122))
                num_char += char
    return num_char


font = ImageFont.truetype("pingfang.ttf", 20)
num_char = create_num_char()
print(num_char)
# 创建图像，把num_char写上去
im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)
for x in range(WIDTH):
    for y in range(HEIGHT):
        draw.point((x, y), fill=(random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)))

for i in range(4):
    fillColor = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    draw.text((5+12*i, 0), num_char[i], font=font, fill=fillColor)




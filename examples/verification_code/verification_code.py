from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint


# 随机生成验证码，默认长度为（1）
def random_character(length=1):
    code = ''
    for character in range(length):
        code += chr(randint(65, 90))
    return code


# 随机生成颜色，默认颜色范围（1，255）
def random_color(start=1, end=255):
    r = randint(start, end)
    g = randint(start, end)
    b = randint(start, end)
    return (r, g, b)


# 生成验证码和图片，验证码长度为（4），宽度为（240），高度为（60）
def verification_code(length=4,  width=60, height=60):
    # 创建图片背景对象
    image = Image.new('RGB', (width * length, height), (255, 255, 255))
    # 创建字体对象
    font = ImageFont.truetype('FreeMono.ttf', 40)
    # 创建绘制对象
    draw = ImageDraw.Draw(image)
    # 随机颜色填充图片背景的每个像素（注释以下三条语句图片更清晰)
    # for x in range(width * length):
    #     for y in range(height):
    #         draw.point((x, y), fill=random_color(200, 255))
    # 验证码
    code = random_character(length)
    # 随机颜色验证码绘制到图片
    for text in range(length):
        draw.text((height * text + 10, 10), code[text],
                  font=font, fill=random_color(30, 120))
    # 模糊滤镜（注释以下一条语句图片更清晰)
    # image = image.filter(ImageFilter.BLUR)
    return code, image



# 调用方法
code, image = verification_code()
print(code, image)
image.save('code.jpg')

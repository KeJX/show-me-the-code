from PIL import Image, ImageDraw, ImageFont ,ImageColor
# get an image
base = Image.open('javaStudy.jpg')
img_draw =ImageDraw.Draw(base)

# get a font
fnt = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40)
font_color =ImageColor.colormap.get('red')
# get a drawing context
final_image = img_draw.text((base.size[0]-30,0),'1',font_color,fnt)
base.save('result.jpg','jpeg')
Image.open('result.jpg').show()

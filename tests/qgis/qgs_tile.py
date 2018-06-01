import time

def yazdir(x,y):
# create image
img = QImage(QSize(1211, 612), QImage.Format_ARGB32_Premultiplied)
# set image's background color
color = QColor(255, 255, 255)
img.fill(color.rgb())
# create painter
p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)
render = QgsMapRenderer()
# set layer set
lst = [layer.getLayerID()]  # add ID of every layer
render.setLayerSet(lst)
# set output size
render.setOutputSize(img.size(), img.logicalDpiX())
# do the rendering
render.render(p)
p.end()
# save image
img.save("/home/ser/Documents/qgs/street/"+str(x)+"_"+str(y)+".png","png")



x= 2878051.0
y=5552686.0
yy=810.0
xx=1602.0
canvas = iface.mapCanvas()

i=1
j=1
#for i in range(2):
#	for j in range(2):
rect = QgsRectangle((x)+i*xx,(y)+j+yy,(x)+(i+1)*xx,(y)+(j+1)*yy)
canvas.setExtent(rect)
pt = QgsPoint((x)+i*xx,(y)+j+yy)
canvas.refresh()
time.sleep(2)
yazdir((x)+i*xx,(y)+j+yy)




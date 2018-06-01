qid = QInputDialog()
canvas = iface.mapCanvas()
input, ok = QInputDialog.getText( qid, "Enter Coordinates", "Enter New Coordinates as 'xcoord,ycoord'", QLineEdit.Normal, "X" + "," + "Y")
if ok:
	x = input.split( "," )[ 0 ]
	print x
	y = input.split( "," )[ 1 ]
	print y
	if not x:
		print "Ooops!X value is missing!"
	if not y:
		print "Ooops!Y value is missing!"
	print x + "," + y



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
	render.setOutputSize(img.size(), img.logicalDpiX())	render = QgsMapRenderer()
	
	# do the rendering
	render.render(p)
	p.end()
	
	# save image
	img.save("/home/ser/Documents/qgs/street/"+str(x)+"_"+str(y)+".png","png")
	
	


x= 2878051.0
y=5552686.0
yy=810.0
xx=1602.0

for(i in range(29)):
	for(j in range(42)):

		rect = QgsRectangle((x)+i*xx+,(y)+j+yy,(x)+(i+1)*xx,(y)+(j+1)*yy)
		canvas.setExtent(rect)
		pt = QgsPoint((x)+i*xx+,(y)+j+yy)
		canvas.refresh()
		time.sleep(2)
		yazdir((x)+i*xx+,(y)+j+yy)









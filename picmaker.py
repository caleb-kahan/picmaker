import math
def main():
    image = [[[255,255,255] for i in range(550)] for i in range(550)];
    editImage(image)
    generateFile(image);
def generateFile(image):
    f = open("pic.ppm","w")
    f.write("P3\n")
    f.write("550 550\n")
    f.write("255\n")
    for i in range(550):
        for j in range(550):
            for k in range(3):
                f.write(str(image[j][i][k])+" ");
    f.close()
def editImage(image):
    for i in range(550):
        for j in range(550):
            if distance((i,j),(250,250))<200 and distance((i,j),(250,250))>184:
                image[i][j] = [50,50,50]
            if distance((i,j),(250,250))<135 and distance((i,j),(250,250))>119:
                image[i][j] = [50,50,50]
            if distance((i,j),(250,250))<10:
                image[i][j] = [50,50,50]
            distBetweenBarCenter = 85
            barRadius = 7
            barLength = 170
            #Making 4 big bars
            makeBar(image,250,250,i,j,distBetweenBarCenter,barRadius,barLength,"up")
            makeBar(image,250,250,i,j,distBetweenBarCenter,barRadius,barLength,"down")
            makeBar(image,250,250,i,j,distBetweenBarCenter,barRadius,barLength,"left")
            makeBar(image,250,250,i,j,distBetweenBarCenter,barRadius,barLength,"right")

            barLength = 40
            distBetweenBarCenter = 16
            distBetweenOldNew = 56
            #Two Horizontal Down-bars
            makeBar(image,250,250+distBetweenOldNew,i,j,distBetweenBarCenter,barRadius,barLength,"left")
            makeBar(image,250,250+distBetweenOldNew,i,j,distBetweenBarCenter,barRadius,barLength,"right")

            #Two Horizontal Up-bars
            makeBar(image,250,250-distBetweenOldNew,i,j,distBetweenBarCenter,barRadius,barLength,"left")
            makeBar(image,250,250-distBetweenOldNew,i,j,distBetweenBarCenter,barRadius,barLength,"right")

            #Two Vertical Right-bars
            makeBar(image,250+distBetweenOldNew,250,i,j,distBetweenBarCenter,barRadius,barLength,"up")
            makeBar(image,250+distBetweenOldNew,250,i,j,distBetweenBarCenter,barRadius,barLength,"down")

            #Two Vertical Left-bars
            makeBar(image,250-distBetweenOldNew,250,i,j,distBetweenBarCenter,barRadius,barLength,"up")
            makeBar(image,250-distBetweenOldNew,250,i,j,distBetweenBarCenter,barRadius,barLength,"down")

            '''
            if distance((i,j),(310,250))<25 and distance((i,j),(310,250))>21:
                image[i][j] = [225,198,153]
            if distance((i,j),(250,250))<50 and distance((i,j),(310,250))<21:
                image[i][j] = [0,0,0]
            if i>235 and i <265 and j<250 and j>150:
                image[i][j] = [225,198,153]
            '''

    return image
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
def makeSemiCircle(image,cX,cY,i,j,radius,orientation):
    switch = {
        "up":lambda centerX,centerY,x,y: y<centerY,
        "down":lambda centerX,centerY,x,y: y>centerY,
        "left":lambda centerX,centerY,x,y: x<centerX,
        "right":lambda centerX,centerY,x,y: x>centerX
    }
    if distance((cX,cY),(i,j))<radius:
        conditional = switch.get(orientation)
        if conditional(cX,cY,i,j):
            image[i][j] = [50,50,50]
def makeBar(image,cX,cY,i,j,distBetweenBarCenter,barRadius,barLength,orientation):
    switchWithinRect = {
        "left": i<=cX-distBetweenBarCenter and i>=cX-distBetweenBarCenter-barLength and j<cY+barRadius and j>cY-barRadius,
        "right": i<=cX+distBetweenBarCenter+barLength and i>=cX+distBetweenBarCenter and j<cY+barRadius and j>cY-barRadius,
        "down": j<=cY+distBetweenBarCenter+barLength and j>=cY+distBetweenBarCenter and i<cX+barRadius and i>cX-barRadius,
        "up": j>=cY-distBetweenBarCenter-barLength and j<=cY-distBetweenBarCenter and i<cX+barRadius and i>cX-barRadius
    }
    if switchWithinRect.get(orientation):
        image[i][j] = [50,50,50]
    if(orientation=="up"):
        makeSemiCircle(image,cX,cY-distBetweenBarCenter,i,j,barRadius,"down")
        makeSemiCircle(image,cX,cY-distBetweenBarCenter-barLength,i,j,barRadius,"up")
    if(orientation=="down"):
        makeSemiCircle(image,cX,cY+distBetweenBarCenter,i,j,barRadius,"up")
        makeSemiCircle(image,cX,cY+distBetweenBarCenter+barLength,i,j,barRadius,"down")
    if(orientation=="left"):
        makeSemiCircle(image,cX-distBetweenBarCenter,cY,i,j,barRadius,"right")
        makeSemiCircle(image,cX-distBetweenBarCenter-barLength,cY,i,j,barRadius,"left")
    if(orientation=="right"):
        makeSemiCircle(image,cX+distBetweenBarCenter,cY,i,j,barRadius,"left")
        makeSemiCircle(image,cX+distBetweenBarCenter+barLength,cY,i,j,barRadius,"right")
main()

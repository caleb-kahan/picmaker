import math
def main():
    image = [[[0,0,0] for i in range(500)] for i in range(500)];
    editImage(image)
    generateFile(image);
def generateFile(image):
    f = open("pic.ppm","w")
    f.write("P3\n")
    f.write("500 500\n")
    f.write("255\n")
    for i in range(500):
        for j in range(500):
            for k in range(3):
                f.write(str(image[j][i][k])+" ");
    f.close()
def editImage(image):
    for i in range(500):
        for j in range(500):
            if distance((i,j),(250,250))<50:
                image[i][j] = [225,198,153]
            if distance((i,j),(310,250))<25 and distance((i,j),(310,250))>21:
                image[i][j] = [225,198,153]
            if distance((i,j),(250,250))<50 and distance((i,j),(310,250))<21:
                image[i][j] = [0,0,0]
            if i>235 and i <265 and j<250 and j>150:
                image[i][j] = [225,198,153]
            

    return image
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

main()

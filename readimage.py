import numpy as np
from PIL import Image, ImageChops


imgA = Image.open('images/A.png')
imgB = Image.open('images/B.png')
imgC = Image.open('images/C.png')
img1 = Image.open('images/1.png')
img2 = Image.open('images/2.png')
img3 = Image.open('images/3.png')
img4 = Image.open('images/4.png')
img5 = Image.open('images/5.png')
img6 = Image.open('images/6.png')


# difference between ab
diff1 = ImageChops.difference(imgA, imgB)
diffAB = diff1.getbbox()
print('Difference between A and B',  diffAB)

#difference between bc
diff2 = ImageChops.difference(imgB, imgC)
diffBC = diff2.getbbox()
print('Difference between B and C', diffBC)

diff3 = ImageChops.difference(imgA, imgC)
diffAC = diff3.getbbox()
print('Difference between A and C', diffAC)

#use for loop to iterate a list of file names - research

#difference between c and all test stuff
diffC1 = ImageChops.difference(imgC, img1)
diffCand1 = np.array(diffC1.getbbox())
print('Difference between c and 1', diffCand1)

diffC2 = ImageChops.difference(imgC, img2)
diffCand2 = diffC2.getbbox()
print('Difference between c and 2', diffCand2)

diffC3 = ImageChops.difference(imgC, img3)
diffCand3 = diffC3.getbbox()
print('Difference between c and 3', diffCand3)

diffC4 = ImageChops.difference(imgC, img4)
diffCand4 = diffC4.getbbox()
print('Difference between c and 4', diffCand4)

diffC5 = ImageChops.difference(imgC, img5)
diffCand5 = diffC5.getbbox()
print('Difference between c and 5', diffCand5)

diffC6 = ImageChops.difference(imgC, img6)
diffCand6 = diffC6.getbbox()
print('Difference between c and 6', diffCand6)

if diffCand1 is not None:
    False
else:
    print('1 is the answer')

if diffCand2 is not None:
    False
else:
    print('2 is the answer')

if diffCand3 is not None:
    False
else:
    print('3 is the answer')

if diffCand4 is not None:
    False
else:
    print('5 is the answer')

if diffCand5 is not None:
    False
else:
    print('5 is the answer')

if diffCand6 is not None:
    False
else:
    print('6 is the answer')



""" source = Image.open('images/img1.jpg')
target = Image.open('images/img2.jpg')


diff = ImageChops.difference(source, target)
print(diff.getbbox())

if diff.getbbox():
    diff.show()

# size_300 = (300,300)
# for f in os.listdir('images/'):# a dot meant current directory
#     if f.endswith('.jpg'):
#         #print(f)
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#
#         i.thumbnail(size_300)
#         i.save('300/{}_300{}'.format(fn, fext))
       # print(fn)
#image1 = Image.open('images/dog1.jpg')
#image1.save('images/pup1.png')

file = open ("images/ProblemData.txt")
lines = file.readlines()
file.close()

for line in lines:
    #print(line)
    if line == "A":
        print(line) """
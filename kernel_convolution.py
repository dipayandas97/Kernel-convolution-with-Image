import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(filename):
    img = cv2.imread(filename,0)
    return img

def disp_image(img,label):
    cv2.imshow(label,img)

    
def make_kernel(size):
    var1 = []
    for i in range(size):
        var2 = []
        for j in range(size):
             var2.append(float(input('Enter: ')))
        var1.append(var2)
    return np.asarray(var1)

def convolve(img, kernel):
    img_w = img.shape[1]
    img_h = img.shape[0]

    k_size = kernel.shape[0]

    img2_w = img_w - k_size + 1
    img2_h = img_h - k_size + 1
    
    conv = np.zeros((img2_h, img2_w),'float')

    for x in range(img2_h):
        for y in range(img2_w):
            conv[x][y] = float(np.sum(np.multiply(kernel,img[x:x+k_size,y:y+k_size])))
    return conv
    

file = input('Enter name of image with extension: ')
s = int(input('Enter size of kernal: '))


img = read_image(file)
print('Enter kernal values: ')
k = make_kernel(s)
#to input kernel within script
#k = np.asarray([ [8,-1,-1],[-1,8,-1],[-1,-1,8]],'float')

#convolve image and kernel
c = convolve(img,k)

#map the output matrix to 0-255
max_val = np.amax(c)
cc = np.interp(c,[0,max_val],[0,255])

#display using cv2
disp_image(img,'input_image')
disp_image(cc/255,'result_image') #standarize for imshow()
cv2.imwrite('result.jpg',cc)

#to display result using matplotlib
#plt.imshow(cc, cmap = 'gray')
#plt.show()

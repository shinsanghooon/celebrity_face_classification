def ImgToArr(name, pwd):
    
    from PIL import Image
    import numpy as np
    import os
    
    path = pwd + "/" + name
    os.chdir(path)
    
    X = []
    y = []
    
    # 디렉토리에 있는 사진 
    for img in os.listdir(path):
        if img != ".DS_Store":
            im = Image.open(img)
            col,row =  im.size
            data = np.zeros((row*col, 3))
            pixels = im.load()
            for i in range(row):
                for j in range(col):
                    g =  pixels[i,j]
                    data[i*col + j,:] = g,i,j
            X.append(data)
            y.append(name)
    
    return X, y

import os

pwd = "/Users/sinsanghun/Desktop/project3/label"
dfX = []
dfy = []
for j in os.listdir(pwd):
    if j != ".DS_Store":
        X, y = ImgToArr(j, pwd)

        for i in range(len(X)):
            dfX.append(X[i])
            dfy.append(y[i])
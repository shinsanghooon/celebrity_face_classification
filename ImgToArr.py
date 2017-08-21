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
           
        
        
def ImgToArr2(name, pwd):
    
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
            print(img)
            im = Image.open(img)
            col,row =  im.size
            data = np.zeros((row, col))
            pixels = im.load()
            for i in range(row):
                for j in range(col):
                    data[j, i] =  255-pixels[i,j]
            # 1 person's data and label
            X.append(data)
            y.append(name)
    
    return X, y


# 이렇게해서 저장하고 
d = dfX.reshape(3432, -1)
dd = pd.DataFrame(d)
dd["label"] = dfy
dd.to_csv("temp_face.csv")

# 다시 불러온 뒤 
ar = np.array(dd.iloc[:,:-1]).reshape(3432, 96, 96)

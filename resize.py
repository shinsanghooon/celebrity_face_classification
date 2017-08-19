def resize(name, pwd):
    from PIL import Image
    import os
    
    path = pwd + "/" + name
    os.chdir(path)
    
    for i in os.listdir(path):
        try :
            im = Image.open(i)
            im2 = im.resize((96, 96))
            im2.save(i)
        except :
            pass
        

pwd = "/Users/sinsanghun/Documents/pycharm/seleniumTest/image1/"
for j in os.listdir(pwd):
    if j != ".DS_Store":
        resize(j, pwd)
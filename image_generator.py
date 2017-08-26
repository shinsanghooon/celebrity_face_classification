def aug_image(name, pwd):
    
    from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
    import os
    
    path = pwd + "/" + name
    
    datagen = ImageDataGenerator(
            rotation_range=10, # change picture's angle 
            width_shift_range=0.1, 
            height_shift_range=0.05,
            shear_range=0, 
            zoom_range=0.1,
            horizontal_flip=False, 
            fill_mode='nearest')
    
    for i in os.listdir(path):
        if i != ".DS_Store":
            img = load_img(path + "/" + i) 
            x = img_to_array(img)  
            x = x.reshape((1,) + x.shape)  
            i = 0
            for batch in datagen.flow(x, batch_size=1, save_to_dir=path, save_prefix='temp', save_format='jpg'):
                i += 1
                # loop for how many pictures you want to generate 
                if i > 1:
                    break  
                  
import os
pwd = "/Users/sinsanghun/Desktop/project3/generator"

for j in os.listdir(pwd):
    if j != ".DS_Store":
        aug_image(j, pwd)

        

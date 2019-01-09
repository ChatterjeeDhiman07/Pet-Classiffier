import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import random
from tqdm import tqdm
import pickle

DATADIR = "E:/Datasets/PetImages"
training_data=[]
CATEGORIES = ["DOG", "CAT"]
IMG_SIZE =100

def data_set_creator():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)

        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


data_set_creator()
print(len(training_data))

random.shuffle(training_data)

for sample in training_data[:10]:
    print(sample[1])

x = []
y = []

for features, label in training_data:
    x.append(features)
    y.append(label)
print(x[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out = open("x.pickle", "wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out )
pickle_out.close()


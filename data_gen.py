from tqdm import tqdm
import glob
import pickle
import numpy as np
import cv2

original_data = glob.glob("./dataset/*/*.png")

for path in tqdm(original_data):
    resized_img = cv2.resize(cv2.imread(path), (100, 75))
    path = path.replace("img", "")
    cv2.imwrite("./dataset2/"+path.split("/")[-1], resized_img)

data = glob.glob("./dataset2/*.png")

labels = []
images = []

for path in tqdm(data):
    image = cv2.imread(path, 0)
    label = int(path.split("/")[-1].split("-")[0])
    images.append(image)
    labels.append(label)

np_imgs = np.asarray(images)
np_labels = np.asarray(labels)

with open("np_imgs.pkl", "wb") as output:
    pickle.dump(np_imgs, output)

with open("np_lables.pkl", "wb") as output:
    pickle.dump(np_labels, output)

#### Testing
with open("np_imgs.pkl", "rb") as output:
    data = pickle.load(output)


with open("np_lables.pkl", "rb") as output:
    labels = pickle.load(output)

print ("Size of input data: {}".format(data.shape))
print ("Size of labels: {}".format(labels.shape))




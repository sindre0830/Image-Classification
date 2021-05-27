import zipfile
from os import path, remove, listdir
import requests
import cv2
from matplotlib import pyplot as plt
import numpy as np

def initilizeDataset():
    print("Initializing dataset...")
    if (path.exists("./dataset") == False):
        print("Requesting compressed data, this might take a while...")
        url = 'http://www.josiahwang.com/dataset/leedsbutterfly/leedsbutterfly_dataset_v1.0.zip'
        r = requests.get(url, allow_redirects=True)
        open('compressedData.zip', 'wb').write(r.content)
        print("Uncompressing data...")
        with zipfile.ZipFile("compressedData.zip", 'r') as zip_ref:
            zip_ref.extractall("./dataset")
        print("Deleting temporary files...")
        remove('compressedData.zip')
    print("Dataset is initializied")

def parseDataset():
    images = []
    masks = []
    labels = []
    print("Parsing dataset...")
    for filename in listdir("dataset/leedsbutterfly/images"):
        img = cv2.imread(path.join("dataset/leedsbutterfly/images", filename))
        mask = cv2.imread(path.join("dataset/leedsbutterfly/segmentations", filename[:-4] + "_seg0.png"), 0)
        if img is not None:
            images.append(img[...,::-1])
            masks.append(mask)
            labels.append(int(filename[:3]))
    print("Dataset is parsed")
    return images, masks, labels

def segmentData(images, masks):
    print("Segmenting data...")
    for image in range(len(images)):
        images[image] = cv2.bitwise_and(images[image], images[image], mask = masks[image])
    print("Segmented " + str(len(images)) + " images")
    return images

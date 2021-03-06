LABEL_FILENAME = 'labels'
LABEL_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# status - wether to run these during runtime
CROSS_VALIDATION_STATUS = True
CONVERT_TO_GRAYSCALE = False
# set parameters for RGB color data
COLOR_DATA_FILENAME = 'color-data'
COLOR_IMAGE_FILENAME = 'modelColor.png'
COLOR_IMAGE_SIZE = 50
COLOR_IMAGE_SPLITS = 5
COLOR_IMAGE_TRAIN_SIZE = 0.80
COLOR_IMAGE_EPOCHS = 50
COLOR_IMAGE_BATCH_SIZE = 256
# set parameters for gray color data
GRAY_DATA_FILENAME = 'gray-data'
GRAY_IMAGE_FILENAME = 'modelGray.png'
GRAY_IMAGE_SIZE = 100
GRAY_IMAGE_SPLITS = 4
GRAY_IMAGE_TRAIN_SIZE = 0.70
GRAY_IMAGE_EPOCHS = 50
GRAY_IMAGE_BATCH_SIZE = 256
# status messages
DONE = 'DONE'
SUCCESS = 'SUCCESS'
FAILED = 'FAILED'

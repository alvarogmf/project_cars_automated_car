import numpy as np
from alexnet import alexnet
import tensorflow.keras.backend as K
from tensorflow.config.experimental import list_physical_devices, set_memory_growth

physical_devices = list_physical_devices('GPU')
set_memory_growth(physical_devices[0], True)

K.clear_session()

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'model/pygta5-car-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

hm_data = 22

for i in range(EPOCHS):
    for i in range(1,hm_data+1):
        train_data = np.load('data/training_data_v3.npy'.format(i), allow_pickle=True)

        train = train_data[:-2000]
        test = train_data[-2000:]
        
        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

        model.save(MODEL_NAME)


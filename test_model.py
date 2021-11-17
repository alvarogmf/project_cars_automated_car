import os
import numpy as np
from PIL import ImageGrab
import cv2
import time
from direct_keys import PressKey, ReleaseKey, W, A, S, D
from alexnet import alexnet
from getkeys import key_check
print(1)
WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 2
MODEL_NAME = 'pygta5-car-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCHS)
MODEL_PATH = 'model/'

t_time = 0.09

print(2)
def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)


def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)


def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)

print(3)
model = alexnet(WIDTH, HEIGHT, LR)
model.load(os.path.join(MODEL_PATH, MODEL_NAME))
print(4)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    while (True):

        if not paused:
            # 800x600 windowed mode
            screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
            print('loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160, 120))
            prediction = model.predict([screen.reshape(160, 120, 1)])[0]
            print(prediction)

            turn_thresh = .75
            fwd_thresh = 0.70

            if prediction[1] > fwd_thresh:
                straight()
            elif prediction[0] > turn_thresh:
                left()
            elif prediction[2] > turn_thresh:
                right()
            else:
                straight()

        keys = key_check()

        # p pauses game and can get annoying.
        if 'Q' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)


main()

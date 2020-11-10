import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

def build_model():
    model = keras.Sequential([
    layers.Dense(32, activation='relu', input_shape=(28224,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(6)
    ])
    return model

if __name__ == '__main__':
    model = build_model()
    print('hello')
    model.summary()
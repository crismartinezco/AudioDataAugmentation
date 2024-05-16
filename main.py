import random
import librosa
import scipy
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import IPython.display as ipd
# import cv2
# import torch
# import torchaudio
# from torchaudio import transforms

# %matplotlib inline

pop_file = fr"C:\Users\LEGION\PycharmProjects\AudioDataAugmentation\Pop_voice.wav"
pop_voice, sr = librosa.load(pop_file)
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
pop_amp_to_db = librosa.amplitude_to_db(np.abs(librosa.stft(pop_voice)), ref=np.max)

# linear power spec
linear_power_spec = librosa.display.specshow(pop_amp_to_db, y_axis='linear', x_axis='time',
                                             sr=sr, ax=ax[0])
ax[0].set(title='Linear-frequency power spectrogram')
ax[0].label_outer()

# log power spec
hop_length = 1024
librosa.display.specshow(pop_amp_to_db, y_axis='log', sr=sr, hop_length=hop_length,
                         x_axis='time', ax=ax[1])
ax[1].set(title='Log-frequency power spectrogram')
ax[1].label_outer()

fig.colorbar(linear_power_spec, ax=ax, format="%+2.f dB")
#%%
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                               sr=sr, ax=ax[0])
ax[0].set(title='Linear-frequency power spectrogram')
ax[0].label_outer()

hop_length = 1024

D = librosa.amplitude_to_db(np.abs(librosa.stft(y, hop_length=hop_length)),

                            ref=np.max)

librosa.display.specshow(D, y_axis='log', sr=sr, hop_length=hop_length,

                         x_axis='time', ax=ax[1])

ax[1].set(title='Log-frequency power spectrogram')

ax[1].label_outer()

fig.colorbar(img, ax=ax, format="%+2.f dB")
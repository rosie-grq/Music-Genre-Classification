#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:24:23 2020

@author: ruoqigao
"""

import os
import librosa
from pydub import AudioSegment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import savetxt
import pickle
from matplotlib import cm
import pylab
from PIL import Image
from matplotlib.pyplot import imshow

#convert mp3 file into .wav format
rootdir = r'fma_small/'
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mp3"):
            src=os.path.join(subdir, file)
            new_name=os.path.splitext(file)[0]+'.wav'
            dst = os.path.join('All/',new_name)
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")

#Randomly extract 4 samples of 2-second audio clip from each .wav file, 
#the processed audios are saved in the folder 'Slice'
alldir=r'All/'
for subdir, dirs, files in os.walk(alldir):
    for file in files:
        if file.endswith(".wav"):
            src=os.path.join(subdir, file)
            song = AudioSegment.from_wav(src)
            #randomly extract 4 samples of 2 second audio from each wav file
            random_start=np.random.rand(4)*(song.duration_seconds-2)
            sliced_sound=AudioSegment.empty()
            for num,s in enumerate(random_start):
                two_sec_slice = song[s*1000:(s*1000+2*1000)]
                sliced_sound=two_sec_slice
                name=os.path.splitext(file)[0]+'.'+str(num)+'.wav'
                dst = os.path.join('Slice/',name)
                sliced_sound.export(dst, format="wav")
                
                img_dir =r'spec_images/'

#plot each extracted audioclip as melspectrogram and save as .jpg file
all_dir=r'slice/'
melspec_all=[]
id_all=[]
for subdir, dirs, files in os.walk(all_dir):
    for file in files:
        if file.endswith(".wav"):
            track_id=os.path.splitext(file)[0]
            id_all.append(track_id)
            wav=os.path.join(subdir, file)
            y, sr = librosa.load(wav)
            melspec = librosa.feature.melspectrogram(y=y, hop_length = hop_length, 
                                                     n_fft = n_fft, n_mels = n_mels)
            melspec = librosa.power_to_db(melspec**2)
            pylab.figure(figsize=(5,5))
            pylab.axis('off') 
            pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
            librosa.display.specshow(melspec, cmap=cm.jet)
            pylab.savefig(img_dir + track_id +'.jpg', bbox_inches=None, pad_inches=0)
            pylab.close()
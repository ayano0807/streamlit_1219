# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:22:02 2021

@author: ayano
"""

import numpy as np
import librosa

y, sr = librosa.load("_input.wav", mono=True)

# STFT
n_fft = 2048
hop_length = 512
spec = librosa.stft(y, n_fft=n_fft, hop_length=hop_length) #短時間フーリエ変換
mag, phase = librosa.magphase(spec) #振幅スペクトログラム、位相スペクトログラムを抽出
phase_rad = np.angle(phase)

mag, phase = your_processing(mag, phase)　# 時間周波数領域の処理を記載

# Inv. STFT
spec_rec = mag * phase
#spec_rec = mag * np.exp(1j * phase_rad)
y_rec = librosa.istft(spec_rec, hop_length=hop_length) #逆短時間フーリエ変換

# Dump .wav file
librosa.output.write_wav("_output.wav", y_rec, sr)

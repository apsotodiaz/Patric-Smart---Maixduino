import librosa
import numpy as np

# Cargar el archivo de audio
audio, sample_rate = librosa.load('alexis.ogg', sr=None)

# Calcular los coeficientes MFCC
mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)

# Mostrar los coeficientes MFCC resultantes
print(mfccs)
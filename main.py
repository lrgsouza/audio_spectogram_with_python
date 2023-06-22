from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

#Função responsável por gerar o gráfico em 3D
def specgram3d(y, srate, ax=None, title=None):
    if not ax:
        ax = plt.axes(projection='3d')
    ax.set_title(title, loc='center', wrap=True)
    spec, freqs, t = mlab.specgram(y, Fs=srate)
    X, Y = np.meshgrid(t, freqs)
    Z = 2.5 * np.log10(spec)
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('time (s)')
    ax.set_ylabel('frequencies (Hz)')
    ax.set_zlabel('amplitude (dB)')
    ax.set_zlim(-10, 50)
    return X, Y, Z

#Função responsável por gerar o gráfico em 3D
def specgram2d(y, srate, ax=None, title=None):
    if not ax:
        ax = plt.axes()
    ax.set_title(title, loc='center', wrap=True)
    spec, freqs, t, im = ax.specgram(y, Fs=srate, scale='dB', vmin=-10, vmax=50)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('frequencies (Hz)')
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Amplitude (dB)')
    cbar.minorticks_on()
    return spec, freqs, t, im

# Parâmetros do arquivo WAV de áudio
audio_file = 'connection_sound.wav'
srate, stereo_y = wavfile.read(audio_file)

# Converter o sinal estéreo para mono (usando média dos canais)
y = np.mean(stereo_y, axis=1)

# Título para os espectrogramas
title = audio_file

# Plotar espectrograma 2D
fig1, ax1 = plt.subplots()
specgram2d(y, srate=srate, title=title, ax=ax1)

# Plotar espectrograma 3D
fig2, ax2 = plt.subplots(subplot_kw={'projection': '3d'})
specgram3d(y, srate=srate, title=title, ax=ax2)

#Mostrar espectogramas
plt.show()


# 💻🎶 Audio Augmentation and Analysis Toolbox

This repository provides a collection of Python functions for audio augmentation, analysis, and visualization. It includes tools for adding noise within specific frequency ranges, time displacement, time stretching, and a mix of these tools, as well as various plotting utilities.

## Installation

````markdown
  
  pip install librosa numpy scipy matplotlib ipython scipy
````

## Dependencies

  - librosa
  - numpy
  - scipy (for time stretching)
  - matplotlib
  - ipython (for audio playback in notebooks)

## Usage

The functions are organized into several modules:

### 1\. Fourier Analysis

  - `fourier_db(stft)`: Computes the magnitude in decibels from an STFT.
  - `freq_filters(cents_interval)`: Creates psychoacoustically relevant frequency filters.

### 2\. Augmentation

  - `noise_in_freq_range(signal, low_freq, high_freq, noise_level_dB, band_pass=False, n_fft=2048)`: Adds or replaces noise within a specified frequency range.
  - `time_displacement(signal, noise=False, duration=5.0, n_fft=1024)`: Applies time displacement to an audio signal.
  - `time_stretch_with_padding(signal, speed_range=(0.7, 1.3), noise_level=0.001, n_fft=1024)`: Performs time stretching with padding.
  - `random_time_stretch(signal, n_fft, speed_range=(0.7, 1.3), noise_level=0.001)`: Applies random time stretching.
  - `mix_up(signal, patch, noise_level_dB, low_freq, high_freq, n_fft=1024)`: Applies a patch audio file to the original STFT within a specific frequency range.
  - `specaug_time_mask(duration, hop_length, signal_stft, patch_stft)`: Performs random time masking.
  - `specaug_freq_mask(width, signal_stft, patch_stft, n_mels, sr_signal)`: Performs random frequency masking.
  - `spec_augmentation(signal, patch, duration, hop_length, width, n_mels, n_fft)`: Combines random time and frequency masking.

### 3\. Plotting

  - `plot_spectrogram(signal, sr, title, hop_length)`: Plots a spectrogram.
  - `plot_fourier(signal, fft_freqs, title, fill_area=None, fill=False)`: Plots the Fourier transform.
  - `plot_compare(original_audio, modified_audio)`: Compares spectrograms of original and modified audio.

### 4\. Playback

  - `play_file(signal)`: Plays an audio signal in a Jupyter Notebook.

## Example

```python
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import zoom  
from IPython.display import Audio 

# Load audio
audio_file = "\path\to\audio"
signal, sr = librosa.load(audio_file, duration=5)

# Add noise in a specific frequency range
noisy_stft = noise_in_freq_range(audio_file, 500, 1000, -20, band_pass=False, n_fft=1024)
noisy_audio = librosa.istft(noisy_stft)

# Time displacement
time_displaced_stft = time_displacement(audio_file, n_fft=1024)
time_displaced_audio = librosa.istft(time_displaced_stft)

# Time stretching
time_stretched_stft = time_stretch_with_padding(audio_file, n_fft=1024)
time_stretched_audio = librosa.istft(time_stretched_stft)

# Plot spectrograms
plot_spectrogram(librosa.stft(signal), sr, "Original Spectrogram", 512) #Example hop_length
plot_spectrogram(librosa.stft(noisy_audio), sr, "Noisy Spectrogram", 512)
plot_spectrogram(librosa.stft(time_displaced_audio), sr, "Time Displaced Spectrogram", 512)
plot_spectrogram(librosa.stft(time_stretched_audio), sr, "Time Stretched Spectrogram", 512)

# Play audio in notebook
Audio(signal, rate=sr) #Original
Audio(noisy_audio, rate=sr) #Noisy
Audio(time_displaced_audio, rate=sr) #Time Displaced
Audio(time_stretched_audio, rate=sr) #Time Stretched

```

## Contributing

Contributions are welcome\! Please open an issue or submit a pull request.

## License

[MIT License](https://www.google.com/url?sa=E&source=gmail&q=LICENSE)
```
```

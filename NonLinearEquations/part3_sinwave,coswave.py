import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



def sin_wave(x):
    return np.sin(x)


def cos_wave(x):
    return np.cos(x)


x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = sin_wave(x)
z = cos_wave(x)


# plotting the sine and cosine waves
st.title("Sine and Cosine Waves")
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='blue')
plt.plot(x, z, label='Cosine Wave', color='orange')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Sine and Cosine Waves")
plt.xlabel("x (radians)")
plt.ylabel("Amplitude")
plt.legend()
st.pyplot(plt)

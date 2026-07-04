import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Point-Slope: y - y1 = m(x - x1)")

m = st.slider("slope m", -5.0, 5.0, 1.0, 0.1)
x1 = st.slider("x1", -10.0, 10.0, 0.0, 0.5)
y1 = st.slider("y1", -10.0, 10.0, 0.0, 0.5)

x = np.linspace(-10, 10, 100)
y = m * (x - x1) + y1

fig, ax = plt.subplots()
ax.plot(x, y, color="#378ADD")
ax.plot(x1, y1, "o", ms=12, color="red")
ax.axhline(0, color="gray", lw=0.5)
ax.axvline(0, color="gray", lw=0.5)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True, alpha=0.3)
st.pyplot(fig)
''' y = slop * x + intercept'''

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



st.title("Linear Equation: y = m·x + b")


m = st.slider("slope m",  -5.0 , 5.0, 1.0, 0.1 )
b = st.slider("intercept b",  -10.0 , 10.0, 0.0, 0.1 )


x= np.linspace(-10,10,100)
y = m * x + b 


fig,ax = plt.subplots()
ax.plot(x,y, color="#6B6BFA")
ax.axhline(0,color="gray",lw=0.5)
ax.axvline(0,color="gray",lw=0.5)

ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax.grid(True, alpha=0.3)

st.pyplot(fig)

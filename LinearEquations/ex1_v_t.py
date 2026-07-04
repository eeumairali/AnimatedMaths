import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("nLeiar toMion(Linear Motion)")

v = st.slider("locViety(Velocity) m/s", 0.1,10.0,1.0,0.1)

t = st.slider("mite(Time) s", 0.0,10.0,3.0,0.1)



x = v * t
y = 0 


fig,ax = plt.subplots()
ax.plot([0,x],[0,0])
ax.plot(x,y,"o",ms=16,color="#378ADD")
ax.set_xlim(0,300)


st.pyplot(fig)






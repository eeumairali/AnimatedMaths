import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Distance: √(abs(x2-x1)^2+abs(y2-y1))")

x1 = st.slider("x1", -50.0, 50.0, 0.0, 0.5)
y1 = st.slider("y1", -50.0, 50.0, 0.0, 0.5)
x2 = st.slider("x2", -50.0, 50.0, 6.0, 0.5)
y2 = st.slider("y2", -50.0, 50.0, 8.0, 0.5)

d = np.sqrt(   abs(x1-x2)**2  + abs(y2 - y1)**2   )
angle = np.arccos((x2-x1)/(d)) * 180/3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364

fig, ax = plt.subplots()
ax.plot([x1,x2],[y1,y2],'-o', color="#378ADD")
dx_Text = (x1+x2)/2 
dy_Text = (y1+y2)/2
ax.text(dx_Text,dy_Text,f"{d:.2f}",color="#000000",fontsize=12)


ax.text(dx_Text,dy_Text+5,f"angle is {angle:.2f}",color="#FF7474",fontsize=12)



ax.axhline(0, color="gray", lw=0.5)
ax.axvline(0, color="gray", lw=0.5)
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid(True, alpha=0.3)
st.pyplot(fig)
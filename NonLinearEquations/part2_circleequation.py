# formula for circule equation
# x^2 + y^2 = r^2


import streamlit as st
import matplotlib.pyplot as plt


def circle_equation(x, y, r):
    return x**2 + y**2 - r**2

# sliders
x = st.slider("X-coordinate", -10.0, 10.0, 0.0, 0.1)
y = st.slider("Y-coordinate", -10.0, 10.0, 0.0, 0.1)
r = st.slider("Radius", 0.1, 10.0, 1.0, 0.1)


st.write(f"Circle Equation: x^2 + y^2 = {r**2}")

x_start = st.number_input("Enter starting x value for plotting:", value=-10.0)
x_end = st.number_input("Enter ending x value for plotting:", value=10.0)
y_start = st.number_input("Enter starting y value for plotting:", value=-10.0)
y_end = st.number_input("Enter ending y value for plotting:", value=10.0)


# plotting the circle

plt.figure(figsize=(6, 6))
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
# plot the circle
theta = [i * 0.01 for i in range(0, 628)]
x_circle = [r * (3.14159 / 180) * (i * 180 / 3.14159) for i in theta]
y_circle = [r * (3.14159 / 180) * (i * 180 / 3.14159) for i in theta]
plt.plot(x_circle, y_circle, label=f"Circle with radius {r}")
# plot the point
plt.scatter(x, y, color='red', label=f"Point ({x}, {y})")
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Circle Equation Plot")
plt.legend()
st.pyplot(plt)


import streamlit as st
import matplotlib.pyplot as plt
from math import exp


def logistics(L, k, x, x0):
    return L / (1 + exp(-k * (x - x0)))


L = st.number_input("Enter the carrying capacity (L):", value=1.0)
k = st.number_input("Enter the growth rate (k):", value=1.0)
x0 = st.number_input("Enter the x-value of the sigmoid's midpoint (x0):", value=0.0)
x = st.number_input("Enter the x-value to evaluate the logistics function:", value=0.0)



# plotting 
n = st.number_input("Enter the number of points to plot:", value=100, step=1)
x_values = [i * 0.1 for i in range(-n, n + 1)]
y_values = [logistics(L, k, i, x0) for i in x_values]
plt.plot(x_values, y_values, label=f"Logistics Function: L={L}, k={k}, x0={x0}")
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Logistics Function Plot")
plt.xlabel("x")
plt.ylabel("f(x)")  
st.pyplot(plt)


import streamlit as st
import matplotlib.pyplot as plt


from math import log as ln
def log_andy(a, b, x):
    return a*ln(x)*b


a = st.number_input("Enter the coefficient a:", value=1.0)
b = st.number_input("Enter the coefficient b:", value=1.0)
x = st.number_input("Enter the value of x:", value=1.0) 


st.write(f"The result of the logarithmic function is: {log_andy(a, b, x)}")

# plotting
plt.figure(figsize=(10, 5))
n = st.number_input("Enter the number of points to plot:", value=100, step=1)
x_values = [i * 0.1 for i in range(1, n + 1)]
y_values = [log_andy(a, b, i) for i in x_values]
plt.plot(x_values, y_values, label=f"Logarithmic Function: {a}*ln(x)*{b}")
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Logarithmic Function Plot")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
st.pyplot(plt)
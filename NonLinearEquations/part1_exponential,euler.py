import streamlit as st
import matplotlib.pyplot as plt
# exponential function
def exponential(x):
    return 2.71828**x

def euler_method(x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        y += h * exponential(x)
        x += h
    return y

if __name__ == "__main__":
    st.title("Euler's Method for Exponential Function")
    
    x0 = st.number_input("Enter initial x value (x0):", value=0.0)
    y0 = st.number_input("Enter initial y value (y0):", value=1.0)
    h = st.number_input("Enter step size (h):", value=0.1)
    n = st.number_input("Enter number of steps (n):", value=10, step=1)

    result = euler_method(x0, y0, h, n)
    st.write(f"Approximate value of y after {n} steps: {result}")


    # plot
    x_values = [x0 + i * h for i in range(n + 1)]
    y_values = [y0]
    for i in range(n):
        y_values.append(y_values[-1] + h * exponential(x_values[i]))
    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Euler's Method for Exponential Function")
    st.pyplot(plt)
# Nonlinear Equations Reference Guide

This document outlines various mathematical formulas for classic nonlinear paths and functions, building upon the foundational components (Exponential, Circular, and Trigonometric waves) covered in parts 1–3.

---

## 1. Quadratic (Parabolic) Curves
Creates a distinct U-shaped curve. It models gravitational trajectories, projectile physics, and simple acceleration.

*   **Mathematical Formula:** 
    $$y = ax^2 + bx + c$$
*   **Key Behavior:** The rate of change increases linearly, causing the value of $y$ to grow quadratically with $x$.
*   **Suggested Filename:** `part4_parabola,quadratic.py`

---

## 2. Logarithmic Functions
The inverse of exponential functions. These curves feature rapid initial vertical growth that slows drastically over time, creating a flattening profile.

*   **Mathematical Formula:** 
    $$y = a \cdot \ln(x) + b$$
*   **Key Behavior:** Defined only for $x > 0$. As $x$ approaches $0$, $y$ goes to negative infinity. As $x$ increases, the growth rate approaches zero.
*   **Suggested Filename:** `part5_logarithmic.py`

---

## 3. Rational (Hyperbolic) Relationships
Creates asymptotic curves that approach but never quite touch the structural axes. Excellent for modeling inverse relationships such as the inverse-square law of light or gravitational degradation.

*   **Mathematical Formula:** 
    $$y = \frac{k}{x}$$
*   **Key Behavior:** Undefined at $x = 0$ (vertical asymptote). As $x \to \infty$, $y \to 0$ (horizontal asymptote).
*   **Suggested Filename:** `part6_hyperbola,rational.py`

---

## 4. Cubic Polynomials
An elegant "S-curve" that changes direction twice over its span. It is widely used in spline math, computer graphics pathfinding, and smooth transitions.

*   **Mathematical Formula:** 
    $$y = ax^3 + bx^2 + cx + d$$
*   **Key Behavior:** Contains up to two local extrema (a peak and a valley) depending on coefficients, crossing from negative infinity to positive infinity.
*   **Suggested Filename:** `part7_cubic,polynomial.py`

---

## 5. Logistic (Sigmoid) Easing
A bounded S-curve that models natural limits. It maps any real-valued number into a clean range between 0 and 1, starting slowly, accelerating through the center, and leveling off.

*   **Mathematical Formula:** 
    $$y = \frac{L}{1 + e^{-k(x - x_0)}}$$
*   **Key Behavior:** Strictly bounded between $0$ and $L$. Widely used for population growth thresholds, neural network activation layers, and animation easing.
*   **Suggested Filename:** `part8_sigmoid,logistic.py`
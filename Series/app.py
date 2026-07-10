import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from arithmetic_funs import arith_sum_of_nth_term, arith_nth_term,sum_expended
from geometric_funs import geo_nth_term, geo_sum_nth_terms, geo_infinity_sum
from harmonic_funs import harmonic_num, harominic_nth_term, asym_aprox


st.title("Series")

st.write("1 3 5 7 --- 19")
st.write("in the example above, a1=1, d=2, n=last number position which is 10, and an=19(last value)")
d_arith = st.slider("d_arith", -100.0, 100.0, 2.0, 1.0)

n_arith = st.slider("n_arith", -100.0, 100.0, 10.0, 1.0)

a1_arith = st.slider("a1_arith", -100.0, 100.0, 1.0, 1.0)

an_arith = st.slider("a_n_arith", -100.0, 100.0, 19.0, 1.0)


x = arith_nth_term(a1_arith, n_arith, d_arith, ) # 1 4 7 10
st.write(x,"arithmetic nth term")

st.write(arith_sum_of_nth_term(n_arith, a1_arith, an_arith), "sum of nth term") # sum of 100 terms -> 14950
st.write(sum_expended(n_arith, a1_arith, d_arith), "sum expanded")    # same -> 14950

st.title("Geometric Series")
st.write("1 4 16 64 . . . 7th")
r_geometric = st.slider("r_geometric", -10.0, 10.0, 0.0, 0.5)
n_geometric = st.slider("n_geometric", -10.0, 10.0, 3.0, 0.5)
a1_geometric = st.slider("a1_geometric", -10.0, 10.0, 1.0, 0.5)

st.write(geo_nth_term(a1_geometric, r_geometric, n_geometric), "geometric nth term")
st.write(geo_sum_nth_terms(a1_geometric, r_geometric, n_geometric), "sum of nth terms")
st.write(geo_infinity_sum(a1_geometric, r_geometric), "infinite sum")

st.title("Harmonic Series")
st.write("1 1/2 1/3 1/4 . . . 1/n")
n_harmonic = st.slider("n_harmonic", -100.0, 100.0, 10.0, 1.0)
k_harmonic = st.slider("k_harmonic", -100.0, 100.0, 1.0, 1.0)
a1_harmonic = st.slider("a1_harmonic", -100.0, 100.0, 1.0, 1.0)
d_harmonic = st.slider("d_harmonic", -100.0, 100.0, 1.0, 1.0)
lbda_harmonic = st.slider("lambda_harmonic", -100.0, 100.0, 0.5772156649, 0.0000000001)   

st.write(harmonic_num(n_harmonic, k_harmonic), "harmonic number")
st.write(harominic_nth_term(a1_harmonic, n_harmonic, d_harmonic), "harmonic nth term")
st.write(asym_aprox(n_harmonic, lbda_harmonic), "asymptotic approximation")   


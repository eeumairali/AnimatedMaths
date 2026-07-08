import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from arithmetic_funs import arith_sum_of_nth_term, arith_nth_term,sum_expended

st.title("Series")

st.write("1 3 5 7 --- 19")
st.write("in the example above, a1=1, d=2, n=last number position which is 10, and an=19(last value)")
d = st.slider("d", -100.0, 100.0, 2.0, 1.0)

n = st.slider("n", -100.0, 100.0, 10.0, 1.0)

a1 = st.slider("a1", -100.0, 100.0, 1.0, 1.0)

an = st.slider("a_n", -100.0, 100.0, 19.0, 1.0)


x = arith_nth_term(a1, n, d, ) # 1 4 7 10
st.write(x,"arithmetic nth term")

st.write(arith_sum_of_nth_term(n, a1, an), "sum of nth term") # sum of 100 terms -> 14950
st.write(sum_expended(n, a1, d), "sum expanded")    # same -> 14950



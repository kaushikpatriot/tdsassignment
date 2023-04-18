import streamlit as st

def maximum(n1,n2,n3):
    return max(n1,n2,n3)

st.title("Find the biggest number")
n1= int(st.number_input("Number 1"))
n2= int(st.number_input("Number 2"))
n3= int(st.number_input("Number 3"))
maxnum=maximum(n1,n2,n3)
st.title(maxnum)
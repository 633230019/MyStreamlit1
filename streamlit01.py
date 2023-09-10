import streamlit as st

st.title('My title')
col1, col2 = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")
with col1:
    st.header("A")
with col2:
    st.image("./pic/iris1.jpg")

st.header('สิทธิพงษ์')
st.subheader('My sub')

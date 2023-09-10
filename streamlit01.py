import streamlit as st

st.title('ทดสอบการเขียนเว็บด้วย Streamlit')
col1, col2 = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")
with col1:
    st.header("Iris")
    st.image("./pic/iris1.jpg")
with col2:
    st.header("สิทธิพงษ์ แจ้งไพร")
    st.text("สาขาเทคโนโลยีสารสนเทศ")
    st.write("คณะวิทยาศาสตร์และเทคโนโลยี")    
    st.markdown("มหาวิทยาลัยราชภัฏนครปฐม")


st.header('สิทธิพงษ์ แจ้งไพร')
st.subheader('My sub')

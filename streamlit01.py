import streamlit as st
import pandas as pd

st.title('ทดสอบการเขียนเว็บด้วย Streamlit')
col1, col2 = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")
with col1:
    st.image("./pic/iris1.jpg")
with col2:
    st.header("สิทธิพงษ์ แจ้งไพร")
    st.text("สาขาเทคโนโลยีสารสนเทศ")
    st.write("คณะวิทยาศาสตร์และเทคโนโลยี")    
    st.markdown("มหาวิทยาลัยราชภัฏนครปฐม")

html_1 = """
<div style="background-color:#ABEBC6;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

colx1, colx2, colx3 = st.columns(3)
with colx1:
    st.image("./pic/iris1.jpg")
with colx2:
    st.image("./pic/iris2.jpg")
with colx3:
    st.image("./pic/iris3.jpg")    

dt = pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("show chart"):
    st.bar_chart(dx2)
    st.button("Don't show chart")
else:
    st.button("Don't show chart")
    

import streamlit as st

def bless_for_gaokao(name):
    return (
        f"亲爱的{name}：\n"
        "高考在即，希望你考的全会，蒙的全对，\n"
        "所有努力都能在考场上得到回报，\n"
        "相信你自己呀！，\n"
        "你是最棒的，\n"
        "金榜题名，前程似锦！\n"
        "加油！"
    )

st.title("高考祝福小程序")
name = st.text_input("请输入你的名字：", "")
if st.button("获取祝福"):
    if name:
        st.success(bless_for_gaokao(name))
    else:
        st.warning("请输入名字哦！")

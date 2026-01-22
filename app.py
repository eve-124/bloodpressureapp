import streamlit as st

st.markdown(
    """
    <style>
    input[type="number"] {
        font-size: 22px;
        height: 3em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='font-size:28px; text-align:center;'>血圧・脈拍 平均計算</h2>",
    unsafe_allow_html=True
)

max_list = []
min_list = []
num_list = []

for i in range(3):
    st.markdown(
    f"<h5 style='text-align:center;'>{i+1}回目</h5>",
    unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)

    with col1:
        max_list.append(
            st.number_input(
                "最高",
                min_value=50,
                max_value=250,
                value=None,
                step=1,
                key=f"max{i}"
            )
        )

    with col2:
        min_list.append(
            st.number_input(
                "最低",
                min_value=30,
                max_value=150,
                value=None,
                step=1,
                key=f"min{i}"
            )
        )

    with col3:
        num_list.append(
            st.number_input(
                "脈拍",
                min_value=30,
                max_value=200,
                value=None,
                step=1,
                key=f"num{i}"
            )
        )

if st.button("平均を計算"):
    if None in max_list or None in min_list or None in num_list:
        st.warning("すべて入力してください")
    else:
        st.markdown(
    "<div style='text-align:center; font-size:16px; color:gray;'>平均</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style='text-align:center; font-size:32px; font-weight:600;'>
        最高：{sum(max_list) // 3}<br>
        最低：{sum(min_list) // 3}<br>
        脈拍：{sum(num_list) // 3}
    </div>
    """,
    unsafe_allow_html=True
)
        
st.set_page_config(
    page_title="血圧計算",
    layout="centered"
)







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
    st.subheader(f"{i+1}回目")

    col1, col2, col3 = st.columns(3)

    with col1:
        max_list.append(
            st.number_input(
                "最高",
                min_value=50,
                max_value=250,
                value=120,
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
                value=80,
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
                value=70,
                step=1,
                key=f"num{i}"
            )
        )

if st.button("平均を計算"):
    st.header("〔平均〕")
    st.write(f"最高：{sum(max_list) // 3}")
    st.write(f"最低：{sum(min_list) // 3}")
    st.write(f"脈拍：{sum(num_list) // 3}")

st.set_page_config(
    page_title="血圧計算",
    layout="centered"
)




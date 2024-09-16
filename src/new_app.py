import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit_option_menu
from streamlit_option_menu import option_menu
import numpy as np

# 데이터 로드
temp_df = sns.load_dataset('iris')

# side bar
with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,

  )
  if selected == "Home":
        st.header('Snowflake Healthcare App')
        # Create a row layout
        c1, c2= st.columns(2)
        c3, c4= st.columns(2)

        with st.container():
            c1.write("c1")
            c2.write("c2")

        with st.container():
            c3.write("c3")
            c4.write("c4")

        with c1:
            chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
            st.area_chart(chart_data)
            
        with c2:
            chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
            st.bar_chart(chart_data)

        with c3:
            chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
            st.line_chart(chart_data)

        with c4:
            chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
            st.line_chart(chart_data)

  if selected == "Projects":
    st.write("### Sepal Length vs Sepal Width Scatter Plot")
    sns.set_style('whitegrid')
    fig, ax = plt.subplots()
    sns.scatterplot(
        data=temp_df,
        x='sepal_length',
        y='sepal_width',
        hue='species',
        ax=ax
    )

    # 차트 출력
    st.pyplot(fig)


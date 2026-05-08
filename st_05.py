import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.write('## aaaaaaaaaaa')

# 예제 1

st.write('Hello, *World!* :sunglasses:')

# 예제 2

st.write(1234)

# 예제 3

df = pd.DataFrame({
     '첫 번째 컬럼': [1, 2, 3, 4],
     '두 번째 컬럼': [10, 20, 30, 40]
     })
st.write(df)

# 예제 4

st.write('아래는 DataFrame입니다.', df, '위는 dataframe입니다.')

# 예제 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# matplotlib, seaborn, pandas의 plot도 st.write로 출력 가능
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots()    # fig - axis
sns.scatterplot(x='a', y='b', size='c', hue='c', data=df2, ax=ax)
st.write(fig)


# streamlit은 matplotlib과 연결되어 있어서
# matplotlib 계열(matplotlib, pandas)의 plot streamlit으로 출력 가능
fig, ax = plt.subplots()        # 객체, 절차
# df2.plot.scatter(x='a',y='b',c='c',s=(df2['c']+4)*10,ax=ax)
df2['size'] = (df2['c']+4)*10
df2.plot.scatter(x='a',y='b',c='c',s='size',ax=ax)
st.write(fig)

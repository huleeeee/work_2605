import pandas as pd
import streamlit as st


FILE_PATH_A = '../[3]시각화/data/heart_failure_a.json'
FILE_PATH_B = '../[3]시각화/data/heart_failure_b.json'

df_a = pd.read_json(FILE_PATH_A)
df_b = pd.read_json(FILE_PATH_B)

df = pd.merge(df_a, df_b, on='person_id', how='inner')

dropped_num = len(df_a) - len(df) + len(df_b) - len(df)

# set(df_a['person_id']) - set(df['person_id'])
# set(df_b['person_id']) - set(df['person_id'])


# 그대로 streamlit으로 구현
import seaborn as sns
import matplotlib.pyplot as plt

a = sns.jointplot(df, x='ejection_fraction', y='age', hue='DEATH_EVENT')

# st.pyplot(a.fig)
st.write(a.figure)



# - 스모킹 여부를 한꺼번에 표시하지 말고 라디오로 선택하여 다른 그래프를 볼 수 있도록 구현
smoking_option = st.radio('흡연 여부 선택', 
                          options=[0, 1], 
                          format_func=lambda x:'비흡연자' if x == 0 else '흡연자')

df2 = df[df['smoking'] == smoking_option]

b = sns.violinplot(df2, 
                   x='DEATH_EVENT', 
                   y='platelets', 
                   hue='smoking', 
                   split=True)

st.write(b.figure)



# 심박출(ejection_fraction)로 범위를 한정하여 그래프 구현
# 심박출의 범위는 slider로 선택
ef_range = st.slider('심박출의 범위 선택', 
                     min_value=int(df['ejection_fraction'].min()),
                     max_value=int(df['ejection_fraction'].max()),
                     value=(int(df['ejection_fraction'].min()),
                            int(df['ejection_fraction'].max())))

df3 = df[(df['ejection_fraction'] >= ef_range[0]) & df['ejection_fraction'] <= ef_range[1]]

c, ax = plt.subplots(figsize=(8, 5))

sns.histplot(df3, x='time', bins=20, hue='DEATH_EVENT', ax=ax)

st.write(c.figure)


# 구현 후 git에 업로드하고,
# streamlit cloud로 호스팅 (git과 연동)
# 접속해서 확인할 수 있도록 해서 링크 제출!!!
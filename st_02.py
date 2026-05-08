# 이 python 코드 자체를 문서처럼 생각하면 됨
# 소스코드가 입력된 순서대로 문서가 만들어짐

import streamlit as st

st.header('st.button')


# st.write는 문서에 텍스트 추가하는 함수
# st.write는 다양한 데이터 타입을 지원. 텍스트,숫자,데이터프레임,이미지
st.write('버튼을 눌렀을 때, 특정 행동을 하도록 할 수 있습니다.')
st.write(3)

import pandas as pd
st.write(pd.Series([1,2,3,4,5]))

# 버튼을 누르면 페이지 갱신됨
# 맨 위부분 부터 다시 실행
# 다시 실행할 때 리턴값이 달라짐
# -> 최초 실행할 때는 버튼 생성 후 False 리턴. 기본값
# -> 버튼 누르면 버튼 생성되고 True 리턴. 눌렀을때

# a =  st.button('나를 눌러주세요!')

# st.write("버튼을 눌렀는지 여부: ",  a)

# if a:
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')


# 버튼 누를때마다 출력 숫자 증가
if 'count' not in st.session_state:
    st.write("초기화!")
    st.session_state.count = 0
else:
    st.write("이미 초기화 됨...")


a =  st.button('나를 눌러주세요!')

if a:
    st.session_state['count'] += 1

st.write(st.session_state.count)

import streamlit as st
st.title('동물 이미지 찾아주기!!!🐱')
keyword = st.text_input("영어로 동물 이름을 적어주세요")
newkeyword = keyword.lower()

if st.button('찾아보기'):
    url = 'https://edu.spartacodingclub.kr/random/?'+keyword
    url = 'https://edu.spartacodingclub.kr/random/?'+newkeyword
    st.image(url)
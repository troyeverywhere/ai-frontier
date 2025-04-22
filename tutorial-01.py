import streamlit as st

st.set_page_config(page_title="컴포넌트 소개", page_icon="🧩", layout="centered")

st.title("🧩 Streamlit 컴포넌트 체험하기")
st.markdown("하나씩 주석을 풀어서 어떤 역할인지 확인해보세요!")

# --------------------------------------------
# 1️⃣ 텍스트 출력 컴포넌트
st.header("1. 텍스트 출력")
st.text("이건 일반 텍스트예요.")
st.markdown("**이건 굵은 텍스트**입니다. _이탤릭도 되고요!_")
st.code("print('Hello, world!')", language="python")
st.write("숫자도 됩니다:", 123)

# --------------------------------------------
# 2️⃣ 버튼 컴포넌트
st.header("2. 버튼")
if st.button("여기를 눌러보세요"):
    st.success("오! 버튼이 눌렸어요.")

# --------------------------------------------
# 3️⃣ 텍스트 입력
st.header("3. 텍스트 입력")
name = st.text_input("이름을 입력해보세요")
if name:
    st.write(f"안녕하세요, {name}님!")

# --------------------------------------------
# 4️⃣ 숫자 입력
st.header("4. 숫자 입력")
age = st.number_input("나이를 입력해주세요", min_value=0, max_value=120)
st.write(f"당신의 나이는 {age}세입니다.")

# --------------------------------------------
# 5️⃣ 체크박스
st.header("5. 체크박스")
like = st.checkbox("스트림릿 좋아하세요?")
if like:
    st.balloons()

# --------------------------------------------
# 6️⃣ 선택박스
st.header("6. 선택박스")
color = st.selectbox("좋아하는 색깔은?", ["빨강", "초록", "파랑", "보라"])
st.write(f"선택하신 색깔은 {color}입니다.")

# --------------------------------------------
# 7️⃣ 멀티셀렉트
st.header("7. 멀티셀렉트")
hobbies = st.multiselect("취미를 선택하세요", ["영화", "운동", "게임", "그림"])
st.write("선택한 취미:", hobbies)

# --------------------------------------------
# 8️⃣ 슬라이더
st.header("8. 슬라이더")
mood = st.slider("오늘의 기분은?", 0, 100, 50)
st.progress(mood / 100)

# --------------------------------------------
# 9️⃣ 파일 업로드
st.header("9. 파일 업로드")
file = st.file_uploader("파일을 올려보세요 (예: .txt, .csv)")
if file:
    st.success("파일이 업로드되었습니다.")

# --------------------------------------------
# 🔟 이미지 출력
st.header("10. 이미지 출력")
st.image("https://i.imgur.com/IKZC9Ld.png", caption="스트림릿은 사랑입니다", width=200)

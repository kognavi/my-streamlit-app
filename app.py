import streamlit as st

st.title('My First Streamlit App')
st.write('Hello, Streamlit!')

# ボタンを作成
if st.button('Click Me'):
    st.write('Button clicked!')

# チェックボックスを作成
if st.checkbox('Show/Hide'):
    st.write('Checkbox is checked!')

# スライダーを作成
age = st.slider('Select your age', 0, 130, 25)
st.write(f"Your age is {age}")

# テキスト入力を表示
name = st.text_input('Enter your name', 'Type here...')
if name != 'Type here...':
    st.write(f'Hello, {name}!')

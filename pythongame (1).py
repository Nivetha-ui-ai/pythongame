import streamlit as st
import random

st.set_page_config(page_title="Guess the Number Game", page_icon="🎯")

st.title("🎯 Guess the Number Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.warning("Try a higher number!")
    elif guess > st.session_state.number:
        st.warning("Try a lower number!")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
streamlit run guess_the_number.py lt --port 8501



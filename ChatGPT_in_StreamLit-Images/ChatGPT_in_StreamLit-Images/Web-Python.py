import openai
import streamlit as st

openai.api_key = "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"

comment = "Don't write anything except Code even don't write that I can do this and that...."

def get_answer(q):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=q,
    temperature=1,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response["choices"][0]["text"]

def Code(q):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"You are expert Python Programmer for over 20 Years. You have to help me out with the Problem and convert in into a code that can solve my Problem. My Problem: {q}. Please code it with Python and don't implement any comments.{comment}",
    temperature=1,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response["choices"][0]["text"]

__name__ == "ChatGPT"

st.title("Ask Anything")
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)

st.title("Code")
code_question = st.text_input("What you want to convert to a code")

if st.button("Code it in Python"):
    code = Code(code_question)
    st.write(f"```\n{code}\n```")
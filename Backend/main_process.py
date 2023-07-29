import streamlit as st
from Backend import get_text, get_chunks,\
    get_vectorstore, get_conversation_chain, get_answers


def main_process_home(audio, question):
    raw_text = get_text.get_pdf(audio)
    text_chunks = get_chunks.get_chunks(raw_text)
    vector_store = get_vectorstore.embed_n_vectorstore(text_chunks)
    # prompt
    get_answers.answer_user_question_home(question)


def main_process_meetings(audio, question):
    raw_text = get_text.get_pdf(audio)
    text_chunks = get_chunks.get_chunks(raw_text)
    vector_store = get_vectorstore.embed_n_vectorstore(text_chunks)
    st.session_state.conversation = get_conversation_chain.get_conversation_chain_home(vector_store)
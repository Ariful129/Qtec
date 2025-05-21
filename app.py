import streamlit as st
from chat_parser import parse_chat_folder

# Title for the app
st.title("AI Chat Log Analysis and Summary")

# Folder input box for user
folder_path = st.text_input("Enter folder path containing chat logs:", value="input")

# Button to generate summary
if st.button("Generate Summary"):
    if folder_path:
        summary = parse_chat_folder(folder_path)
        if summary.strip():
            st.text_area("Summary", summary, height=400)
        else:
            st.warning("No valid chat logs found.")
    else:
        st.error("Please provide a valid folder path.")

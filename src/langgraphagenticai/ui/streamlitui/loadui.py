import os
import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import Config
from dotenv import load_dotenv



class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title = " 🤖 " + self.config.get_page_title() ,layout = "wide") 
        st.header(" 🤖 " + self.config.get_page_title()) 



        with st.sidebar:
            #Get Options from Config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_use_case_options()

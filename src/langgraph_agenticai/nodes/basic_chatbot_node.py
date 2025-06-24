from langgraph.graph import START,END
import os
from src.langgraph_agenticai.state.state import State
from typing_extensions import TypedDict
from typing import Annotated

class BasicChatbotNode:
    """
    Basic Chatbot login Implementation
    """
    def __init__(self,model):
        self.llm = model

    def process(self,state:State)->dict:
        """
        Process the Input state and genetraes a chatbot responses
        """
        return {"messages":self.llm.invoke(state['message'])}
    

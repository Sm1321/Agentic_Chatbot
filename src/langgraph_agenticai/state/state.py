import os
from pydantic import Field,BaseModel
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from src.langgraph_agenticai.state.state import State


class State(TypedDict):
    """
    Represent the Structure of the state used in the Graph
    """
    message : Annotated[list,add_messages]







import os
from typing_extensions import TypedDict,List
from langgraph.graph.messages import add_messages
from typing import Annotated





class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    message : Annotated[list,add_messages]

import os 
from langgraph.graph import StateGraph,START,END
from src.langgraph_agenticai.state.state import State
from src.langgraph_agenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_graph(self):
        """
        Builds a Basic Chatbot graph using the Langgraph.
        This Method initializes a chatbot node using the 'BasicChatbotNode' Class
        and integrates it into the graph. the Chatbot node is set as both the
        entry and exit point of the graph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_graph.process)
        self.graph_builder.add(START,"chatbot")
        self.graph_builder.add("chatbot",END)
import os
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langgraph.checkpoint.memory import MemorySaver

# 1. Define the State with message history support
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 2. Setup the LLM (Mistral is excellent for coding/math)
# 2. Setup the LLM (Using a stable, non-deprecated model)
llm_endpoint = HuggingFaceEndpoint(
    # Llama-3-8B is currently one of the most stable and performant options
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct", 
    task="text-generation",
    max_new_tokens=512,
    # Ensure this environment variable is set or paste your token string
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN") 
)
model = ChatHuggingFace(llm=llm_endpoint)

# 3. Define the Node
def call_model(state: State):
    # The model receives the full history stored in 'messages'
    response = model.invoke(state["messages"])
    return {"messages": [response]}

# 4. Build the Graph with Persistence
workflow = StateGraph(State)
workflow.add_node("agent", call_model)
workflow.add_edge(START, "agent")
workflow.add_edge("agent", END)

# Adding memory allows the 'thread_id' to work
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# --- Test Run: 3 Sequential Queries ---
config = {"configurable": {"thread_id": "logic-test-101"}}

queries = [
    "Coding: Write a Python function to reverse a string.",
    "Math: Using the power rule, what is the derivative of x^2 + 5x?",
    "General: Who painted the Mona Lisa and did I ask you about Python earlier?"
]

for query in queries:
    print(f"\n--- User Query: {query} ---")
    # input_data matches the State TypedDict
    input_data = {"messages": [("user", query)]}
    
    for event in app.stream(input_data, config, stream_mode="values"):
        # Grab the most recent message from the state
        if "messages" in event:
            last_msg = event["messages"][-1]
    
    print(f"Assistant: {last_msg.content}")

import os
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langgraph.checkpoint.memory import MemorySaver

# 1. Define the State
class State(TypedDict):
    # 'messages' stores the raw chat history
    messages: Annotated[list, add_messages]
    # 'clarified_question' stores the output of the first agent
    clarified_question: str

# 2. Setup the LLM (Using a stable model to avoid 410 Errors)
llm_endpoint = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=512,
    huggingfacehub_api_token="YOUR_HF_TOKEN_HERE" # Replace with your token
)
model = ChatHuggingFace(llm=llm_endpoint)

# 3. Define the "Question Analyzer" Node
def question_analyzer(state: State):
    last_user_msg = state["messages"][-1].content
    prompt = f"Rewrite the following user query to be more precise and detailed for an AI assistant: {last_user_msg}"
    
    response = model.invoke([("system", "You are a prompt engineer."), ("user", prompt)])
    # We update the 'clarified_question' field in the state
    return {"clarified_question": response.content}

# 4. Define the "Answer Generator" Node
def answer_generator(state: State):
    # This agent uses the result from the previous node
    refined_query = state["clarified_question"]
    
    response = model.invoke([
        ("system", "Answer the user question accurately."),
        ("user", refined_query)
    ])
    return {"messages": [response]}

# 5. Build the Graph
workflow = StateGraph(State)

workflow.add_node("analyzer", question_analyzer)
workflow.add_node("generator", answer_generator)

# Direct linear flow: Start -> Analyzer -> Generator -> End
workflow.add_edge(START, "analyzer")
workflow.add_edge("analyzer", "generator")
workflow.add_edge("generator", END)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# --- Test with the 3 categories ---
config = {"configurable": {"thread_id": "multi-agent-test"}}
queries = [
    "Coding: Python reverse string",
    "Math: d/dx of x^2 + 5x",
    "General: Mona Lisa painter"
]

for q in queries:
    print(f"\n--- Original: {q} ---")
    inputs = {"messages": [("user", q)]}
    
    # We use stream_mode="values" to watch the state update
    for event in app.stream(inputs, config, stream_mode="values"):
        if "clarified_question" in event and not "messages" in event:
            print(f"Analyzer output: {event['clarified_question'][:100]}...")
        
        if "messages" in event and len(event["messages"]) > (inputs["messages"].__len__()):
            last_msg = event["messages"][-1]
            
    print(f"Final Answer: {last_msg.content.strip()}")

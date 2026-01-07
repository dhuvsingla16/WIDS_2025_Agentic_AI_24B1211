# WIDS_2025_Agentic_AI_24B1211
# Learning Agentic AI  
## Concepts, Architectures, and Execution

This repository documents my learning journey into Agentic AI, with an emphasis on theory, architectural thinking, and execution workflows rather than only code outputs.

The code present in this repository serves as proof of execution for the concepts learned through lectures, readings, and hands-on experimentation.

---

## Purpose of This Repository

The goal of this repository is to demonstrate:

- Conceptual understanding of Agentic AI systems  
- How modern LLM-based agents are architected  
- The transition from LLM usage to agent workflows and multi-agent reasoning  
- Practical execution of these ideas using open-source tools  

Rather than treating assignments as isolated tasks, this repository reflects a continuous learning pipeline.

---

## Learning Flow Followed

My learning progressed through the following conceptual stages:

1. Understanding LLMs as probabilistic text generators  
2. Learning how tasks are abstracted using pipelines  
3. Running and controlling open-source models  
4. Understanding agents as stateful decision systems  
5. Moving from single-call LLMs to graph-based and multi-agent workflows  

Each stage is backed by small executable experiments referenced throughout the repository.

---

## Core Tools and Ecosystem

### Libraries and Frameworks
- Hugging Face Transformers  
- LangChain  
- LangGraph  

### Open-Source Models Used
- BART  
- Qwen  
- LLaMA  
- Zephyr  

### Conceptual Exposure
- Retrieval-Augmented Generation (RAG)  
- Agent-to-Agent (A2A) communication  
- Multi-agent supervision patterns  

---

## Part 1 — LLM Fundamentals (Theory and Execution)

### Theory

From videos and documentation, I learned that an LLM is not a chatbot but a general-purpose language engine. The same model can generate text, summarize information, or classify sentiment depending on how the task is framed.

Hugging Face pipelines abstract tokenization, model loading, and inference execution, allowing developers to focus on reasoning and usage rather than internal mechanics.

---

### Execution

To validate these concepts, I executed three representative tasks:

- Summarization for information compression  
- Text generation for probabilistic continuation  
- Sentiment analysis for classification with confidence scores  

The code demonstrates pipeline initialization, parameter control, and batch inference.

Code references:
text_summarization.py
text_generation.py
sentiment_analysis.py


---

### Relevance to Agentic AI

Agents rely on these primitives to read and compress context, generate plans and actions, and interpret user intent and sentiment. These tasks form the cognitive building blocks of agent systems.

---

## Part 2 — From LLM Calls to Agent Architecture

### Conceptual Shift

A key realization from Agentic AI and LangGraph material is that an agent is not an LLM call but a control system built around an LLM.

Agents require state, memory, flow control, and decision boundaries. LangGraph enables this structured approach.

---

## LangGraph: Graph-Based Reasoning

### Theory

LangGraph introduces nodes as reasoning steps, edges as execution flow, and state as shared memory across steps. This approach aligns more closely with systems engineering than prompt engineering.

Key ideas:
- LLMs are stateless  
- Agents become intelligent by persisting state  
- Graphs enforce determinism and debuggability  

---

### Execution: Single-Agent with Memory

I implemented a single-agent LangGraph with persistent message history and sequential queries within the same thread.

This showed that memory enables contextual continuity and changes agent behavior meaningfully.

Code reference:
langgraph_single_agent_memory.py

---

### Architectural Insight

Agents can be described as:

LLM + state + execution loop

Memory is an architectural requirement, not a feature, and agent behavior emerges from history combined with control flow.

---

## Part 3 — Multi-Step and Multi-Agent Reasoning

### Theory

Multi-agent reasoning emphasizes decomposition of complex problems, specialization of agent roles, and structured collaboration. These ideas parallel compiler pipelines, human problem-solving, and distributed systems.

---

### Execution: Two-Agent Sequential Workflow

To demonstrate this, I implemented a two-agent workflow:
- A question analyzer that refines user queries  
- An answer generator that produces the final response  

Shared state passes information between agents, enabling sequential reasoning.

Code reference:
langgraph_two_agent_pipeline.py


---

### Key Insight

Multi-agent systems are not about using more LLMs but about better orchestration. LangGraph provides a clean framework for this orchestration.

---

## High-Level Architectural Takeaways

- Prompting alone is not architecture  
- Agents require state, memory, and flow control  
- Graph-based execution shifts thinking from asking questions to designing decision flows  

This shift represents the core transition into Agentic AI.

---

## Future Direction

This repository will later expand into:
- Tool-using agents  
- Retrieval-Augmented Generation (RAG)  
- Agent supervisors  
- Agent-to-Agent communication  
- UI-backed agents  

---

## Final Reflection

This repository emphasizes learning over polish. The focus is on understanding how agents think, validating theory through minimal execution, and building intuition before scale.

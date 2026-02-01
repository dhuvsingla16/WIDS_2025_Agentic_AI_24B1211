# WIDS_2025_Agentic_AI_24B1211
## Agentic AI — Concepts, Architectures, and Execution

This repository documents a structured learning journey into Agentic AI, focusing on architectural reasoning, system design, and controlled execution rather than isolated model usage.

The code included serves as proof of execution for the theoretical concepts studied through lectures, readings, and hands-on experimentation.

---

## Repository Objectives

This repository demonstrates:

- Conceptual understanding of Agentic AI systems  
- Architectural patterns for LLM-based agents  
- Transition from single-call LLM usage to multi-agent workflows  
- Practical implementation using open-source ecosystems  

The work is organized as a continuous learning pipeline rather than discrete assignments.

---

## Learning Progression

The learning process followed these conceptual stages:

1. Understanding LLMs as probabilistic language models  
2. Abstracting tasks using pipelines  
3. Executing and controlling open-source models  
4. Viewing agents as stateful control systems  
5. Designing graph-based and multi-agent workflows  

Each stage is supported by executable experiments included in the repository.

---

## Tools and Ecosystem

### Frameworks and Libraries
- Hugging Face Transformers  
- LangChain  
- LangGraph  

### Models Explored
- BART  
- Qwen  
- LLaMA  
- Zephyr  

### Core Concepts
- Retrieval-Augmented Generation (RAG)  
- Agent supervision and orchestration  
- Agent-to-Agent communication  

---

## Part I — LLM Fundamentals

### Conceptual Understanding

LLMs are general-purpose language engines rather than chatbots. Their behavior depends on task framing rather than internal specialization.

Hugging Face pipelines abstract tokenization, inference, and execution, allowing focus on reasoning rather than implementation details.

---

### Executed Tasks

The following tasks were implemented to validate foundational concepts:

- Text summarization  
- Text generation  
- Sentiment analysis  

**Code References:**
- `text_summarization.py`  
- `text_generation.py`  
- `sentiment_analysis.py`  

---

### Relevance to Agentic AI

These primitives form the cognitive building blocks of agent systems, enabling compression, intent interpretation, and controlled generation.

---

## Part II — From LLM Calls to Agent Architecture

### Architectural Shift

An agent is not an LLM call but a control system built around an LLM.

Agents require:
- State  
- Memory  
- Execution flow  

LangGraph enables this structured design through explicit graphs.

---

### LangGraph-Based Reasoning

Key architectural principles:
- LLMs are stateless  
- State persistence enables reasoning continuity  
- Graph-based execution improves determinism and debuggability  

**Code Reference:**  
- `langgraph_single_agent_memory.py`

---

## Part III — Multi-Agent Reasoning

### Conceptual Overview

Multi-agent systems emphasize:
- Task decomposition  
- Role specialization  
- Structured coordination  

---

### Two-Agent Sequential Workflow

A two-agent pipeline was implemented consisting of:
- Query analysis agent  
- Response generation agent  

Shared state enables controlled sequential reasoning.

**Code Reference:**  
- `langgraph_two_agent_pipeline.py`

---

## Part IV — Final Project: Departmental Knowledge Assistant (Agentic RAG)

### Problem Statement

Department websites contain valuable academic information that is difficult to query conversationally. The goal of this project was to design an Agentic RAG system capable of answering natural-language queries grounded strictly in departmental data.

---

### System Architecture
The final system follows a modular Agentic RAG pipeline:
Web Data → Scraper Agent → Chunking Agent → Embedding Agent
→ Vector Database → Query Agent → Response Agent

Each agent is independently testable and architecturally scoped.

---

## Agent Design and Responsibilities

### Scraper Agent (scraper_agent.py)
- Extracts clean text from departmental web pages  
- Removes HTML noise and boilerplate  

### Chunking Agent (chunking_agent.py)
- Segments large text into overlapping semantic chunks  
- Preserves contextual continuity  

### Embedding Agent (embedding_agent.py)
- Converts chunks into dense vector representations  
- Stores vectors in a persistent database  

### Query Agent (query_agent.py)
- Performs semantic similarity search  
- Retrieves relevant context for user queries  

### Response Agent (response_agent.py)
- Generates grounded responses using retrieved context  
- Prevents hallucination through controlled prompting  

---

## Supervisor Pipeline

The `main.py` file orchestrates agent execution, coordinating data flow across the pipeline. While implemented procedurally, the structure directly maps to a graph-based supervisor and can be extended using LangGraph.

---

## Key Learnings

- Agent behavior emerges from architecture, not prompting  
- Retrieval quality determines system reliability  
- Memory and state are architectural requirements  
- Modular design improves transparency and debuggability  

---

## Challenges Encountered

### Technical
- Environment setup and dependency isolation  
- Debugging silent pipeline failures  
- Managing vector database persistence  

### Conceptual
- Moving beyond prompt-centric thinking  
- Designing systems for control rather than creativity  

---

## Final Reflection

This project marks a transition from model-level experimentation to system-level thinking. Agentic AI was understood not as increased model intelligence, but as disciplined architectural design.

The resulting system is minimal yet complete, providing a strong foundation for future extensions such as LangGraph supervision, tool-using agents, and user-facing interfaces.



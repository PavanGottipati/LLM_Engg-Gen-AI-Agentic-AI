# Chain-of-Thought (CoT) Reasoning with Ollama and Flask

## Overview

This project demonstrates **Chain-of-Thought (CoT) Prompting**, a reasoning technique that encourages Large Language Models (LLMs) to solve problems through a sequence of intermediate reasoning steps before producing a final answer.

The application uses:

* Flask
* Ollama
* Qwen 3 0.6B Model
* REST API Integration

## What is Chain-of-Thought?

Chain-of-Thought prompting guides an LLM to reason step by step.

Instead of directly generating an answer, the model breaks the problem into smaller logical steps and solves each step sequentially.

### Example

Problem:

A shirt costs ₹800 and is on a 15% discount. A ₹50 coupon is applied after the discount.

Reasoning:

1. Calculate 15% of ₹800 = ₹120
2. Discounted price = ₹800 − ₹120 = ₹680
3. Apply coupon = ₹680 − ₹50 = ₹630

Final Answer: ₹630

## Architecture

User Question
↓
Flask API
↓
CoT Prompt
↓
Ollama (Qwen Model)
↓
Step-by-Step Reasoning
↓
Final Answer

## Prompt Template

```text
Solve this problem step by step, showing your reasoning clearly before giving the final answer.

Question: {question}

Let's think step by step:
```

## Advantages

* Easy to implement
* Low computational cost
* Improves reasoning accuracy
* Suitable for arithmetic and logical problems
* Generates transparent reasoning steps

## Limitations

* Explores only one reasoning path
* Errors in early steps may propagate
* Not ideal for complex planning tasks
* Cannot compare alternative solutions

## Technologies Used

* Python
* Flask
* Ollama
* Qwen 3 0.6B
* HTML/CSS/JavaScript

## Future Improvements

* Support multiple models
* Add reasoning evaluation metrics
* Compare responses across different LLMs
* Integrate performance benchmarking
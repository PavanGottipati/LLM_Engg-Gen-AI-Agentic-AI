# Tree-of-Thought (ToT) Reasoning with Ollama and Flask

## Overview

This project demonstrates **Tree-of-Thought (ToT) Prompting**, an advanced reasoning framework that allows Large Language Models (LLMs) to explore multiple possible solution paths, evaluate them, and select the most promising answer.

The application uses:

* Flask
* Ollama
* Qwen 3 0.6B Model
* REST API Integration

## What is Tree-of-Thought?

Tree-of-Thought extends Chain-of-Thought reasoning by generating multiple reasoning branches instead of following a single path.

The model:

1. Creates multiple solution approaches
2. Evaluates each approach
3. Selects the most reliable reasoning path
4. Produces the final answer

### Example

Problem:

A shirt costs ₹800 and is on a 15% discount. A ₹50 coupon is applied after the discount.

Generated Approaches:

Approach 1:

* Apply discount
* Apply coupon
* Result = ₹630

Approach 2:

* Apply coupon
* Apply discount
* Result differs

Approach 3:

* Alternative reasoning path

Evaluation:

* Compare all approaches
* Select the most logical and accurate solution

Final Answer: ₹630

## Architecture

User Question
↓
Flask API
↓
ToT Prompt
↓
Generate Multiple Branches
↓
Evaluate Branches
↓
Select Best Branch
↓
Final Answer

## Prompt Template

```text
Solve this problem using Tree-of-Thought reasoning.

Step 1: Generate 3 different possible approaches.
Step 2: Evaluate each approach.
Step 3: Select the best approach.
Step 4: Provide the final answer.
```

## Advantages

* Explores multiple solution paths
* Better handling of complex problems
* Reduces reasoning mistakes
* Supports planning and decision-making tasks
* More robust than single-path reasoning

## Limitations

* Higher computational cost
* Increased response time
* Requires more tokens
* More complex prompt design

## Comparison with Chain-of-Thought

| Feature          | Chain-of-Thought | Tree-of-Thought          |
| ---------------- | ---------------- | ------------------------ |
| Reasoning Paths  | Single           | Multiple                 |
| Complexity       | Low              | High                     |
| Cost             | Low              | Higher                   |
| Speed            | Faster           | Slower                   |
| Accuracy         | Good             | Better for complex tasks |
| Planning Ability | Limited          | Strong                   |

## Technologies Used

* Python
* Flask
* Ollama
* Qwen 3 0.6B
* HTML/CSS/JavaScript

## Future Improvements

* Dynamic branch generation
* Branch scoring algorithms
* Self-reflection and verification
* Integration with ReAct and Agentic workflows
* Performance benchmarking against CoT
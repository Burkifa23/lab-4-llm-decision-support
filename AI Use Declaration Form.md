## **AI Use Declaration Form** 

**Course:** Introduction to Artificial Intelligence

**Lab Title:** LLMs and Prompt Engineering for Decision Support

**Student Name:** Kwizera Mugwaneza Frank

**Student ID:** 36432028 

**GitHub Repository Link:** [https://github.com/Burkifa23/lab-4-llm-decision-support](https://github.com/Burkifa23/lab-4-llm-decision-support) 

**Date Submitted:** 

## **1. AI Use Summary** 

|**1. AI Use Summary**||
|---|---|
|**Question**|**Student Response**|
|Did you use any AI tool for this lab?|Yes |
|Estimated percentage of the work influenced by AI| |
|Did you attach evidence of AI use where applicable?|Yes|



## **2. Details of AI Use** 

Complete the table below for each AI tool used. Add more rows where necessary. 

| **Name of AI Tool Used** | **Purpose for Using the Tool** | **Prompt or Instruction Given to the Tool** | **Part(s) of the Work Influenced by the Tool** | **How I Verified, Edited, or Improved the AI Output** |
| :--- | :--- | :--- | :--- | :--- |
|Gemini |Initial Prompt and Guide for Project |Here is a comprehensive research and conceptual search guide mapped to every section of your lab. Use these search queries and documentation topics to understand the principles and API mechanics before implementing your solution. --- ## Part 0: Environment & API Key Security ### Key Concepts to Search * **`python-dotenv` best practices**: How to read environment variables from a `.env` file without committing secrets. * **`google.colab.userdata`**: Accessing secrets stored securely in Google Colab's secret manager. * **`git` credential leaks and `.gitignore` patterns**: Ensuring configuration files containing credentials are excluded before initial commits. --- ## Section 1: Talking to an LLM Programmatically ### Part 1.1 — Anatomy of an API Call ### Key Concepts & Search Terms * **OpenAI Chat Completions API format**: Structure of the `messages` array, message roles (`system`, `user`, `assistant`), and response schema (`choices`, `message.content`, `usage`). * **LLM Tokenization mechanics**: Byte-Pair Encoding (BPE), subword tokenization, how prompt tokens vs. completion tokens are counted and billed. * **System prompt vs. User prompt separation**: How system messages steer behavior, tone, guardrails, and role constraints compared to episodic user input. ### Part 1.2 — Generation Parameters & Temperature ### Key Concepts & Search Terms * **Sampling temperature in LLMs**: Softmax temperature, probability distribution flattening vs. sharpening, deterministic greedy decoding (`temperature = 0`) vs. stochastic sampling. * **Top-p (nucleus sampling) vs. Temperature**: How sampling parameters influence output diversity, consistency, and repeatability. --- ## Section 2: Domain Context & Dataset Familiarity ### Key Concepts & Search Terms * **Microfinance underwriting in West Africa**: Susu collection schemes, informal group liability, personal guarantors, fixed deposit pledges, and seasonal cash flow patterns. * **Unstructured-to-structured loan triage**: Translating informal qualitative narratives into auditable financial indicators. --- ## Section 3: Prompt Engineering for Decision Support ### Part 3.1 — Component 1: Summarization & Grounding ### Key Concepts & Search Terms * **Role prompting & persona definition**: Guiding the model's tone, brevity, and target audience (e.g., credit officer). * **Hallucination mitigation via negative constraints**: Using explicit negative constraints (e.g., *"extract only stated facts, do not extrapolate or assume"*) to enforce strict grounding. * **Extractive vs. Abstractive summarization trade-offs**: Preserving critical entities (monetary amounts, dates, terms) while compressing narrative prose. ### Part 3.2 — Component 2: Structured JSON Extraction ### Key Concepts & Search Terms * **Few-shot in-context learning for JSON**: Designing clear schemas and high-quality exemplar demonstrations without contaminating evaluation data. * **Explicit null handling & hallucination prevention in extraction**: Forcing the model to output `null` for missing attributes rather than inferring or defaulting values. * **Defensive JSON parsing in Python**: Handling Markdown formatting fences (e.g., `json ... `), catching `json.JSONDecodeError`, and safely sanitizing model outputs into structured dictionaries. ### Part 3.3 — Component 3: Decision-Support Recommendation ### Key Concepts & Search Terms * **Human-in-the-loop (HITL) AI systems**: The distinction between automated decision-*making* (autonomous approval/denial) vs. decision *support* (risk surface highlighting, missing data identification, actionable next steps). * **Credit risk triage frameworks**: Categorizing strengths (collateral, track record, steady profit) and red flags (no collateral, ambiguous repayment, speculative ventures). ### Part 3.4 — Modular Prompt Architecture ### Key Concepts & Search Terms * **Prompt versioning as software artifacts**: Decoupling prompt templates from application execution logic, treating prompts as configuration files. --- ## Section 4: Evaluation: Quality, Reliability, and Appropriateness ### Part 4.1 — Extraction Accuracy & Evaluation Metrics ### Key Concepts & Search Terms * **Exact match vs. normalized string matching**: Case-folding, whitespace trimming, and type-safe numerical comparison for evaluation matrices. * **Confusion matrix and field-level accuracy calculation**: Evaluating precision across disparate data types (booleans, strings, floats, optional fields). ### Part 4.2 — Determinism and Consistency Testing ### Key Concepts & Search Terms * **LLM output variance across temperatures**: Measuring output entropy, JSON parsing validity rates, and semantic drift across repeated runs. * **Canonical JSON serialization**: Using deterministic key sorting to hash and compare structured dictionaries across inference runs. ### Part 4.3 — Adversarial Probing & Red-Teaming ### Key Concepts & Search Terms * **Out-of-domain robustness & empty input handling**: Testing model failure modes when presented with irrelevant or adversarial inputs. * **Faithfulness and hallucination probing**: Asking targeted questions about non-existent facts to verify refusal behavior. ### Part 4.4 — Ethics, Algorithmic Bias, and Regulation ### Key Concepts & Search Terms * **Linguistic bias in language models**: How dialect variations, grammatical fluency, or phrasing styles in English can bias automated assessment against competent informal business operators. * **Cross-border data transfer regulations**: Ghana Data Protection Act 2012 (Act 843), GDPR Article 44 principles regarding personally identifiable information (PII) transmitted to third-party cloud APIs. * **Safeguards in automated underwriting**: Adverse action notice requirements, right to explanation, human escalation paths, and audit logging. --- ## Section 5: Economics, Architecture, and Reflection ### Key Concepts & Search Terms * **LLM token economics & unit cost modeling**: Calculating monthly active user (MAU) cost projections based on input/output token volume. * **API vs. Fine-Tuning vs. Traditional Machine Learning**: Comparing development speed, maintenance overhead, operational latency, deterministic boundaries, and customization trade-offs across AI paradigms. --- Whenever you write your code or draft your answers for any of the **Student Reasoning** sections, share them here. We will review your logic, edge cases, and reasoning together step-by-step. |Rest Parts |Gave me a idea project of how to do this project |

## **3. Attachment of AI Output Evidence** 

Where required, attach evidence of AI use. Tick all that apply. Add more rows where necessary. 
Gemini: https://gemini.google.com/app/7828b62878785314
|**Evidence Type**|**Attached?**<br>**(Yes, No,**<br>**N/A)**|**File Name**|
|---|---|---|
|Link|Yes |https://gemini.google.com/app/7828b62878785314 |



## **4. Student Declaration** 

I declare that: 

|**Response Declaration Statement**| **(Yes/No)** |
|---|---|
|The submitted work is my own work. |Yes |
|Any use of AI tools has been clearly declared in this form. | Yes|
|The prompts, instructions, and AI-generated outputs have been disclosed where applicable. | Yes|
|I reviewed, tested, edited, and improved any AI-generated content before submission. |  Yes|
|My AI usage does not exceed 25% of the entire work.| Yes |
|I understand that undeclared or excessive AI use may be treated as academic misconduct. | Yes |

**Student Signature:** _frank_

**Date:**

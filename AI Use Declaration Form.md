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
|Gemini |Initial Prompt and Guide for Project |As an experienced  tutor who understands LLMs anḍ prompt Engineer for Decion Support.
YOU MUST NEVER GIVE ME THE CODE! You must analyze my code and Student Reasoning to determine whether it is correct. Now for the beginning what should I search on to be able to accomplish each task. Remember never give me code even if I ask for it| All parts of the lab|  I searched for the materials|
|Gemini|Part 1.1 check | import time def ask_llm(user_prompt, system_prompt="You are a helpful assistant.", temperature=0.7, max_tokens=500, return_usage=False): """One-shot chat completion. Returns the reply text, or (text, usage).""" for attempt in range(5):          # free tiers rate-limit; back off and retry try: response = client.chat.completions.create( model=MODEL, messages=[ {"role": "system", "content": system_prompt}, {"role": "user",   "content": user_prompt}, ], temperature=temperature, max_tokens=max_tokens, ) break except Exception as err: if "rate" not in str(err).lower() or attempt == 4: raise wait = 2 ** attempt print(f"  rate limited, retrying in {wait}s ...") time.sleep(wait) text = response.choices[0].message.content return (text, response.usage) if return_usage else text # One simple question, so we can see the shape of a real response. answer, usage = ask_llm( "In two sentences, explain what a susu savings scheme is in Ghana.", system_prompt="You are a concise explainer of financial services in West Africa.", temperature=0.7, return_usage=True, ) print(answer) # Token accounting: this is what you are billed on, and what Section 5 Q3 needs. print("\nresponse.usage ->", usage) print(f"prompt_tokens     = {usage.prompt_tokens}") print(f"completion_tokens = {usage.completion_tokens}") print(f"total_tokens      = {usage.total_tokens}") **Student Reasoning — Anatomy of a call** *1. What is the difference between the `system` and `user` roles? Give an example of something that belongs in each.* > The `system` message carries the standing context for the whole conversation: who the model is, what rules it must obey, and what shape its output must take. > - **system:** "You are an assistant to a microfinance loan officer in Ghana. Be factual, never invent details, and answer in 3-4 sentences." > The `user` message carries the specific request and data for this one turn. A useful rule of thumb for this lab: anything that would be *identical* for all six letters belongs in `system`; anything that *changes per letter* belongs in `user`. > - **user:** the text of letter L001, prefixed with "Summarize this loan application:". *2. What is a token, roughly? Why do API providers bill per token rather than per request?* > A token is the atomic unit a model reads. > Providers bill per token because cost tracks tokens, not requests. Each Request can have varying number of words, or even documents which has more tokens that a prompt. For example in this run the prompt_tokens = 63 tokens and it the  completion_tokens = 85 tokens which brought the  total_tokens = 148 tokens. So charging per request would be a bad business model.|Part 1.1 |I got confirmation to go to 1.2 |
|Gemini|Part 1.2 | Part 1.2 TEMP_QUESTION = "Suggest a name for a savings product for market traders in Accra." # RUN 1: Temperature 0.0 print("temperature = 0.0") answers_0 = [] for i in range(5): # call the API answer = ask_llm(TEMP_QUESTION, temperature=0.0, max_tokens=60).strip() answers_0.append(answer) print(f"[{i + 1}] {answer}\n") # Count distinct answers distinct_count_0 = len(set(answers_0)) print(f"{distinct_count_0} distinct answer(s) out of 5 runs\n") # RUN 2: Temperature 1.2 print("temperature = 1.2") answers_1 = [] for i in range(5): # call the API answer = ask_llm(TEMP_QUESTION, temperature=1.2, max_tokens=60).strip() answers_1.append(answer) print(f"[{i + 1}] {answer}\n") # Count distinct answers distinct_count_1 = len(set(answers_1)) print(f"{distinct_count_1} distinct answer(s) out of 5 runs\n") **Student Reasoning — Temperature** *What did you observe at each temperature? For the loan decision-support system you are about to build, which temperature regime is appropriate, and why?* > I observerd at temperature=0.0 there was only one distinct answer but at temperature=1.2, there were 5 distinct answers. To reproduce a consistent answer, 0 is the appropriate temperature.| Part 1.2| Confirmation to continue |



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

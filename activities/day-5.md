### 5.1 Run the Graph [10]

- Ref: 23-langgraph-orchestration
- Study and run both examples

---------------------------------------------------
10:25 - 10:35 Exercise 5.1
---------------------------------------------------


### 5.2 Langsmith Observability [20]

#### Part 1:

- Run: 24-langsmith-observability\db-graph-buggy-code.py
- Observe that it is stuck
- Access: smith.langchain.com
- Sign-up and create a API key, store in key-vault
- Update the keys in: 24-langsmith-observability\01-db-graph-buggy-code-tracing.py
- Run the code and observe in console and also in the langsmith interface
- Note the errors [3]

---------------------------------------------------
11:15 - 11:35 Tea Break
11:35 - 11:55 Exercise 5.2.1
---------------------------------------------------

#### Part 2:

- Fix the code by un-commenting the section of the file 
- Ref: 24-langsmith-observability\01-db-graph-buggy-code-tracing.py
- Run once again, you should all queries working fine
- Drag and drop the file in ChatGPT
- Find out why state["retries"] is not reaching the value __max_retries__
- Prompt the AI for a fix

---------------------------------------------------
12:30 - 12:45 Complete 5.2.2
---------------------------------------------------

---------------------------------------------------
1:40 - 2:40 Lunch Break
---------------------------------------------------

---------------------------------------------------
4:25 - 4:45 Tea Break
4:45 - 5:00 Test queries
---------------------------------------------------


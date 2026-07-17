### 4.1 Capstone - Part 1 [Classwork][120]


#### Phase 1

- Setup Document Store in Flowise
- Setup Pinecone
  - Sign-up
  - Creating an index
  - Generate API keys
- Upsert the chunks from Flowse -> Pinecone
- Test the retrieval

-------------------------------------------------

#### Phase 2

- Build the system 
- Ref: 17-flowise-rag\02-complete-project-new-version.png
- Test using some of the queries
- Ref: 16-rag-capstone\cis-basic\sample-queries\test-queries

-------------------------------------------------
11:00 - 11:20 Tea Break
-------------------------------------------------

-------------------------------------------------
12:05 - 12:25 Complete Part 1/Phase 2 of the capstone project
-------------------------------------------------

-------------------------------------------------
1:30 - 2:15 Lunch BReak
-------------------------------------------------


### 4.2 Creating a Tool Based Agent [20]

- Review: 20-tools-deep-dive\01-langchain-tools-and-agents.ipynb
- Declare a list
  - M = []
- Create functions that stores and retrieve data from M
  - store(data_item)
  - retrieve(index)
  - show()
- Convert them into langchain tools
  - use @tool
- Create an agent using the above tools
  - use create_agent()
- Invoke the agent to perform some tasks
  - Example: 
    - Store 15
    - Show me the contents
    - Get me the second item

-------------------------------------------------
15:20 - 15:40 Exercise 4.2
-------------------------------------------------

-------------------------------------------------
16:10 - 16:30 Tea Break
-------------------------------------------------
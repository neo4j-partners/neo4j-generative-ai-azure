# Medical Assitant Bot - Enrichment & Consumption

## Pre-requisites
- A running Neo4j V5 instance with Medical Case Sheet Data.
- Data can be injected from this [notebook](openai/ingestion/ingestion.ipynb)


Run the following commands to start the services:
1. Create an `.env` file and input your LLM API KEY as shown in `env.example`

2. Start docker services

```
docker-compose up
```

## Sample Questions to ask:
1. Which patient has the most number of symptoms?
2. Which disease affect most of my patients?
3. How many of my patients suffer from both cough and weight loss?
   Follow-up question: who are they?
4. When someone has cough and nausea, do they also lose weight?
5. Which body part got affected in most of my patients?
6. Which age group has the most number of heart diseases?

# Credits
[Tomaz Bratanic](https://github.com/tomasonjo/NeoGPT-Explorer)

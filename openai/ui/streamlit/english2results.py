from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph
from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from retry import retry
from timeit import default_timer as timer
import streamlit as st
import os

host = st.secrets["NEO4J_URI"]
user = st.secrets["NEO4J_USER"]
password = st.secrets["NEO4J_PASSWORD"]
db = st.secrets["NEO4J_DB"]

OPENAI_API_TYPE = st.secrets["OPENAI_API_TYPE"]
OPENAI_API_VERSION = st.secrets["OPENAI_API_VERSION"]
OPENAI_API_BASE = st.secrets["OPENAI_API_BASE"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
OPENAI_MODEL_NAME = st.secrets["OPENAI_MODEL_NAME"]
OPENAI_DEPLOYMENT_NAME = st.secrets["OPENAI_DEPLOYMENT_NAME"]
    

CYPHER_GENERATION_TEMPLATE = """You are an expert Neo4j Cypher translator who understands the question in english and convert to Cypher strictly based on the Neo4j Schema provided and following the instructions below:
1. Generate Cypher query compatible ONLY for Neo4j Version 5
2. Do not use EXISTS, SIZE keywords in the cypher. Use alias when using the WITH keyword
3. Use only Nodes and relationships mentioned in the schema
4. Always enclose the Cypher output inside 3 backticks
5. Always do a case-insensitive and fuzzy search for any properties related search. Eg: to search for a Team name use `toLower(t.name) contains 'neo4j'`
6. Always use aliases to refer the node in the query
7. Cypher is NOT SQL. So, do not mix and match the syntaxes
Schema:
{schema}
Samples:
Question: Which patient has the most number of symptoms?
Answer: ```MATCH (n:Person)-[:HAS_SYMPTOM]->(s:Symptom) return n.id,n.age, n.gender,count(s) as symptoms 
order by symptoms desc```
Question: Which disease affect most of my patients?
Answer: ```MATCH (d:Disease) RETURN d.name as disease, SIZE([(d)-[]-(p:Person) | p]) AS affected_patients ORDER BY affected_patients DESC LIMIT 1```
Question: Which of patients have cough?
Answer: ```MATCH (p:Person)-[:HAS_SYMPTOM]->(s:Symptom) WHERE toLower(s.description) CONTAINS 'cough' RETURN p.id, p.age, p.location, p.gender```

Question: {question}"""
CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)

@retry(tries=5, delay=5)
def get_results(messages):
    start = timer()
    try:
        graph = Neo4jGraph(
            url=host, 
            username=user, 
            password=password
        )
        chain = GraphCypherQAChain.from_llm(
            AzureChatOpenAI(
                deployment_name= OPENAI_DEPLOYMENT_NAME,
                model_name=OPENAI_MODEL_NAME,
                openai_api_base=OPENAI_API_BASE,
                openai_api_version=OPENAI_API_VERSION,
                openai_api_key=OPENAI_API_KEY,
                openai_api_type=OPENAI_API_TYPE,
                temperature=0), 
            graph=graph, verbose=True,
            return_intermediate_steps=True,
            cypher_prompt=CYPHER_GENERATION_PROMPT
        )
        if messages:
            question = messages.pop()
        else: 
            question = 'How many cases are there?'
        return chain(question)
    except Exception as ex:
        print(ex)
    #     return "LLM Quota Exceeded. Please try again"
    finally:
        print('Cypher Generation Time : {}'.format(timer() - start))

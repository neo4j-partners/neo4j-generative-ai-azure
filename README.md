# neo4j-generative-ai-azure
This is a sample notebook and web application which shows how Azure OpenAI can be used with Neo4j.  We will explore how to leverage Azure OpenAI LLMs to build and consume a knowledge graph in Neo4j.

This notebook parses data from a public corpus of Medical Case Sheet using Azure OpenAI's `gpt-4-32k` model. The model is prompted to recognise and extract entities and relationships. 

We then use the `gpt-4-32k` model and prompt it to convert questions in English to Cypher - Neo4j's query language for data retrieval.

## Setup
To get started, we'll need to set up some resources:

1. A Neo4j instance running on Azure cloud. You can find [instructions](https://github.com/neo4j-partners/hands-on-lab-neo4j-and-azure-ml/blob/main/Lab%201%20-%20Deploy%20Neo4j/README.md) here and a [video tutorial](https://youtu.be/k1IJ5m4KCYA) here.

2. [Generate an OpenAI API key](02-create_openai_key/README.md).

3. [Create a managed notebook in Azure ML](03-setup_azureml_workspace/README.md).

Once that has started, open the notebook and a terminal window within that.  Clone this repo with the command:

    git clone https://github.com/neo4j-partners/neo4j-generative-ai-azure.git

## Notebook
The notebook at [ingestion/ingestion.ipynb](ingestion/ingestion.ipynb) walks through prompts and tuning a model.  You will need to run that before the UI. 

## UI
The UI application is based on Streamlit. 

Let's install python & pip first:

    apt install -y python
    apt install -y pip

Now, let's create a Virtual Environment to isolate our Python environment and activate it

    apt-get install -y python3-venv
    python3 -m venv /app/venv/genai
    source /app/venv/genai/bin/activate

To install Streamlit and other dependencies:

    cd ui
    pip install -r requirements.txt

Check if `streamlit` command is accessible from PATH by running this command:

    streamlit --version

If not, you need to add the `streamlit` binary to PATH variable like below:

    export PATH="/app/venv/genai/bin:$PATH"

Next up you'll need to create a secrets file for the app to use.  Open the file and edit it:

    cd streamlit
    cd .streamlit
    cp secrets.toml.example secrets.toml
    vi secrets.toml

You will now need to edit that file to reflect your Azure OpenAI and Neo4j credentials. The file has the following variables:

    OPENAI_API_KEY = "" #OPENAI KEY
    OPENAI_API_TYPE = "azure"
    OPENAI_API_VERSION = "2023-03-15-preview"
    OPENAI_API_BASE = ""
    OPENAI_MODEL_NAME = "gpt-4-32k"
    OPENAI_DEPLOYMENT_NAME = "gpt-4-32k"
    NEO4J_URI = "neo4j+s://xxxxx.databases.neo4j.io" # Neo4j URL. Include port if applicable
    NEO4J_USER = "neo4j" # Neo4j User Name
    NEO4J_PASSWORD = "Foo12345678" #Neo4j Password

Now we can run the app with the commands:

    streamlit run Home.py --server.port=80
   

## Sample Questions to ask:
1. Which patient has the most number of symptoms?
2. Which disease affect most of my patients?
3. How many of my patients suffer from both cough and weight loss?
4. When someone has cough and nausea, do they also lose weight?
5. Which body part got affected in most of my patients?
6. Which age group has the most number of heart diseases?


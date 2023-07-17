import streamlit as st
from PIL import Image

st.set_page_config(page_icon="🧠", layout="wide")
st.markdown("""
This is a Proof of Concept application which shows how Azure OpenAI can be used with Neo4j to build and consume Knowledge Graphs using unstructured Medical Transcript Corpus.
Using OpenAI GPT-4 model, medical transcript text is converted to Knowledge Graph.
            
The Sample Case History text used in this demo looks like:
            
```
A 28-year-old woman was referred with a 4-week history of continuous, moderate right upper quadrant pain associated with jaundice, as well as weight loss (10 kg over 3 months) and a liver mass identified by ultrasonography.
The pain sensation seemed different from previous colicky attacks the patient had experienced before she underwent laparoscopic cholecystectomy 7 years previously.
On physical examination, she was obese (body mass index 37.8), with icterus noted over the conjunctivae, oral mucosa and skin.
Imaging modalities included computed tomography (CT), positron emission tomography (PET) and endoscopic cholangiopancreatography (ERCP) (Fig.1).
The patient underwent exploratory laparotomy.
Intraoperative ultrasonography revealed a cystic lesion measuring 3.5 2.5 cm within the central portion of the liver, anterior to the porta hepatis.
Intraoperative cholangiography demonstrated an extensive stricture obliterating the left hepatic duct, with partial occlusion of the right hepatic duct.
An extended left lobectomy was done en bloc with the biliary confluence.
On frozen-section examination, all margins of the excised specimen were free of malignant cells.
Reconstruction was performed with a Roux-en-Y cholangiojejunostomy to 3 second bile duct radicals in the right side.
Intraoperatively, radiotherapy was applied to the surgical margins.
After this, the patient underwent 6 weeks of image-guided external beam radiation centred on the resection field labelled at surgery.
The final pathology described this tumour as an infiltrating, moderately differentiated squamous cell carcinoma associated with severe dysplasia of the bile-duct epithelium (Fig.2).
The patient recovered without complications and was doing well 18 months after the initial surgical procedure, with an unremarkable CT scan.
```

### Why Neo4j is a great addition to LLMs:
- *Fine-grained access control of your data* : You can control who can and cannot access parts of your data
- Greater reliability with factual data
- More Explainability
- Domain specificity
- Ability to gain insights using Graph Algorithms
- Vector embedding support and Similarity Algorithms on Neo4j

""", unsafe_allow_html=True)

arch = Image.open('./images/arch.png')
langchain = Image.open('./images/langchain-neo4j.png')
schema = Image.open('./images/schema.png')

st.image(arch)
st.markdown("""
---

This the schema in which the transformed data are stored in Neo4j
""")
st.image(schema)
st.markdown("""
---

This is how the Chatbot flow goes:
""")
st.image(langchain)

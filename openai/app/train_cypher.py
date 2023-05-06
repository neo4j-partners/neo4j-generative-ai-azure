examples = [{
    "question": "Which patient has the most number of symptoms?",
    "answer": """MATCH (n:Person)-[:HAS_SYMPTOM]->(s:Symptom) return n.id,n.age, n.gender,count(s) as symptoms 
order by symptoms desc"""
}, {
    "question": 'Which disease affect most of my patients?',
    "answer": """MATCH (d:Disease) RETURN d.name as disease, SIZE([(d)-[]-(p:Person) | p]) AS affected_patients ORDER BY affected_patients DESC LIMIT 1"""
}, {
    "question": 'Which of patients have cough?',
    "answer": """MATCH (p:Person)-[:HAS_SYMPTOM]->(s:Symptom) WHERE toLower(s.description) CONTAINS 'cough' RETURN p.id, p.age, p.location, p.gender"""
}]

instr_template = """
Here are the instructions to follow:
1. Use the Neo4j schema to generate cypher compatible ONLY for Neo4j Version 5
2. Do not use EXISTS, SIZE keywords in the cypher.
3. Use only Nodes and relationships mentioned in the schema while generating the response
4. Reply ONLY in Cypher when it makes sense.
5. Whenever you search for an Officer name or an Entity name or an Intermediary name, always do case-insensitive and fuzzy search
6. Officer node is synonymous to Person
7. Entity nodes are synonymous to Shell Companies
"""


template = """
Using this Neo4j schema and Reply ONLY in Cypher when it makes sense.

Schema: {text}
"""

schema = """
Nodes:
    label:'Case',id:string,summary:string //Case Node
    label:'Person',id:string,age:string,location:string,gender:string //Patient Node
    label:'Symptom',id:string,description:string //Symptom Node
    label:'Disease',id:string,name:string //Disease Node
    label:'BodySystem',id:string,name:string //Node for Body Part affected Eg: Heart, lungs
    label:'Diagnosis',id:string,name:string,description:string,when:string //Diagnostic Node
    label:'Biological',id:string,name:string,description:string //Node for Results identified from Diagnosis

Relationships:
    (:Case)-[:FOR]->(Person)
    (:Person)-[:HAS_SYMPTOM{when:string,frequency:string,span:string}]->(Symptom)
    (:Person)-[:HAS_DISEASE{when:string}]->(:Disease)
    (:Symptom)-[:SEEN_ON]->(:BodySystem)
    (:Disease)-[:AFFECTS]->(:BodySystem)
    (:Person)-[:HAS_DIAGNOSIS]->(:Diagnosis)
    (:Diagnosis)-[:SHOWED]->(:Biological)
"""

output_fmt = """
---------------
The output should be in this JSON format:
{
  "cypher": ".."
}"""

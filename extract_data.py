"""
輸入query回傳pandas DataFrame
"""
import os
import py2neo
graph = py2neo.Graph(
    host=os.environ['neo4j_host'], 
    user='neo4j', 
    password=os.environ['neo4j_password']
)

query = """
MATCH (a:person)-[r:has_father]-(b:person)
RETURN 
    a.id_number AS from, 
    b.id_number AS to, 
    r.link_dt AS link_dt
LIMIT 1000
"""
result = graph.run(query).to_data_frame()
print(result)
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://127.0.0.1:7687", auth=basic_auth("neo4j", "pokemon"))
session = driver.session()

def add_node(tx, id, new_id):
    tx.run("MERGE (a:Node {id: $id}) "
           "MERGE (a)-[:GO_TO]->(node:Node {id: $new_id})",
           id=id, new_id=new_id)

session.run("CREATE (a:Node {id: {id}, x: {x}, y: {y}})",
              {"id": 1, "x": 43.23, "y": 32.12} )

session.run("CREATE (a:Node {id: {id}, x: {x}, y: {y}})", {"id": 2, "x": 3.13, "y": 123.32})

session.write_transaction(add_node, 1, 2)

result = session.run("MATCH (a:Node) WHERE a.id = {id} "
                       "RETURN a.id AS id, a.x AS x, a.y AS y",
                       {"id": 1})
result1 = session.run("MATCH (a:Node) WHERE a.id = {id} "
                       "RETURN a.id AS id, a.x AS x, a.y AS y",
                       {"id": 2})
for record in result:
     print("%s %s %s" % (record["id"], record["x"], record["y"]))

for record in result1:
     print("%s %s %s" % (record["id"], record["x"], record["y"]))

session.close()
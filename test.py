from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "pokemon"))


def add_friends(tx, id, x, y, new_id, new_x, new_y):
    tx.run("MERGE (a:Node {id: $id, x: $x, y: $y}) "
           "MERGE (a)-[:GOTO]->(new:Node {id: $new_id, x: $new_x, y: $new_y})",
           id=id, new_id=new_id, x=x, y=y, new_x=new_x, new_y=new_y)


def print_relations(tx, id, x, y):
    for record in tx.run("MATCH (a:Node)-[:GOTO]->(new) WHERE a.id = $id "
                         "RETURN new.id, new.x, new.y ORDER BY new.id, new.x, new.y", id=id):
        print(record["new.id"], record["new.x"], record["new.y"])


with driver.session() as session:
    session.write_transaction(add_friends, 1, 43.23, 32.12, 2, 23.14, 25.42)
    session.write_transaction(add_friends, 2, 23.14, 25.42, 3, 74.25, 74.35)
    session.write_transaction(add_friends, 2, 23.14, 25.42, 4, 16.24, 77.42)
    session.read_transaction(print_relations, 2, 23.14, 25.42)

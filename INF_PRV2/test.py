import sqlite3

conn = sqlite3.connect(r'C:\Users\alex2\Desktop\INF_PRV2\static\db\main.db')
cur = conn.cursor()

import random
rdtXT = "Considered discovered ye sentiments projecting entreaties of melancholy is. In expression an solicitude principles in do. Hard do me sigh with west same lady. Their saved linen downs tears son add music. Expression alteration entreaties mrs can terminated estimating. Her too add narrow having wished. To things so denied admire. Am wound worth water he linen at vexed."
serv = ["msk", "spb"]
typ = ["w", "r"]
dec = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt labore quis omnis, repellat dolor velit iusto atque dicta placeat maiores necessitatibus incidunt deleniti alias amet."

for i in range(100):
    sql = f"INSERT INTO CampSearch values ('{random.choice(rdtXT.split())}{i}', '{random.choice(serv)}', '{random.choice(typ)}', '{dec}', '{random.choice(dec.split())}', '{random.randint(1,30)}/{random.randint(1,12)}/20{random.randint(10,22)}')"

    cur.execute(sql)
    conn.commit()
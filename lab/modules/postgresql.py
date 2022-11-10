import psycopg2
import pandas as pd

class PostgresSql:
    
  def __init__(self):
    conn = psycopg2.connect(
        host="postgresdns",
        database="postgres",
        user="postgres",
        password="postgres")
    cursor = conn.cursor()
    self.cursor = cursor

  def exec(self, query, cursor=None, to_df=False):
    c = self.cursor if not cursor else cursor
    c.execute(query)
    chunk = c.fetchall()
    if to_df:
        names = list(map(lambda x : x[0], c.description))
        return pd.DataFrame(chunk, columns=names)
    
    return chunk

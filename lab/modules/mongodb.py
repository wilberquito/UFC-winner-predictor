import pymongo
import pandas as pd
import math
import time

class MongoDB:
  
  def __init__(self):  
    mongo_str = 'mongodb://mongo:mongo@mongodns'
    client = pymongo \
            .MongoClient(mongo_str)
    self.clientInstance = client
  
  def client(self):
    return self.clientInstance

  def __send_mongo(self, df, collection):
    chunk = df.to_dict('records')
    collection.insert_many(chunk)

  def __send(self, df, collection, it=3, per=0.5):
    N = len(df)
    iters = it
    period = per
    chunks = math.floor(N / iters)

    def clamp(n):
      return N if n > N else n

    transfering = True
    i = 0
    while transfering:
      start = i * chunks
      end  = clamp(i * chunks + chunks)
      df_slice = df.iloc[start:end]
      self.__send_mongo(df_slice, collection)
      time.sleep(period)
      i = i + 1
      transfering = end < N
  
  def send(self, df, collection):
    self.__send(df, collection)

  def exec(self, collection, pipeline):
    return collection.aggregate(pipeline)
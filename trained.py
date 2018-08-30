import gensim
from datetime import datetime

startTime = datetime.now()

from gensim.models import Word2Vec
model = Word2Vec.load("new1.model")

w1 = "court"

w1 = w1.lower()

print("Word is "+w1)
print(model.wv.most_similar (positive=w1,topn=4))

print(datetime.now() - startTime)

import gzip
import gensim
import logging
from datetime import datetime

startTime = datetime.now()
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data_file="test.txt.gz"
count = 0
with open ('test.txt.gz', 'rb') as f:
    for i,line in enumerate (f):
        print(line)
        break

def read_input(input_file):
    logging.info("reading file {0}...this may take a while".format(input_file))
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f):

            if (i%10000==0):
                print ("read {0} reviews".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

# read the tokenized reviews into a list
# each review item becomes a series of words
# so this becomes a list of lists
documents = list (read_input (data_file))

logging.info ("Done reading data file")

sizes = [100,110,120,130,140,150,160]
windows = [5,6,7,8,9,10,11,12]
min_counts = [2,3,4,5]
epochs = [5,6,7,8,9,10,11]
'''
for size in sizes:
    for window in windows:
        for min_count in min_counts:
            for epoch in epochs:
                '''
model = gensim.models.Word2Vec (documents, size=100, window=10, batch_words=500,alpha=0.025, min_alpha=0.025,min_count=2, workers=25)
model.train(documents,total_examples=len(documents),epochs=10)
#MODEL_NAME = 'SearchModel-Size{}-Windows{}-Min_Count{}-epoch{}.model'.format(str(size),str(window),str(min_count),str(epoch))
model.save("new1.model")
#count+=1
#print("MODEL "+str(count)+" CREATED")
print(datetime.now() - startTime)

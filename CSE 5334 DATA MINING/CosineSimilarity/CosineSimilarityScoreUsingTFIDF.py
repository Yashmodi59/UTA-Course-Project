from nltk.corpus.reader import documents
import nltk,math
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from math import log10,sqrt
from collections import Counter
stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
import os
corpusroot = './presidential_debates'

# corpusroot = 'D:\FALL 2022\DM\P1\P1\presidential_debates\presidential_debates'
tfIdfectors={}                          #tf-idf vectors for all documents
documentFrequency=Counter()             #storage for document frequency
termFrequencyDictionary={}              #permanent storage for tfs of all tokens in all documents
lengths=Counter()                       #used for calculating lengths of documents
postings_list={}                        #posting list storage for each token in the corpus
vectors= {}

def tokenize_docstring(doc):
    """
    removing stopword tokenize and return array
    :param doc:
    :return:
    """
    doc = doc.lower()
    tokens = tokenizer.tokenize(doc)                                                    #tokenizing each document #reference given p1_guidelines
    sw=stopwords.words('english')
    tokens = [stemmer.stem(token) for token in tokens if token not in sw]               #removing stopwords and performing stemming #reference given p1_guidelines
    return tokens

def getIdf(token):
  """
  idf = log10(N/documentFrequency)
  N = len(tfs)
  documentFrequency = df[token]
  """
  if documentFrequency[token] == 0:
    return -1
  return log10(len(termFrequencyDictionary)/documentFrequency[token])


def calculateWeight(filename, token):
    idf = getIdf(token)
    return (1 + log10(termFrequencyDictionary[filename][token])) * idf




def calulate_length():
    """
    Find the length of the vector to find the weight of the given token
    """
    for filename in termFrequencyDictionary:
        vectors[filename] = Counter()
        length = 0
        for token in termFrequencyDictionary[filename]:
            vectors[filename][token] = calculateWeight(filename, token)
            length += vectors[filename][token] ** 2
        lengths[filename] = math.sqrt(length)
def calculatePostingList():
    """Get Posting List and store it in posting list diction"""
    for filename in vectors:
        for token in vectors[filename]:
            vectors[filename][token] = vectors[filename][token] / lengths[filename]
            if token not in postings_list:
                postings_list[token] = Counter()
            postings_list[token][filename] = vectors[filename][token]

def getWeight(filename,token):
  """
  return normalized weight
  :param filename:
  :param token:
  :return:
  """
  # vectors = getPostingList()[1]
  return vectors[filename][token]
def query(querryString):                             #function that returns the best match for a query
    """
    if present in posting list and common docs false than return fetch more and 0.00
    if not present in posting list return (none, 0.00)
    if present in posting list and common docs true than return max_score
    :param querryString:
    :return:
    """

    querryTermFrequency={}
    querryLength=0
    flag=0
    local_documents={}
    upperBoundDictionary={}
    tokenList = tokenize_docstring(querryString.lower())  ## call function to tokenize querry string
    for token in tokenList:
        if token not in postings_list:          #return (None,0.00) if not present
            return (None, 0.000)
        if getIdf(token)==0:                    #if a token has idf = 0, store all the documents
            local_documents[token], weights = zip(*postings_list[token].most_common())         #to avoid that, we store all docs
        else:
            local_documents[token],weights = zip(*postings_list[token].most_common(10))        #storing top 10 in postings list
        upperBoundDictionary[token]=weights[9]                                                         #storing the upper bound of each token
        if flag==1:
            commondocs=set(local_documents[token]) & commondocs                                #commondocs keeps track of docs that have all tokens
        else:
            commondocs=set(local_documents[token])
            flag=1
        querryTermFrequency[token]=1+log10(querryString.count(token))    #updating term freq of token in query
        querryLength+=math.pow(querryTermFrequency[token],2)                      #calculating length for normalizing the query tf later
    querryLength=math.sqrt(querryLength)
    result, weight = calculateCosineSimilarity(local_documents, querryLength, querryTermFrequency,
                                          upperBoundDictionary) #Calculate Similarity
    if result[0] in commondocs:                                                             #if doc has actual score, return score
        return result[0],weight[0]
    else:
        return "fetch more",0                                                            #if upperbound score is greater, return fetch more


def calculateCosineSimilarity(local_documents, querryLength, querryTermFrequency, upperBoundDictionary):
    """
    Return Cosine Similarity for the document,
    if present in top10 than use it to calculate cosine similarity else use its upperbound vector
    :param local_documents:
    :param querryLength:
    :param querryTermFrequency:
    :param upperBoundDictionary:
    :return:
    """
    cosineSimilarities=Counter()                          #initialize a counter
    for doc in vectors:
        cosineSimilarity = 0
        for token in querryTermFrequency:
            if doc in local_documents[token]:
                cosineSimilarity = cosineSimilarity + (querryTermFrequency[token] / querryLength) * postings_list[token][
                    doc]  # use actual score if in top 10
            else:
                cosineSimilarity = cosineSimilarity + (querryTermFrequency[token] / querryLength) * upperBoundDictionary[
                    token]  # otherwise, use its upper bound

        cosineSimilarities[doc] = cosineSimilarity
    max =  cosineSimilarities.most_common(1)  # extract maximum cosine similarity
    answer, weight = zip(*max)
    return answer, weight

for filename in os.listdir(corpusroot):
    file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
    doc = file.read()
    file.close()
    tokens = tokenize_docstring(doc)
    termFrequency=Counter(tokens)
    documentFrequency+=Counter(list(set(tokens)))
    termFrequencyDictionary[filename]=termFrequency.copy()                              #making a copy of termFrequency copy and store it in dictionary #reference given p1_guidelines
    termFrequency.clear()                                                               #instead of overwriting the variable clear the data store it in to reuse same variable again

calulate_length()
calculatePostingList()
"""
References:
www.stackoverflow.com
www.nltk.org
https://www.geeksforgeeks.org/python-counter-objects-elements/
https://www.w3schools.com/python/python_ref_dictionary.asp
"""

print("%.12f" % getIdf("health"))
print("%.12f" % getIdf("agenda"))
print("%.12f" % getIdf("vector"))
print("%.12f" % getIdf("reason"))
print("%.12f" % getIdf("hispan"))
print("%.12f" % getIdf("hispanic"))
print("%.12f" % getWeight("2012-10-03.txt","health"))
print("%.12f" % getWeight("1960-10-21.txt","reason"))
print("%.12f" % getWeight("1976-10-22.txt","agenda"))
print("%.12f" % getWeight("2012-10-16.txt","hispan"))
print("%.12f" % getWeight("2012-10-16.txt","hispanic"))
print("(%s, %.12f)" % query("health insurance wall street"))
print("(%s, %.12f)" % query("particular constitutional amendment"))
print("(%s, %.12f)" % query("terror attack"))
print("(%s, %.12f)" % query("vector entropy"))

import json
import re
from collections import Counter, defaultdict
import operator
from nltk.corpus import stopwords
import string
from datetime import datetime
import sys

def readTweets(file):
    count_all = Counter()
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via']
    com = defaultdict(lambda : defaultdict(int))
    with open(file, 'r') as f:
        for line in f.readlines():
            tweet = json.loads(line)
            terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))]

            # Build co-occurrence matrix
            for i in range(len(terms_only)-1):
                for j in range(i+1, len(terms_only)):
                    w1, w2 = sorted([terms_only[i], terms_only[j]])
                    if w1 != w2:
                        com[w1][w2] += 1
                        com_max = []
        # For each term, look for the most common co-occurrent terms
        for t1 in com:
            t1_max_terms = max(com[t1].items(), key=operator.itemgetter(1))[:5]
            for t2 in t1_max_terms:
                com_max.append(((t1, t2), com[t1][t2]))
        # Get the most frequent co-occurrences
        terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
        print(terms_max[:50])

#print(count_all.most_common(50))

emoticons_str = r"""
    (?:
    [:=;] # Eyes
    [oO\-]? # Nose (optional)
    [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
             emoticons_str,
             r'<[^>]+>', # HTML tags
             r'(?:@[\w_]+)', # @-mentions
             r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
             r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
             
             r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
             r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
             r'(?:[\w_]+)', # other words
             r'(?:\S)' # anything else
             ]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

if __name__ == '__main__':
    file = sys.argv[1]
    readTweets(file)
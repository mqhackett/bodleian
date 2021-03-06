# -*- coding: utf-8 -*-
import os
import gensim
import smart_open
import random
# Set file names for train and test data


# open some files
test_data_dir = os.path.join(gensim.__path__[0], 'test', 'test_data')
lee_train_file = os.path.join(test_data_dir, 'lee_background.cor')
lee_test_file = os.path.join(test_data_dir, 'lee.cor')

# method to open the corpus
# looks like it does some tokenization? 
# we will need to build a corpus out of our yamls 
# also, note that it's one of those yield functions
# like .. it returns, but one at a time
# and it gets called in the train_corpus
def read_corpus(fname, tokens_only=False):
    with smart_open.open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])


# put our train and test data into a list.
train_corpus = list(read_corpus(lee_train_file))
test_corpus = list(read_corpus(lee_test_file, tokens_only=True))


# instantiate our model
model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)
model.build_vocab(train_corpus)
model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)

# translate some random document into a vector
vector = model.infer_vector(['only', 'you', 'can', 'prevent', 'forest', 'fires'])
print("inferred vector", vector)

# pick a random document from the test data
doc_id = random.randint(0, len(test_corpus) - 1)
print("test document", test_corpus[doc_id])
inferred_vector = model.infer_vector(test_corpus[doc_id])

#get the most similar vectors
sims = model.dv.most_similar([inferred_vector], topn=len(model.dv))

print('Test Document ({}): «{}»\n'.format(doc_id, ' '.join(test_corpus[doc_id])))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))


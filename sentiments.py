{
 "cells": [
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Sentiment Analysis"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import nltk\n",
    "from nltk.corpus import stopwords\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import naive_bayes\n",
    "from sklearn.metrics import roc_auc_score, accuracy_score\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\dagbo\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": "True"
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('stopwords')"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Load the data"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 3,
   "outputs": [],
   "source": [
    "# Load the reviews\n",
    "df = pd.read_csv('reviews.txt', sep='\\t', names=['Reviews', 'Comments'])"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "outputs": [
    {
     "data": {
      "text/plain": "      Reviews                                           Comments\n0           1            The Da Vinci Code book is just awesome.\n1           1  this was the first clive cussler i've ever rea...\n2           1                   i liked the Da Vinci Code a lot.\n3           1                   i liked the Da Vinci Code a lot.\n4           1  I liked the Da Vinci Code but it ultimatly did...\n...       ...                                                ...\n6913        0                     Brokeback Mountain was boring.\n6914        0       So Brokeback Mountain was really depressing.\n6915        0  As I sit here, watching the MTV Movie Awards, ...\n6916        0    Ok brokeback mountain is such a horrible movie.\n6917        0   Oh, and Brokeback Mountain was a terrible movie.\n\n[6918 rows x 2 columns]",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Reviews</th>\n      <th>Comments</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>The Da Vinci Code book is just awesome.</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>this was the first clive cussler i've ever rea...</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>i liked the Da Vinci Code a lot.</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>i liked the Da Vinci Code a lot.</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>I liked the Da Vinci Code but it ultimatly did...</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>6913</th>\n      <td>0</td>\n      <td>Brokeback Mountain was boring.</td>\n    </tr>\n    <tr>\n      <th>6914</th>\n      <td>0</td>\n      <td>So Brokeback Mountain was really depressing.</td>\n    </tr>\n    <tr>\n      <th>6915</th>\n      <td>0</td>\n      <td>As I sit here, watching the MTV Movie Awards, ...</td>\n    </tr>\n    <tr>\n      <th>6916</th>\n      <td>0</td>\n      <td>Ok brokeback mountain is such a horrible movie.</td>\n    </tr>\n    <tr>\n      <th>6917</th>\n      <td>0</td>\n      <td>Oh, and Brokeback Mountain was a terrible movie.</td>\n    </tr>\n  </tbody>\n</table>\n<p>6918 rows × 2 columns</p>\n</div>"
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Preprocessing"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 5,
   "outputs": [],
   "source": [
    "stopset = set(stopwords.words('english'))"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Vectorization"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 6,
   "outputs": [],
   "source": [
    "vectorizer = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii', stop_words=stopset)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Train the model"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 7,
   "outputs": [],
   "source": [
    "X = vectorizer.fit_transform(df['Comments'])\n",
    "y = df['Reviews']\n",
    "pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Test the model"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 8,
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Naive Bayes"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 9,
   "outputs": [
    {
     "data": {
      "text/plain": "MultinomialNB()",
      "text/html": "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>MultinomialNB()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">MultinomialNB</label><div class=\"sk-toggleable__content\"><pre>MultinomialNB()</pre></div></div></div></div></div>"
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf = naive_bayes.MultinomialNB()\n",
    "clf.fit(X_train, y_train)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Evaluation"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 10,
   "outputs": [
    {
     "data": {
      "text/plain": "0.9747109826589595"
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test, clf.predict(X_test))"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# ROC AUC"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 11,
   "outputs": [
    {
     "data": {
      "text/plain": "0.9722293703894321"
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "roc_auc_score(y_test, clf.predict(X_test))"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 16,
   "outputs": [
    {
     "data": {
      "text/plain": "MultinomialNB()",
      "text/html": "<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>MultinomialNB()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">MultinomialNB</label><div class=\"sk-toggleable__content\"><pre>MultinomialNB()</pre></div></div></div></div></div>"
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf = naive_bayes.MultinomialNB()\n",
    "clf.fit(X,y)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "outputs": [
    {
     "data": {
      "text/plain": "0.9877167630057804"
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test, clf.predict(X_test))"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "outputs": [
    {
     "data": {
      "text/plain": "0.9860653628409675"
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "roc_auc_score(y_test, clf.predict(X_test))"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "source": [
    "# Save the model"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
=======
>>>>>>> 1d9f45bab07eda5c2b32d352fdbd2364afa2483c
   "cell_type": "code",
   "execution_count": 20,
   "outputs": [],
   "source": [
    "filename = 'finalized_model.pkl'"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "outputs": [],
   "source": [
    "pickle.dump(clf, open(filename, 'wb'))"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [],
   "metadata": {
    "collapsed": false
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
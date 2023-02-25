from textblob import TextBlob

en_blob = TextBlob(u'Simple is better than complex.')
print(en_blob.translate(from_lang='en', to='es'))


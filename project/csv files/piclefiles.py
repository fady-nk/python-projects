import pickle

#write a pickle file
ordering = {"first":1, "Second":2, "Third":3}
pickle.dump(ordering, open("new.pkl", "wb"))

#read a pickle file
reading_pickle = pickle.load(open("new.pkl", "rb"))
print(reading_pickle)

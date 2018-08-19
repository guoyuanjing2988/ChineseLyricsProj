import pickle

def getPoems():
    poems = pickle.load(open("poems.pickle","rb"))
    print(poems[0])
getPoems()
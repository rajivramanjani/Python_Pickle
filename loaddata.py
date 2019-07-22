try:
	import pickle # for python 3
except ImportError:
	import cPickle # fall back for python 2.7

def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    for keys in db: 
        print(keys, '=>', db[keys]) 
    dbfile.close() 
	
if __name__ == '__main__': 
    loadData() 
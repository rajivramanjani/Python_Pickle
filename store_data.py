try:
	import pickle # for python 3
except ImportError:
	import cPickle # fall back for python 2.7

def storeData(): 
    # initializing data to be stored in db 
    Omkar = {'EmpId' : 'E101', 'EName' : 'Omkar Pathak', 
    'age' : 21, 'pay' : 40000} 
    Jagdish = {'EmpId' : 'E102', 'EName' : 'Jagdish Pathak', 
    'age' : 50, 'pay' : 50000} 
  
    # database 
    db = {} 
    db['Omkar'] = Omkar 
    db['Jagdish'] = Jagdish 
      
    # Its important to use binary mode 
    dbfile = open('examplePickle', 'ab') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
if __name__ == '__main__': 
    storeData() 

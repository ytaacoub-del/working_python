import os 
import pandas as pd


def factoriel(nombre :int )->int :
  if (nombre ==0 or nombre ==1) : 
     print("release")
     return 1 
  else:  
    return nombre * factoriel(nombre-1)
 
def get_age(name :str)->int :
   print("ok")
   dataset= pd.read_csv("C:/Users/PC/Documents/DataFactory/Code/name_age.csv")
   return dataset



   




 


 

def main() :
    dataset=pd.read_csv("C:/Users/PC/Documents/DataFactory/Code/name_age.csv",sep=";",encoding="utf-8").head()
    ## exemple = factoriel(10)
    ## print(exemple)
    ##output= get_age("yaacoub")
    print(dataset)




if __name__ == "__main__" :

    main() 

    
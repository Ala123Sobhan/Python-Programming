""" Import Library """
import numpy as np
import pandas as pd
import scipy
from sklearn.cross_validation import train_test_split

""" Read CSV file """

df = pd.read_csv("banknote.csv")
X = df.iloc[:,:-1].values
Y = df.iloc[:,4].values

""" Split Training Testing Dataset """
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2, random_state= 0)



""" prior calculate """
def prior(data, K):
    p = np.ones((K))
    nrow = data.shape[0]
    for k in np.arange(K):
        p[k] = np.sum(data == k) /nrow
        
    return p
prior_ = prior(Y_train,2)



""" Gaussain components Calculate """    

def learn_Gaussain(data ,J,K) :
    mean = np.zeros(J*K).reshape((J,K))
    variance = np.zeros(J*K).reshape((J,K))
    classes = Y_train
    for j in np.arange(J):
        for k in np.arange(K):
             mean[j,k]= np.sum(data[classes==k,j])/np.sum(classes==k)
             variance[j,k]=np.sum((data[classes==k,j]-mean[j,k]) ** 2)/(np.sum(classes==k)- 1)
     
    return mean,variance

gaussians = learn_Gaussain(X_train,4,2)
gauss_mean = gaussians[0]
gauss_variance = gaussians[1]


""" Likelihood Calculate """
def likelihood(xi, k , gauss_mean, gauss_variance):
       product_of_gaussians = 1
       for j in np.arange(4):
           
           gaussian = scipy.stats.norm.pdf(xi[j],gauss_mean[j,k] ,np.sqrt(gauss_variance[j,k]))
           product_of_gaussians = product_of_gaussians * gaussian
       return product_of_gaussians

""" posterior compute """
def posterior (xi,K):
           
    post =[]
    for k in np.arange(K):
        post.append( prior_[k] * likelihood(xi, k, gauss_mean, gauss_variance))   
    return post


def naive_bayes():
    posterior(X_train,2)
    
    
    
""" Testing with Test datasetset """
classes_test = np.ones((len(X_test)))   
for i in np.arange(X_test.shape[0]):
        post = posterior(X_test[i,:], 2)
        classes_test[i] = (np.where(post == np.max(post)))[0][0]


"""accurancy Function"""        
def accurancy():
    count=0
    p=Y_test.shape[0]
    for i in np.arange(p):
        if (Y_test[i]==classes_test[i]):
            count=count+1
    
    print( "Accurancy = "+str( (count/p)*100)) 
     
    
    
"""Prediction Count """ 
def func():
    count=0
    count2=0
    count3=0
    count4=0
    p=Y_test.shape[0]
    for i in np.arange(p):
        if (Y_test[i]==0 and classes_test[i]==0 ):
            count=count+1
        if (Y_test[i]==0 and classes_test[i]==1 ):
            count2=count2+1    
        if (Y_test[i]==1 and classes_test[i]==0 ):
            count3=count3+1
        if (Y_test[i]==1 and classes_test[i]==1 ):
            count4=count4+1 
            
            
    print("0’s were predicted as 0-----" +str(count))
    print("0’s were not predicted as 0-----" +str(count2))
    print("1’s were predicted as 1-----" +str(count4))
    print("1’s were not predicted as 1-----"+ str(count3))
       

""" FUNCTION CALL """   
naive_bayes()        
accurancy()     
func()
   
        
    
 
    

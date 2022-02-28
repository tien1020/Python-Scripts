def avg(X):
    sum = 0
    for t in X:
        sum = sum + t           

    avg = sum / len(X)
    return avg

def l_sqr(X):
    return map(pow, X, [2]*len(X))
    
def var(X):
    temp = 0
    for i in X:
        for j in X:
            temp = temp + (1.0/2)*(i-j)**2
    temp = temp*1.0/len(X)**2
    return temp
        
        
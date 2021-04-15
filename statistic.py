def moyenne(L):
    S=0
    nb=0
    
    for i in L:
        S=S+i
        nb=nb+1
    
    return int(S/nb)
  
  
def trier(l):
    """Retourne une liste triée dans l'ordre croissant"""
    
    l_res = []
    ln = len(l)
    
    for i in range(ln):
        
        mini = l[0]
        p = 0
        
        for i2 in range(len(l)):
            if l[i2] < mini:
                mini = l[i2]
                p = i2
        l_res.append(l[p])
        del l[p]
        
    return l_res

  
def mediane(liste) :
    liste=trier(liste)
    n= len(liste)
    if n%2 != 0 :
        index_python  = int((n-1)/2)
        med = liste[index_python]
        return med
    else :
        index1_python = int(n/2)
        index2_python = int(n/2 - 1)
        med = (liste[index1_python] + liste[index2_python])/2
        return med

      
def quartiles(l):
    n = len(l)
    m1 = n//4
    m2 = (n*3)//4
    ltri = trier(l)
    if (n%4) == 0 :
        return (ltri[m1-1],ltri[m2-1])
    return (ltri[m1],ltri[m2])

  
def  ecart_interquartiles(l):
    q = quartiles(l)
    return q[1]-q[0]
  
  
def variance(L) :
    s = 0
    m = moyenne(L)
    for i in L :
        s = s + (i - m)*(i - m)
    return s/len(L)
  
  
def ecart-type(L) :
  return sqrt(variance(L))


def liste_reduite(l):
    q1 , q2 = quartiles(l)
    ec_int = q2-q1    
    inf = q1 - 1.5 * ec_int
    sup = q2 + 1.5 * ec_int
    L_res=[]
    
    for i in range(len(l)):       
        if l[i] <= sup and l[i] >= inf:
            L_res.append(l[i])

    return L_res

def moyenne_reduite(l):
    return moyenne(liste_reduite(l))

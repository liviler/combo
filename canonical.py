# NOTE：
# use set to store up or lo indices
# use list to store all indices.
# because list can keep the order of ele while set may change the original order. 

# PROBLEMS：
# [√] 集合的顺序会出现不规则的变化不保持原来顺序？为什么？
# FinishSet 的集合之间判断 in 似乎存在问题？


#use tuple to store indices and use list to process indices.DO NOT USEset!!

from sympy import IndexedBase
from sympy import symbols
X=IndexedBase('X')
delta=IndexedBase(chr(948))
n=IndexedBase('n')

def _selectDeltaTerms(_inputTerms):
    _deltaTerms=1
    _otherTerms=1
    for i in _inputTerms.args:
        if i.base==delta:
            _deltaTerms*=i
        else:
            _otherTerms*=i
    return _deltaTerms,_otherTerms


def _formDeltaRule(deltaTerms)->list:
    if deltaTerms==1:
        return []
    res=[]
    if deltaTerms.args[0]==delta:# only one delta item 
        eleDelta=tuple([deltaTerms])
    else:
        eleDelta=deltaTerms.args#separate delta terms  of 'deltaTerms'

    for i in eleDelta:#这里需要优化结构
        up,lo=i.args[1],i.args[2]
        if (str(up)>str(lo)):# must trans to str to compare.
            # beenReplace=symbols(str(up))
            # afterReplace=symbols(str(lo)) #big index to small index. Is it necessary to trans to a small one?
            beenReplace = up
            afterReplace = lo
        else:
            # beenReplace=symbols(str(lo))
            # afterReplace=symbols(str(up))
            beenReplace = lo
            afterReplace = up
        res.append([beenReplace,afterReplace])
    return res

def _intersection(set1,set2):
    '''
    if set1( or list1) have common elements with set2 return true.
    '''
    for i in set1:
        for j in set2:
            if i==j: return True
    return False

def changeIndices(exp,allrules):
    '''
    Replace the indices  by appling the rule.

    ## Case:
    rule={{a->b},{c->d}}
    rule={{codition,a->b},{codition,c->d}}
    rule=[[{a},{b}],[{c,f},{d}]]
    '''
    if allrules==[]:#no need to apply rule
        return exp

    for rule in allrules:#replace rule[0] to rule[1] for each allrules' element.
        if type(exp)==type(X[(),()]):
            expEle=(exp,)
        else:
            expEle=exp.args#separate the ele of exp.
        tmp=1
        for i in expEle:
            newUp,newLo=[],[]#stor up and low indices.
            eleArgs=i.args#separate the indices of ele.
            oldUp,oldLo=eleArgs[1],eleArgs[2]
            if _intersection(rule[0],oldUp): #replace the up symbols of one element.
                for j in oldUp:
                    if j in rule[0]:
                        newUp.append(rule[1][0])
                    else: newUp.append(j)
            else:newUp=oldUp
                # for k in rule[0]:
                #  for j in oldUp:
                #     if j==k:
                #          newUp.append(rule[1])
                #     else: newUp.append(j)
            if _intersection(rule[0],oldLo):#replace the dow symbols of one element.
                for j in oldLo:
                    if j in rule[0]:
                        newLo.append(rule[1][0])
                    else: 
                        newLo.append(j)
            else: newLo=oldLo
            tmp*=eleArgs[0][tuple(newUp),tuple(newLo)]
        exp=tmp

    return exp

def processDeltaTerms(inputTerms):
    '''
    Process the delta terms of the expression.

    # Examples:
    >>> processDeltaTerms(G[{i,j},{a,b}]*H[{c,d},{k,l}]*delta[{a},{c}]*delta[{b},{d}])
    G[{i, j}, {a, b}] H[{a, b}, {k, l}]

    # Note:
    - When the sets have common eles, it just show one of them, {1,1}={1}.
    - Will the inputTerms' indices have common ele?or appear after i process the delta  terms?
    - notice that delta[left,right]'s left and right come from idxup and idxLo,so it is impossible to 
    appear the common ele in a up or lo indices sets. It means that H[{c,c},{k,l}] can not appear.

    '''
    deltaTerms,otherTerms=_selectDeltaTerms(inputTerms)
    deltaRule=_formDeltaRule(deltaTerms)
    deltaRemoved=changeIndices(otherTerms,deltaRule)
    return deltaRemoved


def processDelta():
    '''
    Prcess delta terms of the exp when exp is the sum of multiterms like: A{{},{}}delta[{},{}]+B[{},{}]delta[{},{}]
    '''
    pass

def _getIndices(exp):
    res=[]
    if type(exp)==type(X[(),()]):
        res=[[exp.args[1],exp.args[2]]]
    else:
        for i in exp.args:
            up=i.args[1]
            lo=i.args[2]
            res+=[[up,lo]]
    return res

def _flattenIdx(indices):
    res=[]
    for i in indices:
        for j in i:
            res+=list(j)
    return res

def _internalAndRepeatedIdx(flatIdx,externalIdx=[]):
    res=[]
    idxdict={}#initial a dict
    for i in flatIdx:
        idxdict[i]=0
    for i in flatIdx:
        if i not in externalIdx:
            idxdict[i]+=1
            if(idxdict[i]==2):
                res.append(i)
    return res

def _getindexSet(indices,internalIdx):
    indexSets=[]
    for i in indices:
        for j in i:
            if(_union(j,internalIdx)):
                indexSets.append(_union(j,internalIdx)) 
    return indexSets


def _union(set1,set2):
    res=[]
    for i in set1:
        for j in set2:
            if i ==j:
                res.append(i)
    return tuple(res)#it seems that the set cannot keep the original order.#yes so i changed it into tuple

def _diff(set1,set2):
    '''return the diffent ele of set2 with set1'''
    res=[]
    for i in set2:
        tmp=0
        for j in set1:
            if j==i:
                tmp=1
        if tmp==0:
            res.append(i)
    return tuple(res)    

def _findEquivalentIndices(indexSets):
    equi=[]
    selectedSet=set()#stored selected ele in one-dimension set.
    for beingSelectedSet in indexSets:
        diffset=_diff(selectedSet,beingSelectedSet)
        if diffset!=():
            equi.append(diffset)
            selectedSet.update(set(diffset))# set will remove the common elements when you update it.
    return equi

def _replaceRules(equivalents):
    dummyPos=97
    rules=[]
    for set in equivalents:
        for j in set:
            rules.append([(j,),(symbols(chr(dummyPos)*2),)])
            dummyPos+=1
    return rules

def processEmptySetIn_n(exp):
    '''
    Replace EmptySet indices in 'n' to {}.
    '''
    res=1
    if type(exp)==type(X[(),()]):
        if exp.base==n:
            res*=n[(),exp.args[2]]
        else:res=exp
    else:
        for i in exp.args:
            if i.base==n:
                res*=n[(),i.args[2]]
            else:res*=i     
    return res

def canonicalOrder(term):
    res=processDeltaTerms(term)# processdeltaTerms terms
    indices=_getIndices(res)# extract out  all indices from res.
    flatIdx= _flattenIdx(indices)# all of indices in a line.
    internalIdx=_internalAndRepeatedIdx(flatIdx,externalIdx=[])#find reaped elements in flatIdx.
    indexSets=_getindexSet(indices,internalIdx)#find out the reaped indices and keep original order.
    equivalents=_findEquivalentIndices(indexSets)#remove common elements from the reaped indices which keep the original order 
    rules=_replaceRules(equivalents)#form the replace fules.
    res=changeIndices(res,rules)#apply rules
    res=processEmptySetIn_n(res)
    return res



def canonicalize(exp):
    res=0
    for i in  exp.args:
        if type(i)!=type(X[{},{}]):
            coef=i.args[0]
            if type(coef)!=type(X[{},{}]):#if it has coefficient,
                res+=coef*canonicalOrder(i/coef)# get rid of the coefficient before use canonicalOrder function.
            else:
                res+=canonicalOrder(i)
        else:
            res+=i
    return res



if __name__=='__main__':
    from sympy import IndexedBase
    from sympy import symbols

    Alpha=IndexedBase(chr(913))
    xi=IndexedBase(chr(958))
    lamda=IndexedBase(chr(955))
    delta=IndexedBase(chr(948))
    n=IndexedBase('n')

    X=IndexedBase('X')
    A=IndexedBase('A')
    B=IndexedBase('B')
    C=IndexedBase('C')
    G=IndexedBase('G')
    H=IndexedBase('H')
    a=IndexedBase('a')
    b=IndexedBase('b')
    p=IndexedBase('p')
    q=IndexedBase('q')
    r=IndexedBase('r')
    s=IndexedBase('s')
    

    case1=G[(a,), (b,)]*H[(p, q), (r, s)]*delta[(a,), (s,)]*lamda[(p, q), (b, r)]
    case1=A[(p,), (s,)]*G[(a,), (b,)]*H[(p, q), (r, s)]*n[(), (q,)]*delta[(a,), (r,)]*delta[(q,), (b,)]
    case1=G[(a,), (b,)]*H[(p, q), (r, s)]*A[(p, q), (b, s)]*delta[(a,), (r,)]
    # case1=H[(p, q), (r, s)]*delta[(a,), (s,)]
    #G[{aa}, {bb}]*H[{cc, dd}, {aa, ee}]*λ[{cc, dd}, {bb, ee}]
    caseRes=canonicalOrder(case1)
    print(case1)
    print(caseRes)
    # inputcase=A[{i, j}, {a, b}]*B[{a, b}, {k, l}] + 5*A[{i, j}, {c, d}]*B[{c, d}, {k, l}] + lamda[{c, d}, {e, f}]*A[{i, j}, {c, d}]*B[{e, f}, {k, l}]+A[{1},{2}]
    


if __name__=='canonical':
    from sympy import IndexedBase
    from sympy import symbols
    X=IndexedBase('X')
    delta=IndexedBase(chr(948))
    n=IndexedBase('n')
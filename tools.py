from sympy import IndexedBase#用于存储指标
from sympy import simplify


X=IndexedBase('X')
Y=IndexedBase('Y')#  X,Y just used to present the type of different input expression.like some multi-expr:X[{},{}]*Y[{},{}] or add-expr:X[{},{}]+Y[{},{}] 
A=IndexedBase('A')# A used to identify the exist of it in expression.
xi=IndexedBase(chr(958))
lamda=IndexedBase(chr(955))
delta=IndexedBase(chr(948))
n=IndexedBase('n')

class SmplifyRule:
    def xiRule(exp):
        expArgs=exp.args#表达式按照加减分成元组不同元素
        res=0
        for i in expArgs:
            elemArgs=i.args#表达式按照乘分成元组的不同元素
            subexp=1
            for j in elemArgs:
                if (j!=-1 and j.base==xi):
                    superscript=j.args[1]
                    subscript=j.args[2]
                    j=lamda[superscript,subscript]-delta[superscript,subscript]
                subexp*=j
            res+=subexp
        return simplify(res)

    def natRule(exp):
        expArgs=exp.args#表达式按照加减分成元组不同元素
        res=0 
        for i in expArgs:
            elemArgs=i.args#表达式按照乘分成元组的不同元素
            subexp=1
            for j in elemArgs:
                if (j!=-1 and j.base==lamda and len(j.args[1])==1):
                    superscript=j.args[1]
                    subscript=j.args[2]
                    j=n[(),superscript]*delta[superscript,subscript]
                subexp*=j
            res+=subexp
        return simplify(res)



class Filter:
    def filterbody(terms,bodyType):
        if (type(terms)!=type(X[{},{}]+Y[{},{}])):#input terms like A[{},{}]*B[{},{}] or A[{},{}]
            if(type(terms)==type(X[{},{}]*Y[{},{}])):#like A[{},{}]*B[{},{}] or -A[{},{}]*B[{},{}]
                if (type(terms.args[0])==type(A[{},{}])):#if input terms like A[{},{}]*B[{},{}]
                    firstTerm=terms.args[0]
                    if(firstTerm.base==A and len(firstTerm.args[1])==bodyType ):
                        return terms
                    else: return 0
                elif(type(terms.args[1])==type(A[{},{}])):#if input terms like -A[{},{}]*B[{},{}]
                    secondTerm=terms.args[1]
                    if(secondTerm.base==A and len(secondTerm.args[1])==bodyType ):
                        return terms
                    else: return 0    
                elif(bodyType==0):# 0-body term
                    return terms
                else: return 0 
            else:# like  A[{},{}]
                if(terms.base==A and len(terms.args[1]==bodyType)):
                    return terms
                elif(bodyType==0):
                    return terms 
                else: 
                    return 0

        else:#terms like A[{},{}]*B[{},{}] + C[{},{}]*D[{},{}]
            res=0
            for i in terms.args:# i:(A[{},{}]*B[{},{}] , C[{},{}],-D[{},{}]*E[{},{}])
                    if(type(i)==type(X[{},{}]*Y[{},{}])):#i like A[{},{}]*B[{},{}] or -A[{},{}]*B[{},{}]
                        if (type(i.args[0])==type(A[{},{}])):#if input terms like A[{},{}]*B[{},{}]
                            firstTerm=i.args[0]
                            if(firstTerm.base==A and len(firstTerm.args[1])==bodyType ):
                                res+=i
                            elif(firstTerm.base!=A and bodyType==0):
                                print(i)
                                res+=i
                        elif(type(i.args[1])==type(A[{},{}])):#if input terms like -A[{},{}]*B[{},{}]
                            secondTerm=i.args[1]
                            if(secondTerm.base==A and len(secondTerm.args[1])==bodyType ):
                                res+=i
                            elif(secondTerm.base!=A  and bodyType==0):
                                res+=i
                        elif(bodyType==0):
                            res+=i
                    else:# like  A[{},{}]
                        if(i.base==A and len(i.args[1])==bodyType):
                            res+=i
                        elif(i.base!=A and bodyType==0):
                            res+=i
            return res


def _sepatate(tmpCom,otherTerms):
    '''
    Select terms from otherTerms which has tmpCom term  to removeComTerms.
    Store term to other terms to otherTerms.
    '''
    otherComTerms=0
    if type(otherTerms)==type(X[{},{}]+Y[{},{}]):
        otherTerms=otherTerms.args
    else: otherTerms=set([otherTerms])

    for i  in otherTerms:#(-C*D,E*F)
        for j  in i.args:#(-1,C,D)
            if (j==tmpCom):
                otherComTerms+=i/tmpCom
                break
    return otherComTerms

def uniteSimilarTerms(exp):
    if(type(exp)!=type(X[{},{}]+Y[{},{}])):# return exp when it don't have add terms
        return exp
    baseTerms=exp.args[0]# select A*B from A*B+C*D
    otherTerms=exp-baseTerms
    for tmpCom in baseTerms.args:#turn A*B to (A,B),term=A,B
        com=tmpCom
        comTermsDivideCom=baseTerms/com
        otherComTermsDivideCom=_sepatate(tmpCom,otherTerms)

        if(otherComTermsDivideCom!=0):
            comTermsDivideCom+=otherComTermsDivideCom
            otherTerms=exp-(comTermsDivideCom*com).expand()
            break
    res=com*(uniteSimilarTerms(comTermsDivideCom))+uniteSimilarTerms(otherTerms)#recurse it. 
    return res









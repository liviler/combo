
from sympy import IndexedBase,symbols

from .wickcaculate import Wick 
from . import canonical
from .tools import SimplifyRule,Filter,uniteSimilarTerms,indicesMultToSimp
from . import output

A=IndexedBase('A')
G=IndexedBase('G')
H=IndexedBase('H')
delta=IndexedBase(chr(948))



class bodys:
    def __init__(self,leftIndices:list[list],rightIndices:list[list] ) -> None:
        leftIndices=[list(map(lambda x:symbols(x),i))for i in leftIndices]
        rightIndices=[list(map(lambda x:symbols(x),i))for i in rightIndices]
        self.incices=[leftIndices,rightIndices]
    
    def commutate(self):
        wickCase=Wick(self.incices[0],self.incices[1])
        wickCase.commmutate()
        self.gw=wickCase.gw
        self.cmt=wickCase.cmt
    #Infact it is not the commutate result.

    def applyRule(self,ruleType='both'):
        '''
        Chose your rule that apply to commutate result. The default value of ruleType is 'both', and you can set 'xi' or 'nat' instead.
        '''
        if ruleType=='both':
            self.cmtXN=SimplifyRule.natRule(SimplifyRule.xiRule(self.cmt))
        elif ruleType=='xi':
            self.cmtXi=SimplifyRule.xiRule(self.cmt)
        elif ruleType=='nat':
            self.cmtNat=SimplifyRule.natRule(self.cmt)
   
    def regulate(self,filterbody=None):
        self.allTerms=(G[tuple(self.incices[0][0]),tuple(self.incices[0][1])]*H[tuple(self.incices[1][0]),tuple(self.incices[1][1])]*self.cmtXN).expand()
        #Fliter
        if filterbody!=None and type(filterbody)==int:
            self.filterTerms=Filter.filterbody(self.allTerms,filterbody)
        else:
            self.filterTerms=self.allTerms
        
        #canonicalize
        canonTemp=canonical.canonicalize(self.filterTerms)
        self.canon,self.indicesSet=indicesMultToSimp(canonTemp)
    
    def amcExport(self):
        output.amcInputFIle(self.canon,self.indicesSet)

    def amcEnd(self,fliterbody=None):
        self.commutate()
        self.applyRule()
        self.regulate(fliterbody)
        self.amcExport()

def texExp(exp):
    lat_exp=output.transSymbolsToLatex(exp)
    return lat_exp

def uniteSame(exp):
    return uniteSimilarTerms(exp.expand())

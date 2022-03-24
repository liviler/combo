
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

    def help(self):
        '''
        Display the meaning of attributes.
        '''
        print("# The attribute in class bodys")
        print("Attribute".rjust(15),"Description")
        atrMsg=[
            ["gw","Generalized Wick Result"],
            ["cmt", "gw1 - gw2"],
            ["cmtXN","Apply xiRule and natRule to cmt"],
            ["cmtXi","Apply xiRule to cmt"],
            ["cmtNat","Apply natRule to cmt"],
            ["allTerms","All Terms after applying  xiRule and natRule"],
            ["filterTerms","Filter Result"],
            ["canon","Canonicalized Result(Deal the deal term and rename the indices)"], 
        ]
        for i in atrMsg:
            print((i[0]+':').rjust(15),i[1])

        print("\n\n")
        print("# The methods in class bodys")
        print("Method".rjust(15),"Description")
        mtdMsg=[
            ["commutate","Caculate commutation relation."],
            ["apply","Apply rule to the commutation relation result."],
            ["regular","Filter your input body type and  Canonicalized the filter terms(deal the deal term and rename the indices )"],
            ["amcExport","Form a amc document based on the regular result(after filtering)"],
            ["amcEnd","Do the above 4 steps  in this function directly."],
            ["texplay","Display all step result by latex in jupyter. "],

        ]
        for i in mtdMsg:
            print((i[0]+':').rjust(15),i[1])


        print("\n\n")
        print("# The function in mboc")
        print("Function".rjust(15),"Description")
        fucMsg=[
            ["texExp","Trans the expression to latex."],
            ["uniteSame","Combine the same terms."],
        ]
        for i in fucMsg:
            print((i[0]+':').rjust(15),i[1])

    def texplay(self,jupyter="yes"):
        '''
        Display all step result by latex in jupyter.If you just want to show the latex expression, please set  the parameter: jupyter="no".
        '''
        attributes=["gw","cmt","cmtXN","cmtXi","cmtNat","allTerms","filterTerms","canon",]
        if jupyter=="yes":
            for i in attributes:
                try:
                    exp=getattr(self,i)
                    laxExp=output.transSymbolsToLatex(exp)
                    if i=="filterTerms":
                       print( "filterTerms("+ str(filterBodyType) + "bodys) :")
                    else:
                        print(i,":") 
                    output.jupyterTexDisplay(laxExp)
                except:
                    print('No attribute called:',i )
        if jupyter=="no":
            for i in attributes:
                try:
                    exp=getattr(self,i)
                    laxExp=output.transSymbolsToLatex(exp)
                    if i=="filterTerms":
                       print( "filterTerms("+ str(filterBodyType) + "bodys) :")
                    else:
                        print(i,":") 
                    print(laxExp) 
                except:
                    print('No attribute called:',i )

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
            global filterBodyType
            filterBodyType=filterbody
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



from sympy import IndexedBase

from urllib import request
import webbrowser


from wickcaculate import Wick 
import canonical
from tools import SmplifyRule,Filter,uniteSimilarTerms
import output


a=IndexedBase('a')
b=IndexedBase('b')
p=IndexedBase('p')
q=IndexedBase('q')
s=IndexedBase('s')
r=IndexedBase('r')
A=IndexedBase('A')
G=IndexedBase('G')
H=IndexedBase('H')



def Z(Low,Up)->list:
    return [Low,Up]

def main():
    #use generalizedwick to caculate commutate 
    my_wick_test=Wick(Z([a],[b]),Z([p,q],[r,s]))
    my_wick_test.commmutate()
    res1=my_wick_test.cmt
    print('commuteResult:\n',res1,'\n')

    #apply xiRule and natRule
    res2=SmplifyRule.xiRule(res1)
    res3=SmplifyRule.natRule(res2)
    print('Apply xiRule and natRule Result:\n',res3,'\n')

    #nuiltiply the head and  form allTerms 
    allTerms=res3*G[(a,),(b,)]*H[(p,q),(r,s)]
    allTerms=allTerms.expand()
    print('mutiply the head Result:\n',allTerms,'\n')


    #canonical it (remove delta Terms)
    res5=canonical.canonicalize(allTerms)
    print('Canonicalize it Result:\n',res5,'\n')

    #unite the similiar terms
    res6=uniteSimilarTerms(res5)
    print('unite the similiar terms:\n',res6,'\n')

    #Filter x-body terms:
    res7=Filter.filterbody(res5,2)
    print('Terms of 2bodys in canonicalized Result:\n',res7,'\n')

    #Trans to latex:
    lat_exp=output.transSymbolsToLatex(res7)
    print('latex expression:\n',lat_exp,'\n')

## TODO 
## 1. 要将latex公式输出实现
## 2. 测试之前出现的1体二体之间出现符号的事故原因
## 3. 测试是否满足反对称性质
## 4. 研究如何导出未amc对接口

    # tex_request='https://www.zhihu.com/equation?tex='+lat_exp
    # print(tex_request)
    # webbrowser.open(tex_request)

    # lat_exp='$'+lat_exp+'$'
    # mathtext.math_to_image(lat_exp, r'.\demo_1.png')

main()

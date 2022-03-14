'''
输出结果
'''


from IPython.display import display, Latex#latex公式输出
import sympy as sy
sy.init_printing()


def transSymbolsToLatex(tmp):
    str_exp=str(tmp)
    str_lax=''
    state_body=0#1  means process a multi terms 
    state_idx=0# =1 finish processing  the up idx,=2 means finish processing the dow idx.
    pos=0# store the work position of str_exp
    for i in str_exp:
        if(state_body==0 and i=='['):
            str_lax+='^'
            state_body=1
        elif(state_body==1 and i=='('):
            str_lax+='{'
        elif(state_body==1 and state_idx==0 and i==')'):
            str_lax+='}'
            state_idx=1
        elif(state_idx==1 and i==','):
            str_lax+='_'
            state_idx=2
        elif(state_body==1 and state_idx==2 and i==')'):
            str_lax+='}'
            state_idx=0
        elif(state_body==1 and i==']'):
            state_body=0
        elif(i=='*'):
            pass
        elif(i==chr(913)):
            str_lax+='A'
        elif(i==chr(958)):
            str_lax+='\\xi'
        elif(i==chr(955)):
            str_lax+='\\lambda'
        elif(i==chr(948)):
            str_lax+='\\delta'
        elif(i==',' and str_exp[pos+1]==')'):# do not show ',' when  up or down idx only have one element.
            pass
        else:
            str_lax+=i
        pos+=1
    return str_lax

def jupyterTexDisplay(lat_exp):
    display(Latex(f"$${lat_exp}$$")) 
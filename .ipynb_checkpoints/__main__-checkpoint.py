
#输入
## * 输入指标不能有相同的


from operations import Wick 
import output
import sys

def main():
    my_wick_test=Wick(['a'],['b'],['c','d'],['e','f'])
    my_wick_test.generalizedWick()
    lat_exp=output.transSymbolsToLatex(my_wick_test.res)
    print(lat_exp)


main()
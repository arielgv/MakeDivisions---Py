#Clossure ,  applied in mathematics

def dividendo (n):
    def divisor (m):
        return m/n
    return divisor
#So this is a  easily understandable clossure case where a function applies in as a dividend and divisor

def run():
    divided_by_3=dividendo(3)
    divided_by_5=dividendo(5)
    divided_by_18=dividendo(18)
    numb = int(input("number : "))
    print(divided_by_3(numb))
    print(divided_by_5(numb))
    print(divided_by_18(numb))

if __name__== "__main__":
    run()
    
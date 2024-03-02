

def is_substring(s:str, p:str):
    p_split = p.split("*")
    val=True
    ind = 0
    for ele in p_split:
        if ele in s:
            if s.index(ele)>=ind:
                ind = s.index(ele)
            else:
                val=False
        else:
            val = False
    return val

if __name__ == '__main__':
    print(is_substring("helloworld", "s*l*d"))
    
import sys
# import numpy as np

def read_data(filename):
    """
    Reads the data from a given file and returns a list of tuples.
    """
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            b, g, c, f = map(int, line.strip().split())
            data.append((b, g, c, f))
    return data

bdic = {}
cdic = {}
gdic = {}
fdic = {}
def count(data):
    """
    Updates the  (bdic, cdic, gdic, fdic) dictionaries by iterating over the data.
    """
    for d in data:
        b,g,c,f =d
        if b not in bdic:
            bdic[b] = 1
        else:
            bdic[b] += 1
        if c not in cdic:
            cdic[c] = 1
        else:
            cdic[c] += 1    
        if (b,g) not in gdic:
            gdic[(b,g)] = 1
        else:
            gdic[(b,g)] += 1
        if (g,c,f) not in fdic:
            fdic[(g,c,f)] = 1
        else:
            fdic[(g,c,f)] += 1

b1  = c1  = g1b0=g1b1=f1g1c1=f1g1c0= f1g0c1= f1g0c0= float("inf")   

def calculate_probabilities():
    """
    Calculates the probabilities of each variable and their combinations and prints them out
    """
    b1 = bdic[1]/(bdic[0]+bdic[1])
    c1 = cdic[1]/(cdic[0]+cdic[1])
    g1b1 = gdic[(1,1)]/bdic[1]
    g1b0 = gdic[(0,1)]/bdic[0]
    f1g1c1 = fdic[(1,1,1)]/ (fdic[(1,1,1)] + fdic[(1,1,0)])
    f1g1c0 = fdic[(1,0,1)]/ (fdic[(1,0,1)] + fdic[(1,0,0)])
    f1g0c1 = fdic[(0,1,1)]/ (fdic[(0,1,1)] + fdic[(0,1,0)])
    f1g0c0 = fdic[(0,0,1)]/ (fdic[(0,0,1)] + fdic[(0,0,0)])
    print("P(B=True) = {:.4f} | P(B=False) = {:.4f}".format(b1,1-b1))
    print("P(C=True) = {:.4f} | P(C=False) = {:.4f}".format(c1,1-c1))
    print("P(G=True),P(B=True) = {:.4f}  | P(G=False),P(B=True) = {:.4f}".format(g1b1,1-g1b1))
    print("P(G=True),P(B=False) = {:.4f} | P(G=False),P(B=False) = {:.4f}".format(g1b0,1-g1b0))
    print("P(F=True),P(G=True),P(C=True) = {:.4f} | P(F=False),P(G=True),P(C=True) = {:.4f}".format(f1g1c1, 1-f1g1c1))
    print("P(F=True),P(G=True),P(C=False) = {:.4f} | P(F=False),P(G=True),P(C=False) = {:.4f}".format(f1g1c0, 1-f1g1c0))
    print("P(F=True),P(G=False),P(C=True) = {:.4f} | P(F=False),P(G=False),P(C=True) = {:.4f}".format(f1g0c1, 1-f1g0c1))
    print("P(F=True),P(G=False),P(C=False) = {:.4f} | P(F=False),P(G=False),P(C=False) = {:.4f}".format(f1g0c0, 1-f1g0c0))

def calculate_jpd(b_val, g_val, c_val, f_val):
    """
    Takes the values of the variables and calculates the joint probability distribution of all the variables by multiplying and selecting it from each dictionary.
    """
    # P(B, G, C, F) = P(F | G, C) * P(G | B) * P(C) * P(B)
    p_f_gcf = fdic[(g_val, c_val, f_val)] / (fdic[(g_val, c_val, 1)] + fdic[(g_val, c_val, 0)])
    p_g_b = gdic[(b_val, g_val)] / bdic[b_val]
    p_c = cdic[c_val] / (cdic[0] + cdic[1])
    p_b = bdic[b_val] / (bdic[0] + bdic[1])
    jpd = p_f_gcf * p_g_b * p_c * p_b
    return jpd


def main():
    if len(sys.argv) == 6:
        filename = sys.argv[1]
        b_val = 1 if sys.argv[2] == "Bt" else 0
        g_val = 1 if sys.argv[3] == "Gt" else 0
        c_val = 1 if sys.argv[4] == "Ct" else 0
        f_val = 1 if sys.argv[5] == "Ft" else 0
        data = read_data(filename)
        # print(data)
        count(data)
        calculate_probabilities()
        prob = calculate_jpd(b_val,g_val,c_val,f_val)
        print("P(B={}, G={}, C={}, F={}) = {:.4f}".format(sys.argv[2][1:], sys.argv[3][1:], sys.argv[4][1:], sys.argv[5][1:], prob))
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        data = read_data(filename)
        # print(data)
        count(data)
        calculate_probabilities()
    else:
        print("Invalid number of arguments. Please provide either 2 or 6 arguments.")
        return

if __name__ == '__main__':
    main()

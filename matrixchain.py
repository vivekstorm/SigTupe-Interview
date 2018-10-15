import sys
import argparse

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    print('Example usage is: python matrixchain.py 3,1,5,8')
    parser.add_argument("--list","-l",help="Enter the elements of list seperated by comma",required=True)
    args=parser.parse_args()
    list=args.list
    a=[int(x) for x in list.split(',')]
    a=[1]+a+[1]
    prize = [[0]*len(a) for _ in range(len(a))]
    n=len(a)
    print('----------------------')
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            prize[i][j] = -sys.maxsize
            for k in range(i, j):
                prize[i][j]=max(prize[i][j],prize[i][k] + prize[k+1][j] + a[i-1]*a[k]*a[j])

    print(prize[1][n-1])

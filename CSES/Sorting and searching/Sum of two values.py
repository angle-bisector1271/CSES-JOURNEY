def main():
    n,x=map(int, input().split())
    l=list(map(int, input().split()))
    a=[]
    for i in range(n):
        a.append((l[i],i+1))
    a.sort()
    l=0
    r=n-1
    while(l<r):
        if a[l][0]+a[r][0]>x:
            r-=1
        elif a[l][0]+a[r][0]<x:
            l+=1
        else:
            print(a[l][1],a[r][1]) # type: ignore
            return
    print("IMPOSSIBLE")
 
if __name__ == '__main__':
    main()

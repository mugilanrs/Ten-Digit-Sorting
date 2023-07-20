#Ten Digit Sorting
def tendigit(a):
    return sorted(a,key=lambda x:((x//10)%10,-x))
    
a=list(map(int,input().split()))
print(tendigit(a))

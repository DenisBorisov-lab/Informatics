n = int(input())
list_ = list(map(int, input().split()))
max = max(list_)
list_.sort()
cnt = 0
flist = []
slist = []
for i in range(len(list_) - 1):
    cnt += list_[i]
if(n < 3):
    print("no")
elif cnt < max:
    print("no")
else:
    cnt = 0
    for i in list_:
        cnt += i
    s = cnt // 3
    cnt = 0
    j = 0
    while cnt < s:
        flist.append(list_[j])
        cnt += list_[j]
        j += 1
    list_.remove(max)
    for i in range(j, len(list_)):
        slist.append(list_[i])
    print("yes")
    print(len(flist), " ", *flist)
    print(len(slist), " ", *slist)
    print(1, " ", max)











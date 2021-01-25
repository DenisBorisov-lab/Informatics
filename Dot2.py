n = int(input())
list_ = list(map(int, input().split()))
flist = []
slist = []
tlist = []
l = len(list_)
ans = l // 3
for i in range(0, ans):
    flist.append(list_[i])
print(flist)

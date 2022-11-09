import random

ans=["1","2","3","4"]
random.shuffle(ans)
for i in range(len(ans)):
    print(chr(i+65)+". "+ans[i])
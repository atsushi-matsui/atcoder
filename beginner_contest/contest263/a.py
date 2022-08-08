a,b,c,d,e = map(int, input().split())
CA = [0] * 13

CA[a-1] +=1
CA[b-1] +=1
CA[c-1] +=1
CA[d-1] +=1
CA[e-1] +=1

is_triple = False
is_double = False
for ca in CA:
    if ca == 3:
        is_triple =True 
    if ca == 2:
        is_double = True
        
if is_triple and is_double:
    print("Yes")
else:
    print("No")
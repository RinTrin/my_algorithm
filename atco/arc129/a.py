N, L ,R = map(int, input().split())

add = 0
for x in range(L, R+1):
    if x^N < N:
        add+=1
print(add)

N_bin = bin(N)[2:]
N_bin_len = len(N_bin)
L_bin = bin(L)[2:]
L_bin_len = len(L_bin)
R_bin = bin(R)[2:]
R_bin_len = len(R_bin)

for spell_i in range(L_bin_len+1, R_bin_len+1):
    N_spell = N_bin[spell_i]
    next_spell = L_bin[spell_i]
    if N_spell==1 and :


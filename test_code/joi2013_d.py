d, n = map(int, input().split())
t_list = []
for d_ in range(d):
    t_list.append(int(input()))
data_list = []
for n_ in range(n):
    data_list.append(list(map(int,input().split())))

dp = [[[None, None] for _ in range(n)] for _2 in range(d)]
for n_ in range(n):
    a, b, c = data_list[n_]
    if a<=t_list[0]<=b:
        dp[0][n_] = [0, c]
for day, t in enumerate(t_list[1:]):
    for i, (a, b, c) in enumerate(data_list):
        if a<=t<=b:
            input_val = -1
            for n_ in range(n):
                if dp[day][n_][1] is not None:
                    if abs(dp[day][n_][1]-c)+dp[day][n_][0] >= input_val:
                        input_val = abs(dp[day][n_][1]-c)+dp[day][n_][0]
            # print(f'day : {day}, c : {c}, dp_data : {dp[day]}')
            if input_val>=0:
                dp[day+1][i] = [input_val, c]
        else:
            pass
max_value = 0
for value, c in dp[-1]:
    if value is not None:
        if value > max_value:
            max_value = value
print(max_value)
# print(dp)
# print(max(dp[-1], key=lambda x:x[0])[0])

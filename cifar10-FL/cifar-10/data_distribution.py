import random

data_sum = 0

clients = dict()
for i in range(1000):
    data = random.randint(1,100)
    data_sum += data
    if data not in clients:
        clients[data] = 1
    else:
        clients[data] += 1

print(data_sum)
print(clients)

if data_sum > 50000:
    over = data_sum - 50000
    while over > 0:
        index1 = random.randint(1,100)
        index2 = random.randint(1,100)
        if over - abs(index2 - index1) < 0:
            continue
        over -= abs(index2 - index1)
        if index1 < index2:
            clients[index1] += 1
            clients[index2] -= 1
        else:
            clients[index1] -= 1
            clients[index2] += 1


data_sum = 0
client_sum = 0
for data in clients:
    data_sum += data * clients[data]
    client_sum += clients[data]

print(data_sum, client_sum)

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(101)
clients = dict(sorted(clients.items(), key=lambda item: item[0], reverse=False))
clients = list(clients.values())

output_list = []
for index, num_clients in enumerate(clients):
    for i in range(num_clients):
        output_list.append(index + 1)
random.shuffle(output_list)
print(len(output_list))
print(output_list)
print(sum(output_list))
# values = [0] + list(clients.values())
# values = [0 for i in range(101)]
# values[50] += 1000


# plt.bar(x, values)
# plt.rc('font', size=10)
# plt.title("WO/ data quantity heterogeneity")
# plt.xlabel('#data')
# plt.ylabel('#clients')
# plt.show()
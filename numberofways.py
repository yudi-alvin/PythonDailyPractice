def decode(data,k, memo=[]):
    if k ==0:
        return 1
    s= len(data)-k
    if data[s] == '0':
        return 0

    result = decode(data, k-1)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result = result + decode(data,k-2)
    # memo.append(result)
    return result

def num_ways(data):
    return decode(data, len(data))

print(num_ways("123456"))

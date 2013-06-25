#Basically just finding the prime divisors and multiplying their highest powers
def prime_div(check_num):
    primes = set([])
    cur_prime = 2
    prime_div = []
    while cur_prime <= check_num:
        isPrime = True
        for prime in primes:
            if cur_prime % prime == 0:
                isPrime = False
                cur_prime += 1
        if isPrime:
            primes.add(cur_prime)
            if check_num % cur_prime == 0:
                prime_div.append(cur_prime)
    return prime_div

def num_prime_div(check_num, ind_list):
    true_num = check_num
    primes = prime_div(check_num)
    for num in primes:
        true_num = check_num
        flag = 0
        ind = 0
        while true_num % num == 0:
            ind += 1
            true_num /= num
        for i in range(len(ind_list)):
            if num == ind_list[i][0]:
                ind_list[i][1].append(ind)
                flag = 1
        if flag == 0:
            ind_list.append([num, [ind]])

def ans(lis):
    ind_list = []
    acc = 1
    for thing in lis:
        num_prime_div(thing, ind_list)
    for things in ind_list:
        acc *= things[0]**max(things[1])
    return acc

print ans([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
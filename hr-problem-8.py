if __name__ == '__main__':
    M = int(input())
    m = set(input().split())
    N = int(input())
    n = set(input().split())
    set_m = m.difference(n)
    set_n = n.difference(m)
    joined_set = sorted(list(map(int, set_m.union(set_n))))
    for i in joined_set:
        print(i)
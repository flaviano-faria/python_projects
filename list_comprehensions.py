def create_list(i_max, j_max, k_max, n):
    complete_list = []
    for i in range(0, i_max + 1):
        for j in range(0, j_max + 1):
            for k in range(0, k_max + 1):
                if (is_n_sum(i, j, k, n)):
                    continue
                else:
                    temp_list = [i, j, k]
                    complete_list.append(temp_list)

    print(complete_list)


def is_n_sum(i, j, k, n):
    return i + j + k == n


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    create_list(x, y, z, n)

import sys



def size_sum(*args):
    mem_sum = 0
    var_values = [] # добавляем посчитанные значения

    for i in args:

        if isinstance(i, dict):
            mem_sum += sys.getsizeof(i)

            for key, value in i.items():

                if key not in var_values:
                    mem_sum += sys.getsizeof(key)
                    var_values.append(key)
                if value not in var_values:
                    mem_sum += sys.getsizeof(value)
                    var_values.append(value)

        if isinstance(i, list):
            mem_sum += sys.getsizeof(i)
            for j in i:
                if j not in var_values:
                    mem_sum += sys.getsizeof(j)
                    var_values.append(j)

        else:
            if i not in var_values and not isinstance(i, dict):
                mem_sum += sys.getsizeof(i)
                var_values.append(i)

    print(f'Задействованно памяти = {mem_sum}')


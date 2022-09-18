import sys

if __name__ == '__main__':
# Ввести список A из 10 элементов .

 a=list(map(int,input().split ()))
print(min(a))
 #Проверить количество элементов списка.
if len(a) != 10:
 print("Неверный размер списка", file=sys.stderr)

#переставить наименьший элемент с последним
i_min = a.index(min(a))
i_max = a.index(max(a))

a[i_min],a[i_max]=a[i_max],a[i_min]
print(a)

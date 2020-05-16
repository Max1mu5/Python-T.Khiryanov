"""
Эта программа прошла все тесты кроме последних двух, так как в них нарушены условия входных данных

main_arr - Основной массив для хранения значений экзаменов студентов
count_top - Массив, в котором хранится числовое значение,
            показывающее количество элементов в подмассиве основного массива с совпадающим индексом
"""
N = int(input())
main_arr = [[]] * N
count_top = [0] * N

stud_info = input()
while stud_info != '#':
    stud_id, stud_val = map(int, stud_info.split())

    temp = [-1] * (count_top[stud_id] + 1)
    for i in range(count_top[stud_id]):
        temp[i] = main_arr[stud_id][i]

    temp[count_top[stud_id]] = stud_val
    count_top[stud_id] += 1
    main_arr[stud_id] = sorted(temp, reverse=True)

    stud_info = input()

main_arr.sort(key=lambda x: sum(x), reverse=True)
for i in range(N):
    for j in main_arr[i]:
        print(j, end=' ')

from datetime import datetime
from time import sleep


# создать дэйт тайм объект в функции, сохраняем, проверяем есть ли объект, в момент йилда к последнему значению +1 и в конце в сроковый вид и возвращаем
def show_time(numb):
    for i in numb:
        time = datetime.now()
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        print(now_time)
        sleep(1)
    pass


n = input("Enter a numb: ")
[show_time(n) for x in range(1, int(n)+1)]

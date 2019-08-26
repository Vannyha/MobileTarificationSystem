# MobileTarificationSystem
Программа для подсчёта стоимости услуг мобильной связи за определённый месяц, где учитывается роуминг (в т.ч. если абонент вошёл в него раньше), длительность звонка, количество символов в СМС, потраченный интернет.

В data записаны события: Звонки, СМС, вход и выход с роуминга, потраченный пакет интернета. Не стал делать отдельным файлом, всё находится в main.py т.к. так требует задание.

В консоль вводим месяц и год, за который нужно посчитать, и будет выведена в консоль подробная детализация.

Пример с данными, которые уже есть в программе:

Ввод:
> 1.1982

Вывод:
```
Detalization
Total recharge: 0
Total expenses: 461
Incoming calls (home net): 0 |Lenght: 0 min |Charged: 0 RUB
Incoming calls (roaming): 1 |Lenght: 2 min |Charged: 16 RUB
Outgoing calls (home net): 0 |Lenght: 0 min |Charged: 0 RUB
Outgoing calls (roaming): 2 |Lenght: 2 min |Charged: 40 RUB
Incoming SMS: 0 |Charged: 0 RUB
Outgoing SMS (home net): 0 |Charged: 0
Outgoing SMS (roaming): 1 |Charged: 5
Mobile internet (home net): 0 |Charged: 0
Mobile internet (roaming): 20 |Charged: 400
----------------
Do you want see another period? Y/N

```

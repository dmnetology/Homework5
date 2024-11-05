'''Задание 1
Печатные газеты использовали свой формат дат для каждого выпуска. 
Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
The Moscow Times — Wednesday, October 2, 2002
The Guardian — Friday, 11.10.13
Daily News — Thursday, 18 August 1977'''

from datetime import datetime

while True:
    dt = input("Введите дату (любой одиночный символ - завершить программу): ")
    if len(dt) == 1:
        print("Конец программы!")
        break
        
    try:
        dt1 = print("The Moscow Times — ", datetime.strptime(dt, "%A, %B %d, %Y"))
    except ValueError:
        try:
            dt1 = print("The Guardian — ", datetime.strptime(dt, "%A, %d.%m.%y"))
        except ValueError:
            try:
                dt1 = print("Daily News — ", datetime.strptime(dt, "%A, %d %B %Y"))
            except ValueError:
                print("Неизвестный формат даты. Попробуйте еще раз!")

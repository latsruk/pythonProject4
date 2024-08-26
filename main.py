Number_of_completed_homework=12 # Количество выполненных ДЗ
Number_of_hours_spent=1.5 # Количество затраченных часов
Course_Title='Python' # Название курса
time_task = (Number_of_completed_homework and Number_of_hours_spent ) # Время на одно задание
print('Курс:',Course_Title,',всего задач:',Number_of_completed_homework,', затрачено часов:',Number_of_hours_spent,
', среднее время выполнения',(Number_of_hours_spent/Number_of_completed_homework,'часа'))
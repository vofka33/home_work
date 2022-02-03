#Практический кейс на списки
users = [
         [15634602, 15647311, 15619304, 15701354],#'CustomerId'
         ['Hargrave', 'Hill', 'Onio', 'Boni'],#'Surname'
         [619, 608, 502, 699], #'CreditScore'
         ['Female', 'Female', 'Female', 'Female'], #'Gender'
         [42, 41, 42, 39], #'Age'
         [1, 0, 1, 0] #Exited
         ]


#Расчитает среднее по признаку кредитного рейтинга для ушедших клиентов
middle_creditScore = (users[2][0] + users[2][2]) / users[5].count(1)
print("Cреднее по признаку кредитного рейтинга для ушедших клиентов", middle_creditScore)

#Средний возраст всех клиентов
middle_age = sum(users[4]) / len(users[4])
print('Средний возраст всех клиентов:', middle_age)

#Долю ушедших клиентов
exited_clients = users[5].count(1) / len(users[5])
print("Доля ушедших клиентов:", exited_clients)

#Выведет идентификаторы клиентов, которые ушли от банка
print("Идентификаторы клиентов, которые ушли от банка:", users[0][0], users[0][2])


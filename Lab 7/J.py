# J
# -*- coding: utf-8 -*-
def deposit(arg):
    name, money = arg
    bank[name] = bank.setdefault(name, 0) + int(money) #функция для депозита


def balance(arg):
    name = arg[0]
    if name in bank:	#функция для проверки баланса
        print(bank[name])
    else:
        print('ERROR')

def withdraw(arg):
	name, money = arg   #функция для снятия денег
	bank[name] = bank.setdefault(name, 0) - int(money)

def transfer(arg):
    name_1, name_2, money = arg   #функция для перевода
    for name in (name_1, name_2):
        if name not in bank:
            deposit((name, 0))
    withdraw((name_1, money))
    deposit((name_2, money))

def income(arg):
    percent = int(arg[0])
    for name, balanse in bank.items():	#для начисления
        if balanse > 0:
            bank[name] = bank.get(name) + balanse * percent // 100

bank = {}
bank_vozm = {
    'DEPOSIT': deposit, 'WITHDRAW': withdraw, #создание словаря
    'BALANCE': balance, 'TRANSFER': transfer,
    'INCOME': income
}
for _ in range(int(raw_input())):
    data = input().split()
    fun_name = data[0]	#обработка команд
    arg = data[1:]
    bank_vozm[fun_name](arg)
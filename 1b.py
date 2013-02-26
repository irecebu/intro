balance = float(raw_input('balance : '))
a_rate = float(raw_input('annual rate : '))


def calculate(balance, annualInterestRate):
    start = 10
    while True:
        temp = balance
        for i in range(12):
            balance -= (start - (balance-start)*annualInterestRate/12)

        print 'balance', balance
        if balance <= 0:
            print 'found min' , start
            break
        start += 10
        balance = temp
calculate(balance, a_rate)

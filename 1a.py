balance = float(raw_input('balance : '))
a_rate = float(raw_input('annual rate : '))
m_rate = float(raw_input('min monthly : '))


def calculate(balance, a_rate, m_rate):
    a = round(a_rate/12)
    total = 0
    for i in range(12):
        monthly = round(balance*m_rate,2)
        balance -= (monthly - round((balance-monthly)*a_rate/12, 2))
	total += monthly
        print 'Month : ', i + 1
        print 'Minimum monthly payment ', round(monthly,2)
        print 'Remaining balance', balance 
    print 'Total paid:', total
    print 'Remaining Balance:', balance



calculate(balance, a_rate, m_rate)

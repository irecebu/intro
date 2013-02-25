balance = float(raw_input('balance : '))
a_rate = float(raw_input('annual rate : '))
m_rate = float(raw_input('min monthly : '))


def calculate(balance, a_rate, m_rate):
    for i in range(12):
        monthly = balance*m_rate
        print 'month : ', i + 1
        print 'monthly ', round(monthly,2)
        print 'remaining balance', balance - monthly
        balance -= (monthly - balance*a_rate/12)




calculate(balance, a_rate, m_rate)

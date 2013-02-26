balance = float(raw_input('balance :'))
a_rate = float(raw_input('annual rate : '))

def calculate(balance, annualInterestRate):
    low = balance/12
    high = (balance*(1 + annualInterestRate/12)**12)/12.0
    ans = (high+low)/2
    while True:
        temp = balance
        for i in range(12):
            balance -= (ans - (balance-ans)*annualInterestRate/12)

        #print 'balance', balance
        #a = raw_input('hi')
        if abs(balance) - 0.01 <= 0:
            print 'Lowest Payment:', round(ans,2)
            break
        if balance < 0:
            high = ans
        else: 
            low = ans
        ans = (high + low)/2
        balance = temp


calculate(balance, a_rate)

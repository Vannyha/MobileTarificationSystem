import math

EVENT_TOPUP = 1  # [EVENT_TOPUP, RUB, MM.YYYY]
EVENT_IN_CALL = 2  # [EVENT_INC_CALL, DURATION, MM.YYYY]
EVENT_OUT_CALL = 3  # [EVENT_OUT_CALL, DURATION, MM.YYYY]
EVENT_IN_SMS = 4  # [EVENT_INC_SMS, SMS, MM.YYYY]
EVENT_OUT_SMS = 5  # [EVENT_OUT_SMS, SMS, MM.YYYY]
EVENT_INTERNET = 6  # [EVENT_INTERNET, MB, MM.YYYY]
EVENT_ENT_R = 7  # [EVENT_ENT_R, MM.YYYY]
EVENT_OUT_R = 8  # [EVENT_OUT_R, MM.YYYY]

data = [
    [EVENT_TOPUP, 400, 12.1981],
    [EVENT_ENT_R, 12.1981],
    [EVENT_IN_CALL, 61, 1.1982],
    [EVENT_OUT_CALL, 61, 1.1982],
    [EVENT_OUT_CALL, 2, 1.1982],
    [EVENT_OUT_SMS, 'hello world123', 1.1982],
    [EVENT_INTERNET, 20, 1.1982],
    [EVENT_OUT_R, 1.1982],
    [EVENT_IN_CALL, 171, 2.1982],
    [EVENT_OUT_CALL, 33, 2.1982],
    [EVENT_OUT_CALL, 2, 2.1982],
    [EVENT_OUT_SMS, 'test sms', 2.1982],
]


def calc(mm, yyyy):
    i = 0  # counter
    topup = 0  # total topup in mounth
    expenses = 0  # total expenses
    incalls = 0  # incoming calls in home network (minutes)
    incalls_count = 0  # incoming calls in home network (count)
    incalls_rub = 0  # incoming calls in home network (RUB)
    outcalls = 0  # outgoing calls in home network (minutes)
    outcalls_count = 0  # outgoing calls in home network (count)
    outcalls_rub = 0  # outgoing calls in home network (RUB)
    incalls_r = 0  # incoming calls in roaming (minutes)
    incalls_r_count = 0  # incoming calls in roaming (count)
    incalls_r_rub = 0  # incoming calls in roaming (RUB)
    outcalls_r = 0  # outgoing calls in roaming minutes
    outcalls_r_count = 0  # outgoing calls in roaming (count)
    outcalls_r_rub = 0  # outgoing calls in roaming (RUB)
    insms = 0  # incoming sms
    outsms = 0  # outgoing sms in home network (counter)
    outsms_rub = 0  # outgoing sms in home network (RUB)
    outsms_r = 0  # outgoing sms in roaming (counter)
    outsms_r_rub = 0  # outgoing sms in roaming (RUB)
    internet = 0  # internet in home network (MB)
    internet_rub = 0  # internet in home network (RUB)
    internet_r = 0  # internet in roaming (MB)
    internet_r_rub = 0  # internet in roaming (RUB)

    roaming = 0;  # 0 if home, 1 if roaming
    for i in range(len(data)):
        splitdate = str(data[i][len(data[i]) - 1]).split('.')  # split date in database
        if (data[i][0] == EVENT_ENT_R):
            roaming = 1  # If roaming enter
        if (data[i][0] == EVENT_OUT_R):
            roaming = 0  # If roaming exit
        if (int(splitdate[0]) == mm and splitdate[1] == yyyy):
            if (data[i][0] == EVENT_TOPUP):  # topup balance
                topup = topup + data[i][1]

            if (data[i][0] == EVENT_IN_SMS):  # incoming sms are free, only++ counter each 70 symbols
                symbols = int(math.ceil(len(data[i][1]) / 70))
                insms = insms + symbols

            if (data[i][0] == EVENT_IN_CALL):  # incoming call
                duration = int(math.ceil(data[i][1] / 60))
                rub = incall(duration, roaming)
                if (roaming == 0):
                    incalls_count = incalls_count + 1
                    incalls = incalls + duration
                    incalls_rub = incalls_rub + rub
                if (roaming == 1):
                    incalls_r_count = incalls_r_count + 1
                    incalls_r = incalls_r + duration
                    incalls_r_rub = incalls_r_rub + rub
                expenses = expenses + rub

            if (data[i][0] == EVENT_OUT_CALL):  # outgoing call
                duration = 0
                if (data[i][1] > 3):  # if call length > 3 sec.
                    duration = int(math.ceil(data[i][1] / 60))
                rub = outcall(duration, roaming)
                if (roaming == 0):
                    outcalls_count = outcalls_count + 1
                    outcalls = outcalls + duration
                    outcalls_rub = outcalls_rub + rub
                if (roaming == 1):
                    outcalls_r_count = outcalls_r_count + 1
                    outcalls_r = outcalls_r + duration
                    outcalls_r_rub = outcalls_r_rub + rub
                expenses = expenses + rub

            if (data[i][0] == EVENT_OUT_SMS):  # outgoing sms
                symbols = int(math.ceil(len(data[i][1]) / 70))
                rub = outsmsf(symbols, roaming)
                if (roaming == 0):
                    outsms = outsms + 1
                    outsms_rub = outsms_rub + rub
                if (roaming == 1):
                    outsms_r = outsms_r + 1
                    outsms_r_rub = outsms_r_rub + rub
                expenses = expenses + rub

            if (data[i][0] == EVENT_INTERNET):  # internet
                traffic = int(math.ceil(data[i][1] / 1))
                rub = internetf(traffic, roaming)
                if (roaming == 0):
                    internet = internet + traffic
                    internet_rub = internet_rub + rub
                if (roaming == 1):
                    internet_r = internet_r + traffic
                    internet_r_rub = internet_r_rub + rub
                expenses = expenses + rub
    if (expenses == 0 and insms == 0):
        print('No data found')
    else:
        print('Detalization')
        print('Total recharge:', topup)
        print('Total expenses:', expenses)
        print('Incoming calls (home net):', incalls_count, '|Lenght:', incalls, 'min |Charged:', incalls_rub, 'RUB')
        print('Incoming calls (roaming):', incalls_r_count, '|Lenght:', incalls_r, 'min |Charged:', incalls_r_rub,
              'RUB')
        print('Outgoing calls (home net):', outcalls_count, '|Lenght:', outcalls, 'min |Charged:', outcalls_rub, 'RUB')
        print('Outgoing calls (roaming):', outcalls_r_count, '|Lenght:', outcalls_r, 'min |Charged:', outcalls_r_rub,
              'RUB')
        print('Incoming SMS:', insms, '|Charged: 0 RUB')
        print('Outgoing SMS (home net):', outsms, '|Charged:', outsms_rub)
        print('Outgoing SMS (roaming):', outsms_r, '|Charged:', outsms_r_rub)
        print('Mobile internet (home net):', internet, '|Charged:', internet_rub)
        print('Mobile internet (roaming):', internet_r, '|Charged:', internet_r_rub)
        print('----------------')


def incall(duration, roaming):
    sums = 0
    if (roaming == 1):
        sums = duration * 8
    return sums


def outcall(duration, roaming):
    if (roaming == 0):
        sums = duration * 2
    if (roaming == 1):
        sums = duration * 20
    return sums


def outsmsf(symb, roaming):
    if (roaming == 0):
        sums = symb
    if (roaming == 1):
        sums = symb * 5
    return sums


def internetf(traf, roaming):
    if (roaming == 0):
        sums = int(traf * 0.2) + 1
    if (roaming == 1):
        sums = traf * 20
    return sums


def read():
    print('Please enter date (MM.YYYY): ')
    l = input().split('.')
    if (int(l[0]) > 12 or int(l[0]) < 1 or int(l[1]) < 1980 or int(l[1]) > 2019):
        print('Incorrect date')
        return
    else:
        calc(int(l[0]), l[1])
        return


def main():
    yn = 'Y'
    print('This program *insert here*, dates from 01.1980 to 12.2019')
    read()
    while (yn == 'Y' or yn == 'y'):
        print('Do you want see another period? Y/N')
        yn = input()
        if (yn == 'Y' or yn == 'y'):
            read()
    return


if __name__ == '__main__':
    main()
#This program solves Project Euler #79.

logins = [319,680,180,690,129,
          620,762,689,762,318,
          368,710,720,710,629,
          168,160,689,716,731,
          736,729,316,729,729,
          710,769,290,719,680,
          318,389,162,289,162,
          718,729,319,790,680,
          890,362,319,760,316,
          729,380,319,728,716]

def is_valid(passcode,login):
    "Given a passcode and a login attempt, check if the passcode could be valid."
    login = list(str(login))
    passcode = list(str(passcode))
    if login[0] not in passcode:
        return False
    passcode = passcode[(passcode.index(login[0]))+1:]
    if login[1] not in passcode:
        return False
    passcode = passcode[(passcode.index(login[1]))+1:]
    if login[2] not in passcode:
        return False
    else:
        return True


def is_valid_for_all(logins,passcode):
    """Check if a given passcode is valid for all given login attempts."""
    for login in logins:
        if not is_valid(passcode,login):
            return False
    return True

for passcode in range(100,100000000):
    if is_valid_for_all(logins,passcode):
        print(passcode)
        break
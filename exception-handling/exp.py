
class TooYoungException(Exception):
    #provide description
    def __init__(self,msg):
        self.msg=msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg

try: 
    age=int(input("enter age "))
    if age>60 :
        raise TooYoungException('Please wait..')
    elif age < 14 :
        raise TooOldException('you have alr crossed your age..')
    else:
        print("you will get matched details soon")
except TooYoungException as e:
    print(f"TooYoungException: {e.msg}")
except TooOldException as e:
    print(f"TooOldException: {e.msg}")

print("end of code")
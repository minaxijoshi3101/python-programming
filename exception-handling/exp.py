
class TooYoungException(Exception):
    #provide description
    def __init__(self,msg):
        self.msg=msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input("enter age "))
if age>60 :
    raise TooYoungException('Please wait..')
elif age < 14 :
    raise TooOldException('you have alr crossed your age..')
else:
    print("you will get matched details soon")
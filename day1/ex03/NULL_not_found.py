def NULL_not_found(object: any) -> int:
    if (object == None):
        print(f"Nothing: None {type(object)}")
    elif (isinstance(object, float) and object != object):
        print(f"Cheese: nan {type(object)}")
    elif (isinstance(object, bool) and object == False):
        print(f"Fake: False {type(object)}")
    elif (isinstance(object, int) and object == 0):
        print(f"Zero: 0 {type(object)}")
    elif (isinstance(object, str) and object == ""):
        print(f"Empty: {type(object)}")
    else :
        print("Type not Found")
        return 1
    return 0
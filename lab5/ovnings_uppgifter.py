def create_lock(num, str):
    def actual_lock(guess):
        if guess == num:
            print(str)
        else:
            print("Fel kod!")
    return actual_lock

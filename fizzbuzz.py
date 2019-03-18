def fizzbuzz(a, b):
    pass
    try:
        combined_length= len(a)+len(b)
        if combined_length%3==0 and combined_length%5==0:
            return "fizzbuzz"
        elif combined_length%5==0:
            return "buzz"
        elif combined_length%3==0:
            return "fizz"
        else:
            return combined_length
            
    except TypeError:
        return "Invalid input"   
#  WAP2 to create a module having a function with 5 subject marks as parameters. In another module print the average of these marks

# Args will hold 5 subject marks
def marks(*args):
    avg = 0

    # Loop through all Marks 
    for mark in args:
        # Grabbing to total mark 
        avg += mark
    
    # Returning the val 
    return avg/len(args)



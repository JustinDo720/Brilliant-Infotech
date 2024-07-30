class AverageMarks:

    def __init__(self, mark_list):
        self.mark_list = mark_list

    def total(self):
        total = 0 
        for mark in self.mark_list:
            total += mark 
        return total 
    
    def avg(self):
        return self.total()/len(self.mark_list)
    


def student_report(**kwargs):
    total+0
    for k,v in kwargs:
        print(k,v)
        total +=v
    return len(kwargs),total/len(kwargs)


#ex call    
print(student_report(rohan=50))

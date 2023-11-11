# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20221447
# Date: 12/13/2022


print('''              Hello,Welcome!

              INSTRUCTIONS:

Range of your credits should be within [0,20,40,60,80,100,120]
Total should not exceed 120 credits
''')

credit_list=[]
outcome_list=[]
ID_list=[]
mydict={}

ranges=[0,20,40,60,80,100,120]        
def inputs(prompt):
    """ Checks erros in inputs"""
    while True:
        try:
            credit=int(input(prompt))
            if credit not in ranges:
                print("Out of range")
                continue
        except ValueError:
            print("Integer required")
            continue
        break
    return credit

        
def process():
    global progress,trailer,retreiver,exclude,Total
    while True:
        pass_credit=inputs("Please enter your PASS credits: ")
        defer_credit=inputs("Please enter your DEFER credits: ")
        fail_credit=inputs("Please enter your FAIL credits: ")

        student_id=input("Please enter your student ID with 8 characters(w_ _ _ _ _ _ _ ): ")
        ID_list.append(student_id)
        
        credit=[pass_credit,defer_credit,fail_credit]
        credit_list.append(credit)

        if pass_credit+ defer_credit + fail_credit == 120:
        
            if pass_credit == 120:
                outcome = "Progress"
            
            elif pass_credit==100:
                 outcome ="Progress(module trailer)"
                 
            elif pass_credit <=80 and fail_credit <=60:
                 outcome ="Module Retriever"
            
            else:
                 outcome ="Exclude"
                 
        else:
            print('Total incorrect')
            continue
        outcome_list.append(outcome)
        print(outcome)
        break
    print(" ")

process()

while True:
    do=input("Would you like to enter another set of data?\nEnter y for 'yes'or q for 'quit': ")
    if do == "q":
       break
            
    elif do == 'y':
        print(" ")
        process()
    
    else:
        print('INVALID')


print(" ")   
#dictionary
for i in range(len(outcome_list)):
    mydict[ID_list[i]]=[outcome_list[i],'-',credit_list[i]] #creating dictionary
    
for k,v in mydict.items():
    s = (f"{k} : {v}")    #converting to string to remove list brackets,single quotes
    s = s.replace("'","")
    s = s.replace("[","").replace("]","")
    print(s,end=" ")
    




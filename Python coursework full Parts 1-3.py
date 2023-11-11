# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20221447
# Date: 12/13/2022


print('''               Hello,Welcome!

                INSTRUCTIONS:

Range of your credits should be within [0,20,40,60,80,100,120]
Total should not exceed 120 credits
''')

progress=0
trailer=0
retreiver=0
exclude=0
Total=0
credit_list=[]
outcome_list=[]

ranges=[0,20,40,60,80,100,120]

def inputs(prompt):
    """Checks errors in input"""
    while True:
        try:
            credit=int(input(prompt))
            if credit not in ranges:
                print("out of range")
                continue
        except ValueError:
            print("Integer required")
            continue
        break
    return credit


def process():
    """Getting input and processing it to get progression outcomes"""
    
    global progress,trailer,retreiver,exclude,Total
    while True:
        pass_credit=inputs("Please enter your PASS credits: ")
        defer_credit=inputs("Please enter your DEFER credits: ")
        fail_credit=inputs("Please enter your FAIL credits: ")

        credit=[pass_credit,defer_credit,fail_credit]
        credit_list.append(credit)

        if pass_credit+ defer_credit + fail_credit == 120:
        
            if pass_credit == 120:
                outcome = "Progress"
                progress+=1
                Total+=1
            
            elif pass_credit==100:
                 outcome ="Progress(module trailer)"
                 trailer+=1
                 Total+=1
                 
            elif pass_credit <=80 and fail_credit <=60:
                 outcome ="Module Retriever"
                 retreiver+=1
                 Total+=1
            
            else:
                 outcome ="Exclude"
                 exclude+=1
                 Total+=1
        
        else:
            print('Total incorrect')
            continue
        outcome_list.append(outcome)
        print(outcome)
        break
    print(" ")

process()
#quit or rerun the program
while True:
    do=input("Would you like to enter another set of data?\nEnter y for 'yes'or q for 'quit': ")
    if do == "q":
        print('...........................................')
        print('Progress ',progress, ':','*'*progress)
        print('Trailer  ',trailer ,':','*'*trailer)
        print('Retriever',retreiver ,':','*'*retreiver)
        print('Exclude ',exclude ,' :','*'*exclude)
        print(Total, 'outcomes in total')
        print('...........................................')
        break
            
    elif do == 'y':
        print(" ")
        process()
    
    else:
        print('INVALID')

  
#part2 list
for i,j in zip(outcome_list,credit_list):
    x=(f'{i} - {j}')
    x=x.replace("[","").replace("]","") 
    print(x)
          
#part 3 text file-write
f=open("cwlist.txt","w")
for i,j in zip(outcome_list,credit_list):
    x=(f'{i} - {j} \n')
    x=x.replace("[","").replace("]","")
    f.write(x)
f.close()

print(" ")

#part 3 text file-read
print("This is the print outcome of read-(text-file):")
f=open("cwlist.txt","r")
content=f.read()
print(content)
f.close()


#referred this website for zip() function - https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples 























                                                  














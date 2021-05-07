

import pandas as pd
from random import randint
import random

user = pd.read_csv('user_test.csv')
mentor_pref = pd.read_csv('mentor_pref.csv')
mentee_pref = pd.read_csv('mentee_pref.csv')


def match_score(mentor_pref, mentee_pref):
    
    # pulling mentee 1's answer
    mentee_a1 = mentee_pref.loc[0,'question1']
    mentee_a2 = mentee_pref.loc[0,'question2']
    mentee_a3 = mentee_pref.loc[0,'question3']
    
    mentor_pref['score']=0
    
    answers = [mentee_a1, mentee_a2, mentee_a3]
    questions = ['question1','question2','question3']
    
    i=0
    
    for answer in answers:
        answer = answer.strip('][').split(', ')


        
        total_len = len(answer)
        q_name = questions[i]

        for choice in answer:
            
            choice = str(choice)
            mentor_pref.loc[mentor_pref[str(q_name)].str.contains(choice),'score'] += 1/total_len
    
        
        i+=1
    
    
    
    
    mentor_pref = mentor_pref.sort_values('score', ascending=False)
    
    return mentor_pref






def top_3(mentor_pref):
    mentor_pref = mentor_pref.sort_values('score', ascending=False).head(30)

    indexs = random.sample(range(0, 29), 3)

    top_3 = []

    for index in indexs:

        top_3.append(int(mentor_pref.iloc[index]['id']))
        
    return top_3



def match_maker(mentor_pref, mentee_pref):
    
    
    mentor_pref = match_score(mentor_pref, mentee_pref)



    # Final Output
    top_3_list = top_3(mentor_pref)
    
    return top_3_list



match_maker(mentor_pref, mentee_pref)

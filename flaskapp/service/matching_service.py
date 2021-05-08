import pandas as pd
import random

from .user_service import get_all_mentors


def token_words(string):
    """
    This function creates tokens for the provided string
    """


    stop_words = "안녕하세요 입니다 에서 로서 하고 있습니다 입니다 일을 을 맡고 nan 에서 를 만들때 되는 합니다 가 및 , 에서 . 그리고 등을 \'\' \' \" \"\" 지금 좋아합니다 자주 거의 가끔 게속 매일"
    stop_end_words =['를','을','로서','하는','에','과','와','으로','가','의','습니다','입니다','어요','도']



    stop_words=stop_words.split(' ')

    string_cleaned = string.replace('.','').replace('"','')

    string_token = string_cleaned.split(' ')



    result = []
    for w in string_token:
        
        if w not in stop_words and len(w)>=2:
            for s_word in stop_end_words:
                w = w.rstrip(s_word)
                
            if len(w)>=2:
                result.append(w)
    return result

def match_score(mentor_pref, mentee_pref):
    
    # pulling mentee 1's answer
    field = mentee_pref.loc[0,'field'].strip('][').split(', ')
    major = mentee_pref.loc[0,'major'].strip('][').split(', ')
    interest = mentee_pref.loc[0,'interest'].strip('][').split(', ')

    if mentee_pref.loc[0,'project'] != None and mentee_pref.loc[0,'hobby'] != None:
        project = token_words(mentee_pref.loc[0,'project'])
        hobby = token_words(mentee_pref.loc[0,'hobby'])
    else:
        project = []
        hobby = []

    #Reset Mentor's Score
    mentor_pref['score']=0
    
    # Combining All Mentee's Keywords Into One List
    keywords = field + major  + project + hobby
    
    # Combining All Mentor's Info
    mentor_comb = mentor_pref['job_title'] + ' ' + mentor_pref['job_desc']+ ' ' + mentor_pref['field'] + ' ' + mentor_pref['major'] + ' ' + mentor_pref['interest']
    
    # For all keywords, find a match!
    for keyword in keywords:
        mentor_pref.loc[mentor_comb.str.contains(keyword), 'score'] += 1
    
    # for interest, add less points
    for keyword in interest:
        mentor_pref.loc[mentor_comb.str.contains(keyword), 'score'] += 0.5
    
    
    mentor_pref = mentor_pref.sort_values('score', ascending=False)

    return mentor_pref

def top_3(mentor_pref):
    mentor_pref = mentor_pref.sort_values('score', ascending=False).head(30)
    
    # Choose Randomly From Top N
    N = 10
    indexs = random.sample(range(0, 10), 3)
    top_3 = []

    for index in indexs:
        top_3.append(int(mentor_pref.iloc[index]['id']))
        print(mentor_pref.iloc[index])

    return top_3


def match_maker(mentor_pref, mentee_pref):
    mentor_pref = match_score(mentor_pref, mentee_pref)
    # Final Output
    top_3_list = top_3(mentor_pref)
    return top_3_list

def convert_to_dict(mentor):
  return mentor.to_dict()

def perform_matching(mentee):
  # TODO: Caching? maybe in the far future..

  mentor_dicts = []
  mentors = get_all_mentors()
  for mentor in mentors:
    mentor_dicts.append(mentor.to_dict())

  mentors_df = pd.DataFrame(mentor_dicts)
  mentees_df = pd.DataFrame([mentee.to_dict()])
  
  print(mentees_df)
#   print(mentors_df)

  ###### MAGIC STUFF #######
  # TODO: super fancy ML algorithm
  matched_mentor_ids =  match_maker(mentors_df, mentees_df)

  ##########################
  return matched_mentor_ids

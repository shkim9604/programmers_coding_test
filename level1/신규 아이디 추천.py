import re
def solution(new_id):
    answer = ''
    answer = new_id.lower() #1단계
    answer = re.sub("[^a-z\d\-_.]",'',answer) #2단계
    while ".." in answer: #3단계
        answer = answer.replace("..",".")
    answer = re.sub('^\.|\.$', '', answer) #4단계
    if len(answer) == 0:
        answer += 'a'
    if len(answer) >= 16:
        answer = re.sub('\.$','',answer[0:15])
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer
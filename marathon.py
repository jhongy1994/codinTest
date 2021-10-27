#제출답안, 정확도는 통과하였으나 효율성에서 탈락

def solution(participant,completion):
    plus = participant + completion
    for part in participant:
        if plus.count(part)%2!=0:
            fail = part
            break
    return fail

#참석자 리스트 participant와 완주명단 completion을 알 때, 완주하지 못한 한사람을 찾아야 함 (선수이름 중복가능)
#첫번째 해답/ 정확성 OK, 효율성 Bad
def solution(participant, completion):
    for comPerson in completion:
        participant.remove(comPerson)
    answer = participant[0]
    return answer

#sort 사용 정답
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            answer = participant[i]
            break
    return answer

#답안 참고 collection사용
import collections

def solution(participant, completion):
    notCom = collections.Counter(participant) - collections.Counter(completion)
    answer = list(notCom)[0]
    return answer

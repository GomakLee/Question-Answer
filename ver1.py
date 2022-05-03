#이상형 질문게시판 ver1. {질문1:답변1,질문2:답변2}
total_dict={}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dict[question] = ""

print(total_dict)

for k in total_dict: 
    print(k)
    answer = input("답변을 입력해주세요 : ")
    total_dict[k] = answer

print(total_dict)

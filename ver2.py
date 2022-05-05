#이상형 질문게시판 ver2. [{'질문':'취미는?','답변':'먹기'},{'질문':'특기','답변':'피아노'}]
total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == 'q':
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})


for k in total_list:
    print(k['질문'])
    answer = input("답변을 입력해주세요 : ")
    k['답변'] = answer

print(total_list)
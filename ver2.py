#이상형 질문게시판 ver2. [{'질문':'취미는?','답변':'먹기'},{'질문':'특기','답변':'피아노'}]
total_list = []

dict={}
while True:
    question = input("질문을 입력해주세요 : ")
    if question == 'q':
        break
    else:
        dict['질문'] = question
        print(dict)
        total_list.append(dict)
        print(total_list)



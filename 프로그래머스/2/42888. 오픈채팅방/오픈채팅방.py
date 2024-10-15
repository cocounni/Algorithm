def solution(record):
    answer = []
    user_dict = {}

    for i in record:
        word = i.split()
        command = word[0]
        userId = word[1]
        
        if command in ["Enter", "Change"]:
            userNick = word[2]
            user_dict[userId] = userNick

    for i in record:
        word = i.split()
        command = word[0]
        userId = word[1]
        
        if command == "Enter":
            answer.append(f"{user_dict[userId]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{user_dict[userId]}님이 나갔습니다.")

    return answer
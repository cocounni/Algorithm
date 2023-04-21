# 문자열 입력받기
text = input()
ppap_find = []
# change_str = text.replace("PPAP", "P")

if text == "PPAP" or text == "P":           #초기 text가 PPAP, P일 경우
    print("PPAP")
else:
    for i in text:
        ppap_find.append(i)

        PPAP = ['P', 'P', 'A', 'P']

        if ppap_find[-4:] == PPAP:        #PPAP가 쌓이면
            ppap_find.pop()
            ppap_find.pop()
            ppap_find.pop()

    if ppap_find == PPAP or ppap_find == ['P']:     #최종 결과가 PPAP거나 P면
        print('PPAP')
    else:
        print('NP')
    


# elif len(text) > 4 and change_str == "PPAP":
#     print("PPAP")
# else:
#     print("NP")

# for i in range(text):
#     stack.append(text)

# print(text)

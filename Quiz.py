# ## Quiz 1 : 구구단 2~9단을 출력하라 출력할때, 2x3=6 같이 어떤 값을 곱하였는지도 함께 출력하라.
#
# for index in range(2,10) :
#     for beta in range(1,10) :
#         print(index , "x" , beta , "=" , index*beta)


# ## Quiz 2 : 구구단 함수를 작성. 매개변수 입력에 따라 해당 구구단을 화면에 출력하는 함수 작성.
#
# def alpha(a) :
#     print(a, "단")
#     for g in range(1,10) :
#         print(a ,"x", g, "=", a*g)
#
# # input과 함수의 정의는 다름! 별개로 따로 사용할 것.
# # 사용자에게 입력받은 값은 문자열로 출력되기 때문에 int 사용해서 숫자열로 바꿔줘야 함.
# # int를 아래에 사용하지 않고 input 앞에 사용해도 됨.
# p = (input("숫자를 입력해주세요. : "))
# alpha(int(p))

# ## Quiz 3 : 문자메세지 길이 판별 함수. 메시지 길이 20 이하 50원, 20 초과 100원 문자 요금을 반환하는 코드 작성.
#
# def seta(k) :
#     result = 0
#     if len(k) <= 20:
#         # print("50원 입니다.")
#         result = 50
#     elif len(k) > 20:
#         # print("100원 입니다.")
#         result = 100
#     return result
#
# p = (input("문자메세지를 입력해주세요. : "))
# print(seta(p))

# ## Quiz 4 : 학점 변환기 함수. 점수 구간에 해당하는 학점이 아래와 같이 정의 시 사용자로부터 score 입력 받아 학점으로 환산하고 반환
# ## A : 81 ~ 100 / B : 61 ~ 80 / C : 41 ~ 60 / D : 21~ 40 / E : 0 ~ 20
#
# def score(x) :
#     a = 0
#     if 81 <= x <= 100 :
#         a = "A"
#     elif 61 <= x <= 80 :
#         a = "B"
#     elif 41 <= x <= 60 :
#         a = "C"
#     elif 21 <= x <= 40 :
#         a = "D"
#     elif 0 <= x <= 20 :
#         a = "E"
#
#     return a
#
# q = int(input("점수를 입력해주세요. : "))
# print(score(q))

# ## Quiz 5 : 리스트 변수의 평균 값을 구하는 함수를 작성하시오.
# ## 리스트의 길이는 매번 달라질수 있음에 유의. sum 함수 사용 금지
#
# def aver(c) :
#     qwer = 0
#     for f in


# ## Quiz 6 : 홀수/짝수 판별기 함수, 매개변수 입력에 따라 홀수 또는 짝수를 자동으로 판별하는 함수를 작성.
# ## 반환되는 값은 '홀수' 또는 '짝수'이다.
#
# def version(y) :
#     if y % 2 == 0 :
#         j = "짝수"
#     else :
#         j = "홀수"
#     return j
#
# j = int(input("숫자를 입력하세요. :"))
# print(version(j))


## Quiz 7 : 판매가가 저장된 리스트가 있을 때 부가ㅔ 포함된 가격 리스트 반환 함수

numbers = [100,200,300]
def pay(numbers) :
    money = []
    for num in numbers :
        money.append(num + (num*0.1))
    return money

print(pay(numbers))
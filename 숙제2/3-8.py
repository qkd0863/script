name = input("사원 이름을 입력하세요:")
hour = eval(input("주 당 근무시간을 입력하세요:"))
pay = eval(input("시간 당 급여를 입력하세요:"))
tax1 = eval(input("원천징수세율을 입력하세요:"))
tax2 = eval(input("지방세율을 입력하세요:"))

print("사원 이름:", name)
print("주당 근무시간:", hour)
print("임금", pay)
print("총 급여:", pay * hour)
print("공제:")
print("원천징수세(", (pay * hour) * tax1, "):")
print("주민세(", (pay * hour) * tax2, "):")
print("총 공제:", (pay * hour) * tax1 + (pay * hour) * tax2)
print("공제 후 급여:", pay * hour - ((pay * hour) * tax1 + (pay * hour) * tax2))

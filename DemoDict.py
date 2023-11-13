#DemoDict.py

device = {"아이폰":5,"아이패드":10, "윈도우타블렛":20}

print(len(device))
print(device)

#검색
print(device["아이폰"])

#입력
device["맥북"] = 15

#삭제
del device["아이패드"]
#print(device[0]) 이렇게 사용하면 에러남. dict는 인덱싱이 되지 않음.
print(device)

#수정
device["아이폰"] = 6

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

#전화번호 저장
phone = {"kim":"1111","lee":"2222","park":"3333"}
print("kim" in phone) # 여기서 in 은 include로 키가 포함이 되어 있는지 확인
print("kang" not in phone)

#참조를 전달
p = phone
p["kang"] = "1234"
print(phone)
print(p)
print(id(phone)) #id는 메모리의 identity 값 확인
print(id(p))


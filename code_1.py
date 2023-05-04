total = 0;
counter = 1;
while counter <= 10:
    grade= int(input("점수입력하시오.:"));
    total= grade + total;
    counter= counter + 1;
average = total / 10;
print("평균은 ",average, "입니다.")
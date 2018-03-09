s = float(input('请输入您的身高：'))
t = float(input('请输入您的体重：'))
BMI = t / (s*s)
if BMI < 18.5:
    print('您的BMI值为：%.2f'%BMI,'，体重过轻')
elif BMI >= 18.5 and BMI <= 25:
    print('您的BMI值为：%.2f'%BMI,'，体重正常')
elif BMI >25 and BMI < 28:
    print('您的BMI值为：%.2f'%BMI,'，体重过重')
elif BMI >=28 and BMI <= 32:
    print('您的BMI值为：%.2f'%BMI,'，体重肥胖')
else:
    print('您的BMI值为：%.2f'%BMI,'，体重严重肥胖')
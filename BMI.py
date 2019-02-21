name = input('name:')
height = input('height(m):')
weight = input('weight(kg):')
BMI = float(float(weight)/(float(height)**2))
print('your BMI is:', BMI)
if BMI < 18.5 :
    print('太重')
elif BMI <= 25 :
    print('标准')
elif BMI <=32 :
    print('有点胖')
else :
    print('太胖')
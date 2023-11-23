height = float(input("输入身高（米）："))
weight = float(input("输入体重（千克）："))
bmi = weight / (height ** 2)
print(f"您的BMI指数为：{bmi:.2f}")
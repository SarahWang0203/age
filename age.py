driving = input('請問你有沒有開過車?')
if driving != '有' and '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit #觸發系統離開錯誤 raise是觸發的意思

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了!')
	else:
		print('你沒有通過測驗。')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照了!')
	else:
		print('再過幾年就可以考駕照了!')

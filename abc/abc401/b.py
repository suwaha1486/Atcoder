n = int(input())

error_sum = 0
login_flg = False
for _ in range(n):
  action = input()
  if action == 'login':
    login_flg = True
  elif action == 'logout':
    login_flg = False
  elif action == 'private' and not login_flg:
    error_sum += 1

print(error_sum)
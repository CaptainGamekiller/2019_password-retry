i = 3
while True and i >0:
    password = input('請輸入密碼，最多輸入3次密碼：')
    if password == 'a123456' :
        print('登入成功！')
        break#break縮進位置在if的block裡面
    else:
        i = i-1
        print('密碼錯誤！')
        if i > 0:
            print('還有', i, '次機會')

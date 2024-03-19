
var = 15

# 変数varが3の倍数と5の倍数のとき
if var % 15 == 0:
    print("fizzBuzz")
    
# 変数varが3の倍数のとき
elif var % 3 == 0:
    print("Fizz")
    
# 変数varが5の倍数のとき
elif var % 5 == 0:
    print("Buzz")
    
# どの場合も該当なし
else :
    print("var")  
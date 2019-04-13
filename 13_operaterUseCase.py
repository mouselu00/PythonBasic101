# 項目：運算子功能範例

saving = int(input("請輸入你的存款："))

if saving >= 10000 and saving <= 50000:
     print("你可以做零股投資")

elif saving > 50000 and saving < 100000:
     print("可以考慮繼續存並買股票")

elif saving >= 100000:
     print("你可以直接買股票")
else:
     print("對不起，請確認你的存款")

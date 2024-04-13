schaurmaBase = 120
schaurmaDayTwoIncreasePerc = 15
schaurmaDayThreeDecreasePerc = 13
schaurmaDayFourthIncreaseFlat = 34
schaurmaDayLastDecreasePerc = 16

schaurmaDayTwoPrice = schaurmaBase + (schaurmaBase * schaurmaDayTwoIncreasePerc / 100)
schaurmaDayThreePrice = (100 - schaurmaDayThreeDecreasePerc) * schaurmaDayTwoPrice / 100
schaurmaDayFourthPrice = schaurmaDayThreePrice + schaurmaDayFourthIncreaseFlat
schaurmaDayLastPrice = (100 - schaurmaDayLastDecreasePerc) * schaurmaDayFourthPrice / 100

# Отдельные вычисления
#print("Цена второго дня:", schaurmaDayTwoPrice )
#print("Цена третьего дня:", schaurmaDayThreePrice )
#print("Цена четвёртого дня:", schaurmaDayFourthPrice)
print("В итоге шаурма стоит", schaurmaDayLastPrice, "денег")
import pandas

myData = {
    "Brands" : ["Lamborghini", "Pagani", "Ferrari", "TatuNanu"],
    "Top Speed" : [300,450,275,500],
    "Price" : ["1.3M", "1.5M", "1.75M", "0.25M"]
}

dataFrame = pandas.DataFrame(myData)
print(dataFrame)
print()
print(dataFrame.loc[3])
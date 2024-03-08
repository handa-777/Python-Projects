import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_num = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
red_num = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
black_num = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()

num_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_num, red_num, black_num]
}

df = pandas.DataFrame(num_dict)
df.to_csv("squirrel_count.csv")
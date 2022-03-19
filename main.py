import pandas
a = pandas.read_csv("nato.csv")
dict = {row.letter : row.code for (index,row) in a.iterrows()}
word = input("ENTER A WORD: ").upper()
di = [dict[letter] for letter in word]
print(di)

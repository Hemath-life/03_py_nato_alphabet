# student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # print(row.student)
#     # Access index and row
#     # Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}


# Project

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

file_frame = pd.read_csv("07_Nato_alphabet/a.csv")
phonetic_dict = {row.letter: row.code for (index, row) in file_frame.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter Your  Word : ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)





# for word in words:
#     for letter in word:
#         for ky, vl in phonetic_dict.items():
#             if letter == ky:
#                 print(vl)
#     print("")
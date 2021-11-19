from os import PathLike, path
import pandas as pd

cities_df = pd.read_csv('Instructions/Resources/cities.csv')

 #convert table to html
city_table = cities_df.to_html()
print(city_table)

text_file= open("city_table.html", "w")
text_file.write(city_table)
text_file.close()

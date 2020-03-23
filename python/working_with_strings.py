#filename: working_with_strings.py
#whitespaces
favorite_language = '    python '
print("Before stripping: " + favorite_language + ".")

print("After cleaning the whitespace: " + favorite_language.strip() + ".")
# Apostrophies need to be escaped
message = 'One of Python\'s strengths is it\'s diverse community.'
print(message)
#numbers
age = 40
message = "Happy " + str(age) + "th Birthday."
print (message)
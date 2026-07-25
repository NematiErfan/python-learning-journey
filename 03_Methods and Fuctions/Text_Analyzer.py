

def count_characters(text_inp):
	character_count = len(text_inp)
	return character_count


def count_uppercase(text_inp):
	uppercase_count = 0

	for char in text_inp:
		if char.isupper():
			uppercase_count += 1

	return uppercase_count

def count_lowercase(text_inp):
	lowercase_count = 0

	for char in text_inp:
		if char.islower():
			lowercase_count += 1

	return lowercase_count

def count_digits(text_inp):
	digit_count = 0

	for char in text_inp:
		if char.isdigit():
			digit_count += 1

	return digit_count

def count_words(text_inp):

	word_list = text_inp.split()
	word_count = len(word_list)

	return word_count

def get_unique_words(text_inp):
	word_list = text_inp.split()
	unique_word = []

	for word in word_list:
		if word not in unique_word:
			unique_word.append(word)

	return unique_word

def count_word_frequency(text_inp):
	word_list = text_inp.split()
	unique_words = get_unique_words(text_inp)

	word_count = {}

	for word in unique_words:
		word_count[word] = word_list.count(word)

	return word_count




def clean_text(text_inp):
    cleaned_text = text_inp.lower()
    return cleaned_text

def analyze_text(text_inp):

	cleaned_text = clean_text(text_inp)

	characters  	= count_characters(text_inp)
	uppercase  		= count_uppercase(text_inp)
	lowercase  		= count_lowercase(text_inp)
	digits 	    	= count_digits(text_inp)
	words 	    	= count_words(cleaned_text)
	word_unique 	= get_unique_words(cleaned_text)
	word_frequency  = count_word_frequency(text_inp)


	print("=================")
	print("Analyze your Text")
	print("=================")
	print()
	print("Characters :", characters)
	print("Uppercase Count: ",uppercase)
	print("Lowercase Count: ",lowercase)
	print("Digital Count: ",digits)
	print("Word Count: ",words)
	print("Unique Words: ",word_unique)
	print("Unique Word Count:", len(word_unique))

text_inp = input("Enter your Text: ")
analyze_text(text_inp)
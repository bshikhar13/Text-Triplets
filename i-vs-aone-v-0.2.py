import nltk
nltk.data.path.append('/home/shikhar/Documents/Shikhar/namo/nltk_data')
from nltk.corpus import stopwords



#Stemming the document
def stem_document(document):
	from nltk.stem import LancasterStemmer
	stemmer = LancasterStemmer()
	return stemmer.stem(document)

#Lemmatizing the documennt
def lemmatize_document(document):
	from nltk.stem import WordNetLemmatizer
	lemmatizer = WordNetLemmatizer()
	return lemmatizer.lemmatize(document)


#Can implement babblefish here for language translation

def translate_document(source_lang,target_lang,document):
	from nltk.misc import babelfish
	return babelfish.translate(document,source_lang,target_lang)

def regex_replacer_document(document):
	from replacers import RegexpReplacer
	replacer = RegexpReplacer()
	return replacer.replace(document)

def repeat_replacer_document(document):
	from replacers import RepeatReplacer
	replacer = RepeatReplacer()
	return replacer.replace(document)

def spelling_replacer(document):
	from replacers import SpellingReplacer
	replacer = SpellingReplacer()
	return replacer.replace(document)

def antonym_dealer(document):
	from replacers import AntonymReplacer
	replacer = AntonymReplacer()
	return replacer.replace_negations(document)

def filter_sent(sent):
	from transforms import filter_insignificant
	from transforms import correct_verbs
	from transforms import swap_verb_phrase
	from transforms import swap_infinitive_phrase
	from transforms import singularize_plural_noun
	from transforms import swap_noun_cardinal

	print filter_insignificant(sent)
	return singularize_plural_noun(swap_infinitive_phrase(swap_noun_cardinal(swap_verb_phrase(correct_verbs(filter_insignificant(sent))))))

document = """Iphone is expensive. Iphone has battery drain problem issue. the terrible movie. is your children learning. The book of recipes was great. Android One is good. Iphone has battery Drain problem. Andrid One has good design. Android one includes SnapDragon Processor. Android one has high RAM . The feeling of un boxing it and switching it on for the first time is something in itself! You will be surprised to find it so light compared to its screen size. Amazingly smooth and has a much better battery life. Charges faster if you use an ipad charger with it. The double tap for accessibility is great and very useful. The camera does far better than its predecessor. You will love it when you own it. smooth performance when compared to iPhone 5S
iOS 8.0 having some bugs hope it will fixed by Apple in upcoming updates 8.3
Battery backup is also good when using 3G 
Metal body is giving rich look
Same 8 megapixel rear camera with some new features like time lapse, fast motion...etc.
Screen is big.so just difficult to deal with thump on top Back button on screen.
But we double tap on Touch ID screen will coming down so it is good option to use.
Overall it's great."""

print(document)
sentences = nltk.sent_tokenize(document)
words = [nltk.word_tokenize(sent) for sent in sentences]
words = [w for w in words if not w in stopwords.words('english')]

document = regex_replacer_document(document)


for sent in nltk.sent_tokenize(document):
	#print(sent)
	sent = nltk.pos_tag(sent.split())
	#print(sent)
	sent = filter_sent(sent)
	l = len(sent)
	print(sent)
	for i in range (0,l):
		print(sent[i][0])
	#print(sent)
	print("\n")
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Sample texts for comparison
text1 = "This is the first text sample. It contains some words for analysis."
text2 = "The second text sample is different. It has different words for analysis."

# Tokenize the texts
tokens1 = word_tokenize(text1)
tokens2 = word_tokenize(text2)

# Convert tokens to lowercase and remove stopwords
stop_words = set(stopwords.words('english'))

filtered_tokens1 = [word.lower() for word in tokens1 if word.isalpha() and word.lower() not in stop_words]
filtered_tokens2 = [word.lower() for word in tokens2 if word.isalpha() and word.lower() not in stop_words]

# Calculate word frequency distributions
freq_dist1 = FreqDist(filtered_tokens1)
freq_dist2 = FreqDist(filtered_tokens2)

# Compare the word distributions
common_words = set(freq_dist1.keys()) & set(freq_dist2.keys())
unique_words1 = set(freq_dist1.keys()) - set(freq_dist2.keys())
unique_words2 = set(freq_dist2.keys()) - set(freq_dist1.keys())

print("Common words:")
print(common_words)
print("\nUnique words in Text 1:")
print(unique_words1)
print("\nUnique words in Text 2:")
print(unique_words2)

# Optionally, you can print the frequency distribution of common words
print("\nFrequency distribution of common words in Text 1:")
for word in common_words:
    print(f"{word}: {freq_dist1[word]} times")

print("\nFrequency distribution of common words in Text 2:")
for word in common_words:
    print(f"{word}: {freq_dist2[word]} times")


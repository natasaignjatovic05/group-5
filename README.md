# group-5
## Dataset Description

This project uses the labMT 1.0 dataset (Language Assessment by Mechanical Turk), developed by Dodds et al. (2011) to construct a large-scale “hedonometer” for measuring happiness in text.

The dataset contains 10,222 high-frequency English words. Each word was rated for happiness by 50 participants on Amazon Mechanical Turk using a scale from 1 (least happy) to 9 (most happy). The average score represents the perceived emotional valence of each word.

In addition to happiness ratings, the dataset includes frequency ranks of words in four different corpora:

- Twitter  
- Google Books  
- The New York Times  
- Song Lyrics  

These frequency ranks indicate how often each word appears in different types of texts.

The labMT dataset allows researchers to estimate the overall happiness of large collections of text by averaging the happiness scores of the words they contain.
## Data Preparation

### Cleaning Process

The labMT 1.0 dataset was cleaned and prepared for analysis through the following steps:

1. **Metadata removal**  
   The first rows of the file contain descriptive metadata rather than tabular data. These rows were skipped to ensure proper parsing of the dataset.

2. **Handling missing values**  
   The dataset uses "--" to indicate that a word does not appear in a specific corpus (e.g., Twitter, Google Books, NYT, or Lyrics). These entries were replaced with `NaN` to ensure consistent handling of missing values in subsequent analysis.

3. **Type conversion**  
   All numeric columns (happiness scores and frequency ranks) were converted to appropriate numeric data types. This ensures accurate statistical calculations and prevents unintended string-based operations.

4. **Data validation**  
   The dataset structure was verified after cleaning. The final cleaned dataset contains 10,222 rows and 8 columns.

5. **Reproducibility**  
   A cleaned version of the dataset was saved to the `data/clean/` directory to ensure reproducibility and consistent use across analysis scripts.

The cleaning process ensures that the dataset is structured in one way that allows reliable quantitative analysis while preserving information about specific corpus coverage.

### Missing Values

Several frequency rank columns contain missing values. 

This happens because many words do not appear in all corpora.  
For example, some words may appear in Twitter but not in song lyrics or news articles.

Keeping these missing values allows us to see differences between corpora.

### Data Dictionary

- **word**: The English word evaluated in the survey.

- **happiness_rank**: The rank of the word based on its average happiness score.

- **happiness_average**: The mean happiness rating on a 1–9 scale.

- **happiness_standard_deviation**: The standard deviation of ratings, indicating the level of agreement among participants.

- **twitter_rank**: Frequency rank of the word in the Twitter corpus.

- **google_rank**: Frequency rank of the word in the Google Books corpus.

- **nyt_rank**: Frequency rank of the word in the New York Times corpus.

- **lyrics_rank**: Frequency rank of the word in the song lyrics corpus.

### Transition to Quantitative Analysis

With the dataset cleaned and properly structured, we can now proceed to quantitative exploration. 

The preparation steps ensure that the happiness scores and frequency ranks are stored in consistent numeric formats, allowing reliable statistical analysis. 

In the following section, we examine the distribution of happiness scores and identify key patterns within the dataset.

### Interpret the histogram in words
### Is the distribution centered? skewed? clustered?
### Identify 1 pattern you did not expect.

The scatterplot shows a large cluster of words around happiness_average ≈ 5–7 with moderate disagreement (SD ≈ 1.1–1.7), meaning most words are rated somewhat positive and people mostly agree. Disagreement is highest for mid-range/neutral-ish words (~3–6) and generally lower at the extremes, where words have clearer emotional meanings. A surprising pattern is the dense “valley” of very low SD near happiness_average ≈ 5, suggesting many neutral everyday words are rated quite consistently.

### Pick 5 of the “most disagreed-about” words and discuss why they might be contested:
### – ambiguity / multiple meanings
### – cultural references
### – slang and time period
### – irony, profanity, or taboo

1) fucking / fuck / fuckin / fucked / motherfucking / motherfuckers (profanity + context + intensity)

These words are context-dependent:
	•	Some people rate them very negative because they’re rude/aggressive/offensive.
	•	Others rate them less negative (or even positive-ish) because they’re used as emphasis (“that’s fucking amazing”), joking, or in friendly slang.
That split creates huge disagreement → high standard deviation.

2) pussy (multiple meanings + taboo)

This word has very different meanings:
	•	As an insult (“coward”), it’s negative.
	•	As a sexual term, people might react with anything from positive to negative depending on comfort, gender norms, and values.
Because it’s taboo and ambiguous, ratings spread out a lot.

3) slut (taboo + cultural norms)

Strong moral/cultural judgement is involved:
	•	Some see it as a harsh insult (very negative).
	•	Others may see it as reclaimed language in some contexts, or interpret it differently based on culture/generation.
That leads to big disagreement.

4) porn (taboo + personal values)

People’s reactions differ a lot:
	•	Some associate it with shame/exploitation/addiction → negative.
	•	Others associate it with pleasure/freedom/neutral media → less negative or even positive.
So responses vary widely → high SD.

5) capitalism (cultural/political associations)

This one is interesting because it’s not “emotional” in a simple way:
	•	Some connect it to opportunity/freedom/success → positive.
	•	Others connect it to inequality/exploitation → negative.
It’s contested because it’s tied to ideology and lived experience, not a single emotion.

### Connect the qualitative interpretation to the quantitative pattern

A strong pattern in the list is that the highest-disagreement words are mostly:
	•	taboo/profanity/sex words, or
	•	culture/ideology-loaded words

Those categories usually create polarized reactions, meaning some raters give very low scores and others give higher scores. That "split” produces a large standard deviation, which is exactly what  the ranking is measuring.


### Interpret what your plot suggests about the four corpora.
The overlap heatmap shows that Google Books and the NYT share the most vocabulary in their top-5000 lists (3414 shared words), suggesting a more similar “edited/formal” register. Lyrics is the most distinct corpus, with the smallest overlaps—especially with NYT (2241)—indicating more genre-specific, emotional, and stylistic language. Twitter sits between them and overlaps relatively strongly with Lyrics (3127), consistent with both being more informal and conversational.

### Give one concrete example of a word that is “common” in one corpus but missing in another, and interpret why that might be.
Example word: lol — It’s very common on Twitter (rank 42) because it’s internet slang used for quick reactions and humor in casual conversation. It’s missing from Google Books’ top words because published books are more formal/edited and rarely use abbreviations like “lol,” so it doesn’t appear frequently enough to rank in that corpus.
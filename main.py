import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

# Read text files
text_resume = open('Resume.txt', mode='r', encoding='utf-8').read()
text_jd = open('JD.txt', mode='r', encoding='utf-8').read()

# Create a figure with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(16, 8))  # Adjust figsize for better visualization

# Create and display word cloud for resume
wc_resume = WordCloud(
    background_color='white',
    stopwords=STOPWORDS,
    height=600,
    width=400
)
wc_resume.generate(text_resume)
axes[0].imshow(wc_resume, interpolation='bilinear')
axes[0].axis("off")
axes[0].set_title('Word Cloud - Resume')  # Add title for resume word cloud

# Create and display word cloud for job description
wc_jd = WordCloud(
    background_color='white',
    stopwords=STOPWORDS,
    height=600,
    width=400
)
wc_jd.generate(text_jd)
axes[1].imshow(wc_jd, interpolation='bilinear')
axes[1].axis("off")
axes[1].set_title('Word Cloud - Job Description')  # Add title for job description word cloud

# Adjust layout (optional)
plt.tight_layout()  # Adjust spacing between plots for better readability

# Display the word clouds
plt.show()

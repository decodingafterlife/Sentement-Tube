import matplotlib.pyplot as plt
from wordcloud import WordCloud

class DataVisualizer:
    def __init__(self, df):
        """
        Initialize the DataVisualizer with a DataFrame.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing comments, replies, user names, dates, and sentiments.
        """
        self.df = df

    def plot_pie_chart(self):
        """
        Plot a pie chart for sentiment distribution.

        Output:
        - Displays a pie chart showing the distribution of sentiments.
        """
        sentiment_counts = self.df['sentiment']['label'].value_counts()
        plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title('Sentiment Distribution')
        plt.show()

    def plot_bar_chart(self):
        """
        Plot a bar chart for sentiment distribution.

        Output:
        - Displays a bar chart showing the distribution of sentiments.
        """
        sentiment_counts = self.df['sentiment']['label'].value_counts()
        sentiment_counts.plot(kind='bar', color=['green', 'red', 'yellow'])
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.title('Sentiment Distribution')
        plt.show()

    def generate_word_cloud(self):
        """
        Generate and plot a word cloud for comments.

        Output:
        - Displays a word cloud based on the comments.
        """
        all_comments = ' '.join(self.df['comment'])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud for Comments')
        plt.show()

# Example Usage:
# Create an instance of DataVisualizer
visualizer = DataVisualizer(df)

# Call the visualization functions
visualizer.plot_pie_chart()
visualizer.plot_bar_chart()
visualizer.generate_word_cloud()

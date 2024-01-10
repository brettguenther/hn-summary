# HackerNews Summarizer

Cohere and Streamlit for a simple interface to get a summary of a Hackernews thread.

![Example output](https://github.com/brettguenther/hn-summary/blob/main/example_use.png?raw=true)

# Usage

1. Get an API key from [Cohere](https://cohere.com)
2. Find a hacker news page of interest and copy the url. It should be of the form `https://news.ycombinator.com/item?id={item.id}`
3. `pip install requirements.txt`
4. Run the streamlit app and input the url and api key.

`streamlit run cohere_hacker_news_summary.py`
import cohere
import streamlit as st
from hackernews import HackerNews
from urllib.parse import urlparse
from urllib.parse import parse_qs

st.title('Hacker News Summary')

st.text_input("Hacker News Story Url", key="url")
st.text_input("Cohere API key", key="api_key")

hackernews_api = HackerNews()

if st.button('Summarize story'):
    dialogue = ''
    # extract the url param that is the item id
    # parsed_item = st.session_state.url.rsplit('/', 1)[1]
    parsed_url = urlparse(st.session_state.url)
    parsed_item_id = parse_qs(parsed_url.query)['id'][0]

    co = cohere.Client(st.session_state.api_key)

    hacker_news_item = hackernews_api.get_item(parsed_item_id)

    if hacker_news_item['type'] == 'story':
        dialogue = hacker_news_item['by'] + ": " + hacker_news_item['title']
        for kid in hacker_news_item['kids']:
            hacker_news_item = hackernews_api.get_item(str(kid))
            if hacker_news_item['type'] == 'comment':
                dialogue = dialogue + "\n{}: ".format(hacker_news_item['by']) + hackernews_api.clean_text(hacker_news_item['text'])
                if "kids" in hacker_news_item:
                    if len(hacker_news_item['kids']) >= 1:
                        for kid in hacker_news_item['kids']:
                            hacker_news_item = hackernews_api.get_item(str(kid))
                            dialogue = dialogue + "\n{}: ".format(hacker_news_item['by']) + hackernews_api.clean_text(hacker_news_item['text'])

    response = co.summarize(
        text=dialogue,
        model='command',
        length='medium',
        extractiveness='medium'
    )

    summary = response.summary

    # print(summary)

    # st.write(summary)

    st.markdown(summary, unsafe_allow_html=True)

    # st.components.v1.html("<div>" + summary + "</div>")

    # embed
    # response = co.embed(
    #   texts=['hello', 'goodbye'],
    #   model='small',
    # )
    # print(response)
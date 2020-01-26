import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('zh')

page_py = wiki_wiki.page('中国')
print(page_py.exists())

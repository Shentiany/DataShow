import jieba
import wordcloud

w = wordcloud.WordCloud(width=1000,
                       height=700,
                       background_color='white',
                       font_path='msyh.ttc',
					   scale=10)

f = open('data.txt', encoding='utf-8')
txt = f.read()
txtlist = jieba.lcut(txt)
string = "".join(txtlist)
w.generate(string)
w.to_file('wordcloud.png')

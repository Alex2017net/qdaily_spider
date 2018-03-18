#coding=utf-8

import jieba
import csv
import sys
from wordcloud import WordCloud
import string

reload(sys)
sys.setdefaultencoding('utf-8')
'''
stopwords = {}.fromkeys(['商业','给','下','一','一样','智能','娱乐','城市',
                         '设计','时尚','公司','广告',
                         '游戏','TED','中国','日本','美国','的','还','和',
                         '一个','有','吗','最','没','多','后','为',
                         '被','从','将','个','与','里','到','连','找',
                         '去','帮','得','已经','们','他们','拿','比','谈','出',
                         '很','上','看','事','让','就','更','来','卖',
                         '他','小','不','成','用','对','为了','内','怎么',
                         '会','说','年','把','想',
                         '好奇心','什么','都','人','能','但','大',
                         '现场报道','可能','也','会''和','这个','你',
                         '日报','是','要','又','它','这','-',r'“',r'”',
                         '「','」','《','》','？','、','：','做','了',
                         '在','，','!',r'｜',r'·','；','。'])

'''

#取出字符串
with open('demo2.csv') as f:
    reader=csv.reader(f)
    column = [row[1] for row in reader]
    s=str(column).decode("string_escape") #list中乱码的解决方法
    delstr=string.punctuation+' '+string.digits+'-'#对string的操作，除去一部分标点与数字
    s=s.translate(None,delstr)
    #print(s) 输出字符串


#分词
segs = jieba.cut(s, cut_all=False)
#segs = [word.encode('utf-8') for word in list(segs)]

#segs = [word for word in list(segs) if word not in stopwords]

#for seg in segs: 去掉了标点，保留了一些字母，segs是list，seg是str
    #print seg
segs = [word for word in list(segs) if len(word)>=2 ]#没有使用停用词表而是直接筛选出了两个字以上的字符串，注意这里是两个中文字符

print(len(segs))

'''
mycount = collections.Counter(segs) #用counter筛选词频
for key, val in mycount.most_common(10):  # 有序
    print(key)
    print(val)
'''

#制作词云（此处采取预先统计词频的方法，generate方法传入一个字典
reslist=list(segs)
wordDict = {}
for i in reslist:
    if i in wordDict:
        wordDict[i] = wordDict[i] + 1
    else:
        wordDict[i] = 1

wc = WordCloud(font_path='PingFang.ttc',
               width=1000,height=800,
                    background_color="white", max_words=600,
                    max_font_size=200, random_state=50)

wc.generate_from_frequencies(wordDict)

wc.to_file("%s.png"%(file))


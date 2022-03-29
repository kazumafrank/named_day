from pyexpat import model
from tkinter import E
from unicodedata import name
import numpy as np
from gensim.models.word2vec import Word2Vec
from janome.tokenizer import Tokenizer
from pprint import pprint
import random

#この下にモデルを導入する必要がある
model_path = 'word2vec.gensim.model'
model = Word2Vec.load(model_path)

#モデルのお試し
#pprint(model.wv.most_similar("日本"))

#以下で文章に対する感情分析
t = Tokenizer()
s = input()

try:
  output_data=[]
  x = np.empty((0,4), float)
  for token in t.tokenize(s):
    if token.part_of_speech.split(',')[0]=="名詞" or token.part_of_speech.split(',')[0]=="形容詞":
      #print(token.surface)
      similarity1 = model.wv.similarity(w1=token.surface, w2="嬉しい")
      #print("喜び：{0}".format(similarity1))
      similarity2 = model.wv.similarity(w1=token.surface, w2="楽しい")
      #print("悲しみ：{0}".format(similarity2))
      similarity3 = model.wv.similarity(w1=token.surface, w2="悲しい")
      #print("不安：{0}".format(similarity3))
      similarity4 = model.wv.similarity(w1=token.surface, w2="興奮")
      #print("興味：{0}".format(similarity4))
      x = np.append(x, np.array([[similarity1, similarity2, similarity3, similarity4]]), axis=0)
      break
except:
  print("データにない文字が確認されました")
  print("お手数ですが、再試行をお願いします")
  exit()

#---------------------
#[数字　数字　数字　数字]
#嬉　楽　悲　興　
#上記の表示を行う。実際の機能には直接関係ない。
print("-"*30)
print(np.mean(x, axis=0))
print("嬉：{0}".format(np.mean(x, axis=0)[0]))
print("楽：{0}".format(np.mean(x, axis=0)[1]))
print("悲：{0}".format(np.mean(x, axis=0)[2]))
print("興：{0}".format(np.mean(x, axis=0)[3]))

#以下出力に関するコード
#0~1の間で区切ってランダムに言葉を表現させる？
jo = np.mean(x, axis=0)[0] #「嬉しさ」の値
fu = np.mean(x, axis=0)[1] #「楽しさ」の値
so = np.mean(x, axis=0)[2] #「悲しみ」の値
ex = np.mean(x, axis=0)[3] #「興奮」の値

jo_word = []
fu_word = []
so_word = []
ex_word = []
day = ["な日"]

if 0 <= jo < 0.25:
  jo_word.append(random.choices(["a","b","c","d"], k=1))
if 0.25 <= jo < 0.50:
  jo_word.append(random.choices(["a","b","c","d"], k=1))
if 0.50 <= jo < 0.75:
  jo_word.append(random.choices(["a","b","c","d"], k=1))
if 0.75<= jo <= 1:
  jo_word.append(random.choices(["a","b","c","d"], k=1))

if 0 <= fu < 0.25:
  fu_word.append(random.choices(["a","b","c","d"], k=1))
if 0.25 <= fu < 0.50:
  fu_word.append(random.choices(["a","b","c","d"], k=1))
if 0.50 <= fu < 0.75:
  fu_word.append(random.choices(["a","b","c","d"], k=1))
if 0.75<= fu <= 1:
  fu_word.append(random.choices(["a","b","c","d"], k=1))

if 0 <= so < 0.25:
  so_word.append(random.choices(["a","b","c","d"], k=1))
if 0.25 <= so < 0.50:
  so_word.append(random.choices(["a","b","c","d"], k=1))
if 0.50 <= so < 0.75:
  so_word.append(random.choices(["a","b","c","d"], k=1))
if 0.75<= so <= 1:
  so_word.append(random.choices(["a","b","c","d"], k=1))

if 0 <= ex < 0.25:
  ex_word.append(random.choices(["a","b","c","d"], k=1))
if 0.25 <= ex < 0.50:
  ex_word.append(random.choices(["a","b","c","d"], k=1))
if 0.50 <= ex < 0.75:
  ex_word.append(random.choices(["a","b","c","d"], k=1))
if 0.75<= ex <= 1:
  ex_word.append(random.choices(["a","b","c","d"], k=1))

#リストの括弧と""をはずして、「～な日」を加えて表示(空白があったほうが表現の認識が簡単だろう)
name_add = jo_word + fu_word + so_word + ex_word 
name_add = np.array(name_add)
name_add = name_add.flatten()
print(*name_add, *day)
# -*- coding: utf-8 -*-
from django import forms



Q1='您被分到一个单位当领导，想提出一些解决工作中烦难问题的好方法。这时候，您第一件要做的是什么呢？'
class question_1(forms.Form):
    Question_1 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','起草一个议事日程，以便充分利用和大家在一起讨论的时间 '),
                                          ('B','给人们一定的时间相互了解 '),
                                          ('C','让每一个人说出如何解决问题的想法 '),
                                          ('D','采用一种创造性地发表意见的形式，鼓励每一个人说出此时进入他脑子里的任何想法，而不管该想法有多疯狂 '),))
Q2=' 您3岁的儿子非常胆小，实际上，从他出生起就对陌生地方和陌生人有些神经过敏或者说有些恐惧。您该怎么办呢？ '    
class question_2(forms.Form):
    Question_2 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','接受他具有害羞气质的事实，想办法让他避开他感到不安的环境 '),
                                          ('B','带他去看儿童精神科医生，寻求帮助 '),
                                          ('C','有目的地让他一下子接触许多人，带他到各种陌生的地方，克服他的恐惧心理 '),
                                          ('D','设计渐进的系列挑战性计划，每一个相对来说都是容易对付的，从而让他渐渐懂得他能够应付陌生的人和陌生的地方 '),))
    
Q3="多年以来，您一起想重学一种您在儿时学过的乐器，而现在只是为了娱乐，您又开始学了。您想最有效的利用时间。您该怎么做呢？"   
class question_3(forms.Form):
    Question_3 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','每天坚持严格的练习  '),
                                          ('B','选择能稍微扩展能力的有针对性的曲子去练习  '),
                                          ('C','只有当自己有情绪的时候才去练习 '),
                                          ('D','选择远远超出您的能力但通过勤奋的努力能掌握的乐曲去练习 '),))
    
Q4='你在准备一道做法复杂的菜时,一边正在播放收音机, 还有朋友的来电.你会: '
class question_4(forms.Form):
    Question_4 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','三件事同时进行 '),
                                          ('B','关掉收音机,但嘴巴和手都没有停'),
                                          ('C','告诉朋友,你做好菜后马上回电话给他'),
                                          ('D','无视电话，先做完手头的菜 '),))
Q5='解释一个想法或概念时,你很可能会怎么做:  '    
class question_5(forms.Form):
    Question_5 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','会利用铅笔、纸和肢体语言 '),
                                          ('B','口头解释加上肢体语言 '),
                                          ('C','口头上清楚简单的解释'),))
Q6='你听到一首新歌,是你喜欢的歌手唱的,通常你会 '
class question_6(forms.Form):
    Question_6 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','听完后,你可以毫无困难的跟着唱 '),
                                          ('B','如果是首很简单的歌,听过后你可以跟着哼唱一小段 '),
                                          ('C','很难记得歌曲的旋律,但是你可以回想起部分歌词'),
                                          ))
Q7='你忘了把钥匙时放在哪里,你会:'
class question_7(forms.Form):
    Question_7 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','先做别的事,等到自然想起为止 '),
                                          ('B','做别的事,但同时试着回想你把钥匙放在哪里 '),
                                          ('C','在心理回想刚刚做了哪些事,藉此想起放在何处'),
                                          ))
Q8='请输入您的出生年份 '
class question_8(forms.Form):
    Question_8 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"四位数字，如：1994",}))

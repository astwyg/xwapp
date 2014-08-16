# -*- coding: utf-8 -*-
from django import forms



Q1='找出不同类的一项'
class question_1(forms.Form):
    Question_1 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','铁锅'),
                                          ('B','小勺'),
                                          ('C','米饭'),
                                          ('D','碟子'),))
Q2='一本书降价50%，如果现在又按照原价出售，那么提价了多少？'    
class question_2(forms.Form):
    Question_2 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','50%'),
                                          ('B','75%'),
                                          ('C','100%'),))
    
Q3="说一个岛上有100个人，其中有5个红眼睛，95个蓝眼睛。"\
    "1. 他们不能照镜子，不能看自己眼睛的颜色。"\
    "2. 他们不能告诉别人对方的眼睛是什么颜色。"\
    "3. 一旦有人知道了自己眼睛的颜色，他就必须在当天夜里自杀。"\
    "某天，有个旅行者到了这个岛上。由于不知道这里的规矩，所以他在和全岛人一起狂欢的时候，不留神就说了一句话：【你们这里有红眼睛的人。】"\
    "问题：假设这个岛上的人足够聪明，每个人都可以做出缜密的逻辑推理。请问这个岛上将会发生什么？"
    
class question_3(forms.Form):
    Question_3 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','相安无事'),
                                          ('B','第五天夜里全部自杀'),
                                          ('C','第六天夜里全部自杀'),))
    
Q4='一笼子中关有若干鸡和兔，可以看到笼子中有20个头，60个脚，请问其中有多少只鸡？'
class question_4(forms.Form):
    Question_4 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','8只鸡'),
                                          ('B','10只鸡'),
                                          ('C','12只鸡'),))
Q5='请观察下面数组规律，填出?的值： 7，1，8，2，8，1，?，2，8，4'    
class question_5(forms.Form):
    Question_5 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','0'),
                                          ('B','6'),
                                          ('C','8'),))
Q6='如果所有甲都是乙，所有乙都是丙，那么所有甲都是丙，这句话：'
class question_6(forms.Form):
    Question_6 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','正确'),
                                          ('B','错误'),))
Q7='下列数字哪个是多余的？'
class question_7(forms.Form):
    Question_7 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','4'),
                                          ('B','5'),
                                          ('C','8'),
                                          ('d','10'),
                                          ('e','11'),
                                          ('f','16'),
                                          ('g','19'),
                                          ('h','32'),
                                          ('i','36'),))
Q8='一只熊先向南走1000米，再向东走1000米，又向北走1000米后回到了原点，请问这只熊是什么颜色的？'
class question_8(forms.Form):
    Question_8 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','黑色'),
                                          ('B','棕色'),
                                          ('C','白色'),))
Q9='连续写下1，2，3……2006，组成一个很长的数字1234567891011……20052006，该数字除以9的余数是？'
class question_9(forms.Form):
    Question_9 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','0'),
                                          ('B','3'),
                                          ('C','4'),
                                          ('D','6'),))
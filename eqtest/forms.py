# -*- coding: utf-8 -*-
from django import forms



Q1='假如你有一段刻骨铭心的旧恋情，你恋恋不忘，但是现在你已经有了新的恋人，面对手上新旧情人的照片你会'
class question_1(forms.Form):
    Question_1 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','把新感情(相片)摆放起来，将旧回忆(相片)收起来'),
                                          ('B','一起摆在床头'),
                                          ('C','两者摆在不同的地方'),
                                          ('D','统统先收起来，等婚后再说'),))
Q2='坐飞机时，突然受到很大的震动，你开始随着机身左右摇摆。这时候，您会怎样做呢？'    
class question_2(forms.Form):
    Question_2 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','继续读书或看杂志，或继续看电影，不太注意正在发生的骚乱 '),
                                          ('B','注意事态的变化，仔细听播音员的播音，并翻看紧急情况应付手册，以备万一 '),
                                          ('C','A和B都有一点 '),
                                          ('D','不能确定--根本没注意到 '),))
    
Q3="假设您是一个大学生，想在某门课程上得优秀，但是在其中考试时却只得了及格。这时候，您该怎么办呢？"   
class question_3(forms.Form):
    Question_3 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','制定一个详细的学习，并决心按计划进行 '),
                                          ('B','决心以后好好学 '),
                                          ('C','告诉自己在这门课上考不好没什么大不了的，把精力集中在其他可能考得好的课程上'),
                                          ('D','去拜访任课教授，试图让他给您高一点的分数 '),))
    
Q4='带一群4岁的孩子去公园玩，其中一个孩子由于别人都不和他玩而大哭起来。这个时候，您该怎么办呢？ '
class question_4(forms.Form):
    Question_4 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','置身事外--让孩子们自己处理'),
                                          ('B','和这个孩子交谈，并帮助她想办法 '),
                                          ('C','轻轻地告诉她不要哭'),
                                          ('D','想办法转移这个孩子的注意力，给她一些其他的东西让她玩 '),))
Q5='假设您是一个保险推销员，去访问一些有希望成为您的顾客的人。可是一连十五个人都只是对您敷衍，并不明确表态，您变得很失望。这时候，您会怎么做呢？ '    
class question_5(forms.Form):
    Question_5 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','认为这只不过是一天的遭遇而已，希望明天会有好运气 '),
                                          ('B','考虑一下自己是否适合做推销员'),
                                          ('C','在下一次拜访时再做努力，保持勤勤恳恳工作的状态 '),
                                          ('D','考虑去争取其他的顾客 '),))
Q6='您是一个经理，提倡在公司中不要搞种族歧视。一天您偶然听到有人正在开有关种族歧视的玩笑。您会怎么办呢？ '
class question_6(forms.Form):
    Question_6 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','不理它--这只是一个玩笑而已 '),
                                          ('B','把那人叫到办公室去，严厉斥责他一顿 '),
                                          ('C','当场大声告诉他，这种玩笑是不恰当的，在您这里是不能容忍的 '),
                                          ('D','建议开玩笑的人去参加一个有关反对种族歧视的培训班  '),))
Q7='您的朋友开车时别人的车突然危险地抢到你们前面，您的朋友勃然大怒，而您试图让他平静下来。您会怎么做呢？ '
class question_7(forms.Form):
    Question_7 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','告诉他忘掉它吧--现在没事了，这不是什么大不了的事 '),
                                          ('B','放一盘他喜欢听的CD，转移他的注意力 '),
                                          ('C','一起责骂那个司机，表示自己站在他那一边 '),
                                          ('D',' 告诉他您也曾有同样的经历，当时您也一样气得发疯，可是后来您看到那个司机出了车祸，被送到医院急救室'),))
Q8='您和伴侣发生了争论，两人激烈地争吵；盛怒之下，互相进行人身攻击，虽然你们并不是真的想这样做。这时候，最好怎么办呢？ '
class question_8(forms.Form):
    Question_8 = forms.ChoiceField(widget= forms.RadioSelect,
                                 choices=(('A','停止20分钟，然后继续争论 '),
                                          ('B','停止争吵……保持沉默，不管对方说什么 '),
                                          ('C','向对方说抱歉，并要求他（她）也向您道歉 '),
                                          ('D','先停一会儿，整理一下自己的想法，然后尽可能清楚地阐明自己的立场 '),))

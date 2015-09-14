# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode

import xml.etree.ElementTree as ET
import urllib,urllib2,time,hashlib

import random

TOKEN = "ast123456"

YOUDAO_KEY = 973199845
YOUDAO_KEY_FROM = "pytest"
YOUDAO_DOC_TYPE = "xml"

@csrf_exempt
def handleRequest(request):
	if request.method == 'GET':
		#response = HttpResponse(request.GET['echostr'],content_type="text/plain")
		response = HttpResponse(checkSignature(request),content_type="text/plain")
		return response
	elif request.method == 'POST':
		#c = RequestContext(request,{'result':responseMsg(request)})
		#t = Template('{{result}}')
		#response = HttpResponse(t.render(c),content_type="application/xml")
		response = HttpResponse(responseMsg(request),content_type="application/xml")
		return response
	else:
		return None

#用于微信平台的Token验证
def checkSignature(request):
	global TOKEN
	signature = request.GET.get("signature", None)
	timestamp = request.GET.get("timestamp", None)
	nonce = request.GET.get("nonce", None)
	echoStr = request.GET.get("echostr",None)

	token = TOKEN
	tmpList = [token,timestamp,nonce]
	tmpList.sort()
	tmpstr = "%s%s%s" % tuple(tmpList)
	tmpstr = hashlib.sha1(tmpstr).hexdigest()
	if tmpstr == signature:
		return echoStr
	else:
		return None

#用于处理用户的普通消息
def responseMsg(request):
	rawStr = smart_str(request.raw_post_data)
	#rawStr = smart_str(request.POST['XML'])
	msg = paraseMsgXml(ET.fromstring(rawStr))
	
	#先判断微信发来的消息类型，如果是普通文本，处理
	if msg.get('MsgType')=="text":
		queryStr = msg.get('Content','You have input nothing~')

		if queryStr == '求签':
			num = str(random.randint(1,11))
			return getQiuqianReplyXml(msg,num)
		raw_youdaoURL = "http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q=" % (YOUDAO_KEY_FROM,YOUDAO_KEY,YOUDAO_DOC_TYPE)	
		youdaoURL = "%s%s" % (raw_youdaoURL,urllib2.quote(queryStr))

		req = urllib2.Request(url=youdaoURL)
		result = urllib2.urlopen(req).read()

		replyContent = paraseYouDaoXml(ET.fromstring(result))

		return getReplyXml(msg,replyContent)
	#如果是事件，只处理订阅
	elif msg.get('MsgType')=="event":
		if msg.get('Event')=="subscribe":
			replyContent="欢迎订阅，您可以随时回复任意内容，自动进行中英文翻译！每月最多推送一次精品内容，绝不骚扰您└(^o^)┘\n"
			
			return getReplyXml(msg,replyContent)

#解析微信发来的XML
def paraseMsgXml(rootElem):
	msg = {}
	if rootElem.tag == 'xml':
		for child in rootElem:
			msg[child.tag] = smart_str(child.text)
	return msg

#解析有道返回的XML
def paraseYouDaoXml(rootElem):
	replyContent = ''
	if rootElem.tag == 'youdao-fanyi':
		for child in rootElem:
			# 错误码
			if child.tag == 'errorCode':
				if child.text == '20':
					return 'too long to translate\n'
				elif child.text == '30':
					return 'can not be able to translate with effect\n'
				elif child.text == '40':
					return 'can not be able to support this language\n'
				elif child.text == '50':
					return 'invalid key\n'

			# 查询字符串
			elif child.tag == 'query':
				replyContent = "%s%s\n" % (replyContent, child.text)

			# 有道翻译
			elif child.tag == 'translation': 
				replyContent = '%s%s\n%s\n' % (replyContent, '-' * 3 + u'通道1(有道)' + '-' * 3, child[0].text)

			# 有道词典-基本词典
			elif child.tag == 'basic': 
				replyContent = "%s%s\n" % (replyContent, '-' * 3 + u'基本词典' + '-' * 3)
				for c in child:
					if c.tag == 'phonetic':
						replyContent = '%s%s\n' % (replyContent, c.text)
					elif c.tag == 'explains':
						for ex in c.findall('ex'):
							replyContent = '%s%s\n' % (replyContent, ex.text)

			# 有道词典-网络释义
			elif child.tag == 'web': 
				replyContent = "%s%s\n" % (replyContent, '-' * 3 + u'网络释义' + '-' * 3)
				for explain in child.findall('explain'):
					for key in explain.findall('key'):
						replyContent = '%s%s\n' % (replyContent, key.text)
					for value in explain.findall('value'):
						for ex in value.findall('ex'):
							replyContent = '%s%s\n' % (replyContent, ex.text)
					replyContent = '%s%s\n' % (replyContent,'--')
	return replyContent

#设置返回微信的消息格式
def getReplyXml(msg,replyContent):
	extTpl = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>";
	extTpl = extTpl % (msg['FromUserName'],msg['ToUserName'],str(int(time.time())),'text',replyContent)
	return extTpl

def getQiuqianReplyXml(msg,replyContent):
	extTpl = '''<xml>
		<ToUserName><![CDATA[%s]]></ToUserName>
		<FromUserName><![CDATA[%s]]></FromUserName>
		<CreateTime>%s</CreateTime>
		<MsgType><![CDATA[news]]></MsgType>
		<ArticleCount>1</ArticleCount>
		<Articles>
		<item>
		<Title><![CDATA[%s]]></Title> 
		<Description><![CDATA[%s]]></Description>
		<PicUrl><![CDATA[http://mmbiz.qpic.cn/mmbiz/HC2hictGLic4SCAXfyyiarHg08k2hCy1psFoLsnicVAkmcjztyoBl7evu8XXByTadJPPOk0HIQ5c6UmqZDDRpFpTBA/640]]></PicUrl>
		<Url><![CDATA[%s]]></Url>
		</item>
		</Articles>
		</xml>'''
	extTpl = extTpl.strip('\n')
	url = random.choice(["http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202282489&idx=1&sn=5af886fc74a60d48846b2d75df7a5297#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202282805&idx=1&sn=42062de3accefe90110bd7265c79d326#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202282935&idx=1&sn=0bc25993449455fe713d0f2bdb19ef29#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202283113&idx=1&sn=7b2daebd4a71fce2ea3ad44ab14312e6#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202283262&idx=1&sn=d7646e17fd459709bd772a27356d08ad#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202283460&idx=1&sn=73f72e8f8e0fe5e03c743a181d8d1a06#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202283657&idx=1&sn=6ddeef8987f4ad36154d9971f91eeca4#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202283710&idx=1&sn=250a3ce83a6c90c760d7b40fa3731291#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202283954&idx=1&sn=5cdfd0e6bf284adc1d3a908fed2ed749#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202283994&idx=1&sn=06f8e4215c2c1553b915cfe312a0646f#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284051&idx=1&sn=417d8364d0a04124d43bdc07befcdd07#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284092&idx=1&sn=74b8bff01d2ba89649d2f6b69c6710e2#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284130&idx=1&sn=d2577bb4e20e660e93df9c9573497a7e#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284159&idx=1&sn=5d98a776015c57cb9b4cd8682fb660bc#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284185&idx=1&sn=7961bcbad2014ff6c7185bd47c243c5e#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284249&idx=1&sn=0205f27d585774a30fef27569c5941b7#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284265&idx=1&sn=1cc9532f3525ee627a6d470db50a44a5#rd", 
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202281980&idx=1&sn=655c575e9bc2202f1c387ddcfa4bcf57#rd", 
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229617260&idx=1&sn=4c3da3e194d8f88bd4363f64fc99dcbf#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229617260&idx=1&sn=4c3da3e194d8f88bd4363f64fc99dcbf#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229618108&idx=1&sn=248acf54e0c47ac76d727a1ad51665b5#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229618394&idx=1&sn=e5bf4a2351756ae4ffac0b0622c96442#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229618584&idx=1&sn=d3c31d889e325f189098a2564ab7ec8c#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229618762&idx=1&sn=caf9215ba19e3f2a78c7e7da1aee53ab#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229618918&idx=1&sn=6df9c0625717c35c355ce679a7cfe2d2#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229619161&idx=1&sn=e73911189bf8500c01e310f0681752bf#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229619376&idx=1&sn=8eee4b03ec57cc5c8e111fe94b7e908a#rd",
		"http://mp.weixin.qq.com/s?__biz=MzA5MjI3ODEyOQ==&mid=229619530&idx=1&sn=6592c043a270bc8ef8f11a3498498484#rd",
		"http://mp.weixin.qq.com/s?__biz=MjM5MjQyOTg3MA==&mid=202284223&idx=1&sn=08aa4c80c555808d0de3907daaf5a7ca#rd"])
	extTpl = extTpl % (msg['FromUserName'],msg['ToUserName'],str(int(time.time())),'求签结果','求签结果',url)
	return extTpl

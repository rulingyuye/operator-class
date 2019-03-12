#! -*- coding:utf-8 -*-
import re

def operator_class(data):
	'''
	将手机号码按照移动、联通、电信分类
	传入可迭代列表
	'''
	data_mobile = []
	data_Unicom = []
	data_telecom = []
	for line in data:
		if len(re.findall('^13[4-9].*',line)) > 0:
			data_mobile.extend(re.findall('^13[4-9].*',line))
		elif len(re.findall('^147.*',line)) > 0:
			data_mobile.extend(re.findall('^147.*',line))
		elif len(re.findall('^15[012789].*',line)) > 0:
			data_mobile.extend(re.findall('^15[012789].*',line))
		elif len(re.findall('^17[8].*',line)) > 0:
			data_mobile.extend(re.findall('^17[8].*',line))
		elif len(re.findall('^18[23478].*',line)) > 0:
			data_mobile.extend(re.findall('^18[23478].*',line))
		elif len(re.findall('^13[012].*',line)) > 0:
			data_Unicom.extend(re.findall('^13[012].*',line))
		elif len(re.findall('^145.*',line)) > 0:
			data_Unicom.extend(re.findall('^145.*',line))
		elif len(re.findall('^15[56].*',line)) > 0:
			data_Unicom.extend(re.findall('^15[56].*',line))
		elif len(re.findall('^16[6].*',line)) > 0:
			data_Unicom.extend(re.findall('^16[6].*',line))
		elif len(re.findall('^17[56].*',line)) > 0:
			data_Unicom.extend(re.findall('^17[56].*',line))
		elif len(re.findall('^18[56].*',line)) > 0:
			data_Unicom.extend(re.findall('^18[56].*',line))
		elif len(re.findall('^133.*',line)) > 0:
			data_telecom.extend(re.findall('^133.*',line))
		elif len(re.findall('^153.*',line)) > 0:
			data_telecom.extend(re.findall('^153.*',line))
		elif len(re.findall('^17[37].*',line)) > 0:
			data_telecom.extend(re.findall('^17[37].*',line))
		elif len(re.findall('^18[019].*',line)) > 0:
			data_telecom.extend(re.findall('^18[019].*',line))
		elif len(re.findall('^19[9].*',line)) > 0:
			data_telecom.extend(re.findall('^19[9].*',line))
	return data_mobile,data_Unicom,data_telecom

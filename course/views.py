from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from course.models import Users, CourseMemberships
import csv

# Create your views here.
humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
businessEconomyId = [1, 9, 10, 30, 31, 33]
lifeScienceId = [8, 11, 27]
engineeringId = [12, 25]
eeId = [2, 4, 34, 35, 36]
otherId = [37,38]
CAD = []
CADApplication = [5, 13, 14, 15, 16, 17, 18, 19]
def dashBoard(request):
	enrolledUsers = CourseMemberships.objects.all()
	number = enrolledUsers.all().count()
	enrolled_number = enrolledUsers.filter(course_membership_role='LEARNER').count()
	benrolledUsers = CourseMemberships.objects.using('sudongpo').all()
	bnumber = benrolledUsers.all().count()
	benrolled_number = benrolledUsers.filter(course_membership_role='LEARNER').count()
	return render_to_response('dashboard.html', locals())

def passrateCourse(request, id):
	myFile=open('/home/user/moocWeb/total/total_passrate_course_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			trys = row['測驗人次']
			test=row['作業份數']
			total_pass=row['通過人次']
			average_pass=row['平均通過率']
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)

	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('passrate_course.html',locals())

def ratingCourse(request, id):
	myFile=open('/home/user/moocWeb/total/total_rating_course_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			total_good=row['good總次數']
			total_bad=row['bad總次數']
			total=row['評價次數']
			average_rating = row['平均分數']
			bad_ratio=row['Bad Ratio']
	# humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
	# businessEconomyId = [1, 30, 31, 9, 33]
	# lifeScienceId = [8, 10, 11, 12, 27, 37, 38]
	# engineeringId = [2, 4, 5, 13, 14, 15, 16, 17, 18, 19, 25, 34]
	# otherId = [35, 36]
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('rating_course.html',locals())

def registerCourse(request, id):
	myFile=open('/home/user/moocWeb/total/total_register_course_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			total_register=row['總註冊人數']
			total_buy=row['總購買人數']
			total_finish=row['總完課人數']
	# humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
	# businessEconomyId = [1, 30, 31, 9, 33]
	# lifeScienceId = [8, 10, 11, 12, 27, 37, 38]
	# engineeringId = [2, 4, 5, 13, 14, 15, 16, 17, 18, 19, 25, 34]
	# otherId = [35, 36]
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('register_course.html',locals())

def studentCourse(request, id):
	myFile=open('/home/user/moocWeb/total/total_register_course_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			country = []#row['country']
			language = []#row['language']
			gender = []#row['gender']
			employment_status = []#row['employment_status']
			educational_status = []#row['educational_status']
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('student_course.html',locals())

def passrateItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_passrate_item_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	test_name=[]
	test_type=[]
	total=[]
	pas=[]
	passrate=[]
	output = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			output.append(row)
			course_name=row['課程名稱']

	# humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
	# businessEconomyId = [1, 30, 31, 9, 33]
	# lifeScienceId = [8, 10, 11, 12, 27, 37, 38]
	# engineeringId = [2, 4, 5, 13, 14, 15, 16, 17, 18, 19, 25, 34]
	# otherId = [35, 36]
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	myFile.close()
	myFile2.close()
	now_id = id

	return render_to_response('passrate_item.html',locals())

def ratingItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_rating_item_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	week=[]
	week_name=[]
	item_name=[]
	item_type=[]
	good=[]
	bad=[]
	bad_ratio = []
	output = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			output.append(row)
			course_name=row['課程名稱']
			week.append(row['周次'])
			week_name.append(row['課程名稱'])
			item_name.append(row['item名稱'])
			item_type.append(row['item類型'])
			good.append(row['good次數'])
			bad.append(row['bad次數'])
			bad_ratio.append(row['Bad_Ratio'])
	# humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
	# businessEconomyId = [1, 30, 31, 9, 33]
	# lifeScienceId = [8, 10, 11, 12, 27, 37, 38]
	# engineeringId = [2, 4, 5, 13, 14, 15, 16, 17, 18, 19, 25, 34]
	# otherId = [35, 36]
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('rating_item.html',locals())

def registerWeeklyItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_register_item_weekly_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	week=[]
	start=[]
	end=[]
	register=[]
	buy=[]
	finish=[]
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			week.append(row['週次'])
			start.append(row['該週開始日期'])
			end.append(row['該週結束日期'])
			register.append(row['註冊人數'])
			buy.append(row['購買人數'])
			finish.append(row['完課人數'])
	# humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
	# businessEconomyId = [1, 30, 31, 9, 33]
	# lifeScienceId = [8, 10, 11, 12, 27, 37, 38]
	# engineeringId = [2, 4, 5, 13, 14, 15, 16, 17, 18, 19, 25, 34]
	# otherId = [35, 36]
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('register_weekly_item.html',locals())

def registerDailyItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_register_item_daily_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	# humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
	# businessEconomyId = [1, 30, 31, 9, 33]
	# lifeScienceId = [8, 10, 11, 12, 27, 37, 38]
	# engineeringId = [2, 4, 5, 13, 14, 15, 16, 17, 18, 19, 25, 34]
	# otherId = [35, 36]
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	day=[]
	date=[]
	register=[]
	buy=[]
	finish=[]
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			day.append(row['天數'])
			date.append(row['日期'])
			register.append(row['註冊人數'])
			buy.append(row['購買人數'])
			finish.append(row['完課人數'])
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('register_daily_item.html',locals())

def download (request, id):
	myFile=open('/home/user/moocWeb/total/total_register_item_daily_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	now_id = id
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
	courseList6 = []
	specializationList1 = []
	specializationList2 = []
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in eeId:
			courseList5.append(row)
		if int(row['id']) in otherId:
			courseList6.append(row)
		if int(row['id']) in CAD:
			specializationList1.append(row)
		if int(row['id']) in CADApplication:
			specializationList2.append(row)
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
	
	myFile.close()
	myFile2.close()
	return render_to_response('download.html', locals())

def download1 (request, id):
	myFile=open('/home/user/moocWeb/total/total_register_item_daily_level.csv','r')
	response = HttpResponse(myFile, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	return response
	# for row in csv.DictReader(myFile):
	# 	if(row['id'] == id):
	# 		try:
	# 			# fname = str(request.user.student_set.first().team.interest) + "_" + str(request.user.student_set.first().team.id)
	# 			fname = 'total'
	# 			file_dir = os.path.join('/home/user/moocWeb/' , fname)
	# 			file_path = os.path.join( file_dir , 'total_register_item_daily_level.csv')
	# 			# f=open(file_path,'rb')
	# 			data=f.read()   #開始讀寫檔案至data變數裡面
	# 			f.close()
	# 			# destination =open(file_path,'rb')
	# 			# for chunk in file.chunks():
	# 			# 	data = data + destination.read(chunk)
	# 			# destination.close()
	# 			# content_type有很多種，有強制下載轉乘PDF的、有ZIP的，我就用force-download
	# 			response = HttpResponse(data , content_type='text/csv')
	# 			#要import urllib
	# 			#檔案原本名稱.encode("utf-8") 記得要換回檔案原本的名稱，轉成utf-8格式以免亂碼
	# 			#不是存在service端的檔案名稱唷！
	# 			response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	# 			return response
	# 		except:
	# 			return HttpResponse('error to download file')
def download2 (request, id):
	myFile=open('/home/user/moocWeb/total/total_register_item_weekly_level.csv','r')
	response = HttpResponse(myFile, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	return response

def download3 (request, id):
	myFile=open('/home/user/moocWeb/total/total_register_course_level.csv','r')
	# path = '/home/user/moocWeb/'
	# for row in csv.DictReader(myFile):
	# 	if(row['id'] == id):
	# 		courseName = row['英文名稱']
	# downloadFile = os.path.join('/home/user/moocWeb/' , fname)
	response = HttpResponse(myFile, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	return response

def download4 (request, id):
	myFile=open('/home/user/moocWeb/total/total_passrate_item_level.csv','r')
	response = HttpResponse(myFile, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	return response

def download5 (request, id):
	myFile=open('/home/user/moocWeb/total/total_passrate_course_level.csv','r')
	response = HttpResponse(myFile, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	return response

def download6 (request, id):
	myFile=open('/home/user/moocWeb/total/total_rating_course_level.csv','r')
	response = HttpResponse(myFile, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	return response

def download7 (request, id):
	myFile=open('/home/user/moocWeb/total/total_rating_item_level.csv','r')
	response = HttpResponse(myFile, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=brief.csv'# % urllib.quote( '1'.encode("utf-8") )
	return response
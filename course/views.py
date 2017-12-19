from django.shortcuts import render_to_response
from course.models import Users, CourseMemberships
import csv

# Create your views here.
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
	courseList = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			trys = row['測驗人次']
			test=row['作業份數']
			total_pass=row['通過人次']
			average_pass=row['平均通過率']
	for row in csv.DictReader(myFile2):
		courseList.append(row['課程名稱'])
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('passrate_course.html',locals())

def ratingCourse(request, id):
	myFile=open('/home/user/moocWeb/total/total_rating_course_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	courseList = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			total_good=row['good總次數']
			total_bad=row['bad總次數']
			total=row['評價次數']
			average_rating = row['平均分數']
	for row in csv.DictReader(myFile2):
		courseList.append(row['課程名稱'])
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('rating_course.html',locals())

def registerCourse(request, id):
	myFile=open('/home/user/moocWeb/total/total_register_course_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	courseList = []
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			total_register=row['總註冊人數']
			total_buy=row['總購買人數']
			total_finish=row['總完課人數']
	for row in csv.DictReader(myFile2):
		courseList.append(row['課程名稱'])
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('register_course.html',locals())

def passrateItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_passrate_item_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	courseList = []
	test_name=[]
	test_type=[]
	total=[]
	pas=[]
	passrate=[]
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			test_name.append(row['作業名稱'])
			test_type.append(row['作業類型'])
			total.append(row['繳交人數'])
			pas.append(row['通過人數'])
			passrate.append(row['通過率'])
	for row in csv.DictReader(myFile2):
		courseList.append(row['課程名稱'])
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('passrate_item.html',locals())

def ratingItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_rating_item_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	course_id = []
	courseList = []
	week=[]
	week_name=[]
	item_name=[]
	item_type=[]
	good=[]
	bad=[]
	for row in csv.DictReader(myFile):
		if(row['id'] == id):
			course_name=row['課程名稱']
			week.append(row['周次'])
			week_name.append(row['課程名稱'])
			item_name.append(row['item名稱'])
			item_type.append(row['item類型'])
			good.append(row['good次數'])
			bad.append(row['bad次數'])
	for row in csv.DictReader(myFile2):
		courseList.append(row['課程名稱'])
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('rating_item.html',locals())

def registerWeeklyItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_register_item_weekly_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	courseList = []
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
	for row in csv.DictReader(myFile2):
		courseList.append(row['課程名稱'])
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('register_weekly_item.html',locals())

def registerDailyItem(request, id):
	myFile=open('/home/user/moocWeb/total/total_register_item_daily_level.csv','r')
	myFile2=open('/home/user/moocWeb/total/course.csv','r')
	humanityHistoryId = [3, 6, 7, 20, 21,22, 23, 24, 26, 28, 29, 32]
	businessEconomyId = [1, 30, 31, 9, 33]
	lifeScienceId = [8, 10, 11, 12, 27, 37, 38]
	engineeringId = [2, 4, 5, 13, 14, 15, 16, 17, 18, 19, 25, 34]
	otherId = [35, 36]
	courseId1 = []
	courseList1 = []
	courseList2 = []
	courseList3 = []
	courseList4 = []
	courseList5 = []
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
	for row in csv.DictReader(myFile2):
		if int(row['id']) in humanityHistoryId:
			courseList1.append(row)
		if int(row['id']) in businessEconomyId:
			courseList2.append(row)
		if int(row['id']) in lifeScienceId:
			courseList3.append(row)
		if int(row['id']) in engineeringId:
			courseList4.append(row)
		if int(row['id']) in otherId:
			courseList5.append(row)
	myFile.close()
	myFile2.close()
	now_id = id
	return render_to_response('register_daily_item.html',locals())
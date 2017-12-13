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
			test=row['測驗次數']
			total_pass=row['通過次數']
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
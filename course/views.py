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

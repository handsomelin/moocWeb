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
	myFile=open('/home/moocWeb/produced_csv/total/total_passrate_course_level.csv','r')
	# myFile2=open('/home/moocWeb/produced_csv/courseList.csv','r')
	# courseList = ['2d-cad', '3d-cad', 'cad', 'cad-bim-shiwu', 'cad3d', 'gabr', 'ji-chu-guang-xue', 'mechanics-of-materials-1', 'ntumlone-mathematicalfoundations', 'qin-shi-huang', 'rengong-zhineng', 'shaonian-fuli', 'shiji', 'shiyan-jingji-xue', 'tang-poems', 'wuli']
	for row in csv.DictReader(myFile):
        course_name=row['課程名稱'][id]
        test=row['測驗次數'][id]
        total_pass=row['通過次數'][id]
        average_pass=row['平均通過率'][id]
    return render_to_response('passrate_course.html',locals())

def passrateItem(request):
	myFile=open('/home/moocWeb/produced_csv/total/total_passrate_course_level.csv','r')
	courseList = ['2d-cad', '3d-cad', 'cad', 'cad-bim-shiwu', 'cad3d', 'gabr', 'ji-chu-guang-xue', 'mechanics-of-materials-1', 'ntumlone-mathematicalfoundations', 'qin-shi-huang', 'rengong-zhineng', 'shaonian-fuli', 'shiji', 'shiyan-jingji-xue', 'tang-poems', 'wuli']
	for row in csv.DictReader(myFile):
        course_name=row['課程名稱']
        test=row['測驗次數']
        total_pass=row['通過次數']
        average_pass=row['平均通過率']
    return render_to_response('passrate_course.html',locals())
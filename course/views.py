from django.shortcuts import render_to_response
from course.models import Users, CourseMemberships

# Create your views here.
def dashBoard(request):
	enrolledUsers = CourseMemberships.objects.all()
	number = enrolledUsers.all().count()
	enrolled_number = enrolledUsers.filter(course_membership_role='LEARNER').count()
	benrolledUsers = CourseMemberships.objects.using('sudongpo').all()
	bnumber = benrolledUsers.all().count()
	benrolled_number = benrolledUsers.filter(course_membership_role='LEARNER').count()
	return render_to_response('dashboard.html', locals())

def passrateCourse(request):
	test = 
	total =

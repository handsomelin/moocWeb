# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AssessmentActions(models.Model):
    assessment_action_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_action_base_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_scope_id = models.CharField(max_length=300, blank=True, null=True)
    assessment_scope_type_id = models.IntegerField(blank=True, null=True)
    assessment_action_version = models.IntegerField(blank=True, null=True)
    assessment_action_ts = models.DateTimeField(blank=True, null=True)
    assessment_action_start_ts = models.DateTimeField(blank=True, null=True)
    guest_user_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_assessments_user_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'assessment_actions'


class AssessmentAssessmentsQuestions(models.Model):
    assessment_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_internal_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_cuepoint = models.IntegerField(blank=True, null=True)
    assessment_question_order = models.IntegerField(blank=True, null=True)
    assessment_question_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_assessments_questions'


class AssessmentCheckboxQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_shuffle_options = models.NullBooleanField()
    assessment_question_allow_partial_scoring = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_checkbox_questions'


class AssessmentCheckboxReflectQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_shuffle_options = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_checkbox_reflect_questions'


class AssessmentMathExpressionPatterns(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_display = models.CharField(max_length=20000, blank=True, null=True)
    assessment_pattern_feedback = models.CharField(max_length=20000, blank=True, null=True)
    assessment_pattern_correct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_math_expression_patterns'


class AssessmentMathExpressionQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    default_incorrect_feedback = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_math_expression_questions'


class AssessmentMcqQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_shuffle_options = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_mcq_questions'


class AssessmentMcqReflectQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_shuffle_options = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_mcq_reflect_questions'


class AssessmentOptions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_option_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_option_display = models.CharField(max_length=20000, blank=True, null=True)
    assessment_option_feedback = models.CharField(max_length=20000, blank=True, null=True)
    assessment_option_correct = models.NullBooleanField()
    assessment_option_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_options'


class AssessmentPatternFlagTypes(models.Model):
    assessment_pattern_flag_type_id = models.IntegerField(blank=True, null=True)
    assessment_pattern_flag_type_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_pattern_flag_types'


class AssessmentPatternTypes(models.Model):
    assessment_pattern_type_id = models.IntegerField(blank=True, null=True)
    assessment_pattern_type_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_pattern_types'


class AssessmentQuestionTypes(models.Model):
    assessment_question_type_id = models.IntegerField(blank=True, null=True)
    assessment_question_type_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_question_types'


class AssessmentQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_base_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_version = models.IntegerField(blank=True, null=True)
    assessment_question_type_id = models.IntegerField(blank=True, null=True)
    assessment_question_prompt = models.CharField(max_length=20000, blank=True, null=True)
    assessment_question_update_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_questions'


class AssessmentReflectQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_question_feedback = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_reflect_questions'


class AssessmentRegexPatternFlags(models.Model):
    assessment_pattern_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_flag_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_regex_pattern_flags'


class AssessmentRegexPatterns(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_regex = models.CharField(max_length=20000, blank=True, null=True)
    assessment_pattern_feedback = models.CharField(max_length=20000, blank=True, null=True)
    assessment_pattern_correct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_regex_patterns'


class AssessmentRegexQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    default_incorrect_feedback = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_regex_questions'


class AssessmentResponseOptions(models.Model):
    assessment_response_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_option_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_response_correct = models.NullBooleanField()
    assessment_response_feedback = models.CharField(max_length=20000, blank=True, null=True)
    assessment_response_selected = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_response_options'


class AssessmentResponsePatterns(models.Model):
    assessment_response_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_response_answer = models.CharField(max_length=10000, blank=True, null=True)
    assessment_response_correct = models.NullBooleanField()
    assessment_response_feedback = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_response_patterns'


class AssessmentResponses(models.Model):
    assessment_response_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_action_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_action_version = models.IntegerField(blank=True, null=True)
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_response_score = models.FloatField(blank=True, null=True)
    assessment_response_weighted_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_responses'


class AssessmentScopeTypes(models.Model):
    assessment_scope_type_id = models.IntegerField(blank=True, null=True)
    assessment_scope_type_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_scope_types'


class AssessmentSingleNumericPatterns(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_type_id = models.IntegerField(blank=True, null=True)
    assessment_pattern_value = models.FloatField(blank=True, null=True)
    assessment_pattern_max = models.FloatField(blank=True, null=True)
    assessment_pattern_min = models.FloatField(blank=True, null=True)
    assessment_pattern_include_min = models.NullBooleanField()
    assessment_pattern_include_max = models.NullBooleanField()
    assessment_pattern_feedback = models.CharField(max_length=20000, blank=True, null=True)
    assessment_pattern_correct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_single_numeric_patterns'


class AssessmentSingleNumericQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    default_incorrect_feedback = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_single_numeric_questions'


class AssessmentTextExactMatchPatterns(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_pattern_display = models.CharField(max_length=20000, blank=True, null=True)
    assessment_pattern_feedback = models.CharField(max_length=20000, blank=True, null=True)
    assessment_pattern_correct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assessment_text_exact_match_patterns'


class AssessmentTextExactMatchQuestions(models.Model):
    assessment_question_id = models.CharField(max_length=50, blank=True, null=True)
    default_incorrect_feedback = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_text_exact_match_questions'


class AssessmentTypes(models.Model):
    assessment_type_id = models.IntegerField(blank=True, null=True)
    assessment_type_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_types'


class Assessments(models.Model):
    assessment_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_base_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_version = models.IntegerField(blank=True, null=True)
    assessment_type_id = models.IntegerField(blank=True, null=True)
    assessment_update_ts = models.DateTimeField(blank=True, null=True)
    assessment_passing_fraction = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessments'


class CourseBranchGrades(models.Model):
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_user_id = models.CharField(max_length=50)
    course_branch_grade_ts = models.DateTimeField(blank=True, null=True)
    course_passing_state_id = models.IntegerField(blank=True, null=True)
    course_branch_grade_overall_passed_items = models.IntegerField(blank=True, null=True)
    course_branch_grade_overall = models.FloatField(blank=True, null=True)
    course_branch_grade_verified_passed_items = models.IntegerField(blank=True, null=True)
    course_branch_grade_verified = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_branch_grades'


class CourseBranchItemAssessments(models.Model):
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_branch_item_assessments'


class CourseBranchItemPeerAssignments(models.Model):
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_branch_item_peer_assignments'


class CourseBranchItemProgrammingAssignments(models.Model):
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_branch_item_programming_assignments'


class CourseBranchItems(models.Model):
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    course_lesson_id = models.CharField(max_length=50, blank=True, null=True)
    course_branch_item_order = models.IntegerField(blank=True, null=True)
    course_item_type_id = models.IntegerField(blank=True, null=True)
    course_branch_item_name = models.CharField(max_length=10000, blank=True, null=True)
    course_branch_item_optional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'course_branch_items'


class CourseBranchLessons(models.Model):
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    course_lesson_id = models.CharField(max_length=50, blank=True, null=True)
    course_module_id = models.CharField(max_length=50, blank=True, null=True)
    course_branch_lesson_order = models.IntegerField(blank=True, null=True)
    course_branch_lesson_name = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_branch_lessons'


class CourseBranchModules(models.Model):
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    course_module_id = models.CharField(max_length=50, blank=True, null=True)
    course_branch_module_order = models.IntegerField(blank=True, null=True)
    course_branch_module_name = models.CharField(max_length=2000, blank=True, null=True)
    course_branch_module_desc = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_branch_modules'


class CourseBranches(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    course_branch_changes_description = models.CharField(max_length=65535, blank=True, null=True)
    authoring_course_branch_name = models.CharField(max_length=255, blank=True, null=True)
    authoring_course_branch_created_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_branches'


class CourseFormativeQuizGrades(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_user_id = models.CharField(max_length=50)
    course_quiz_grade_ts = models.DateTimeField(blank=True, null=True)
    course_quiz_grade = models.FloatField(blank=True, null=True)
    course_quiz_max_grade = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_formative_quiz_grades'


class CourseGrades(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_user_id = models.CharField(max_length=50)
    course_grade_ts = models.DateTimeField(blank=True, null=True)
    course_passing_state_id = models.IntegerField(blank=True, null=True)
    course_grade_overall_passed_items = models.IntegerField(blank=True, null=True)
    course_grade_overall = models.FloatField(blank=True, null=True)
    course_grade_verified_passed_items = models.IntegerField(blank=True, null=True)
    course_grade_verified = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_grades'


class CourseItemAssessments(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    assessment_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_item_assessments'


class CourseItemGrades(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_user_id = models.CharField(max_length=50)
    course_item_grade_ts = models.DateTimeField(blank=True, null=True)
    course_item_passing_state_id = models.IntegerField(blank=True, null=True)
    course_item_grade_overall = models.FloatField(blank=True, null=True)
    course_item_grade_verified = models.FloatField(blank=True, null=True)
    course_item_grade_pending = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_item_grades'


class CourseItemPassingStates(models.Model):
    course_item_passing_state_id = models.IntegerField(blank=True, null=True)
    course_item_passing_state_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_item_passing_states'


class CourseItemPeerAssignments(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_item_peer_assignments'


class CourseItemProgrammingAssignments(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_item_programming_assignments'


class CourseItemTypes(models.Model):
    course_item_type_id = models.IntegerField(blank=True, null=True)
    course_item_type_desc = models.CharField(max_length=255, blank=True, null=True)
    course_item_type_category = models.CharField(max_length=255, blank=True, null=True)
    course_item_type_graded = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'course_item_types'


class CourseItems(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    course_lesson_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_order = models.IntegerField(blank=True, null=True)
    course_item_type_id = models.IntegerField(blank=True, null=True)
    course_item_name = models.CharField(max_length=10000, blank=True, null=True)
    course_item_optional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'course_items'


class CourseLessons(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_lesson_id = models.CharField(max_length=50, blank=True, null=True)
    course_module_id = models.CharField(max_length=50, blank=True, null=True)
    course_lesson_order = models.IntegerField(blank=True, null=True)
    course_lesson_name = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_lessons'


class CourseMemberships(models.Model):
    taiwan_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_membership_role = models.CharField(max_length=50, blank=True, null=True)
    course_membership_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_memberships'


class CourseModules(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_module_id = models.CharField(max_length=50, blank=True, null=True)
    course_module_order = models.IntegerField(blank=True, null=True)
    course_module_name = models.CharField(max_length=2000, blank=True, null=True)
    course_module_desc = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_modules'


class CoursePassingStates(models.Model):
    course_passing_state_id = models.IntegerField(blank=True, null=True)
    course_passing_state_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_passing_states'


class CourseProgress(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_user_id = models.CharField(max_length=50)
    course_progress_state_type_id = models.IntegerField(blank=True, null=True)
    course_progress_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_progress'


class CourseProgressStateTypes(models.Model):
    course_progress_state_type_id = models.IntegerField(blank=True, null=True)
    course_progress_state_type_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_progress_state_types'


class Courses(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_slug = models.CharField(max_length=2000, blank=True, null=True)
    course_name = models.CharField(max_length=2000, blank=True, null=True)
    course_launch_ts = models.DateTimeField(blank=True, null=True)
    course_update_ts = models.DateTimeField(blank=True, null=True)
    course_deleted = models.NullBooleanField()
    course_graded = models.NullBooleanField()
    course_desc = models.CharField(max_length=10000, blank=True, null=True)
    course_restricted = models.NullBooleanField()
    course_verification_enabled_at_ts = models.DateTimeField(blank=True, null=True)
    primary_translation_equivalent_course_id = models.CharField(max_length=50, blank=True, null=True)
    course_preenrollment_ts = models.DateTimeField(blank=True, null=True)
    course_workload = models.CharField(max_length=100, blank=True, null=True)
    course_session_enabled_ts = models.DateTimeField(blank=True, null=True)
    course_promo_photo_s3_bucket = models.CharField(max_length=255, blank=True, null=True)
    course_promo_photo_s3_key = models.CharField(max_length=10000, blank=True, null=True)
    course_level = models.CharField(max_length=50, blank=True, null=True)
    course_planned_launch_date_text = models.CharField(max_length=255, blank=True, null=True)
    course_header_image_s3_bucket = models.CharField(max_length=255, blank=True, null=True)
    course_header_image_s3_key = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'


class DemographicsAnswers(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    taiwan_demographics_user_id = models.CharField(max_length=50)
    submission_ts = models.DateTimeField(blank=True, null=True)
    choice_id = models.IntegerField(blank=True, null=True)
    answer_int = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demographics_answers'


class DemographicsChoices(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    choice_id = models.IntegerField(blank=True, null=True)
    choice_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demographics_choices'


class DemographicsQuestionTypes(models.Model):
    question_type_id = models.IntegerField(blank=True, null=True)
    question_type_desc = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demographics_question_types'


class DemographicsQuestions(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    question_type_id = models.IntegerField(blank=True, null=True)
    question_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demographics_questions'


class DiscussionAnswerFlags(models.Model):
    taiwan_discussions_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_answer_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_answer_flag_active = models.NullBooleanField()
    discussion_answer_flag_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_answer_flags'


class DiscussionAnswerVotes(models.Model):
    taiwan_discussions_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_answer_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_answer_vote_value = models.IntegerField(blank=True, null=True)
    discussion_answer_vote_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_answer_votes'


class DiscussionAnswers(models.Model):
    discussion_answer_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_discussions_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_answer_content = models.CharField(max_length=20000, blank=True, null=True)
    discussion_question_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_answer_parent_discussion_answer_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_answer_created_ts = models.DateTimeField(blank=True, null=True)
    discussion_answer_updated_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_answers'


class DiscussionCourseForums(models.Model):
    discussion_forum_id = models.CharField(max_length=50, blank=True, null=True)
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_course_forum_title = models.CharField(max_length=20000, blank=True, null=True)
    discussion_course_forum_description = models.CharField(max_length=20000, blank=True, null=True)
    discussion_course_forum_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_course_forums'


class DiscussionQuestionFlags(models.Model):
    taiwan_discussions_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_question_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_question_flag_active = models.NullBooleanField()
    discussion_question_flag_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_question_flags'


class DiscussionQuestionFollowings(models.Model):
    taiwan_discussions_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_question_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_question_following_active = models.NullBooleanField()
    discussion_question_following_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_question_followings'


class DiscussionQuestionVotes(models.Model):
    taiwan_discussions_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_question_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_question_vote_value = models.IntegerField(blank=True, null=True)
    discussion_question_vote_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_question_votes'


class DiscussionQuestions(models.Model):
    discussion_question_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_discussions_user_id = models.CharField(max_length=50)
    discussion_question_title = models.CharField(max_length=20000, blank=True, null=True)
    discussion_question_details = models.CharField(max_length=20000, blank=True, null=True)
    discussion_question_context_type = models.CharField(max_length=50, blank=True, null=True)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_module_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_forum_id = models.CharField(max_length=50, blank=True, null=True)
    country_cd = models.CharField(max_length=2, blank=True, null=True)
    group_id = models.CharField(max_length=50, blank=True, null=True)
    discussion_question_created_ts = models.DateTimeField(blank=True, null=True)
    discussion_question_updated_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_questions'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EcbEngines(models.Model):
    ecb_engine_id = models.CharField(max_length=267, blank=True, null=True)
    ecb_engine_name = models.CharField(max_length=1024, blank=True, null=True)
    ecb_engine_updated_ts = models.DateTimeField(blank=True, null=True)
    ecb_engine_memory_limit_mb = models.IntegerField(blank=True, null=True)
    ecb_engine_timeout_ms = models.BigIntegerField(blank=True, null=True)
    ecb_engine_disk_limit_mb = models.IntegerField(blank=True, null=True)
    ecb_engine_cpu_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecb_engines'


class EcbEvaluationRequests(models.Model):
    course_id = models.CharField(max_length=255, blank=True, null=True)
    course_item_id = models.CharField(max_length=255, blank=True, null=True)
    taiwan_ecb_user_id = models.CharField(max_length=50)
    ecb_evaluator_id = models.CharField(max_length=267, blank=True, null=True)
    ecb_evaluation_requested_ts = models.DateTimeField(blank=True, null=True)
    ecb_evaluation_duration_ms = models.BigIntegerField(blank=True, null=True)
    ecb_evaluation_expression = models.CharField(max_length=65535, blank=True, null=True)
    ecb_evaluation_result = models.CharField(max_length=65535, blank=True, null=True)
    ecb_evaluation_errors = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecb_evaluation_requests'


class EcbEvaluators(models.Model):
    course_id = models.CharField(max_length=255, blank=True, null=True)
    course_item_id = models.CharField(max_length=255, blank=True, null=True)
    ecb_evaluator_id = models.CharField(max_length=267, blank=True, null=True)
    ecb_engine_id = models.CharField(max_length=255, blank=True, null=True)
    ecb_evaluator_harness = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecb_evaluators'


class FeedbackCourseComments(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    feedback_system = models.CharField(max_length=100, blank=True, null=True)
    taiwan_feedback_user_id = models.CharField(max_length=50)
    feedback_category = models.CharField(max_length=50, blank=True, null=True)
    feedback_text = models.CharField(max_length=20000, blank=True, null=True)
    feedback_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_course_comments'


class FeedbackCourseRatings(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_feedback_user_id = models.CharField(max_length=50)
    feedback_system = models.CharField(max_length=100, blank=True, null=True)
    feedback_rating = models.IntegerField(blank=True, null=True)
    feedback_max_rating = models.IntegerField(blank=True, null=True)
    feedback_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_course_ratings'


class FeedbackItemComments(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    feedback_unit_id = models.CharField(max_length=50, blank=True, null=True)
    feedback_unit_type = models.CharField(max_length=50, blank=True, null=True)
    feedback_system = models.CharField(max_length=100, blank=True, null=True)
    detailed_context = models.CharField(max_length=200, blank=True, null=True)
    taiwan_feedback_user_id = models.CharField(max_length=50)
    feedback_category = models.CharField(max_length=50, blank=True, null=True)
    feedback_text = models.CharField(max_length=20000, blank=True, null=True)
    feedback_ts = models.DateTimeField(blank=True, null=True)
    feedback_active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'feedback_item_comments'


class FeedbackItemRatings(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    course_item_id = models.CharField(max_length=50, blank=True, null=True)
    feedback_unit_id = models.CharField(max_length=50, blank=True, null=True)
    feedback_unit_type = models.CharField(max_length=50, blank=True, null=True)
    feedback_system = models.CharField(max_length=100, blank=True, null=True)
    taiwan_feedback_user_id = models.CharField(max_length=50)
    feedback_rating = models.IntegerField(blank=True, null=True)
    feedback_max_rating = models.IntegerField(blank=True, null=True)
    detailed_context = models.CharField(max_length=200, blank=True, null=True)
    feedback_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_item_ratings'


class OnDemandSessionMemberships(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    on_demand_session_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_user_id = models.CharField(max_length=50)
    on_demand_sessions_membership_start_ts = models.DateTimeField(blank=True, null=True)
    on_demand_sessions_membership_end_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'on_demand_session_memberships'


class OnDemandSessions(models.Model):
    course_id = models.CharField(max_length=50, blank=True, null=True)
    on_demand_session_id = models.CharField(max_length=50, blank=True, null=True)
    on_demand_sessions_start_ts = models.DateTimeField(blank=True, null=True)
    on_demand_sessions_end_ts = models.DateTimeField(blank=True, null=True)
    on_demand_sessions_enrollment_end_ts = models.DateTimeField(blank=True, null=True)
    course_branch_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'on_demand_sessions'


class PeerAssignmentReviewSchemaPartOptions(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_review_schema_part_id = models.CharField(max_length=255, blank=True, null=True)
    peer_assignment_review_schema_part_option_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_review_schema_part_option_text = models.CharField(max_length=65535, blank=True, null=True)
    peer_assignment_review_schema_part_option_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_assignment_review_schema_part_options'


class PeerAssignmentReviewSchemaParts(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_review_schema_part_id = models.CharField(max_length=255, blank=True, null=True)
    peer_assignment_review_schema_part_type = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_review_schema_part_order = models.IntegerField(blank=True, null=True)
    peer_assignment_review_schema_part_prompt = models.CharField(max_length=65535, blank=True, null=True)
    peer_assignment_review_schema_part_maximum_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_assignment_review_schema_parts'


class PeerAssignmentSubmissionSchemaParts(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_submission_schema_part_id = models.CharField(max_length=255, blank=True, null=True)
    peer_assignment_submission_schema_part_type = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_submission_schema_part_order = models.IntegerField(blank=True, null=True)
    peer_assignment_submission_schema_part_prompt = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_assignment_submission_schema_parts'


class PeerAssignments(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_base_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_type = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_required_review_count = models.IntegerField(blank=True, null=True)
    peer_assignment_passing_fraction = models.FloatField(blank=True, null=True)
    peer_assignment_required_reviewer_count_for_score = models.IntegerField(blank=True, null=True)
    peer_assignment_required_wait_for_score_ms = models.BigIntegerField(blank=True, null=True)
    peer_assignment_maximum_score = models.FloatField(blank=True, null=True)
    peer_assignment_update_ts = models.DateTimeField(blank=True, null=True)
    peer_assignment_is_mentor_graded = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'peer_assignments'


class PeerComments(models.Model):
    peer_comment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_peer_assignments_user_id = models.CharField(max_length=50)
    peer_comment_created_ts = models.DateTimeField(blank=True, null=True)
    peer_comment_text = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_comments'


class PeerReviewPartChoices(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_review_schema_part_id = models.CharField(max_length=255, blank=True, null=True)
    peer_assignment_review_schema_part_option_id = models.CharField(max_length=50, blank=True, null=True)
    peer_review_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_review_part_choices'


class PeerReviewPartFreeResponses(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_review_schema_part_id = models.CharField(max_length=255, blank=True, null=True)
    peer_review_id = models.CharField(max_length=50, blank=True, null=True)
    peer_review_part_free_response_text = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_review_part_free_responses'


class PeerReviews(models.Model):
    peer_review_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_peer_assignments_user_id = models.CharField(max_length=50)
    peer_review_created_ts = models.DateTimeField(blank=True, null=True)
    peer_review_first_visible_to_submitter_ts = models.DateTimeField(blank=True, null=True)
    peer_review_marked_helpful_ts = models.DateTimeField(blank=True, null=True)
    peer_review_rated_ts = models.DateTimeField(blank=True, null=True)
    peer_review_rating = models.IntegerField(blank=True, null=True)
    peer_review_is_mentor_review = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'peer_reviews'


class PeerSkips(models.Model):
    peer_skip_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_peer_assignments_user_id = models.CharField(max_length=50)
    peer_skip_created_ts = models.DateTimeField(blank=True, null=True)
    peer_skip_type = models.CharField(max_length=50, blank=True, null=True)
    peer_skip_text = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_skips'


class PeerSubmissionPartFreeResponses(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_part_free_response_text = models.CharField(max_length=32767, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_submission_part_free_responses'


class PeerSubmissionPartScores(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_review_schema_part_id = models.CharField(max_length=255, blank=True, null=True)
    peer_submission_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_part_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_submission_part_scores'


class PeerSubmissionPartUrls(models.Model):
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_id = models.CharField(max_length=50, blank=True, null=True)
    peer_submission_part_url_url = models.CharField(max_length=65535, blank=True, null=True)
    peer_submission_part_url_title = models.CharField(max_length=65535, blank=True, null=True)
    peer_submission_part_url_description = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peer_submission_part_urls'


class PeerSubmissions(models.Model):
    peer_submission_id = models.CharField(max_length=50, blank=True, null=True)
    peer_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_peer_assignments_user_id = models.CharField(max_length=50)
    peer_submission_created_ts = models.DateTimeField(blank=True, null=True)
    peer_submission_is_draft = models.NullBooleanField()
    peer_submission_title = models.CharField(max_length=65535, blank=True, null=True)
    peer_submission_removed_from_public_ts = models.DateTimeField(blank=True, null=True)
    peer_submission_score_available_ts = models.DateTimeField(blank=True, null=True)
    peer_submission_score = models.FloatField(blank=True, null=True)
    peer_submission_is_mentor_graded = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'peer_submissions'


class ProgrammingAssignmentSubmissionSchemaPartGridSchemas(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_grid_gyd0w6 = models.CharField(max_length=65535, blank=True, null=True)
    programming_assignment_submission_schema_part_grid_lb2xog = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_grid_49aqrn = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_assignment_submission_schema_part_grid_schemas'


class ProgrammingAssignmentSubmissionSchemaPartXbkvdx(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_m934n = models.IntegerField(blank=True, null=True)
    programming_assignment_submission_schema_part_d4407a = models.NullBooleanField()
    programming_assignment_submission_schema_part_mrj41 = models.CharField(max_length=65535, blank=True, null=True)
    programming_assignment_submission_schema_part_2fyxz4 = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_assignment_submission_schema_part_xbkvdx'


class ProgrammingAssignmentSubmissionSchemaParts(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_title = models.CharField(max_length=65535, blank=True, null=True)
    programming_assignment_submission_schema_part_type = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_order = models.IntegerField(blank=True, null=True)
    programming_assignment_submission_schema_part_max_score = models.IntegerField(blank=True, null=True)
    programming_assignment_submission_schema_part_is_optional = models.NullBooleanField()
    programming_assignment_submission_schema_part_xacgt8 = models.IntegerField(blank=True, null=True)
    programming_assignment_submission_schema_default_g663i6 = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_assignment_submission_schema_parts'


class ProgrammingAssignments(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_base_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_type = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_type = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_instruction_text = models.CharField(max_length=65535, blank=True, null=True)
    programming_assignment_passing_fraction = models.FloatField(blank=True, null=True)
    programming_assignment_submission_builder_schema_type = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_builder_schema = models.CharField(max_length=65535, blank=True, null=True)
    programming_assignment_update_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_assignments'


class ProgrammingSubmissionPartEvaluations(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_part_score = models.IntegerField(blank=True, null=True)
    programming_submission_part_grading_ts = models.DateTimeField(blank=True, null=True)
    programming_submission_part_feedback = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_submission_part_evaluations'


class ProgrammingSubmissionPartGridGradingStatuses(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_part_grid_grading_status_pgrtf5 = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_part_grid_grading_status_x21exo = models.DateTimeField(blank=True, null=True)
    programming_submission_part_grid_grading_status_jzmjz1 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_submission_part_grid_grading_statuses'


class ProgrammingSubmissionPartGridSubmissions(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_part_grid_submission_url = models.CharField(max_length=65535, blank=True, null=True)
    programming_submission_part_grid_submission_custom_cykkte = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_submission_part_grid_submissions'


class ProgrammingSubmissionPartTextSubmissions(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_part_text_submission_answer = models.CharField(max_length=32767, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_submission_part_text_submissions'


class ProgrammingSubmissionParts(models.Model):
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_submission_schema_part_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_id = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_part_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_submission_parts'


class ProgrammingSubmissions(models.Model):
    programming_submission_id = models.CharField(max_length=50, blank=True, null=True)
    programming_assignment_id = models.CharField(max_length=50, blank=True, null=True)
    taiwan_programming_assignments_user_id = models.CharField(max_length=50)
    programming_submission_created_ts = models.DateTimeField(blank=True, null=True)
    programming_submission_type = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_grading_status = models.CharField(max_length=50, blank=True, null=True)
    programming_submission_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programming_submissions'


class Users(models.Model):
    taiwan_user_id = models.CharField(max_length=50)
    user_join_ts = models.DateTimeField(blank=True, null=True)
    country_cd = models.CharField(max_length=2, blank=True, null=True)
    region_cd = models.CharField(max_length=3, blank=True, null=True)
    profile_language_cd = models.CharField(max_length=8, blank=True, null=True)
    browser_language_cd = models.CharField(max_length=8, blank=True, null=True)
    reported_or_inferred_gender = models.CharField(max_length=50, blank=True, null=True)
    employment_status = models.CharField(max_length=100, blank=True, null=True)
    educational_attainment = models.CharField(max_length=100, blank=True, null=True)
    student_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersCoursesCertificatePayments(models.Model):
    taiwan_user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True, null=True)
    met_payment_condition = models.NullBooleanField()
    was_payment = models.NullBooleanField()
    was_finaid_grant = models.NullBooleanField()
    was_group_sponsored = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'users_courses__certificate_payments'

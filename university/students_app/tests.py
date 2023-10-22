from django.test import TestCase, TransactionTestCase
from .models import Student
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.utils import timezone

# Create your tests here.
class StudentModelTestCase(TestCase,TransactionTestCase):
    @staticmethod
    def print_info(message):
        count = Student.objects.count()
        print(f'{message}: #all_students={count}')

    def setUp(self):
        print('-' * 20)
        self.print_info('Start setUp')
        self.student = Student.objects.create(
            first_name='Samat', last_name='Aliev', age=29, email='somemista@gmail.com')
        self.time_difference = datetime.now() - self.student.created_at.replace(tzinfo=None)
        Student.objects.create(
            first_name='Arzula', last_name='Duvashova', age=28, email='123.com')
        self.student_young = Student.objects.create(
            first_name='Bella', last_name='Chao', age=4, email='bellanaa@gmail.com')
        self.print_info('Finish setUp')

    def test_student_creating(self):
        self.print_info("Start test_student_creating")
        self.assertIsNotNone(self.student.created_at)
        self.assertLessEqual(timezone.now() - self.student.created_at, timedelta(minutes=1))
        self.assertEqual(self.student.first_name, 'Samat')
        self.assertEqual(self.student.last_name, 'Aliev')
        self.assertEqual(self.student.age, 29)
        self.assertEqual(self.student.email, 'somemista@gmail.com')
        self.print_info("Finish test_student_creating")

    def test_student_get_all_records(self):
        self.print_info("Start test_student_get_all_records")
        students = Student.objects.all()
        self.assertEqual(len(students), 3)
        self.print_info("Finish test_student_get_all_records")

    def test_student_get_record(self):
        self.print_info("Start test_student_get_record")
        arzula = Student.objects.get(first_name='Arzula')
        self.assertEqual(arzula.age, 28)
        self.print_info("Finish test_student_get_record")

    def test_student_get_full_name_method(self):
        self.print_info("Start test_student_get_full_name_method")
        self.assertEqual(self.student.get_full_name(), 'Samat Aliev')
        self.print_info("Finish test_student_get_full_name_method")

    def test_student_is_adult_method(self):
        self.print_info("Start test_student_is_adult_method")
        self.assertTrue(self.student.is_adult())
        self.assertFalse(self.student_young.is_adult())
        self.print_info("Finish test_student_is_adult_method")

    def test_student_email_invalid_format(self):
        self.print_info("Start test_student_email_invalid_format")
        student = Student(
            first_name='John',
            last_name='Doe',
            age=25,
            email='invalid-email'
        )
        with self.assertRaises(ValidationError):
            student.full_clean()
        self.print_info("Finish test_student_email_invalid_format")

    def test_student_created_at_auto_now_add(self):
        self.print_info("Start test_student_created_at_auto_now_add")
        student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            age=25,
            email='john.doe@example.com'
        )
        student.refresh_from_db()
        initial_created_at = student.created_at

        student.first_name = "Jane"
        student.save()
        student.refresh_from_db()

        self.assertEqual(initial_created_at, student.created_at)
        self.print_info("Finish test_student_created_at_auto_now_add")

    def test_student_delete_record(self):
        self.print_info("Start test_student_delete_record")
        len_after_expected = Student.objects.count() - 1
        self.student.delete()
        len_after = Student.objects.count()
        self.assertEqual(len_after, len_after_expected)
        self.print_info("Finish test_student_delete_record")

    def test_student_change_record(self):
        self.print_info("Start test_student_change_record")
        self.student.age = 30
        self.assertEqual(self.student.age, 30)
        self.print_info("Finish test_student_change_record")

from django.test import TestCase
from core_admin.models import User
from django.utils.timezone import make_aware
import datetime

class UserTestCase(TestCase):

	databases = ['app']

	def setUp(self):
		now = make_aware(datetime.datetime.now())
		User.objects.create(
			name_first = "john",
			created_at = now,
			updated_at = now,
		)

	def test_name(self):
		"""Basic user model test"""
		u1 = User.objects.get(name_first = "john")
		self.assertEqual(u1.name_first, 'john')

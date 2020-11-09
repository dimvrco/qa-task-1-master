from django.contrib.gis.db import models

class User(models.Model):
	# id bigint NOT NULL,
	id = models.BigAutoField(primary_key = True)
	# uuid uuid DEFAULT public.gen_random_uuid(),
	uuid = models.UUIDField(blank = True, null = False)
	# name_first character varying,
	name_first = models.CharField(max_length = 255, blank = True)
	# name_last character varying,
	name_last = models.CharField(max_length = 255, blank = True)
	# nickname character varying,
	nickname = models.CharField(max_length = 255, blank = True)
	# avatar_url character varying,
	avatar_url = models.CharField(max_length = 255, blank = True)
	# email character varying,
	email = models.CharField(max_length = 255, blank = True)
	# created_at timestamp without time zone DEFAULT now() NOT NULL,
	created_at = models.DateTimeField()
	# updated_at timestamp without time zone DEFAULT now() NOT NULL,
	updated_at = models.DateTimeField()
	# preferences jsonb,
	preferences = models.JSONField(blank = True)
	# avatar_image bytea,
	avatar_image = models.BinaryField(blank = True)
	# non_user_notification_state jsonb
	non_user_notification_state = models.JSONField(blank = True)

	class Meta:
		managed = False
		db_table = 'users'
		required_db_vendor = 'postgis'
		# app_label = 'core_admin'

class Organization(models.Model):
	# id bigint NOT NULL,
	id = models.BigAutoField(primary_key = True)
	# uuid uuid DEFAULT public.gen_random_uuid(),
	uuid = models.UUIDField(blank = True, null = False)
	# name character varying,
	name = models.CharField(max_length = 255, blank = True)
	# address character varying,
	address = models.CharField(max_length = 255, blank = True)
	# phone character varying,
	phone = models.CharField(max_length = 255, blank = True)
	# email character varying
	email = models.CharField(max_length = 255, blank = True)
	# user_id bigint,
	user = models.ForeignKey('core_admin.User', models.DO_NOTHING)
	# user_id = models.BigIntegerField(blank=True, null=True)
	# created_at timestamp without time zone DEFAULT now() NOT NULL,
	created_at = models.DateTimeField()
	# updated_at timestamp without time zone DEFAULT now() NOT NULL,
	updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'organizations'
		required_db_vendor = 'postgis'

class Subscription(models.Model):
	# id bigint NOT NULL
	id = models.BigAutoField(primary_key=True)
	# organization_id integer NOT NULL
	organization = models.ForeignKey('core_admin.Organization', models.DO_NOTHING)
	# aoi jsonb NOT NULL
	aoi = models.JSONField(blank=True, null=True)
	# starts_at timestamp without time zone DEFAULT now() NOT NULL
	starts_at = models.DateTimeField()
	# ends_at timestamp without time zone,
	ends_at = models.DateTimeField(blank=True, null=True)
	# created_at timestamp without time zone DEFAULT now() NOT NULL,
	created_at = models.DateTimeField()
	# updated_at timestamp without time zone DEFAULT now() NOT NULL,
	updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'subscriptions'
		verbose_name_plural = "Subscriptions"

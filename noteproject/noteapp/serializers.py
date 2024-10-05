from rest_framework import serializers
from . models import *


class Noteserializer(serializers.ModelSerializer):
	class Meta:
		model=Note
		exclude=["created_date","updated_date"]
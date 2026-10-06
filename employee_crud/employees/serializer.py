from django.db.models import Model
from rest_framework import serializers
from employees.views import Employee

# class EmployeeSerializer(serializers.Serializer):
#
#     empid = serializers.IntegerField()
#     name = serializers.CharField(max_length=50)
#     age = serializers.IntegerField()
#     place = serializers.CharField(max_length=30)
#     gender_choices = [ ('male','Male'),('female','Female') ]
#     gender = serializers.ChoiceField(choices=gender_choices)
#     salary = serializers.IntegerField()
#     joining_date = serializers.DateField()
#     designation = serializers.CharField()
#
#
#     #After validation and before saving
#     def create(self, validated_data):
#
#         e=Employee.objects.create(**validated_data)
#         return e#returns employees object
#
#     def update(self,i,validated_data):
#
#         i.empid=validated_data.get('empid',i.empid)
#         i.name=validated_data.get('name',i.name)
#         i.age=validated_data.get('age',i.age)
#         i.place=validated_data.get('place',i.place)
#         i.gender=validated_data.get('gender',i.gender)
#         i.salary=validated_data.get('salary',i.salary)
#         i.joining_date=validated_data.get('joining_date',i.joining_date)
#         i.designation=validated_data.get('designation',i.designation)
#         i.save()
#         return i
#
#     from django.contrib.auth.models import User
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ['username', 'password', 'email', 'first_name', 'last_name']

from django.db.models import Model
from rest_framework import serializers
from employees.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '_all_'

        # or
        #
        # fields = ['title','director'......]

from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']
        #to create user account we use user.object.create_user not user.objects.create()
        #for password hashing
    def create(self, validated_data):
        u=User.objects.create_user(**validated_data)
        return u

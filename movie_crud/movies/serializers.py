from django.db.models import Model
from rest_framework import serializers
from movies.models import Movie
class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    director = serializers.CharField()
    language = serializers.CharField()
    year = serializers.IntegerField()
    rating = serializers.FloatField()
    runtime = serializers.IntegerField()
    image=serializers.ImageField()

 #After validation and before saving
    def create(self,validated_data):
        m=Movie.objects.create(**validated_data)
        return m

    def update(self, i, validated_data):
        i.empid = validated_data.get('empid', i.empid)
        i.name = validated_data.get('name', i.name)
        i.age = validated_data.get('age', i.age)
        i.place = validated_data.get('place', i.place)
        i.gender = validated_data.get('gender', i.gender)
        i.salary = validated_data.get('salary', i.salary)
        i.joining_date = validated_data.get('joining_date', i.joining_date)
        i.designation = validated_data.get('designatiom', i.designation)

        i.save()
        return i

    def validate(self, data):
        if data['age'] <= 0:
            raise serializers.ValidationError('age must be positive')
        return data
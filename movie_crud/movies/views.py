from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from movies import serializers
from movies.serializers import MovieSerializer


# Create your views here.
#Get,Post,put,patch,delete

#api view for reading all movie records
#qns
#serializer object
#response
from rest_framework.views import  APIView
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.response import Response

# class MovieList(APIView):
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data)
#
#
# #Api view for creating a new record
# #request.data
# #serializer_instance
# #validation
# #create() in serializer class for saving
# #response
# class MovieCreate(APIView):
#     def post(self,request):
#         form_data=request.data
#         serializers_instance=MovieSerializer(data=form_data)
#         if serializers_instance.is_valid():
#             #data after validation
#             # cleaned_data=serializers_instance.validated_data
#             # title=cleaned_data['title']
#             serializers_instance.save()
#             return Response(serializers_instance.data)
#         else:
#             return Response(serializers_instance.errors)
# class MovieListCreate(APIView):
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data)
#
#     def post(self, request):
#         form_data=request.data
#         serializers_instance=MovieSerializer(data=form_data)
#         if serializers_instance.is_valid():
#             #data after validation
#             # cleaned_data=serializers_instance.validated_data
#             # title=cleaned_data['title']
#             serializers_instance.save()
#             return Response(serializers_instance.data)
#         else:
#             return Response(serializers_instance.errors)

from rest_framework import mixins,generics
class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Movie.objects.all()
    serializers_class=MovieSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializers_class=MovieSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partialupdate(request, pk)
    def delete(self,request,pk):
        return  self.destroy(request,pk)



# #Api view for updating a specific record
# #api view for deleting a specific record
# class MovieRetrieveUpdateDelete(APIView):
#     def get(self,request,id):
#         m=get_object_or_404(Movie,id=id)
#         serializer_instance=MovieSerializer(m)
#         return Response(serializer_instance.data)
# #api view for updating all fields
# #data
# #serializer_instance(instance.data)
# #validation
# #update() in serializer class for having
# #response
#
#
#
#     def put(self, request, id):
#
#         form_data=request.data
#         m=Movie.objects.get(id=id)
#         serializer_instance=MovieSerializer(m,data=form_data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
#     def patch(self, request, id):
#
#         form_data = request.data
#         m = Movie.objects.get(id=id)
#         serializer_instance = MovieSerializer(m, data=form_data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
#
#
#     def delete(self,request,id):
#         m=get_object_or_404(Movie,id=id)
#         m.delete()
#         return Response({"message":"movie is deleted"})


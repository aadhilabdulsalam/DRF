from os import name

from django.contrib.sessions import serializers
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.template.defaultfilters import title
from django.views import View
from rest_framework import status
from rest_framework import response

from employees.models import Employee
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from employees.serializer import EmployeeSerializer


# Create your views here.
#APIView for reading All employee record
# class EmployeeList(APIView):
#     def get(self, request):
#         qs = Employee.objects.all()
#         #read all employee records from Employee Table(qs)
#         serializers_instance = EmployeeSerializer(qs, many=True)
#         #employeeSerializer converts qs into  python native types
#         #qs contains more than one records so we use many=true
#
#         return Response(data=serializers_instance.data)
#     #sends python native data so
#
# #APIView for reading a specific employee detail
# class EmployeeDetails(APIView):
#     def get(self, request,i):
#         # qs = Employee.objects.get(empid=i)
#         qs=get_object_or_404(Employee,empid=i)
#         #read all employee records from Employee Table(qs)
#         serializers_instance = EmployeeSerializer(qs)
#
#         #employeeSerializer converts qs into  python native types
#         #qs contains more than one records so we use many=true
#
#         return Response(data=serializers_instance.data)
#     #sends python native data so
#
# from json import loads
#
#
# class EmployeeCreate(APIView):
#     def post(self, request):
#         serializers_instance=EmployeeSerializer(data=request.data)
#         if serializers_instance.is_valid():
#             serializers_instance.save()
#             return Response({"message":"created"})
#         else:
#             return Response(serializers_instance.errors)
        # data = loads(request.body)
        # data = request.data  #python native type data or dictionary
        # # eid=data['empid']
        # # n=data['name']
        # # a=data['age']
        # # p=data['place']
        # # g=data['gender']
        # # s=data['salary']
        # # j=data['joining_date']
        # # d=data['designation']
        # s = Employee.objects.create(**data)
        # s.save()
        # return Response({"message": "Inserted data Succesfully"})

#         s=Employee.objects.create(empid=eid,name=n,age=a,place=p,gender=g,salary=s,joining_date=j,designation=d)
#         s.save()
#
#         return Response({"message":"Inserted data Succesfully"})
#
#
# class EmployeeRetrieve(View):
#     def get(self,request,i):
#         s=list(Employee.objects.filter(empid=i).values())
#         if s:
#             return Response(s,safe=False)
#         else:
#             return Response({"message":"No Employee Data"})
#
#
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeFullUpdate(View):
#     def put(self,request,i):
#         data=loads(request.body)
#         try:
#             s=Employee.objects.get(empid=i)
#             s.empid=data['empid']
#             s.name=data['name']
#             s.age=data['age']
#             s.place=data['place']
#             s.gender=data['gender']
#             s.salary=data['salary']
#             s.joining_date=data['joining_date']
#             s.designation=data['designation']
#             s.save()
#
#             return Response({"message":"Successfully Updated"})
#
#         except:
#             return Response({"message":"No Employee Data"})
#
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeePartialUpdate(View):
#     def patch(self,request,i):
#         data=loads(request.body)
#
#         try:
#             s=Employee.objects.get(empid=i)
#
#             if 'empid' in data:
#                 s.empid = data['empid']
#             if 'name' in data:
#                 s.name = data['name']
#             if 'age' in data:
#                 s.age = data['age']
#             if 'place' in data:
#                 s.place = data['place']
#             if 'gender' in data:
#                 s.gender = data['gender']
#             if 'salary' in data:
#                 s.salary = data['salary']
#             if 'joining_date' in data:
#                 s.joining_date = data['joining_date']
#             if 'designation' in data:
#                 s.designation = data['designation']
#
#             s.save()
#
#             return Response({"message": "Successfully Updated"})
#
#         except:
#             return Response({"message": "No Employee Data"})
#
# @method_decorator(csrf_exempt,name='dispatch')
#
# class EmployeeDelete(APIView):
#     def delete(self,request,i):
#         qs=get_object_or_404(Employee,empid=i)
#
#         qs.delete()
#
#         return Response({"Message":"Deleted Successfully"})
#
# class EmployeeUpdate(APIView):
#     def put(self,request,id):
#         qs=Employee.objects.get(id=id)
#         serializer_instance=EmployeeSerializer(qs,request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
# class EmployeepartialUpdate(APIView):
#     def patch(self,request,id):
#         qs=get_object_or_404(Employee,id=id)
#         serializer_instance=EmployeeSerializer(qs,request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
#                           MIXIN

from rest_framework import mixins, generics
# class EmployeeListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
# class EmployeeRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def patch(self, request, pk):
#         return self.partialupdate(request, pk)
#     def delete(self,request,pk):
#         return  self.destroy(request,pk)

# class EmployeeList(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
# class EmployeeRetrieveUpdateDelete(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
from rest_framework import viewsets
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#search API View
# class SearchAPIView(APIView):
#     def get(self,request):
#         data=self.request.query_params.get('search')
#         m=Employee.objects.filter(Q(empid__icontains=data)|
#                                   Q(name__icontains=data)|
#                                   Q(age__icontains=data))
#         if not m.exists():
#             return Response({'message':"No Record Found" },status=status.HTTP_200_OK)
#         serializers_instance=EmployeeSerializer(m,many=True)
#         return Response(serializers_instance.data,status=status.HTTP_200_OK)

from rest_framework.filters import SearchFilter

class SearchAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_filter=['empid','name','age']
from employees.serializer import UserSerializer
class RegisterApiView(APIView):
    def post(self,request):
        form_data = request.data

        s_ins =UserSerializer(data=form_data)
        if s_ins.is_valid():
            s_ins.save()
            return Response(s_ins.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s_ins.data,status=status.HTTP_400_BAD_REQUEST)\





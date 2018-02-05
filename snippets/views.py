# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import HttpResponse, JsonResponse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
# from django.http import Http404 # part3
# from rest_framework.views import APIView # part3
# from rest_framework.response import Response # part3
# from rest_framework import status # part3

# from rest_framework import mixins # part 3 - final
from rest_framework import generics

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
from django.contrib.auth.models import User

# @csrf_exempt # part 1
# @api_view(['GET', 'POST']) # part 2
# def snippet_list(request, format=None): # part 1, part 2
# class SnippetList(APIView): # part 3
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView): # part 3 - final
class SnippetList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # """
    # List all code snippets, or create a new snippet.
    # """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # # if request.method == 'GET':
    # # def get(self, request, format=None): # part 3
    # def get(self, request, *args, **kwargs):
    #     # snippets = Snippet.objects.all()
    #     # serializer = SnippetSerializer(snippets, many=True)
    #     # return JsonResponse(serializer.data, safe=False)
    #     # return Response(serializer.data) # part 3
    #     return self.list(request, *args, **kwargs)

    # # elif request.method == 'POST':
    # # def post(self, request, format=None): # part 3
    # def post(self, request, *args, **kwargs):
    #     # data = JSONParser().parse(request)
    #     # serializer = SnippetSerializer(data=request.data)
    #     # # serializer = SnippetSerializer(data=data)
    #     # if serializer.is_valid():
    #     #     serializer.save()
    #     #     # return JsonResponse(serializer.data, status=201)
    #     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # # return JsonResponse(serializer.errors, status=400)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return self.create(request, *args, **kwargs)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
# class SnippetDetail(APIView):
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView): # part 3 - final
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    # """
    # Retrieve, update or delete a code snippet.
    # """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # def get_object(self, pk):
    #     try:
    #         # snippet = Snippet.objects.get(pk=pk)
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         # return HttpResponse(status=404)
    #         # return Response(status=status.HTTP_404_NOT_FOUND)
    #         raise Http404

    # if request.method == 'GET':
    # def get(self, request, pk, format=None):
    # def get(self, request, *args, **kwargs):
    #     # snippet = self.get_object(pk)
    #     # serializer = SnippetSerializer(snippet)
    #     # # return JsonResponse(serializer.data)
    #     # return Response(serializer.data)
    #     return self.retrieve(request, *args, **kwargs)


    # # elif request.method == 'PUT':
    # # def put(self, request, pk, format=None):
    # def put(self, request, *args, **kwargs):
    #     # data = JSONParser().parse(request)
    #     # serializer = SnippetSerializer(snippet, data=data)
    #     # snippet = self.get_object(pk)
    #     # serializer = SnippetSerializer(snippet, data=request.data)
    #     # if serializer.is_valid():
    #     #     serializer.save()
    #     #     # return JsonResponse(serializer.data)
    #     #     return Response(serializer.data)
    #     # # return JsonResponse(serializer.errors, status=400)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return self.update(request, *args, **kwargs)


    # # elif request.method == 'DELETE':
    # # def delete(self, request, pk, format=None):
    # def delete(self, request, *args, **kwargs):
    #     # snippet = self.get_object(pk)
    #     # snippet.delete()
    #     # # return HttpResponse(status=204)
    #     # return Response(status=status.HTTP_204_NO_CONTENT)
    #     return self.destroy(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
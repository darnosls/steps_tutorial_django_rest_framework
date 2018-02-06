# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# from django.http import HttpResponse, JsonResponse
# from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
# # from django.http import Http404 # part3
# # from rest_framework.views import APIView # part3
# # from rest_framework.response import Response # part3
# # from rest_framework import status # part3

# # from rest_framework import mixins # part 3 - final
# from rest_framework import generics

# # from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import renderers
# from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response


# @csrf_exempt # part 1
# @api_view(['GET', 'POST']) # part 2
# def snippet_list(request, format=None): # part 1, part 2
# class SnippetList(APIView): # part 3
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView): # part 3 - final
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })



# class SnippetList(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     # """
#     # List all code snippets, or create a new snippet.
#     # """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

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
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#     # """
#     # Retrieve, update or delete a code snippet.
#     # """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

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


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
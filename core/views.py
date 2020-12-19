from django.urls import resolve, reverse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import *


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProfilePostList(generics.ListAPIView):
    lookup_field = 'userId'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(**self.kwargs)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentPostList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(**self.kwargs)


class CommentPostDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    multiple_lookup_fields = ('pk', 'postId')

    def get_object(self):
        queryset = self.get_queryset()

        obj = get_object_or_404(queryset, **self.kwargs)

        return obj


def getCommentPostUserData():
    profiles = Profile.objects.all()

    data = []

    for profile in profiles:
        posts = Post.objects.filter(userId=profile.id)

        total = 0

        for post in posts:
            total += len(Comment.objects.filter(postId=post.id))

        dict_ = {
            'pk': profile.id,
            'name': profile.name,
            'total_posts': len(posts),
            'total_comments': total,
        }

        data.append(dict_)

    return data


@api_view(['GET', ])
def commentPostUserList(request):
    return Response(getCommentPostUserData())


@api_view(['GET', ])
def commentPostUserDetail(request, pk):
    data = getCommentPostUserData()

    for item in data:
        if pk == item.get('pk'):
            return Response(item)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', ])
def apiRouteList(request):
    print(request.get_full_path())
    print()

    data = [{'url': request.build_absolute_uri() + 'profiles/', 'info': 'Lista todos os usuários'},
            {'url': request.build_absolute_uri() + 'profiles/<int:pk>', 'info': 'Mostra um usuário. <pk>: Id do usuário'},
            {'url': request.build_absolute_uri() + 'profile-posts/', 'info': 'Lista todas as postagens'},
            {'url': request.build_absolute_uri() + 'profile-posts/<int:userId>',
             'info': 'Lista todas as postagens feitas por um usuário. <userId>: Id do usuário'},
            {'url': request.build_absolute_uri() + 'posts-comments/', 'info': 'Lista todos os comentários'},
            {'url': request.build_absolute_uri() + 'posts-comments/<int:pk>', 'info': 'Mostra um comentário. <pk>: Id do comentário'},
            {'url': request.build_absolute_uri() + 'posts/<int:postId>/comments',
             'info': 'Lista todos os comentários de uma postagem. <postId>: Id da postagem'},
            {'url': request.build_absolute_uri() + 'posts/<int:postId>/comments/<int:pk>',
             'info': 'Mostra um comentário de uma postagem. <postId>: Id da postagem, <pk>: Id do comentário'},
            {'url': request.build_absolute_uri() + 'comments-post-user/',
             'info': 'Lista a quantidade de postagens e comentários nas postagens de cada usuário'},
            {'url': request.build_absolute_uri() + 'comments-post-user/<int:pk>',
             'info': 'Mostra a quantidade de postagens e comentários nas postagens de um usuário. <pk>: Id do usuário'}]

    return Response(data)

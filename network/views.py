
from types import ClassMethodDescriptorType
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core import serializers
from django.views.decorators.csrf import csrf_protect

from django.db.models import Q


from .models import User, Post, Followers
import json


def index(request):
    return render(request, "network/index.html")


# def user(request):
#     return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            print(user)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
@login_required
def createPost(request):
    user = request.user

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    # print(data.get('body', ""))
    post_body = data.get("body", "")

    post = Post(creator=user, body=post_body)

    post.save()

    return JsonResponse({"message": "post is created successfully."}, status=201)
    # return getPosts(request, "all")


@csrf_exempt
@login_required
def getPosts(request, type):
    user = request.user
    page = int(request.GET.get("page"))
    id = request.GET.get('id')

    if type == "all":
        posts = Post.objects.all()

    elif type == "user":
        # user = Followers.objects.filter()
        posts = Post.objects.filter(creator=id)
    else:

        f = Followers.objects.filter(followee_id=user).values_list(
            'following_id', flat=True)
        print(list(f))
        posts = Post.objects.filter(creator_id__in=f)
        for i in posts:
            print(i.creator)
        print(posts)
    # return JsonResponse(posts)
    # Return emails in reverse chronologial order

    pp = posts.order_by("-timestamp").all()
    # print(pp)
    object = pp
    # print(10)
    # type(posts)
    pages = Paginator(object, 10)
    try:
        p = pages.page(page)
    except:
        p = 0
        return JsonResponse({'length': f'{p}'})
    # print(posts)

    poster = [post.creator.username for post in p]

    # return JsonResponse(serializers.serialize('json', posts), safe=False)
    return JsonResponse({'post': [serializers.serialize('json', p)], 'poster': poster, 'current_user': f'{user}'}, safe=False)

    # return JsonResponse(serializers.serialize('json', page_posts), safe=False)


@csrf_protect
@ csrf_exempt
@ login_required
def updatePost(request, id):
    user = request.user
    # print('not here')

    if request.method == "PUT" or request.method == 'POST':
        # return JsonResponse({"error": "PUT request required"}, status=400)

        try:
            post = Post.objects.get(id=id)

        except Post.DoesNotExist:
            return JsonResponse({"error": "Post Not Found"}, status=400)

        data = json.loads(request.body)
        # print(data)
        body = data.get('body')
        # likes = data['likes']

        post.body = body
        # print(body)

        post.save()
    return HttpResponse(status=201)


@ csrf_exempt
@ login_required
def updateLikes(request, id):
    user = request.user
    # print('likesss')

    try:
        post = Post.objects.get(id=id)
        # print(post.creator.username)

    except Post.DoesNotExist:
        return JsonResponse({"error": "Post Not Found"}, status=400)
    if request.method == "PUT" or request.method == 'POST':
        # print(post)
        data = json.loads(request.body)
        likes = int(data.get('likes'))
        answer = data.get('answer')
        if answer == 'del':
            user.likes.remove(post)
        else:
            user.likes.add(post)
        post.likes_counter = likes
        post.save()

    else:
        answer = ''
        # print(user.likes.all())
        if post in user.likes.all():
            answer = 'yes'
            # print('yes')
        else:
            answer = 'no'
            # print('no')

        return JsonResponse(answer, safe=False)

    return HttpResponse(status=201)


@ csrf_exempt
@ login_required
def userProfile(request, id):
    current_user = request.user

    s = id
    # try:
    print(id)
    user = User.objects.get(id=s)

    # except User.DoesNotExist:
    #     return JsonResponse({"error": "User not found."}, status=404)
    answer = 'no'
    following = Followers.objects.filter(
        followee_id=user)
    followers = Followers.objects.filter(
        following_id=user)

    print(current_user.following)
    followers_id = followers.values('followee_id')
    following_id = following.values('following_id')
    print(following_id)
    print(followers_id)

    # checking if the current user follows the user
    for i in followers_id:
        if current_user.id == i['followee_id']:

            answer = 'yes'
    print(answer)
    if request.method == "GET":

        followingNum = len(following_id)
        followersNum = len(followers_id)
        print(followersNum)
        print(followingNum)

        return JsonResponse({'user': [serializers.serialize('json', [user, ])], 'answer': f'{answer}', 'following': f'{followingNum}', 'followers': f'{followersNum}', 'current_user': f'{current_user.id}'}, safe=False)

        # return JsonResponse({'user': f'{user}', 'email': f'{user.email}', 'date': f'{user.date_joined}'}, safe=False)

    else:

        # if current_user in following:
        if answer == 'no':
            Followers.objects.create(followee=current_user, following=user)
        else:
            Followers.objects.filter(
                followee_id=current_user, following_id=user).delete()
        print('Done')

    return HttpResponse(status=201)

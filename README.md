# Network 
## Network is twitter alike Web App powered by [Django](https://www.djangoproject.com/) using [Python](https://www.python.org/) . In this platform, readers can search for posts(tweets/articles) arbitrarily , write thier thoughts and post it and many more features such as . 
  - All posts aka timeline is available
  - Profile page :which containes personal inforamtion  and the option to follow and unfollow , in addition to all posts of that user
  - Edit Post: user can edit only thier own posts
  - users can like and unlike posts


# Project Structure


## HTML Files

 - index.html 
   - this page has new feeds (posts) of all users theirs included as well the ability to navigate to other pages 
      
 - user.html
   -  this page has the information about the user , thier likes, posts, username,conatct info and comments 
 
 - login.html:-
   - user has to login in order to participate in  any class 
 
 - Register.html:-
   - a page in which a user with no previous interaction with this site has to register to be able to use this website
  

## JS Files
 -  main.js (include all the functions to handle and manipulate the DOM, using json and Ajax)



# Backend



## Python Files
 - models.py(includes 4 models (user,classes,membership,user_class)
   - it includes 4 models
      - user model (saves user logging data )
      - followers model (hadles relation between user and thier followers)
      - post model ( links each post to its poster as well as saves each post with date , time , likes and which user liked the post )
      
 - views.py (includes methods to linke client side with server side)
     - it includes functions like:
         - log_view
         - createPost
         - getPosts
         - updatePost
         - updateLikes
         - userProfile
 - urls.py (include routes(post,user,followers) as well as API routes(join, class_capacity)
   - routes(Paths):-
      - /
      - /post
      - /user
      - /login
      - logout 
   - API routes:-
      - /post
      - /user



# Setup
   ```shell script
git clone https://github.com/oi19/Network
cd Network
```
Run the following command to run your server.


```shell script
python manage.py runserver
```

Run those following commands to migrate database.

```shell script
python manage.py makemigrations
python manage.py migrate
```



  
  

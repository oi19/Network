# Network 
## Network is twitter alike Web App powered by [Django](https://www.djangoproject.com/). In this platform, readers can search for posts(tweets/articles) arbitrarily , write thier thoughts and post it and many more features such as . 
  - All posts aka timeline is available
  - Profile page :which containes personal inforamtion  and the option to follow and unfollow , in addition to all posts of that user
  - Pagination : the ability to change pages and limit number of posts per page
  - Edit Post: user can edit only thier own posts
  - users can like and unlike posts


# Project Structure


## HTML Files
 - add Page(include a form with post request to add new class)
   - it is a page inwhich a person can add new gym classes to the schedual as well as adding an available  trainer or coach that works at the gym 
      
 - index page (include all classes)
   - this page has all available gym classes with the number of the people joined to that each class as well as each class's trainer's name 
   
   - as well as a button for getting a membership or renew your expired one depends on your situation and if youre expired you see no classes since you cant join classes 
    unless you have youre membership verified 
   
   
 - user page(include user infomation)
   -  this page has the information about the user and thier memebership date info and whether it's expired or not 
 
 - login page:-
   - user has to login in order to participate in  any class 
 
 - Register page:-
   - a page in which a user with no previous interaction with this site has to register to be able to use this website
  

## JS Files
 -  main.js (include all the functions to handle and manipulate the DOM, using json and Ajax)



# Backend



## Python Files
 - models.py(includes 4 models (user,classes,membership,user_class)
   - it includes 4 models
      - user model (saves user logging data )
      - classes model(for class name , trainer of each class as well as date of classes)
      - membership model (for membership info of each user )
      - user_class model (it coordinate each user with classes to which he enrolled (many to many relationship))
      
 - views.py (include different functions such as class_capacity , user,membershipinfo ,join,add)
     - it includes functions
         - class capacity 
         - user
         - membershipinfo
         - join
         - add
 - urls.py (include routes(add,user,membershipinfo) as well as API routes(join, class_capacity)
   - routes(Paths):-
      - /
      - /add
      - /user
      - /membershipinfo 
   - API routes:-
      - /join
      - /class_capacity



# Setup
   ```shell script
git clone https://github.com/me50/oi19.git
cd web50/projects/2020/x/capstone
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



  
  

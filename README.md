# GameBox
[GameBox](https://g4m3b0x-effbc16f1911.herokuapp.com/) is a comprehensive library of games which includes the year of release, metascore, and user score. Users can log in to leave reviews or comments on their favourite games and admins can add, edit, or delete game entries

![screenshot of app](docs/screenshots/homepage.png)

## Contents

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Palette](#colour-palette)

* [Wireframes and Mockups](#wireframes)

* [Entity Relationship Diagram](#erd)

* [Features](#features)
  * [Existing Features](#existing-features)
    * [Navigation Bar](#navigation-bar)
    * [Search Bar](#search-bar)
    * [Account Registration](#account-registration)
    * [About Page](#about-page)
    * [My Comments Page](#my-comments)
    * [Leave a Comment](#comment)
  * [Future Features](#future-features)
    * [Contribute Score](#contribute)
    * [List sorting](#sort-list)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
    * [APIs](#apis)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Acknowledgements](#acknowledgements)

  ---

  ## User Experience (UX)

  ### Project Goals

    This application aims to provide a comprehensive list of games for multiple platforms, and allow the user to see both an aggregated review score (metascore), and also an average user score. It also aims to allow users to leave their own comments and reviews for their favourite games and in the future will also allow them to contribute their own scores to be added to the 'userscore' field of each game page.

## User Stories

### Admin

- As a site admin I can add, modify and delete game entries so that I can curate the library.
- As a site admin I can approve or disapprove comments so that I can filter out objectionable comments.
- As a Site Admin, I can create or update the about page content so that it is available on the site.

### User

- As a Site User, I can click on the About link so that I can read about the site.
- As a site user I can view a list of games so that I can find my favourites.
- As a user I can type the name of a game into a search bar in order to quickly find the game I'm looking for.
- As a site user I can modify or delete my comment on a post so that I can be involved in the conversation.
- As a site user I can open a game page so that I can view the game in more detail.
- As a site user I can register an account so that I can comment on a post.
- As a site user I can leave comments on a game page so that I can be involved in the conversation.
- As a site user I can access a page to view all of my comments so that I can keep track of my conversations.
- As a site user I can view comments on an individual post so that I can read the conversation.

---

## Design

### Colour Palette

![screenshot](docs/screenshots/palette.png)

- The colour palette was taken from the Adobe Color Wheel library and is called 'Profile of David statue by Michelangelo Buonarotti replica in vaporwave style'
- It includes the following colours:
    - #BF349A
    - #8C2771
    - #E7DCF2
    - #2ABFBF
    - #29A6A6

### Wireframes

#### Homepage

![homepage](docs/wireframes/homepage.png)

#### About

![about](docs/wireframes/about.png)

#### Game Detail

![detail](docs/wireframes/detail.png)

#### My Comments

![my comments](docs/wireframes/my_comments.png)

#### Homepage Phone Version

![homepage-phone](docs/wireframes/homepage-phone.png)

---

## Features

### Existing Features

#### Navigation Bar

![screenshot of navigation bar](docs/screenshots/navbar.png)

- A navigation bar at the top of the page allows users to navigate the site quickly.
- Links in the navigation bar include Home, About, My Comments (when logged in), Logout (when logged in), Register (when not logged in), and Login (when not logged in)

#### Search Bar

![screenshot of search bar](docs/screenshots/searchbar.png)

![screenshot of search results](docs/screenshots/search.png)

- There is a search bar at the top of the page allowing users to quickly search for a particular game they are trying to find, or alternatively all games for a specific console, released a specific year, etc.

#### Account Registration

![screenshot of sign up](docs/screenshots/signuppage.png)

- Users are able to register an account in order to leave comments on game pages.
- Registration page includes checks for invalid inputs.

#### About Page

![screenshot of about](docs/screenshots/aboutpage.png)

- About page gives a summary of the website and its goals.

#### My Comments

![screenshot of my comments](docs/screenshots/mycomments.png)

- Users can see all of the comments they have left with links to the game page they left them on.

#### Comment

![screenshot of comment box](docs/screenshots/comment.png)

- When a user is logged in, they can leave a comment or short review on each game page.

### Future Features

#### Contribute Score

- Users will be able to give each game a score out of 10 which will be added to the 'userscore' field.

#### List Sorting

- Users will be able to sort the library of games by name, release year, score, etc.

---

  ## Technologies Used

  ### Languages Used

- HTML5
- CSS3
- Javascript
- Python
- Django
- SQL - Postgres

  ### Frameworks, Libraries & Programs Used

  Git - For version control.

  Github - To save and store the files for the application.

  VSCode - To develop project and organise version control.

  Heroku - To deploy the application.

  Django - To develop project

  Bootstrap - To style project

  IGDB - Used to retrieve box art for games

  pgAdmin 4 - Used to administer database

  Balsamiq - To create wireframes

  ### Installed Packages

asgiref==3.8.1
black==24.10.0
bleach==6.2.0
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.4.0
click==8.1.7
crispy-bootstrap5==0.7
cryptography==44.0.0
defusedxml==0.7.1
dj-database-url==0.5.0
Django==4.2.17
django-allauth==0.57.2
django-crispy-forms==2.3
django-extensions==3.2.3
django-summernote==0.8.20.0
gunicorn==23.0.0
idna==3.10
igdb-api-v4==0.3.3
mypy-extensions==1.0.0
oauthlib==3.2.2
packaging==24.2
pathspec==0.12.1
platformdirs==4.3.6
postgres==4.0
protobuf==5.29.1
psycopg2==2.9.10
psycopg2-binary==2.9.10
psycopg2-pool==1.2
pycparser==2.22
PyJWT==2.10.1
python3-openid==3.2.0
requests==2.32.3
requests-oauthlib==2.0.0
setuptools==75.6.0
sqlparse==0.5.2
style==1.1.0
urllib3==2.2.3
webencodings==0.5.1
whitenoise==5.3.0


  ---

## Deployment & Local Development

### Deployment

The deployment of the project was done using [Heroku](https://www.heroku.com/) through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
   * For this project, the unique name is "g4m3b0x" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and locate the "Config Vars" section and click "Reveal config vars".
6. Add config vars: 
   * For this project I have four config vars:
     * DATABASE_URL - For the database
     * SECRET_KEY - Password for accessing database
     * IGDB_ID - ID to access IGDB API
     * IGDB_SECRET - Password to access IGDB API
7. Navigate to the "Deploy" section by clicking the "Deploy" tab in the top navbar.
8. Select "GitHub" as the deployment method and click "Connect to GitHub".
9. Search for the GitHub repository name in the search bar.
10. Click on "connect" to link the repository to Heroku.
11. Scroll down and click on "Deploy Branch".
12. Once the app is deployed, Heroku will notify you and provide a button to view the app.

NB - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys".

### How to Fork

This can be done to create a copy of the repository. The copy can be viewed and edited without affecting the original repository.

To fork the repository through GitHub, take the following steps:
1. In the "CI_PP4" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository.

### How to Clone

To clone the repository through GitHub:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.
2. Ensure HTTPS is selected in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

### APIs
In order for the app to function properly, APIs need to be set up and connected. In particular, the following APIs were used for this project:

* IGDB API:
  * This was used in order to retrieve box art for games

---

## Testing

Testing was ongoing throughout the build.

### Python PEP8 Testing

I used the Code Institute Python Linter to check for syntax and styling errors and found none.

![screenshot](docs/validators/gamelibrary_views.png)
![screenshot](docs/validators/gamelibrary_urls.png)
![screenshot](docs/validators/gamelibrary_models.png)
![screenshot](docs/validators/gamelibrary_forms.png)
![screenshot](docs/validators/gamelibrary_apps.png)
![screenshot](docs/validators/gamelibrary_admin.png)
![screenshot](docs/validators/gamebox_urls.png)
![screenshot](docs/validators/gamebox_settings.png)
![screenshot](docs/validators/about_views.png)
![screenshot](docs/validators/about_models.png)
![screenshot](docs/validators/about_apps.png)
![screenshot](docs/validators/about_admin.png)

### HTML W3C Validator

I used the W3C HTML validator and found one error on the about page.

![screenshot](docs/validators/home.png)
![screenshot](docs/validators/about.png)
![screenshot](docs/validators/gamedetailw3c.png)

### Solved Bugs

1. While trying to apply a database migration I got the error: django.db.utils.DataError: invalid input syntax for type numeric: "tbd". This happened because I changed the parameters of the userscore field and it would no longer accept the value 'tbd' from the dataset. I was able to use pgAdmin 4 to find the relevant entries and change all instances of 'tbd' to 0.

2. Whenever I attempted to delete a comment as a logged in user, the website would delete that comment but then post an identical one at the same time. This turned out to be a conflict between the post comment and delete comment in the game detail view. To fix this, I added an if statement inside the submit comment function to ensure the POST request was specifically for submitting a new comment, and not for any other reason (like deletion).

3. Users were initially unable to access their 'My Comments' page. This turned out to be an issue with the ordering of paths in urls.py. The were rearranged in order to fix this bug.

### Known Bugs

1. No known bugs at this time.

### Manual Testing

1. Test homepage loading and layout
2. Verify navbar links (home, about, my comments, register, login, logout) redirect correctly
3. Check searchbar functionality with various game titles
4. Test user registration process
5. Test user login process
6. Test user logout process
7. Check game library display and pagination
8. Verify each game entry shows title, release date, metascore, and user score
9. Test opening individual game pages
10. Verify game details are displayed correctly on individual pages
11. Test leaving a comment on a game page as a logged-in user
12. Verify comment appears on the game page after submission
13. Test editing a user's own comment
14. Test deleting a user's own comment
15. Verify "My Comments" page displays all user comments correctly
16. Test admin login process
17. Verify admin can add a new game entry
18. Test admin ability to modify existing game entries
19. Verify admin can delete game entries
20. Test admin approval/disapproval of user comments
21. Verify approved comments are visible and disapproved comments are hidden
22. Test admin ability to create/update About page content
23. Verify About page content is displayed correctly
24. Test responsiveness on various devices (desktop, tablet, mobile)
25. Check cross-browser compatibility (Chrome, Firefox, Safari, Edge)
26. Verify all forms have proper validation
27. Test form submission with valid and invalid data
28. Check for broken links throughout the site
29. Test search functionality with partial game titles
30. Verify search results are accurate and relevant
31. Test pagination in game library
32. Verify correct user roles and permissions (admin vs regular user)
33. Verify success messages appear for completed actions
34. Check for any UI/UX inconsistencies or visual bugs
35. Verify all images load correctly and have alt text


---

## Credits

### Code Used

Basic layout/templates from I think therefore I blog tutorial

### Acknowledgements

[IGDB API for game box art](https://www.igdb.com/api)
[Kaggle for games dataset](https://www.kaggle.com/datasets/destring/metacritic-reviewed-games-since-2000)
[Adobe Color Wheel for colour palette](https://color.adobe.com/create/color-wheel)
[Black for pep8 compliance](https://pypi.org/project/black/)

Big thanks to my tutor Lauren-Nicole Popich for making this mountain seem like a molehill!
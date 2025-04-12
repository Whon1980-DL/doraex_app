# DoraEx


Experience your childhood dream of trying many of Doraemon genius gadgets that by reading about our app and seeing the gadget already bring nostalgic feeling let alone be able to try using one for real. We have amazing range of gadgets for you to try from simple one like Take-copter and to the very popular one like the Anywhere-door. Your mind will be blown once you try them. Through our app you can browse our gadget range when conveniently rent our gadget that will instantly be delivered to your doorstep thanks to our own Anywhere-Door.

![Home Screen](documentation/readme_images/am_i_responsive.png)

[View DoraEx live website here](https://doraex-app-b88d916586ec.herokuapp.com/)
- - -

## Table of Contents
### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [Target Audience](#target-audience)
* [First time user](#first-time-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Wireframes](#wireframes)
* [Data Model](#data-models)
* [User Journey](#user-journey)
* [Database Scheme](#database-scheme)
### [Security Features](#security-features-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Features Left to Implement](#features-left-to-implement)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

Doraemon gadgets brought to your door with few clicks. The range includes most popular gadgets such as Take-copter and Anywhere-door just to name a couple. Through our responsive website your dream of discovering the joy of using these gadgets are very simple. The gadgets are display with Doraemon theme vivid and nostalgic to those who grew up watching the series on TV. Gadget description is very well written and cleared with warning and age restriction guideline for health and safety. The renting process is super simple and enjoyable. With our delivery process made so simple by our Anywhere-door your gadget can be delivered as soon as you confirm your renting for whose who are very keen to try.

### Project Goals

The goal of this project was to create a user friendly website that is intuitive and appealing. The website aim to reintroduce the love of Doraemon and those who have always dreaming about what it would feel like to try some of the very popular gadgets. Renting process had been made very simple with the functionality for user to edit and confirm rent as well as tracking their rent history. Reading about what can each gadget do the info comes with waning and the intended use of each gadgets.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writting the user stories and using Project Boards on Github. Template was created to help write User Stories.

* User stories were created by identifying what are the require features and functionalities and through iterations the project was advancing.
* Project Board is set to public.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns
* Labels were added to sort the issues based on the importance.

<details>
<summary> Project Board
</summary>

![Project Board](documentation/readme_images/project-board.png)
</details>

### User Stories

#### User Stories
1. Manage Category list
2. Manage Gadget Lists
3. Create Draft
4. Create view paginated list of gadgets
5. Create view for gadget to display by category
6. Create view to display gadget of interest with detail
7. Manage user sign up and authentication
8. Create rental form for user interaction
9. Manage user profile
10. Create cart to hold rented gadget
11. User can manage rental with CRUD funcitonality

Detailed look can be found in the [project board](https://github.com/users/Whon1980-DL/projects/4/views/1)

### Target Audience

 Individuals who seek the experience of using Doraemon gadgets
* People who are willing to pay a little extra to gain comfort of many ways the gadget can offer.
* People who are in their 40 who are financially settled and can afford the big price of renting and who don't mind paying to try.
* Family who like to have a great fun together with the gadgets and parents who like to introduce Doraemon to their with their children to creating bonding in the family.
* Food reviewers who can just use our gadget to test million kind of food within short time span.
* Family who wants to bring their home content on holiday.

### First time user

* Simple and intuitive website navigation for easy exploration and discovery.
* Engaging visuals showcasing the cleverness of the gadgets and its usage.
* Informative content providing an overview of guideline usage and warning and age restriction.
* User-friendly forms with clear validation messages to ensure accurate input.
* Easy Registration process.

### Registered User

* Seamless login process with a secure and personalized user account.
* Browsing available gadgets
* Renting
* Access to a personalized dashboard displaying renting history and upcoming renting.
* Ability to easily modify or cancel existing renting for flexibility and convenience.

### Admin user

* Secure and separate login portal for admin users with appropriate access control.
* Access to an admin dashboard for managing customer profile, gadgets and rentings.
* Ability to add, edit, or delete gadget listings, including details and price.
* Managing minumum age usage for appropriate use.
* Ability to delete user accounts, providing the necessary control for managing user data and accounts.
* Management of renting, including the ability to view, modify, or delete rentings as needed.

## Design

DoraEx website brings nostalgic feeling to many people who grew up watching the series and dreamt of one day experiencing the gadgets. Doraemon blue and yellow colour of the bell were use as main theme to associate the hero character to design. The navigation bar features a simple DoraEx word with a touch of an addition of Doraemon iconic bell and easy-to-read text. Clear gadget picture depicting the look of the gadgets with the hero gadget being the first one user will see which is the Anywhere-door. All the form create subtle feeling with the colour usage and simple design. Social media links are presented in the footer to complements the overall design.

### Color Scheme
![Color Scheme](documentation/readme_images/colour_scheme.png)

### Typography

Space Mono is used as the main font throught use of Boostrap ready made template.

### Wireframes

<details>
<summary> Home Page on Mobile
</summary>

![Home Page](documentation/wireframes/home_page_mobile.png)
</details>

<details>
<summary> Multiple Pages on Mobile
</summary>

![Home Page when logged in](documentation/wireframes/multiple_page_mobile.png)
</details>

### Data Models

1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system
    * The User entity has a one-to-many relationship with the Renting entity. This means that a User can have multiple Rentings, but each Renting is associated with only one User.
---
2. Category Model
    * Category model associate with gadget model on  many to one basis. More than one gaget can belong to oen category
    * This allow gadget to be grouped and makes it easy to browse teh gadgets.
---
3. Customer Model
    * Customer model is related to user model on a one-to-one basis ehihc mean one user can only have one customer profile. 
    * The cusotmer in turn is related to gadgets and renting model on a one-to-many basis. Which mean one cusotmer can rent many gadget and have many renting. 
    * Admin can edit customer profile in case an id need to be provided to prove the custome's age and user can also edit their own profile.
    * The customer model allow cusotmer profiel creation for quick booking process as most field in booking form can be autofilled from teh customer existing detail in their customer profile and the detail can be edited.
---
3. Gadget Model
    * A Gadget can have multiple Rentings, but each Rentinging is associated with only one Gadget. This is represented by the foreign key relationship between Gadget and Renting.
    * Admin can add gadget through djangos admin panel.
    * Only Admin can change the data in the backend.
    * User can see the gadget information and image based on the chosen gadget.
    * Information provided is price, image, description, intended use, warning and minumum usage age.
---
4. Renting Model
    * A User can have multiple Rentings, but each Renting is associated with only one User. This is represented by the foreign key relationship between User and Booking.
    * Renting model has a feature to prevent under age renting thus making it safe.
    * Total price is also calculated in the backend that is then displayed to user to show the total price of the renting, depeding on the rent duration and quantity of each gadget rent.
    * Full CRUD functionality is available to the user.
    * User in order to rent has to fill start date, number of day rent and quanity of gadget.
    ---

### User Journey 

![User Journey](documentation/readme_images/user_journey.png)

### Database Scheme

Entity Relationship Diagram (ERD)

![DataScheme](documentation/readme_images/erd.png)

* The Customer entity represents customers that can be associated with renting, with fields id as the primary key. first_name for first anme, last_name for lst name, age for age and contact detail etc.
* The Category entity represents catergory to group gadget together with a field of category name.
* The Gadget entity represents individual gadget listings, with fields id as the primary key, name for the gadget's name, description for the gadget's description, price for the gadget's price, image for the gadget's image, minumun_use_age for age resitiction, and warning and inteded use for customer guideline.
* The Rentinging entity represents a renting made by a customer for a specific gadget, with fields id as the primary key, gadget as a foreign key referencing the Gadget entity, custoemr as a foreign key referencing the Customer entity, start_date for the renting start date, end_date for gadget return date, number_days_rent  for rent duration and total_price is calculate using a decorator function.

This data scheme allows for the management of users, customer, category, gadget, and retings. Users can make rentingings for specific gdgets, and each renting can have associated details such as the start_date, rent duration and quantity of gadget to rent.

## Security Features

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### Login Decorator

* renting_form, cart, rentign_edit_form,renting_delete and renting_confirm: These views involve operations related to user rentings and require authentication.
* This ensures that only authenticated users can access these views.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.

### Form Validation

* The renting_form and renting_edit_form view validates form input using the rentingForm class and rentingEditForm. It checks for various validation errors such as start date, quabity and furation that must not be negatice and datepicker provided for easy date pickin. Past date entering is also screened out and renting will therefor not register if past date is entered. 

### Underage Renting

* If customer wiht age less than the minimum usage age wants to rent teh gdaget the system will block the cusotmer form renting that gadget and not produce booling form when click but an error message instead.


## Features

* Home page showcases images of gadgets with short descriptions.
* User can make an account and login
* When logged in, users get access to the gaget overview and are only able to rent once creating customer profile.
* Users can edit and delete their rentings
* Every user action is accompanied by a corresponding message to ensure that users are promptly notified of any changes or updates.
* Total price of renting is displayed to users in the My Rented Gadget page.

### Existing Features

* Home Page
    * Displays a navigation bar with logo, main heading, category view, paginated gadget view, contact and footer with socials

![Home Page](documentation/readme_images/home_page.png)

* Once logged in the Register button change to logout and login change to profile registration. My Rented Gadget and customer profiel icon also appear.

![Logged In](documentation/readme_images/logged_in.png)


* Logo
    * Logo was made with simple word from the main font with an iconic Doraemon bell.

![Logo](documentation/readme_images/logo.png)

* Profile Registration
    * If user has yet to create their customer profile, when click on customer registration it will display a form to fill in but if user already have profile created then a message will pop up to day view and edit profile instead.

![Profile Registration no exiting profile](documentation/readme_images/profile_registration_new_customer.png)
![Profile Registration with existing profile](documentation/readme_images/profile_registration_exiting_customer.png)

* Amenities
    * Description of the amenities which user might like to experience.

![Amenities](documentation/readme_images/amenities.PNG)

* Cabin Carousel
    * When on home page there is a carousel that displays all available cabins for booking, it also has controls to move left or right, name and description of the cabin, when its clicked it redirects users to cabin overview page and visitors are asked to create an account or login in order to view the cabins in greater detail.

![Cabin Carousel](documentation/readme_images/carousel.PNG)

* About Section
    * It contains a short description of Woodland Whispers Retreat and a short lake tale

![About](documentation/readme_images/about.PNG)

* Footer
    * Contains copyright information, creator and social links which are all linked to the creator of the website, becuase purpouse of this website is educational.

![Footer](documentation/readme_images/footer.PNG)

* Contact Page
    * For educational purposes, the website includes fictional contact information such as an address, phone number, and email. It also includes social links, which are all linked to developer for educational purposes.

![Contact](documentation/readme_images/contact.PNG)

* Sign up
    * User can create an account

![Sign Up](documentation/readme_images/sign-up.PNG)

* Login
    * User can login into an account, if they have created one

![Login](documentation/readme_images/login.PNG)
![Login Message](documentation/readme_images/login-message.PNG)

* Browse Available Cabins
    * Admin can create cabins through django admin panel
    * Cabins are paginated to display 6 cabins per page

![Browse Cabins](documentation/readme_images/browse-cabins.PNG)

* Cabin pagination
    * On the bottom of the page

![Pagination](documentation/readme_images/pagination.PNG)

* Logout
    * User can logout

![Logout](documentation/readme_images/logout.PNG)

* Make a Booking
    * Users can make a booking by clicking the cabin they want and then read details and fill in the booking form.
    * Form validation is implemented to make sure form are submitted correctly and if there is an error user will be notified with alert message, also if everything is good, user gets a message to notifiy them.
    * Form contains amenities which are completely optional and they dont have to be selected.

    ![Message](documentation/readme_images/alert-message.PNG)

![Make a Booking](documentation/readme_images/make-a-booking.PNG)

* Booking Succesful
    * If booking is succesfull, user gets a notified message and an overview of the booking they just made, which includes all the details and a total price of the booking, also there is a button for contact page and my booking button that leads to all of the users bookings.

![Booking Succesful](documentation/readme_images/booking-successful.PNG)

* Booking Overview
    * Includes all of the user bookings, which have buttons to edit or delete bookings.

![Booking Overview](documentation/readme_images/my-bookings.PNG)

* Already booked dates
    * User won't be able to book dates that are already booked.
    * Dates in the past are unavailable.

![Booked Dates](documentation/readme_images/booked-dates.PNG)

* Edit Booking
    * User can change their booking and save changes

![Edit Booking](documentation/readme_images/edit-booking.PNG)

* Delete Booking
    * User can delete their booking, before it is deleted it has to be confirmed.

![Delete Booking](documentation/readme_images/delete-booking.PNG)

* Alert messages
    * For every action there is an alert message to notify user
    * Here is one example

![Alert Message](documentation/readme_images/delete-message.PNG)

* Admin Features
    * Django built in admin panel allows admin control over the website.
    * Admin can access admin panel through his navigation bar
    * Can add, update, delete cabins.
    * Create amenities, update existing amenities which are connected to the cabins.
    * Delete accounts, verifiy emails, delete bookings...

* Error Pages
    * There are custom 404 and 500 error pages set up.
    * They contain buttons to redirect to home page if there is an error.

![Error 404](documentation/readme_images/error.PNG)
![Error 500](documentation/readme_images/500-error-page.PNG)

### Features Left to Implement 

* User Reviews: Allow users to leave reviews and ratings for cabins they have booked, providing valuable feedback for other users.
* Advanced Search: Implement an advanced search functionality, enabling users to search for cabins based on specific criteria such as price range, amenities, and availability.
* Cabin Recommendations: Develop a recommendation engine that suggests cabins to users based on their previous bookings, interests, or preferences.
* Online Payment: Implement an online payment system to allow users to securely make payments for their bookings directly through the website.
* For the purposes of this project these implemenation were not necessary.

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

* [ElephantSQL](https://www.elephantsql.com/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework
* [Bootstrap 4.6.1](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - CSS framework

### Programs Used

* [Github](https://github.com/) - Storing the code online
* [Gitpod](https://www.gitpod.io/) - To write the code.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [Figma](https://www.figma.com/) - Used to create wireframes and schemes
* [Craiyon](https://www.craiyon.com/) - Generate AI images of cabins and logo based on my words descriptions
* [Am I Responsive](https://ui.dev/amiresponsive) - To show the website image on a range of devices.
* [Git](https://git-scm.com/) - Version control
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine
* [Favicon Generator](https://realfavicongenerator.net/) - Used to create a favicon
* [JSHint](https://jshint.com/) - Used to validate JavaScript
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python
* [Colormind](http://colormind.io/) - Color Scheme

## Deployment and Local Developement

Live deployment can be found on this [View Woodland Whispers Retreat live website here](https://woodland-whispers-retreat.herokuapp.com/)

### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
3. Click the fork button in the top right corner

#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### ElephantSQL Database
[Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat) is using [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database

1. Click Create New Instance to start a new database.
2. Provide a name (this is commonly the name of the project: tribe).
3. Select the Tiny Turtle (Free) plan.
4. You can leave the Tags blank.
5. Select the Region and Data Center closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary
[Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat) is using [Cloudinary](https://cloudinary.com/)
1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.



### Heroku Deployment
* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Prepare enviroment and settings.py
* In your GitPod workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* CLOUDINARY_URL - Insert your own Cloudinary API key
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1 - this is temporary, and can be removed for the final deployment
* DATABASE_URL - Insert your own ElephantSQL database URL here

#### Heroku needs two additional files to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

Site is now live

## Testing
Please see  [TESTING.md](TESTING.md) for all the detailed testing performed.

## References
### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
* [Cloudinary](https://cloudinary.com/documentation/diagnosing_error_codes_tutorial)
* [Google](https://www.google.com/)

### Content

* All of the content is imaginary and written by the developer, me, Thomas-Tomo Domitrovic.
* All images were generated with Artificial intelligence (AI) based on my word input and description of the cabins and logo.

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to the Slack community for their continuous engagement and willingness to share knowledge. The collaborative environment provided a platform for learning, troubleshooting, and gaining inspiration from fellow developers.

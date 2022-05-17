# Heather Hope Camping
Portfolio Project 4 Full Stack Toolkit - Code Institute
Find the app [here](https://heatherhope-camp.herokuapp.com/)

# About
The Heather Hope Campsite is a fictional campsite set in the vast expanse of the North York Moors, a place to go for respite from a busy life and adventure. Ever popular, the campsite requires an app with integrated booking service to manage bookings and avoid disappointment for customers. As the business is still expected to receive bookings traditionally via phone calls or "walk-ins" the booking service will still be manually administrated with regards to approvals for bookings.

Note all screen shots have been taken with the iPhone SE responsive sizer (from chrome) and 2560 x 1600 px as a standard 13" laptop screen.

# User Experience
The app will largely be managed by the campsite staff and thus has two main user perspectives: customers and the business.

## Business Goals
Heather Hope is a (fictional) campsite that can host a range of camping arrangements from tents to caravans, motorhomes or vans. The goal of building this booking service is to:
- provide potential customers with an indication of whether the site is available for the pitch type they require at the dates they desire
- keep track of their bookings
- begin building a consistent brand with themic styling

## User Goals
This site will be used by both business staff and customers thus must consider both perspectives.

From a business staff perspective, the site needs to:
- Allow staff to manually approve bookings and send an alert to the customer of the outcome
- Be able to edit the pitches available (both type and number)
- Be able to review bookings
- Be able to manually add bookings from walk-ins or mobile attempts

From a user perspective, the site needs to:
- Be easy to navigate
- Show availability of potential bookings
- Submit bookings for approval
- Review booking history
- Edit potential bookings
- Cancel potential bookings
- See contact information for the site
- See marketing material to help make the decision of whether they want to visit the site

A number of features are requried to carry out these needs and these will be discussed throughout this README.

## User Stories
This project has been tracked using [GitHub Projects](https://github.com/users/mmoore483/projects/2) which contains all the current user stories.


## Structure
Whilst the focus of this project is on the booking capability, the wireframes consider other elements of the user and business experience that may be implemented in the future.

<hr>

<strong>Home Page - Wireframe</strong>

The home page will be responsive with the top menu dropping into a hamburger icon on smaller screen sizes as well as a sticky nav bar to ensure the user can always get to the booking page within a single click. This navbar will be consistent across the entire site for ease of navigation. The "Log in" option on the menu will also update to "Sign Out" once a user is logged in. To achieve the desired look, bootstrap styling will be used. Other themic features include a hero image with a call to action button encouraging potential customers to book. This image can be used in other places (e.g. social media) to allow for brand building. Below that, there will be calls to visit the other marketing-type pages on the site including a photo library of facilities and views. 

![Home Page](READMEImages/WFHome.png)

<strong>Home Page - Actual</strong>
The current home page uses a beautiful image of heather on moorland, consistent with the name and location of the campsite. This image is used across the site for consistent styling and colours for the theme were taken from this image. The navbar is sticky and also collapses down on smaller screen sizes. 

In the future, the circular links to other pages will be included as those pages are developed - enough space has been left on the laptop views to make this look more appealing.

![Home Page Mobile](READMEImages/home-mobile.png)![Dropdown Menu](READMEImages/dropdown-menu-mobile.png) ![Home Page Laptop](READMEImages/home-laptop.png)

<strong>Log In/Sign Up/Sign Out - Intention</strong>

The user requires capability to sign up/log in so that they can make an account and manage their own bookings. Using an email address rather than a username should make it easier for users to remember their details for a site account that is likely to be rarely used. Additionally, the business can keep customer details on file in case of emergencies or last minute cancellations. The majority of the sign up and log in functionality will be achieved using the Django admin site and account templates with the same styling as other pages.
Note: the wireframe has been removed from the readme as I didn't feel it was adding anything: it was essentially a simple form, the same as the standard allauth template.

<strong>Log In/Sign Up/Sign Out - Actual</strong>
As desired, a custom model was created so that only email was required to create an account and sign in - not a username. The styling is the same as that of the rest of the site however there is an overlay with one of the accent colours

![login mobile](READMEImages/signin-mobile.png)
![logout mobile](READMEImages/signout-mobile.png)
![sign up mobile](READMEImages/signup-mobile.png)

<strong>Book - Wireframe</strong>

The booking page will be kept simple with the desire pitch type and dates (preferably with a date picker as this is a better visual for the user but can also restrict data entry). One the submission button has been pressed, the database will be queried and availability displayed back to the user.

![Booking Page Wireframe](READMEImages/WFBooking.png)

<strong>Book - Actual</strong>

The booking page has been kept simple however does not contain a date selector as desired during planning - this can be implemented at a later date. The form is simple and is designed with a secondary accent colour overlay for consistent styling. Prior to access to the booking form, a user must be signed in to ensure that any booking forms submitted could be tied to a customer which the business could contact if required. 

![Book but login first](READMEImages/book-loginfirst-mobile.png)
![Book](READMEImages/bookingform-mobile.png)


<strong>Photos</strong>

The photo page is for the business to entice customers with beautiful images of the campsite. The page layout is simple three column on large screens and one column on small screens. This is a nice-to-have feature that won't be a priority.

![Photo Page](READMEImages/WFPhotos.png)


<strong>Contact Us</strong>

The Contact Us Page is another form page that allows the user to make enquiries to the business easily. This is a simple form that will automate an email sent to the business and a copy of the email sent to the customer. 

![Conact Page](READMEImages/WFContactPage.png)

<hr>

### Database Planning

There needs to be a user table that will be used for account management and for the business to be able to contact customers. This table will contain all details about the customer from email, to name, to phone number etc. The only compulsory fields will be the auto-generated customer_id and the email address as this allows for a unique customer.

There needs to be an area to set business variables such as the different camping pitch types and the quantity of each. This is required to check there is availability. These will only be seen in the admin panel and can only be changed by "superusers" or administrators of the site. Therefore the table is not directly linked but will be queried to ensure that there is availability.

The final table is for the bookings themselves, this will tie in the customer_id where one customer can have multiple bookings however each booking can only have one customer. Therefore this is a one (customer_id) to many (Booking) relationship. The Booking table will also have a unique ID, this will also allow users to query the status of their booking in communication with the business. The booking also requires the pitch type and the dates at which the booking is expected to take place. The status will be pending if available, confirmed if accepted by the business administrators and cancelled if rejected or the user chooses to cancel their booking. Finally, the created_on field can be used to sort bookings so that the business administrators can accept bookings on a first-come-first-serve basis. 

![Database Diagram](READMEImages/DB-diagram.png)

<hr>

### Comment on Logic

1) The customer will fill in the booking form and press submit
2) The app will read in submitted information and filter the booking table by dates and pitch type
3) Using the customer requested pitch type, the Business Variables table will be queried for the quantity of that pitch type available
4) The number of results from step 2 will be compared to step 3 and if less, then the form will be saved to the database and the status will be set to pending. A notification should be displayed to the user that their booking is pending business confirmation. If the value is higher, then the customer will be told that the dates requested are unavailable and give them the option to try again.
5) The business user can then change the status and this will send a notification the customer account of the outcome. 

## Surface

The BootStrap Theme [scrolling nav](https://startbootstrap.com/template/scrolling-nav) has been adapted for use in this project and modified with standard bootstrap classes as well as unique styling.

The background image used in the site (beautiful healther in moorland) was found on [unsplash](https://unsplash.com/photos/f44QzL2ynzo?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink) and the colour theme was selected from this image using the colour picker tool on Chrome. The site's colour palette is comprised of a dark blue/black colour and a white shade as these colours provide the best contrast and have been used for text throughout the site. The purple/pink and green colour are used as accents and generally have been made more transparent in order to not detract from the background image. 

With regards to fonts, the cursive font of Arima Madurai is used to give visual appeal in main headings. The open sans font of Lato is easy to read and used for the majority of the site for that reason.

![colour palette](READMEImages/themecolours.png)

## Features
User Story | Ways in which met |
---|---|
Account Creation| An account can be created easily from the "Register" button featured on every page via the navbar. It is also accessible from the log in page and the booking page (providing you aren't already logged in).|
Create a Booking| Once authenticated, it is possible to make a booking using the booking form. There is also feedback of direction to a booking successful page or a note that those dates are unavailabe and to try again. However, it does require a datepicker as manual entry of dates is difficult and not user-friendly.|
Booking History| Once logged in, this feature is available on the navbar or you can choose to go to it from the booking successful page. It contains a table of all bookings the currently logged in user has made including the booking id (useful for referencing the booking if in contact with the Heather Hope Administration team), the pitch type, the dates selected and then an option to edit or delete the booking if they are in the future.|
Easy Navigation| The navigation bar is sticky in instances where the page gets long. On small screens, the navbar becomes collapsible to allow better use of screen real estate with other features however the Home button is always available. On every page of the site, the most relevant next link is available via buttons e.g. the booking success page directs to booking history or to return home. |
Creating a Brand| Across the site, a consistent image and colour scheme has been used. The cursive font used for the headings and "Welcome to Heather Hope Camping" text could easily be used to create a text logo of "Heather Hope" to be used across other media. The moorland image could also be used on the banner of a facebook page.|
Approve/Reject Bookings| At present this feature is only possible using the standard django administration back end. However, in the future, this should be improved to be accessible through the site itself if the user is authenticated as an administrator with a custom page to achieve this.|
Pitch Variation| The option of business variables e.g. pitch types and the number of each has been integrated into the model and the logic so these are editable in the django administration back end. However, in the future, this should be improved to be accessible through the site itself if the user is authenticated as an administrator. 
<hr>
<br>

## Other Features

Feature | Advantages |
---|---|



## Features Left to Implement

- Notification of booking status changes via email
- A Photo Page
- Business details available in the footer as well as a separate page
- A Contact Form that automates sending an email to business
- A date picker for the booking dates selection in Booking page
- The above date picker would block out unavailable dates visually during the selection process


## Testing

### Validator Testing
- HTML [W3C Validator](https://validator.w3.org/) No Errors on the Home, Log In, Register or Book pages.

- CSS [jigsaw validator](https://jigsaw.w3.org/css-validator/) No errors but some warnings about variable use.

- Python [PEP8 online validator](http://pep8online.com/) No errors beyond formatting.

### Bugs
- 

# Deployment

### Create Application and Postgres DB on Heroku
- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
- Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up. 
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

  - SECRET_KEY = os.environ.get('SECRET_KEY')

- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command python3 manage.py migrate 
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRET_KEY and DATABASE_URL and their values to env.py

### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/mmoore483/camping) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://heatherhope-camp.herokuapp.com/)

### Final Deployment steps
Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows:
- Set DEBUG flag to False in settings.py
- Ensure requirements.txt is up to date using the command pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch


## Forking

To trial changes to the site without affecting the original, the GitHub Repository can be forked.

- Log into GitHub and locate the desired repository
- In the top right, click the Fork button.

## Cloning

[Cloning](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) is useful for a multitude of reasons: to contribute to a project, to trial changes, to fix merge conflicts, add or remove files, and push larger commits.

- Log into your GitHub then find the gitpod repository
- Click the Code button
- If cloning with HTTPS, click the clipboard icon to copy the link
- Open Gitbash
- Change the current working directory to the location where you want the cloned directory to be.
- Type git clone, and then paste the URL you copied earlier.
- Press enter to create your local clone

# Credits

- Code Institute for the template and course content
- [BootStrap Theme](https://startbootstrap.com/template/scrolling-nav)
- The Very Academy YouTube for [videos](https://www.youtube.com/watch?v=Ae7nc1EGv-A&ab_channel=VeryAcademy) on creating administration panels
- [Background image](https://unsplash.com/photos/f44QzL2ynzo?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
- Coolors co for creation of the colour palette image
- LucidCharts for diagramming including the above database diagram
- Mentor: Brian Machari
- Tutor Support: James 
- Student Support: Kieron

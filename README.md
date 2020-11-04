## Milestone Project 4 - Full Stack Frameworks With Django

# Website for Wine Sales

#### This is an online wine sales website aimed at people who want to mail order one or more bottles of wine.


## User Stories

### Site Owner

- As the Site Owner I want my site to be responsive across multiple devices and operating systems so that I can reach the widest market/audience possible.

- As the Site Owner I want to present my wines to my customers via multiple categories so that my customers have more than one way to find wines they're interested in.

- As the Site Owner I want my customers to receive email confirmations about purchases and subscriptions so that they have confirmation outside of my site/system about what they have paid for.

- As the Site Owner I want **authenticated users** to be able to create new wine 'products' on the site via a form so that the correct information is loaded.

- As the Site Owner I want **authenticated users** to be able to edit wine 'products' on the site via a form so that the correct information is maintained and site users have the right information presented to them.

- As the Site Owner I want **authenticated users** to be able to delete wine 'products' from the site so that site users do not see products they cannot purchase.

- As the Site Owner I want Site Users to get on-screen feedback when they are completing their order details e.g. highlighted fields if compulsory information has not been provided, so that 
Site Users can immediately rectify their errors/ommissions and ensure submission of accurate customer purchasing data.


### Site Users

- As a **first time** Site User I want the site to be easy to use, easy to understand, and easy to navigate. In particular, I want it to be mobile or tablet friendly so that I can easily access it from any portable devices.

- As a **first time or returning** Site User I want to be able to view either a list of products or an individual product so that I can make purchasing decisions based on product details such as price, colour, etc.

- As a **first time or returning** Site User I want to be able to log in and out of a user profile so that I can view and manage anything personally relevant to me, such as orders, payments, reviews, my personal information.

- As a **first time or returning** Site User I want to be able to view wines by colour so that I may go straight to the category of my choice and save time on shopping.

- As a **first time or returning** Site User I want to be able to view wines by region of origin so that I may go straight to the category of my choice and save time on shopping.

- As a **first time or returning** Site User I want to be able to add one or more wines from the site to a shopping bag so that I may review my order then purchase them.

- As a **first time or returning** Site User I want to be able to edit one of more items in my shopping bag so that I may purchase the right set of wines and right number of wines.

- As a **first time or returning** Site User I want to be able to delete one or more items from my shopping bag so that I may purchase the right set and number of wines without having to begin my whole shopping process from scratch if I make a mistake.

- As a **first time or returning** Site User I want to be able to use a safe and secure payment method so that I can pay for my purchase without worrying that my card details might get stolen.

- As a **first time or returning** Site User I want to receive an emailed confirmation of my order so that I have confidence it was processed correctly through the website and have a record of my payment.

- As a **first time or returning** Site User I want to be able to access wines I have purchased through my profile so that I can write a review about them.

- As a **returning** Site User I want to be able to have access to current and past orders I have made so that I can be reminded about what I ordered and maybe choose the same wines again.

- As a **returning** Site User I want to be able to access a personalised user account so that I can recover my password if I forget it.


## Design

### Colour Scheme

The colour scheme is reminiscent of colours associated with red wine and dark bottles with associated imagery e.g. the background image.
All text on light backgrounds is black and all text on the dark backgrounds is white in order that each stand out.  
Page content buttons are a burgundy colour to associate them with red wine.

### Typography (font)

The fonts used for headings and buttons are Berkshire Swash and elsewhere Arial or Helvetica are used.  A backup font of either a generic cursive or sans serif font is used in case either of the former fonts is not imported correctly into the site for any user.
The special font chosen is clear and easy to read keeping accessibility in mind for users with visual impairments.

### Imagery

Images are loaded to Amazon Web Services. Images were found via Pixabay's open source option (the background image) or taken from Sainsbury's public grocery store.  Credits for images are listed in the "Credits" section below.


## Features

- The site has a responsive design for ease of use across a wide range of devices.

- The site also has an interactive design for both site owner and site users.


## Data Modelling

- I drafted an entity relationship diagram to map out the data model I originally wanted to achieve, including a number of additional models such as wine colours, wine origins, subscriptions, reviews.
Unfortunately I ran out of time to fully implement the "reviews" functionality and didn't get time to start a "subscriptions" functionality.
- [My data model is here](../blob/master/DataModel/ERD_updated.jpg)

## Wireframes

* Designs for the recipe book have been created for desktop and tablet to have the same layout and mobile phone devices to have a different layout.

### Desktop/tablet

- [Recipe Page Design](../blob/master/wireframes/Wireframe-DesktopTablet-recipeview.jpg)


### Mobile

- [Recipe Page Design](../blob/master/wireframes/Wireframe-Mobile-recipeview.jpg)


## Technologies Used

### Languages

* HTML5
* CSS
* Python
* Javascript and JQuery

### Frameworks, Libraries, and Programs

* Bootstrap and Font Awesome - these were used for the page layouts, app responsiveness across devices, buttons, and button icons
* Django - this is the database that holds the data about users, orders, wines
* Amazon Web Services Postgres database - this is the online server database holding static files such as media files (images) and css
* Google Fonts - this was used for styling the heading fonts
* Git and Github - these were used for keeping a remote backup of my work, for version control between my local files and remote files, and supported deployment to Heroku
* Microsoft Paint - this was used for drawing my wireframes 
* Heroku - this was used as the platform through which to deploy my app to share the finished product with other people
* Stripe - this is the payment mechanism used for my e-commerce site enabling users to checkout/make payments to buy the wines.

## Testing

### Testing Approach

1. Setup database and test connection through the addition and retrieval of some test data via IDE.
2. Create a Heroku app and test deployment.
3. Create the AWS server account and connection and test deployment of static files.
3. Build the remaining application in the IDE, test each slice of functionality, before backing up to Github and before deployment, at regular intervals.
4. Test responsiveness of the application on various devices.
5. Test the application on end users.

### Key Testing Results

1. During work on my database connection and deployment I found that I couldn't login to the system with the superuser I had created.  Initially this was due to creating the user before 
creating the user profiles app (my system threw an error due to the need for each data object to be related).  Subsequently I had a similar error when trying to login to my Heroku deployed 
app with my superuse account but this was due to my not setting up the Postgres database link properly using configuration variables.  A member of Tutor Support talked me through the process
and I was able to rectify the problem.

2. I created my Heroku app and set it so that it would receive automatic deployments from my Github repo.  Following the issues from my previous project I made sure I did not connect to Heroku
directly from Gitpod.  For this project my connection to Heroku via Github ran smoothly and following each push to Github, Heroku continued to update through automatic deployment.

3. Site Owner results

Super User account:
username - cjk2020
password - Codeinst2020

As the Site Owner I want my site to be responsive across multiple devices and operating systems so that I can reach the widest market/audience possible.
- I have tested this using Google Chrome's developer tools as well as checking the site on Mozilla Firefox and Microsoft Edge.  The site functioned the same across all browsers.

As the Site Owner I want to present my wines to my customers via multiple categories so that my customers have more than one way to find wines they're interested in.
- Wines are presented via 2 options: 1) by colour (red or white) and 2) by place of origin (e.g. Spain, Italy, etc).  Filtering through the navigation menu functions accurately.

As the Site Owner I want my customers to receive email confirmations about purchases and subscriptions so that they have confirmation outside of my site/system about what they have paid for.
- Email confirmations about purchases were not implemented due to running out of time.

As the Site Owner I want **authenticated superusers** to be able to create new wine 'products' on the site via a form so that the correct information is loaded.
As the Site Owner I want **authenticated superusers** to be able to edit wine 'products' on the site via a form so that the correct information is maintained and site users have the right information presented to them.
As the Site Owner I want **authenticated superusers** to be able to delete wine 'products' from the site so that site users do not see products they cannot purchase.
- As an authenticated superuser you can access the Product Management menu from the Account element on the navigation bar.  As a logged in shopper but not a superuser, you cannot.
In addition to being able to access this menu item an authenticated superuser can also see options to Edit or Delete a wine both on the All Wines page and on the Product Details page.

As the Site Owner I want Site Users to get on-screen feedback when they are completing their order details e.g. highlighted fields if compulsory information has not been provided, so that 
Site Users can immediately rectify their errors/ommissions and ensure submission of accurate customer purchasing data.
- When purchasing any wine a site user will see any fields highlighted in red that are compulsory but they have not filled in.  

4. Site User results

As a **first time** Site User I want the site to be easy to use, easy to understand, and easy to navigate. In particular, I want it to be mobile or tablet friendly so that I can easily access it from any portable devices.
- I was only able to test the site on one person.  He was able to easily navigate his way around the site, create an account and purchase wine.

As a **first time or returning** Site User I want to be able to view either a list of products or an individual product so that I can make purchasing decisions based on product details such as price, colour, etc.
As a **first time or returning** Site User I want to be able to view wines by colour so that I may go straight to the category of my choice and save time on shopping.
As a **first time or returning** Site User I want to be able to view wines by region of origin so that I may go straight to the category of my choice and save time on shopping.
- Feedback from my test user confirmed that it was easy to search by wine colour, origin or to use the search field in the navigation menu by entering keywords.

As a **first time or returning** Site User I want to be able to log in and out of a user profile so that I can view and manage anything personally relevant to me, such as orders, payments, reviews, my personal information.
As a **returning** Site User I want to be able to have access to current and past orders I have made so that I can be reminded about what I ordered and maybe choose the same wines again.
- My test user was able to create a profile, saving and updating his details as he wished.  He confirmed he could see the order he made as well as historical orders.

As a **first time or returning** Site User I want to be able to add one or more wines from the site to a shopping bag so that I may review my order then purchase them.
As a **first time or returning** Site User I want to be able to edit one of more items in my shopping bag so that I may purchase the right set of wines and right number of wines.
As a **first time or returning** Site User I want to be able to delete one or more items from my shopping bag so that I may purchase the right set and number of wines without having to begin my whole shopping process from scratch if I make a mistake.
- This functionality was tested by my test user as well as thoroughly tested by myself due to various bugs arising during the build.  My test user reported that he could do these things and see the expected changes to his shopping bag 
on screen.  I also logged into the Django database to check what had been recorded there.

As a **first time or returning** Site User I want to be able to use a safe and secure payment method so that I can pay for my purchase without worrying that my card details might get stolen.
- Stripe's "Test" data was used to test the payment functionality.  The processes worked as expected.

As a **first time or returning** Site User I want to receive an emailed confirmation of my order so that I have confidence it was processed correctly through the website and have a record of my payment.
- This functionality has not been implemented.  A user will receive an email though asking them to verify their email address when they sign up for an account.

As a **first time or returning** Site User I want to be able to access wines I have purchased through my profile so that I can write a review about them.
- This functionality has not been implemented (it has been started but not completed in time).

As a **returning** Site User I want to be able to access a personalised user account so that I can recover my password if I forget it.
- My test user changed his password successfully.

### W3C testing

All HTML and CSS tests passed.  
[W3C output](../blob/master/testing/W3C%20results.docx)


## Deployment

### Heroku

I deployed my project to Heroku as follows:

1. I signed up and created a new app in Heroku, giving it a name and choosing the region of Europe so that the app is delivered slightly more quickly than if I chose a server further away.  
2. In my app, under the Settings tab I included my configuration variables (in the Config Vars section).  This includes my IP address, Port number, AWS, STRIPE and EMAIL keys.  
3. I created a requirements.txt file for my application and updated it each time I installed a new app e.g. Stripe.  This file contains a list of applications needed for Heroku to run.
4. In my app, under the Deploy tab, I connected the app to my Github repository, enabling automatic deployments from my master branch.  I did not create any forks in Github.  Doing this enabled deployment directly from my code pushes to Github.
5. I ran a manual deployment (under the Deploy tab) and restarted dynos to see my first successful deployment.
6. I pushed my project files to Github regularly so that (a) my Github repository was kept up-to-date with my progress/changes, and (b) so that I deployed updates to my app regularly as I developed it through each stage.  I checked the Actions tab in Heroku to ensure the app was rebuilding when expected.  

To open my app from Heroku I logged in, went into the app I had created and in the top right-hand corner of the main section of the screen I clicked the "Open app" button.

### AWS Postgres

1. I signed up to the AWS free tier using a Europe (London) server location in order to have as reduced a system lag as possible when users retrieve data.
2. I selected and connected Amazon's s3 cloud service in which I created a 'bucket' into which my static resources were loaded.
3. I set the bucket policies to allow all site users to access the resources loaded so that users can see the images for example.  
4. I setup a user account to enable a superuser to manage my AWS account.  
5. I created an access policy for the user and downloaded access keys which I then added to Heroku Config Vars.
6. I configured Django to connect to s3 by installing boto3 and django-storages into my app, once again freezing requirements and updating my app settings.py file.  
7. All access keys are held in Heroku but referenced in my settings.py file - no actual keys shared in my settings.py file to make sure my system remains secure.
8. Finally, following the above I uploaded the relevant static and media files into AWS.

## Credits/Acknowledgements

### Credits

I credit the boutique-ado course example for being the learning basis of my e-commerce site and helping me step through its setup.

I credit Sainsbury's online grocery store for use of their images.

My thanks go out to my mentor Aaron Sinnott for his advice and assistance in the direction and breadth of my project.  
I also thank the tutors who've shared some inspirational resources and helped me work through various bug fixes.
My thanks also go out to the community on Slack.
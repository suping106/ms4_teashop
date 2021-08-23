## MS4 - Tea Shop ##
---
Tea Shop is a ecommence store for Tea lovers. The website was created by following the basic structure of Boutique Ado with two added models of customer reviews and FAQ.

The website can be access [here](https://ms4-teashop.herokuapp.com/)

## Project Summary
---
The goal of this project was to create a ecommence website where users can purchase  products in this online store. Users also have abilities to create an account, add, edit and delete products, write reviews and view FAQ.

## UX 
---

*User Stories*

**As a shopper I want to**
* View a list of products
* View a specific category of products
* View individual product details
* Quickly identify deals, clearance items and special offer
* Easily view the total of my purchases at anytime
* Sort the list of available products
* Sort a specific category of product 
* Sort multiple categories of products simultaneously
* Search for a product by name or description
* Easily see what I've searched for and the number of results 
* Easily select the quantity of a product when purchasing it
* View items in my bag to be purchased
* Adjust the quantity of individual items in my bag 
* Easily enter my payment information
* Feel my personal and payment information is safe and secure
* View an order confirmation after checkout
* Receive an email confirmation after checking out 
* View FAQ

**As a registered site user I want to**
* Easily register for an account
* Easily login or logout
* Easily recover my password in case I forget it 
* Receive an email confirmation after registering
* Have a personalized user profile

**As a site owner I want to**
* Easily add a product
* Easily edit and update a product
* Easily delete a product

## 5S's
---

*Strategy*

The goal is to create a ecommerce store for tea lovers to purchase tea products.

*Scope*

The overall look and feel of the website was similar to Boutique Ado with simple and easy use and navigation.

*Structure*

The website consists of the following:

**Home page**

Hero image serves as a open door as shoppers walk in to the store.
Navbar with product search function, login/signup account, and view to shopping bag as well as dropdown list to view products by category, type, price etc.
There is also FAQ in navbar.
Shop Now button brings shoppers to product page for shopping.

**Product Page**

Product page lists all products with image card and brief product info. By clicking product image brings the user to products detail page.

**Product Detail Page**

Product information is displayed here. User can select quantity and add the product to shopping bag.

User can also view the reviews other registered users put in. Registered users will have ability to add/edit/delete reviews they put in for the products.

**Shopping Bag Page**

User can view all products added in shopping bag before making a purchase.

**Checkout Page**

Page for user to enter name, email, shipping and payment information.

**Login/Signup Page**

Form for users to login if existing user or signup if new user.

**Profile Page**

For registered users, shows personal details and order history.

## Skeleton ##
---
**Wireframes**

Click[here](/assets/wireframes/MS4_wireframes.pdf) to open wireframes.

**Database Schema**

![here](/assets/data_schema/data_schema.png) 

## Surface ##
---
This website uses simple color scheme with black, white, and olive.

## Features ##
---
**Existing**

Navigation Bar

- Fixed navigation bar is visible on all pages with search form, account, shopping bag and site navigation links

Home Page

- Is styled using bootstrap for responsive design
- Fixed navbar 
- Shop Now button links to product page
- Toasts are used to display action info for user

Product Page

- Displays all product image cards with name and price info
- Product image links to product details page

Product Details Page

- Displays product details info and reviews
- Registered users have the option to add, edit or delete their reviews and give a rating to products through a modal input form

Shopping Bag
- Displays product(s) info in the shopping bag

Checkout Page
- Displays order summary 
- Input form for user input shipping and payment info 

Sign Up Page
- Input form for user to sign up

Sign In Page
- Input form for user to sign in

Profile Page
- Displays user's order history
- Input form for user to edit/update user info

product Management Page
- Input form for owner only to add new products

FAQs page
- Use Materialize collapsible feature to show questions and answers

**Future Improvement**

Due to the time constraints and the scope of the project I could not do too much to the project. That leaves lots of room for improvment. For the future I would like to add 
- More customized design to the project
- Add a contact form 
- Add a blog

## Technologies Used ##
---
Languages:
- HTML5 - define the structure and layout of the web page
- CSS3 - style the web document elements
- Javascript - implement Stripe and custom Javascript
- Python - write the project back-end functions
- Jinja - templating language for Python

Frameworks:
- [Django](https://www.djangoproject.com/) - high-level Python web framework used for the backend of the project
- [Bootstrap](https://getbootstrap.com/) - for the design of framework
- [Jquery](https://jquery.com/) - for implementation of Bootstrap

Storing/editing/deploying Code:
- [Gitpod](https://www.gitpod.io/) - project development environment
- [Github](https://github.com/) - host the project for software development version control using Git
- [Heroku](https://id.heroku.com/login) - for deploying the app to the cloud platform

Storage/Database:
- [Amazon Web Services](https://aws.amazon.com/) - store static and image files
- [Heroku Postgres](https://www.postgresql.org/) - for production database
- [SQlite3](https://www.sqlite.org/index.html) - for development database

Payment Handling:
- [Stripe](https://dashboard.stripe.com/login) - for secure payments

Other:
- [Google Fonts](https://fonts.google.com/) - for using the fonts in the project
- [Font Awesome](https://fontawesome.com/) - for using the icons in the project.
- [Balsamiq](https://balsamiq.com/) - for creating project wireframes

Testing tools 

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - for checking the responsiveness and debugging
- [Am I Responsive](http://ami.responsivedesign.is/) - for checking the responsiveness
- [W3C Markup Validation Service](https://validator.w3.org/) - is used to check HTML5 code
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/) - is used to check CSS3 code
- [JShint](https://jshint.com/) - is used to check JavaScript code.
- [PEP8](http://pep8online.com/) - is used to check Python code.

## Testing ##
---
**Responsiveness**

This website was tested on multiple mobile, tablet, laptop and desktop devices for responsiveness. 

![image](/assets/responsive/responsive_home.png)

![image](/assets/responsive/responsive_products.png)

![image](/assets/responsive/responsive_product_details.png)

![image](/assets/responsive/responsive_products_all_teapots.png)

![image](/assets/responsive/responsive_sign_in.png)

![image](/assets/responsive/responsive_sign_up.png)

![image](/assets/responsive/responsive_faq.png)

![image](/assets/responsive/ms4_responsive_faq2.png)

![image](/assets/responsive/ms4-responsive1.png) 

![image](/assets/responsive/ms4-responsive2.png) 

**Browser Compatibility**

Compatibility of the site was tested on Google Chrome, Microsoft Edge and Firefox.

![image](/assets/responsive/ms4-browser-compatibility.png) 

**Code Validation**

HTML code is validated through [W3 validator](https://validator.w3.org/nu/#textarea). Two errors were found. 

1. Error: Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.) 
2. Error: Duplicate ID

![image](/assets/validation/two_errors.png)

Both errors were corrected by adding ul and changed second ID value.

![image](/assets/validation/html_validation.png)

![image](/assets/validation/home_validation.png)

![image](/assets/validation/products_validation.png)

![image](/assets/validation/product_detail_validation.png)

![image](/assets/validation/product_add_validation.png)

![image](/assets/validation/product_edit_validation.png)

![image](/assets/validation/login_validation.png)

![image](/assets/validation/logout_validation.png)

![image](/assets/validation/profile_validation.png)

![image](/assets/validation/shoppin_bag_validation.png)

![image](/assets/validation/admin_validation.png)

CSS code is validated through [W3 validator](https://validator.w3.org/nu/#textarea). No error found.

![image](/assets/validation/css_validation.png)

base.css

![image](/assets/validation/base_css.png)

profile.css

![image](/assets/validation/profile_css.png)

checkout.css

![image](/assets/validation/checkout_css.png)

JavaScript code is validated through [JShint](https://jshint.com/). No error found.

![image](/assets/validation/jshint_js.png)

Python code is validated through [PEP8](http://pep8online.com/). No error found.


## Deployment ##
---
**Requirements**
- Python3
- Github account
- Heroku account
- Gitpod
- Stripe account
- AWS Amazon account
- Gmail account

**Clone the Project**
- Log in to GitHub
- Locate the project repository
- Click "Code" button
- Copy the link shown on the popup window under "Clone with HTTPS"
- In Gitpod teminal window make a new directory on your computer
- At the command promt type git clone and paste the copied link
- Press enter to create the local clone

**Working with Local Copy**
- Install all the requirements
- Create your own env.py file to store variables
- Add env.py to .gitignore file to keep it from being displayed publicly
- Migrate the models to create the database
- Load the categories data fixture first 
- then load the product data fixture
- then load faq data fixture
- Create a superuser
- Run the app by typing command: python3 manage.py runserver

**Heroku Deployment**
- Set up local workspace for Heroku
  - In terminal window of your IDE type: pip3 freeze -- local > requirements.txt 
  - Create a Procfile with the following text: web: gunicorn tea_shopwsgi:application
  - Push all these files to your GitHub reposity

- Set up Heroku
  - Create a Heroku account and create a new app and select your region.
  - Go to resources in Heroku and search for postgess. Select Hobby dev - Free and click on the provision button to add it to the project.
  - Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars and add the following config variables:

![image](/assets/variables/variable.png)

- Set up Database
  - Copy the DATABASE_URL (Postgres URL) from the config variables of Heroku and past it into the default database in setting.py
  - Migrate the models to create the database 
  - Load the data fixtures for categories, product and faq        
  - Create a superuser        
  - Set DATABASE_URL from settings.py back to original default DATABSE settings.
  - Adjust the ALLOWED_HOSTS to include Heroku app URL and localhost      
  - Push the code to Github.

- Connect with Heroku
  - Click on the Connect to GitHub section in the deploy tab in Heroku.
  - Search your repository to connect with it.
  - When your repository appears click on connect to connect your repository with the Heroku.
  - Set automatic deploment

**AWS S3**

The static and media files are hosted in the AWS S3 Bucket. 
- Create an account [here](https://portal.aws.amazon.com/billing/signup#/start)
- Create an S3 bucket and set a group, policy and user in the IAM environment 

Read more about the the S3 Bucket storage [here](https://aws.amazon.com/s3/). For more information about the storage in your project click [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).


## Credits ##
---
**Content/media**

All product images and product descriptions were downloaded online from various websites. 

**Code**

I have used the code from Code Institute Boutique Ado Project as a base of my project.

## Acknowledgments ##
---
I would like to thank my mentor Precious Ijege for his support, help, patience and encouragements. I am also grateful for the helps from tutors and slack members.



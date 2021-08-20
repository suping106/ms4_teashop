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

![here](/assets/images/data_schema.png) 

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
- Input form for owner to add new products

**Future Improvement**

Due to the time constraints and the scope of the project there's lots of room for improvment. For future features/improvement I would like to add 
- More customized design to the project
- Contact form 
- Blog

## Technologies Used ##

Languages:
- HTML5
- CSS3
- Javascript
- Python

Frameworks:
- Django
- Bootstrap
- Jquery

Storing/editing/deploying Code:
- Gitpod
- Github
- Heroku

Storage/Database:
- Amazon Web Services (to store static/image files)
- Heroku Postgres (for database)

Payment Handling:
- Stripe (for facilitating payments)

Other:
- Google Fonts
- Font Awesome









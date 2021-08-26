## Testing ##

**User Stories**

*As a shopper I want to*
- View a list of products
    - By clicking **Shop Now** in Home page a products page will open and show all the available products.
![image](/assets/user_stories/products.png)

- View a specific category of products
    - Navbar on each page provides shoppers access to different product categoies. By clicking on the dropdown menu shoppers will be able to view products in a specific category.
![image](/assets/user_stories/category_glass_teapots.png)

- View individual product details
    - By clicking a product image in products page will open a product detail page. Shoppers can view the product information such as price, description and reviews.    
![image](/assets/user_stories/product_detail.png)

- Quickly identify deals, clearance items and special offer
    - Navbar fixed on top of every page provides access to deals, clearance items and special offer.
![image](/assets/user_stories/navbar.png)

- Easily view the total of my purchases at anytime
    - A shopping bag fixed on each page provides the total purchases on top right hand corner.
![image](/assets/user_stories/shopping_bag_icon_w_total.png)

- Sort the list of available products
    - A sort dropdown box let shopper sort products
        - by name
![image](/assets/user_stories/sort_name.png)

        - by price
![image](/assets/user_stories/sort_price.png)

        - by category
![image](/assets/user_stories/sort_category.png)

        - by rating
![image](/assets/user_stories/sort_rating.png)

- Sort a specific category of product 
    - Shoppers can sort a specific category of product by clicking a specific category on navbar .
![image](/assets/user_stories/specific_category_sort.png)

- Sort multiple categories of products simultaneously
    - Shoppers can sort multiple categories of products simultaneously by clicking all products of each tea or teapots on navbar.
![image](/assets/user_stories/multi_category_sort.png)

- Search for a product by name or description
    - A search box is fixed on top of each page providing search function. 
![image](/assets/user_stories/search.png)

- Easily see what I've searched for and the number of results 
    - Search results are shown with number of the products found.
![image](/assets/user_stories/search_results.png)

- Easily select the quantity of a product when purchasing it
    - A quantity +/- box in product detail page and shopping bag page provide an easy way to add or reduct the quantity of the products.

![image](/assets/user_stories/quantity_box_detail.png)

- View items in my bag to be purchased
    - Shopping bag lists all the items shopper purchased with item name, quantity, price, subtotal, delivery cost and grand total.
![image](/assets/user_stories/checkout_total.png)

- Adjust the quantity of individual items in my bag 
    - Shopper can adjust the quantity of individual items in the shopping bag page either type in the quantity or use + / - arrows.
![image](/assets/user_stories/quantity_box_bag.png)

- Easily enter my payment information
    - Payment information can be easily entered through payment form provided on chechout page.
![image](/assets/user_stories/checkout_total.png)

- Feel my personal and payment information is safe and secure
    - Payment is handled by Stripe online payment platform which is safe and secure. 
![image](/assets/user_stories/checkout_payment.png)

- View an order confirmation after checkout
    - After checkout an order confirmation page will show the order info, order details, delivery and payment info. 
![image](/assets/user_stories/checkout_confirmation.png)

- Receive an email confirmation after checking out 
    - Email will send out to shopper after checking out.
![image](/assets/user_stories/order_confirmation_email.png)

- View other shopper's review
    - At the bottom of the product detail page shopper can view registered site user's review.
![image](/assets/user_stories/review.png)

- View FAQ
    - Navbar provides access to FAQ.
![image](/assets/user_stories/faq.png)

*As a registered site user I want to*
- Easily register for an account
    - Click **My Account** and select **Register** in Home page a user can easily register an account.
![image](/assets/user_stories/register_my_account.png)
![image](/assets/user_stories/sign_up.png)

- Easily login or logout
    - Click **My Account** and select **Login** in Home page a registered user can easily sign in to his/her account.
![image](/assets/user_stories/register_my_account.png)
![image](/assets/user_stories/sign_in.png)

    - Click **My Account** and select **Logout** in Home page to logout.
![image](/assets/user_stories/registered_my_account.png)
![image](/assets/user_stories/sign_out.png)


- Easily recover my password in case I forget it 
    - If registered user forgot the password his/her can reset the password by entering registered email address and received and email for resetting password.
![image](/assets/user_stories/password_reset.png)
![image](/assets/user_stories/password_reset_email_confirmation.png)
![image](/assets/user_stories/password_reset_email.png)

- Receive an email confirmation after registering
    - After registering user will receive a confirmation email.
![image](/assets/user_stories/signup_confirmation_email.png)

- Have a personalized user profile
    - A registered user can access user profile by clicking **My Account** and select **My Profile**. My profile page lists default delivery information (editable) and order history.
![image](/assets/user_stories/profile.png)

- Enter reviews for products
    - A registered user can add reviews to products in product detail page. **Review** button is available to registered user only. 
![image](/assets/user_stories/review.png)    
    - After clicking Review button a modal input form will popup for user to enter reviews and rating.
![image](/assets/user_stories/review_modal.png)

*As a site owner I want to*
- Easily add a product
    - A site owner can add a product through Product Management page by clicking **My Account** and selecting **Product Management**. 
![image](/assets/user_stories/product_management.png)

- Easily edit and delete a product
    - A site owner can edit and delete a product either through products page or product detail page.
![image](/assets/user_stories/owner_product_detail_page.png)
![image](/assets/user_stories/owner_products_page.png)

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

HTML code is validated through [W3 validator](https://validator.w3.org/nu/#textarea). Two types of error were found. 

1. Error: Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.) 
2. Error: Duplicate ID

![image](/assets/validation/two_errors.png)

![image](/assets/validation/faq_validation_error.png)

All errors were corrected. 

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

![image](/assets/validation/faq_validation_no_error.png)

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

##Bug Fixed##

Accordion on FAQ page was not working. Clicking one question all the answers opened up.

![image](/assets/responsive/ms4_responsive_faq2.png)

With tutor Michael's help by adding f.pk as unique id now accordion works properly. 

![image](/assets/responsive/responsive_faq.png)
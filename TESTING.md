
# DoraEx | Testing

Return to [README](README.md)
- - -
Comprehensive testing has been performed to ensure the website's seamless and optimal functionality.

## Table of Contents
### [Responsiveness Testing](#responsiveness-testing-1)
### [Code Validation](#code-validation-1)
* [HTML Validation](#html-validation)
* [CSS Validation](#css-validation)
* [JavaScript Validation](#javascript-validation)
* [Python](#python)
### [Lighthouse Report](#lighthouse-report-1)
### [Bugs](#bugs-1)
* [Resolved Bugs](#resolved-bugs)
### [Features Testing](#features-testing-1)
---

## Responsiveness Testing

The deployed website underwent rigorous testing on multiple devices and screen sizes to ensure its responsiveness and adaptability. Developer Tools were utilized to simulate various screen sizes, enabling thorough examination of how the website behaves across different devices. Bootstrap classes and media queries were implemented to achieve the desired design, ensuring that the website maintains its visual and functional integrity on all platforms, enhancing the user experience.

![Am I Responsive](documentation/readme_images/am_i_responsive.png)

## Browser Compatibility Testing

The project was tested on multiple web browsers to check for compatibility issues and ensure it functions as expected across all of them. This testing process guarantees a smooth and consistent user experience, regardless of the browser used.

## Device Testing

Device testing was conducted on a variety of phone models, including Samsung Galaxy A52, Oppo, iPhone 12, Huawei. The assistance of family members and friends was sought to perform the testing. This comprehensive approach ensured that the website was thoroughly evaluated on different devices and platforms, contributing to a more robust and user-friendly final product.

## Code Validation

### HTML Validation

<details>
<summary> Home Page
</summary>

![Home Page](documentation/validation/index_html_validation.png)
</details>

<details>
<summary> Contact Page
</summary>

![Contact Page](documentation/validation/contact_html_validation.png)
</details>

<details>
<summary> Sign Up Page
</summary>

![Sign Up Page](documentation/validation/signup_html_validation.png)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](documentation/validation/login_html_validation.png)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](documentation/validation/logout_html_validation.png)
</details>

<details>
<summary> Browse Gadget Page
</summary>

![Browse Gadgets Page](documentation/validation/category_html_validation.png)
</details>

<details>
<summary> Gadget View Page
</summary>

![Gadget View Page](documentation/validation/gadget_view_html_validation.png)
</details>

<details>
<summary> Renting Page
</summary>

![Renting Page](documentation/validation/renting_form_html_validation.png)
</details>

<details>
<summary> My Rented Gadget Page
</summary>

![My Rented Gadget Page](documentation/validation/cart_html_validation.png)
</details>

### CSS Validation

<details>
<summary> Custom CSS (style.css)
</summary>

![Custom CSS (custome_styles.css)](documentation/validation/custom_styles_css_validation.png)
</details>

### JavaScript Validation

<details>
<summary> Delete Edit Confirm Renting JavaScript
</summary>

![Delete Edit Confirm Renting](documentation/validation/rent_edit_confirm_delete_js_validation.png)
</details>

<details>
<summary> Profile Edit Javascript
</summary>

![Edit Customer Profile](documentation/validation/profile_edit_js_validation.png)
</details>

### Python

#### cabin_bookings app

<details>
<summary> admin.py
</summary>

![admin.py](documentation/validation/admin_py_validation.png)
</details>

<details>
<summary> forms.py
</summary>

![forms.py](documentation/validation/forms_py_validation.png)
</details>

<details>
<summary> models.py
</summary>

![models.py](documentation/validation/models_py_validation.png)
</details>

<details>
<summary> views.py
</summary>

![views.py](documentation/validation/views_py_validation.png)
</details>

<details>
<summary> urls.py
</summary>

![urls.py](documentation/validation/urls_py_validation.png)
</details>

## Lighthouse Report

<details>
<summary> Home Page
</summary>

![Home Page](documentation/lighthouse_report/home_page_lighthouse_desktop.png)
</details>

<details>
<summary> Gadget View Page
</summary>

![Gadget View Page](documentation/lighthouse_report/gadget_view_lighthouse_desktop.png)
</details>

<details>
<summary> Rent Page
</summary>

![Rent Page](documentation/lighthouse_report/rent_page_lighthouse_desktop.png)
</details>

<details>
<summary> My Rented Gadget Page
</summary>

![My Rented Gadget Page](documentation/lighthouse_report/cart_page_lighthouse_desktop.png)
</details>

<details>
<summary> Profile Page
</summary>

![Profile Page](documentation/lighthouse_report/profile_page_lighthouse_desktop.png)
</details>

## Bugs

### Resolved Bugs

#### URLs looping

 * In views I used return render to redirect url to a differnt view instend of using Httpresponse redirect and this created URLS looping where url keeps extending and was fixed by using Httpredirect where appropriate.

#### My Rented Gadget Table Heading

* The table heading remain static even when customer has no renting in the list and made the page look very messy. A conditional statement was added to html to check for renting count if non then hide and the bugs was resolved.

## Features Testing
 
| Page          | User Action   | Expected Result  | Notes            |
|---------------|---------------|------------------|------------------|
| Home Page     |               |                  |                  |
|               | Click on Logo | Redirect to Home Page | PASS        |
|               | Click on Sign Up button | Redirect to Sign Up page | PASS |
|               | Click on Sign Up button (Navigation bar) | Redirect to Sign Up page | PASS |
|               | Click on  Category(Navigation bar) | Display category options | PASS |
|               | Click on  Contact| Redirect to contanctpage | PASS |
|               | Click on view on gadget card | Redirect to gadget view | PASS |
|               | Click on social links in footer | Open new tab with appropriate link | PASS |
|               | Click on Logout (Navigation bar) | Redirect to Logout page | PASS |
|               | Click on Login (Navigation bar) | Redirect to Login page | PASS |
| Home Page (Logged In - User)  |                 |          |  |
|               | After Login | Profile Registration, My Rented Gadget and Profiel Icon appear | PASS |
|               | Click View | Redirect to Gadget view and rent button appear | PASS |
|               | Click on Profile Registration | Redirects to profile registration page | PASS |
|               | Click on Rent | Redirects to Rent form if user already have customer profile if not redirects to profile registration pagethenonce complete back to rent form for chosen gadget | PASS |
|               | Click on Profile Icon | If alredy have profile then can edit otherwise refirect to profile registration page with error message  | PASS |
|               | Click on Logout | Redirect to Logout Page | PASS |
| Contact Page     |               |                  |                  |
|               | Click on social links | Open new tab with appropriate link | PASS |
| Sign Up Page  |                  |                  |                  |
|               | Enter invalid email | Field will only accept email address format | PASS |
|               | Enter valid email | No error | PASS |
|               | Email field left empty | Email is optional | PASS |
|               | Type invalid password | Must contain atleast 8 char | PASS |
|               | Type valid password | No error | PASS |
|               | Type password again (different) | Password must be the same | PASS |
|               | Click Sign Up with empty form | Fill in the form fields | PASS |
|               | Click Sign In if you have an account | Redirect to Login page | PASS |
|               | Fill all the form fields | Account created, alert message that you Signed in | PASS |
| Login Page  |                  |                  |                  |
|               | Click on Sign Up, if you don't have an account | Redirect to Sign Up page | PASS |
|               | Try exssting Username | Username alreday exist | PASS |
|               | Try invalid password | Password is not correct | PASS |
|               | Valid password and username | Logs in, message that you signed in | PASS |
|               | Click Sign In with empty form | Fill in the form fields | PASS |
| Logout Page  |                  |                  |                  |
|               | Click on Sign Out button | Sign user out, message that user signed out | PASS |
| Browse Gadget Page  |                  |                  |                  |
|               | Click on Rent on gadget view page | Redirects to renting form for that gadget| PASS |
|               | Click on Next button | Moves to another page, displays different set of gadgets | PASS |
|               | Click on Previous button | Goes back to previous page | PASS |
| Make a Renting Page  |                  |                  |                  |
|               | Click on Add To Cart button while form is empty | Fill in the form fields, alert message | PASS |
|               | Try to rent with profile of underage | error messge dispaly stop the user from renting the gadget | PASS |
|               | Try input negative number of rent duration and quanity | Rent not registered | PASS |
| Renting Succesful Page |  |    |    |
|               | View rented gadget | Rented gadget appear in the my rented gadget list with option to delete, edit and confirm | PASS |
|               | Read the renting details | Details are as expected, match users renting | PASS |
|               | Total price check | Total price is calculated correctly | PASS |
|               | Click on delete button | messgae display wanrning | PASS |
|               | Click on edit button | an edit form appear with prefilled detail | PASS |
|               | Click on confirm button | message display reminding that once confimed rent can no longer be amended and shipping will begin | PASS |
| Edit Renting Page |  |    |    |
|               | Read the renting ID number | It displays correct ID number of chosen renting user wants to edit | PASS |
|               | Try leaving the field blank and click update | Error message display | PASS |
| Delete Renting Page |  |    |    |
|               | Read the booking ID number | It displays correct ID number of chosen renting user wants to delete | PASS |
|               | Click on Confirm Delete button | Booking is deleted, alert message | PASS |
|               | Click on Cancel button | Redirect back to top of My Rented Gadget page| PASS |
| Confirm Renting Page |  |    |    |
|               | Click on Confirm Confirm button | Renting is conmfirmed, alert message and all actions button assocaite with the rent disappear | PASS |
|               | Click on Cancel button | Redirect back to top of My Rented Gadget page | PASS |
| Profile Page |  |    |    |
|               | Read the customer detail entred | Detail display as of the detail enterd in profile registration and edit button available | PASS |
|               | Click on Edit button| Profile Edit form appear with prefilled of exisitng detail | PASS |
|               | Click Update button| Profle detail reflect new change and message display succesful updating | PASS |
| Admin Panel |  |    |    |
|               | CRUD functionality | Working as expected | PASS |

Return to [README](README.md)

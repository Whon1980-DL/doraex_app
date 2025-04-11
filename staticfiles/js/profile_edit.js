const editButton = document.getElementById("editButton");
const firstNameText = document.getElementById("id_first_name");
const lastNameText = document.getElementById("id_last_name");
const ageText = document.getElementById("id_age");
const phoneText = document.getElementById("id_phone");
const emailText = document.getElementById("id_email");
const shippingAddressText = document.getElementById("id_shipping_address");
const profileEditForm = document.getElementById("profileEditForm");
const profileEditFormHolder = document.getElementById("profile-edit-form-holder")
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated customer's ID upon click.
* - Fetches the content of the corresponding customer detail.
* - Populates the various Text input/textarea with the customer detail'scontent for editing.
* - Sets the form's action attribute to the `edit_profile/{commentId}` endpoint.
*/
editButton.addEventListener("click", (e) => {
    let customerId = e.target.getAttribute("data_customer_id");
    profileEditFormHolder.classList.remove("d-none");
    let firstNameContent = document.getElementById("first_name").innerText;
    firstNameText.value = firstNameContent;
    let lastNameContent = document.getElementById("last_name").innerText;
    lastNameText.value = lastNameContent;
    let ageContent = document.getElementById("age").innerText;
    ageText.value = ageContent;
    let phoneContent = document.getElementById("phone").innerText;
    phoneText.value = phoneContent;
    let emailContent = document.getElementById("email").innerText;
    emailText.value = emailContent;
    let addressContent = document.getElementById("shipping_address").innerText;
    shippingAddressText.value = addressContent;
    profileEditForm.setAttribute("action", `edit_profile/${customerId}`);
  });



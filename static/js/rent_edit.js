const editButtons = document.getElementsByClassName("btn-edit");
const rentingQuantityText = document.getElementById("id_quantity");
const rentingStartDateText = document.getElementById("id_start_date");
const rentingDurationText = document.getElementById("id_number_days_rent");
const rentingEmailText = document.getElementById("id_email");
const rentingPhoneText = document.getElementById("id_phone");
const rentingAddressText = document.getElementById("id_address");
const rentEditForm = document.getElementById("rentEditForm");
const submitButton = document.getElementById("submitButton");

const confirmModal = new bootstrap.Modal(document.getElementById("confirmModal"));
const confirmButtons = document.getElementsByClassName('btn-confirm')
const rentConfirm = document.getElementById("rentConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let rentingId = e.target.getAttribute("renting_id");
    rentEditForm.classList.remove("d-none");
    let rentingQuantityContent = document.getElementById(`quantity${rentingId}`).innerText;
    rentingQuantityText.value = rentingQuantityContent;
    let rentingStartDateContent = document.getElementById(`start_date${rentingId}`).innerText;
    rentingStartDateText.value = rentingStartDateContent;
    let rentingDurationContent = document.getElementById(`number_days_rent${rentingId}`).innerText;
    rentingDurationText.value = rentingDurationContent;
    let rentingEmailContent = document.getElementById(`email${rentingId}`).innerText;
    rentingEmailText.value = rentingEmailContent;
    let rentingPhoneContent = document.getElementById(`phone${rentingId}`).innerText;
    rentingPhoneText.value = rentingPhoneContent;
    let rentingAddressContent = document.getElementById(`address${rentingId}`).innerText;
    rentingAddressText.value = rentingAddressContent;
    submitButton.innerText = "Update";
    rentEditForm.setAttribute("action", `edit_renting/${rentingId}`);
  });
}

for (let button of confirmButtons) {
  button.addEventListener("click", (e) => {
  let rentingId = e.target.getAttribute("renting_id");
  rentConfirm.href = `confirm_renting/${rentingId}`;
  confirmModal.show();
  });
}
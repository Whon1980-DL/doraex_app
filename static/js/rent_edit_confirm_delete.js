const editButtons = document.getElementsByClassName("btn-edit");
const rentingQuantityText = document.getElementById("id_quantity");
const rentingStartDateText = document.getElementById("id_start_date");
const rentingDurationText = document.getElementById("id_number_days_rent");
const rentingEmailText = document.getElementById("id_email");
const rentingPhoneText = document.getElementById("id_phone");
const rentingAddressText = document.getElementById("id_address");
const rentEditForm = document.getElementById("rentEditForm");
const submitButton = document.getElementById("submitButton");
const rentingIdText = document.getElementById("rentingIdValue");

const confirmModal = new bootstrap.Modal(document.getElementById("confirmModal"));
const confirmButtons = document.getElementsByClassName('btn-confirm')
const rentConfirm = document.getElementById("rentConfirm");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated renting's ID upon click.
* - Fetches the content of the corresponding renting detail.
* - Populates the various input/textarea with the renting detail content for editing.
* - Sets the form's action attribute to the `edit_renting/{rentingId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let rentingId = e.target.getAttribute("data_renting_id");
    rentEditForm.classList.remove("d-none");
    let rentingIdContent = rentingId;
    rentingIdText.innerHTML = rentingIdContent; 
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

/*
 * Initializes confirmation functionality for the provided confirm buttons.
 * 
 * For each button in the `confirmButtons` collection:
 * - Retrieves the associated renting's ID upon click.
 * - Updates the `rentConfirm` link's href to point to the 
 * confirmation endpoint for the specific comment.
 * - Displays a confirmation modal (`confirmModal`) to prompt 
 * the user for confirmation before confirming.
 */
for (let button of confirmButtons) {
  button.addEventListener("click", (e) => {
  let rentingId = e.target.getAttribute("data_renting_id");
  rentConfirm.href = `confirm_renting/${rentingId}`;
  confirmModal.show();
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated renting's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific renting.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let rentingId = e.target.getAttribute("data_renting_id");
    deleteConfirm.href = `delete_renting/${rentingId}`;
    deleteModal.show();
  });
}
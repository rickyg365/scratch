function validateForm() {
    // Use name attr to reference form elements not id.
    let current_form = document.forms["myForm"];
    let first_name = current_form["fname"].value;
    let text_area = current_form["message"].value;
    let simp_select = current_form["items"].value;
    let mult_select = current_form["multi_items"].value;
    let data_list = current_form["dataList"].value;

    if (first_name == "") {
      alert("Name must be filled out");
      return false;
    }
    if (text_area == "Please input message...") {
        alert("Text Area must be filled out");
        return false;
    }
    if (simp_select == "") {
        alert("Select Simple must choose an option");
        return false;
    }
    if (mult_select == "") {
        alert("Select Multiple must choose at least one");
        return false;
    }
    if (data_list == "") {
        alert("DataList must not be empty");
        return false;
    }

  }

function alertReset() {
    alert("Form has been reset!");
}
function validationForm() {
    let name = document.forms["myForm"]["name"].value

    let age = document.forms["myForm"]["age"].value

    if (name == '' || name == '-') {
        alert("Name must be filled out")
    }

    if (age == '' || age == '-' < 10) {
        alert("Age must be filled out")
    }
}
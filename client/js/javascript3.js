function removeHelpPatient(){
    document.getElementById('invalidPatientName').style.display='none'

    document.getElementById('invalidPatientContact').style.display='none';
    document.getElementById('invalidPatientCity').style.display='none';
    document.getElementById('invalidPatientEmail').style.display='none';
    document.getElementById('invalidPatientPassword').style.display='none';
    document.getElementById('invalidPatientAge').style.display='none';
    document.getElementById('invalidPatientGender').style.display='none';
    document.getElementById('passwordPatientNotMatch').style.display='none';
};
function removeHelpDoctor(){

    document.getElementById('invalidDoctorName').style.display='none';
    document.getElementById('invalidDoctorContact').style.display='none';
    document.getElementById('invalidDoctorCity').style.display='none';
    document.getElementById('invalidDoctorEmail').style.display='none';
    document.getElementById('invalidDoctorPassword').style.display='none';
    document.getElementById('invalidDoctorIMR').style.display='none';
    document.getElementById('passwordDoctorNotMatch').style.display='none';
};
function removeForms(){
    document.getElementById("signUpFormDoctor").style.display='none';
    document.getElementById("signUpFormPatient").style.display='none';
}

$("#signUpFormType").on('submit', (e) => {
    e.preventDefault();

    // FETCH DATA FROM DOM
    data = $('#signUpFormType').serializeArray();

    // REMOVE EXISTING FORMS
    removeForms();

    // DISPLAY CORRESPONDING FORM
    if (data[0]["value"] == "Doctor") {
        document.getElementById("signUpFormDoctor").style.display='block';
    } else {
        document.getElementById("signUpFormPatient").style.display='block';
    }
});

$("#signUpFormPatient").on('submit', (e) => {
    e.preventDefault();

    // FETCH DATA FROM DOM
    const data = $('#signUpFormPatient').serializeArray();
    const utc = new Date().toJSON().slice(0,10).replace(/-/g,'-');
    credentials = {"date" : utc};
    for (let i = 0; i < data.length; ++i) {
        if (data[i]["name"] != "password2")
        credentials[data[i]["name"]] = data[i]["value"];
    }
    console.log(credentials);
    $.ajax({
        type: 'POST',
        url: 'http://localhost:5000/register/patient',
        data: JSON.stringify(credentials),
        success: (r) => {
            console.log('HERE', r)
            location.href = "http://127.0.0.1:5500/pages/success.html";
        }
        , error: console.log,
        contentType: "application/json",
        dataType: 'json'
    });
});

$("#signUpFormDoctor").on('submit', (e) => {
    e.preventDefault();

    // FETCH DATA FROM DOM
    const data = $('#signUpFormDoctor').serializeArray();
    const utc = new Date().toJSON().slice(0,10).replace(/-/g,'-');
    credentials = {"date" : utc,"verified": "F"};
    for (let i = 0; i < data.length; ++i) {
        if (data[i]["name"] != "password2")
        credentials[data[i]["name"]] = data[i]["value"];
    }
    console.log(credentials);
    $.ajax({
        type: 'POST',
        url: 'http://localhost:5000/register/doctor',
        data: JSON.stringify(credentials),
        success: (r) => {
            window.location.href = "http://127.0.0.1:5500/pages/success.html";
        }
        , error: console.log,
        contentType: "application/json",
        dataType: 'json'
    });
});



function signUpReset() {
    document.getElementById("signUpFormDoctor").reset();
    document.getElementById("signUpFormPatient").reset();
    document.getElementById("signUpFormType").reset();
}

function togglePassword1Doctor() {
    a=document.getElementById('signUpPass1Doctor').type
    if(a=='password'){
        document.getElementById('signUpPass1Doctor').type='text';
    }
    else{
        document.getElementById('signUpPass1Doctor').type='password';
    }
    document.getElementById("eye-1-doctor").classList.toggle('bi-eye');
};

function togglePassword1Patient() {
    a=document.getElementById('signUpPass1Patient').type
    if(a=='password'){
        document.getElementById('signUpPass1Patient').type='text';
    }
    else{
        document.getElementById('signUpPass1Patient').type='password';
    }
    document.getElementById("eye-1-patient").classList.toggle('bi-eye');
};

function togglePassword2Doctor() {
    a=document.getElementById('signUpPass2Doctor').type
    if(a=='password'){
        document.getElementById('signUpPass2Doctor').type='text';
    }
    else{
        document.getElementById('signUpPass2Doctor').type='password';
    }
    document.getElementById("eye-2-doctor").classList.toggle('bi-eye');
};

function togglePassword2Patient() {
    a=document.getElementById('signUpPass2Patient').type
    if(a=='password'){
        document.getElementById('signUpPass2Patient').type='text';
    }
    else{
        document.getElementById('signUpPass2Patient').type='password';
    }
    document.getElementById("eye-2-patient").classList.toggle('bi-eye');
};


function validateCredentials(credentials){
    const textPattern=/^[a-zA-Z ]{2,30}$/;
    const contactPattern=/^\d{10}$/;
    const emailPattern=/^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    const passwordPattern=/^[a-zA-Z0-9!@#\$%\^\&*_=+-]{6,10}$/;
    if (!(credentials["name"].match(textPattern))){
        document.getElementById('invalidName').style.display='block';
    }
    else if (!(credentials["contact"].match(contactPattern))){
        document.getElementById('invalidContact').style.display='block';
    }
    else if (!(credentials["city"].match(textPattern))){
        document.getElementById('invalidCity').style.display='block';
    }
    else if (!(credentials["email"].match(emailPattern))){
        document.getElementById('invalidEmail').style.display='block';
    }
    else if (!(credentials["password1"].match(passwordPattern))){
        document.getElementById('invalidPassword').style.display='block';
    }
    else if (credentials["password1"] != credentials["password2"]){
        document.getElementById('passNotMatch').style.display='block';
    }
    else {
        console.log(credentials)
    }
}

removeHelpDoctor();
removeHelpPatient();
removeForms();
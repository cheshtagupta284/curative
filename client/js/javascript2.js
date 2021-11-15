removeHelp();
function removeHelp() {
  // REMOVE THE HELP TEXT FROM THE FORM
  document.getElementById("invalidpassword").style.display = "none";
  document.getElementById("invalidemail").style.display = "none";
}

function signInLogin() {
  event.preventDefault();
  // RETREIVE INPUT VALUES

  const Email = document.getElementById("loginEmail").value;
  const Password = document.getElementById("loginPassword").value;
  const Remember_me = document.getElementById("loginCheckbox").checked;
  const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  const passwordPattern = /^[a-zA-Z0-9!@#\$%\^\&*_=+-]{6,10}$/;

  // REMOVE HELP TEXT FROM DOM
  removeHelp();

  // VALIDATE
  if (!Email.match(emailPattern)) {
    document.getElementById("invalidemail").style.display = "block";
  } else if (!Password.match(passwordPattern)) {
    document.getElementById("invalidpassword").style.display = "block";
  } else {
    const credentials = {
      email: Email,
      password: Password,
    };
    console.log(credentials);
    removeHelp();
  }
}

loginTogglePassword.addEventListener("click", function (e) {
  a = document.getElementById("loginPassword").type;
  if (a == "password") {
    document.getElementById("loginPassword").type = "text";
  } else {
    document.getElementById("loginPassword").type = "password";
  }
  this.classList.toggle("bi-eye");
});

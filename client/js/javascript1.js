let user = null;
removeHelp();

const func = function (token) {
  var base64Url = token.split(".")[1];
  var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
  var jsonPayload = decodeURIComponent(
    atob(base64)
      .split("")
      .map(function (c) {
        return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
      })
      .join("")
  );

  return JSON.parse(jsonPayload);
};

function removeHelp() {
  // REMOVE THE HELP TEXT FROM THE FORM
  document.getElementById("invalidPassword").style.display = "none";
  document.getElementById("invalidEmail").style.display = "none";
}

$("#loginMainForm").on("submit", async (e) => {
  e.preventDefault();
  let token = null;
  let credentials = {};
  const data = $("#loginMainForm").serializeArray();

  for (let i = 0; i < data.length; ++i) {
    credentials[data[i].name] = data[i]["value"];
  }

  await $.ajax({
    type: "POST",
    url: "http://localhost:5000/doctor/login",
    data: credentials,
    success: (r) => {
      token = r.token;
    },
    error: console.log,
  });

  user = token ? func(token).user : user;
  document.querySelector(".dashboard").textContent = JSON.stringify(user);
  document.querySelector(".loginPage").style.display = "none";
});

const loginTogglePassword = () => {
  a = document.getElementById("loginPassword").type;
  if (a == "password") {
    document.getElementById("loginPassword").type = "text";
  } else {
    document.getElementById("loginPassword").type = "password";
  }
  document.getElementById("loginTogglePassword").classList.toggle("bi-eye");
};

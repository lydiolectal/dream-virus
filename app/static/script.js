// validate well-formedness of email input
function verifyEmail() {
    const email = document.getElementById("email-field");
    const error = document.getElementById("error-email");
    if (email.validity.valueMissing) {
        console.log("empty!")
        error.innerHTML = "Please enter an email address";
      }
    else if (email.validity.patternMismatch) {
        console.log("not properly formatted")
        error.innerHTML = "Please enter an email address";
      } 
    else {
        console.log("The email is", email.value);
        error.innerHTML = "Email has been sent!";
        sendLoginEmail(email.value);
      }
}

// send out authentication email
function sendLoginEmail(email) {
  try {
    const url = `${document.location.protocol}//${document.location.host}/email-redirect`;
    console.log(url)
    var actionCodeSettings = {
      // URL you want to redirect back to. The domain (www.example.com) for this
      // URL must be whitelisted in the Firebase Console.
      url: url,
      // This must be true.
      handleCodeInApp: true,
    };

    firebase.auth().sendSignInLinkToEmail(email, actionCodeSettings);
  } catch(error) {
    console.error(error);
    throw error;
  }
}

// validate and authenticate email to complete login
function completeLogin() {
  const email = document.getElementById("email-field");
  const error = document.getElementById("error-email");
  if (email.validity.valueMissing) {
      console.log("empty!")
      error.innerHTML = "Please enter an email address";
    }
  else if (email.validity.patternMismatch) {
      console.log("not properly formatted")
      error.innerHTML = "Please enter an email address";
    } 
  else {
      console.log("The email is", email.value);
      error.innerHTML = "Verifying...";
      authenticateEmail(email.value);
    }
}

// authenticates login from email link 
function authenticateEmail(email) {
// Confirm the link is a sign-in with email link.
if (firebase.auth().isSignInWithEmailLink(window.location.href)) {
  firebase.auth().signInWithEmailLink(email, window.location.href)
    .then(function(result) {
      // Clear email from storage.
      window.localStorage.removeItem('emailForSignIn');
      // grab the rest of dream submission form from flask
      $.get("/_signin")
        .done(function(response) {
          window.location.replace("/dream-form");
        })
        .catch(function(error){
          console.log("error logging in with email", error);
          window.location.replace("/access-denied");
        })
    })
    .catch(function(error) {
      console.log("error authenticating email with firebase", error);
      // errorElement.innerHTML = `Not authorized; try signing in <a href="/submit">here</a>`;
      window.location.replace("/access-denied");
      // Some error occurred, you can inspect the code: error.code
      // Common errors could be invalid email and invalid or expired OTPs.
    });

} else {
      console.log("email not authenticated through firebase", error);
      window.location.replace("/access-denied");
}
}

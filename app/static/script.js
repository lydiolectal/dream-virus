// validate well-formedness of email input
function verifyEmail() {
    const email = document.getElementById("email");
    if (email.validity.valueMissing) {
        email.setCustomValidity("Please enter an email address.");
      }
    else if (email.validity.patternMismatch) {
        email.setCustomValidity("Please enter an email address.");
      } 
    else {
        email.setCustomValidity("");
        sendLoginEmail(email.value);
      }
}

// send out authentication email (https://firebase.google.com/docs/auth/web/email-link-auth)
function sendLoginEmail(email) {
  try {
    var actionCodeSettings = {
      // URL you want to redirect back to. The domain (www.example.com) for this
      // URL must be whitelisted in the Firebase Console.
      url: "https://nightpoems.com",
      // This must be true.
      handleCodeInApp: true,
    };

    firebase.auth().sendSignInLinkToEmail(email, actionCodeSettings);
  } catch(error) {
    console.error(error);
    throw error;
  }
}
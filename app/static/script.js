// validate well-formedness of email input
function verifyEmail() {
    const email = document.getElementById("email");
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
    // const url = document.location.href;
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

// TODO: figure out how to call this when user is taken to /email-redirect
function redirectLoginEmail() {
  // Confirm the link is a sign-in with email link.
if (firebase.auth().isSignInWithEmailLink(window.location.href)) {
  // Get the email if available. This should be available if the user completes
  // the flow on the same device where they started it.
  var email = window.localStorage.getItem('emailForSignIn');
  if (!email) {
    // User opened the link on a different device. To prevent session fixation
    // attacks, ask the user to provide the associated email again. For example:
    email = window.prompt('Please provide your email for confirmation');
  }
  // The client SDK will parse the code from the link for you.
  firebase.auth().signInWithEmailLink(email, window.location.href)
    .then(function(result) {
      // Clear email from storage.
      window.localStorage.removeItem('emailForSignIn');
    })
    .catch(function(error) {
      // Some error occurred, you can inspect the code: error.code
      // Common errors could be invalid email and invalid or expired OTPs.
    });
    const header = document.getElementById("header-email-redirect")
    const message = document.getElementById("message-email-redirect")

    header.innerHTML = "dream submission form <a href='/dream-form'>here</a>"
    message.innerHTML = `not ${email}? sign-in <a href='/submit'>here</a>`
}
}


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
        console.log("hi?")
        sendLoginEmail(email.value)
      }
}

// send out authentication email (https://firebase.google.com/docs/auth/web/email-link-auth)
function sendLoginEmail(email) {
    var actionCodeSettings = {
        // URL you want to redirect back to. The domain (www.example.com) for this
        // URL must be whitelisted in the Firebase Console.
        url: "https://nightpoems.com",
        // This must be true.
        handleCodeInApp: true,
        // iOS: {
        //   bundleId: 'com.example.ios'
        // },
        // android: {
        //   packageName: 'com.example.android',
        //   installApp: true,
        //   minimumVersion: '12'
        // },
      };
      console.log("made ie here")
      console.log("it's not gttung here", firebase)

      firebase.auth().sendSignInLinkToEmail(email, actionCodeSettings)
      console.log("ARE YOU HERE???")
}
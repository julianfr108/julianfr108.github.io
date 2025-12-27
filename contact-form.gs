function doPost(e) {
  try {
    const TO_EMAIL = "astateofmindcounsel@gmail.com";

    // Parse the form data
    const data = JSON.parse(e.postData.contents);

    // Build the email body
    let emailBody = "New contact form submission from astateofmindcounseling.org:\n\n";
    emailBody += `Name: ${data.name || 'Not provided'}\n`;
    emailBody += `Email: ${data.email || 'Not provided'}\n`;
    emailBody += `Phone: ${data.phone || 'Not provided'}\n`;
    emailBody += `Message:\n${data.message || 'No message'}\n`;

    // Send email
    MailApp.sendEmail({
      to: TO_EMAIL,
      replyTo: data.email,
      subject: `Contact Form: ${data.name}`,
      body: emailBody
    });

    // Return success response
    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "Form submitted successfully"
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput(
    "Contact form endpoint. Submit via POST."
  );
}

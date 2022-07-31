console.log('file works');

function sendMail(contactForm) {
    emailjs.send("service_y0ogew3", "template_opd47s5", 
    {"from_email":contactForm.email.value,
     "from_name":contactForm.name.value,
     "text":contactForm.text.value,
 })
 .then(
    function(response) {
        console.log('SUCCESS', response);

    },
    function(error){
        console.log('FAILED', error);
    }
    
    );
    
    return false; 
}
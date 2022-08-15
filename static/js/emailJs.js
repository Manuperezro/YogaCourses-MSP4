function sendMail(contactForm) {
    emailjs.send("service_e6qw1nj", "template_rns6sln", 
    {"from_email":contactForm.email.value,
     "from_name":contactForm.name.value,
     "text":contactForm.text.value,
 })
 .then(
    function(response) {
        console.log('SUCCESS', response);
        $("#send")
        if (response == "success") {
            $('#myModal').modal('show');
        }
    },
    function(error){
        console.log('FAILED', error);
        console.log('SUCCESS', response);
        $("#send")
        if (response == "failed") {
            $('#myModalFail').modal('show');
        }
    }
    
    );

    return false; 
}


module.exports = { };
function Response(response) {
    console.log('SUCCESS', response);
    
    if (response == "success") {
        $('#myModal').modal('show');
    }
    else{
        return "FAILED"
    }
};

function sendMail(contactForm) {
    emailjs.send("service_y0ogew3", "template_opd47s5", 
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

module.exports = { Response };
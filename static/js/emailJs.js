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


function validateForm() {
    var x = document.forms["contact-form"]["name"].value;
    var y = document.forms["contact-form"]["email"].value;
    var z = document.forms["contact-form"]["text"].value;
    
    if (x == null || x == "") {
        var emptyX = document.getElementById("send");
        emptyX.dataset.target = "myModalError";
    } 
    
    else if (y == null || y == "") {
        var emptyY = document.getElementById("send");
        emptyY.dataset.target = "myModalError";
    } 
    
    else if (z == null || z == "") {        
        var emptyZ = document.getElementById("send");
        emptyZ.dataset.target = "myModalError";
    } 
    
    else {return true;}
    }

module.exports = { Response };
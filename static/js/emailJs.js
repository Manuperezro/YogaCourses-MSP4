// Jest test Function
function Response(response) {
    console.log('SUCCESS', response);
    
    if (response == "success") {
        $('#myModal').modal('show');
    }
    else{
        return "FAILED"
    }
};
// Jest test Function End

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
            $('#myModalSucces').modal();
        }
        $('#myModalSucces').modal();
    },
    function(error){
        console.log('FAILED', error);
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
        $('#myModalSucces').modal('hide');
        $('#myModalError').modal();
        var emptyX = document.getElementById("send");
        emptyX.attr("data-target", "myModalError");
        emptyZ.attr("disabled", "true");
    } 
    
    else if (y == null || y == "") {
        $('#myModalSucces').modal('hide');
        $('#myModalError').modal();
        var emptyY = document.getElementById("send");
        emptyY.attr("data-target", "myModalError");
        emptyZ.attr("disabled", "true");
    } 
    
    else if (z == null || z == "") { 
        $('#myModalSucces').modal('hide');
        $('#myModalError').modal();      
        var emptyZ = document.getElementById("send");
        emptyZ.attr("data-target", "myModalError");
        emptyZ.attr("disabled", "true");
    } 
    
    else {return true;}
    }

module.exports = { Response };
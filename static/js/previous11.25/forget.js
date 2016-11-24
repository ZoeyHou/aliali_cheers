$(document).ready(function(){
  $("#forget_email_input").blur(function(){
    if(document.getElementById("forget_email_input").value.length == 0){
      document.getElementById("forget_email_hint").style.visibility="visible";
    }else{
      document.getElementById("forget_email_hint").style.visibility="hidden";
    }
  });
});



$(document).ready(function(){
  $("#signup_email_input").blur(function(){
    if(document.getElementById("signup_email_input").value.length == 0){
      document.getElementById("signup_email_hint").style.visibility="visible";
    }else{
      document.getElementById("signup_email_hint").style.visibility="hidden";
    }
  });

  $("#signup_usr_input").blur(function(){
    if(document.getElementById("signup_usr_input").value.length == 0){
      document.getElementById("signup_usr_hint").style.visibility="visible";
    }else{
      document.getElementById("signup_usr_hint").style.visibility="hidden";
    }
  });

  $("#signup_pwd_input").blur(function(){
    if(document.getElementById("signup_pwd_input").value.length < 6){
      document.getElementById("signup_pwd_hint").style.visibility="visible";
    }else{
      document.getElementById("signup_pwd_hint").style.visibility="hidden";
    }
  });

  $("#signup_rpwd_input").blur(function(){
    if(document.getElementById("signup_pwd_input").value == document.getElementById("signup_rpwd_input").value){
      document.getElementById("signup_rpwd_hint").style.visibility="hidden";
    }else{
      document.getElementById("signup_rpwd_hint").style.visibility="visible";
    }
  });
});



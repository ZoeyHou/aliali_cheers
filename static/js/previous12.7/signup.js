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

    $("#signup_img").click(function(){
    document.getElementById("Upload_image").style.visibility="visible";
  });
  $("#Upload_image_close").click(function(){
    document.getElementById("Upload_image").style.visibility="hidden";
  });
  $("#Signup_bt").click(function(){
    var signup_url = "/login/register/"
    var email = $("#signup_email_input");
    var user = $("#signup_usr_input");
    var password = $("#signup_pwd_input");
    var reenter_password = $("#signup_rpwd_input");
    var avatar = $("#Upload_image_file");
    var discription = $("#signup_dis_input");

    var form = document.createElement('form');
    form.id="signup_form";
    form.action=signup_url;
    form.method='post';
    form.name="signup_form";
    form.enctype="multipart/form-data";;

    form.appendChild(email[0]);//在form中追加input表单
    form.appendChild(user[0]);
    form.appendChild(password[0]);
    form.appendChild(avatar[0]);
    form.appendChild(discription[0]);

    if(password.val()!=reenter_password.val()){
      alert("The passwords entering twice are different");
    }else{
      alert(form)
      form.submit();
    }
  });
});



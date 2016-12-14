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
    document.getElementById("Upload_image_content").style.visibility="visible";
  });
  $("#Upload_image_close").click(function(){
    document.getElementById("Upload_image").style.visibility="hidden";
    document.getElementById("Upload_image_content").style.visibility="hidden";
  });
  $("#filter_btn").click(function(){
    var imgObjPreview=document.getElementById("preview");
    var imgObj=document.getElementById("signup_img_bgd");
    imgObj.src = imgObjPreview.src;
    document.getElementById("Upload_image").style.visibility="hidden";
    document.getElementById("Upload_image_content").style.visibility="hidden";
  });

  $("#Signup_bt").click(function(){
    var signup_url = "/login/register/"
    var email = $("#signup_email_input");
    var user = $("#signup_usr_input");
    var password = $("#signup_pwd_input");
    var reenter_password = $("#signup_rpwd_input");
    var avatar = $("#doc");
    var discription = $("#signup_dis_input");

    var form = document.createElement('form');
    form.id="signup_form";
    form.action=signup_url;
    form.method='post';
    form.name="signup_form";
    form.enctype="multipart/form-data";

    form.appendChild(email[0]);//在form中追加input表单
    form.appendChild(user[0]);
    form.appendChild(password[0]);
    form.appendChild(avatar[0]);
    form.appendChild(discription[0]);

    if(password.val()!=reenter_password.val()){
      alert("The passwords entering twice are different");
    }else{
      form.submit();
    }
  });
});

  function setImagePreview(avalue) {
    var docObj=document.getElementById("doc");
     
    var imgObjPreview=document.getElementById("preview");
    if(docObj.files &&docObj.files[0])
    {
      //火狐下，直接设img属性
      imgObjPreview.style.display = 'block';
      imgObjPreview.style.width = '250px';
      imgObjPreview.style.height = '250px'; 
      //imgObjPreview.src = docObj.files[0].getAsDataURL();
       
      //火狐7以上版本不能用上面的getAsDataURL()方式获取，需要一下方式
      imgObjPreview.src = window.URL.createObjectURL(docObj.files[0]);
    }
    else
    {
      //IE下，使用滤镜
      docObj.select();
      var imgSrc = document.selection.createRange().text;
      var localImagId = document.getElementById("localImag");
      //必须设置初始大小
      localImagId.style.width = "250px";
      localImagId.style.height = "250px";
      //图片异常的捕捉，防止用户修改后缀来伪造图片
      try{
        localImagId.style.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale)";
        localImagId.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = imgSrc;
      }
      catch(e)
      {
        alert("您上传的图片格式不正确，请重新选择!");
        return false;
      }
      imgObjPreview.style.display = 'none';
      document.selection.empty();
    }
    return true;
  }



﻿$(document).ready(function(){
	$("#Nav_Home").mouseover(function(){
    	$("#Line_home").animate({left: '-4px'}, 500); 
  	});
  	$("#Nav_Home").mouseout(function(){
    	$("#Line_home").animate({left: '-100px'}, 500);
  	});
  	$("#Nav_Video").mouseover(function(){
    	$("#Line_video").animate({left: '-4px'}, 500); 
  	});
  	$("#Nav_Video").mouseout(function(){
    	$("#Line_video").animate({left: '-100px'}, 500);
  	});
  	$("#Nav_Audio").mouseover(function(){
    	$("#Line_audio").animate({left: '-4px'}, 500); 
  	});
  	$("#Nav_Audio").mouseout(function(){
    	$("#Line_audio").animate({left: '-100px'}, 500);
  	});
	$("#Nav_Image").mouseover(function(){
    	$("#Line_image").animate({left: '-4px'}, 500); 
  	});
  	$("#Nav_Image").mouseout(function(){
    	$("#Line_image").animate({left: '-100px'}, 500);
  	});

  $("#email_input").focus(function(){
    document.getElementById("email_txt").style.visibility="hidden";
  });
  $("#email_input").blur(function(){
    if(document.getElementById("email_input").value.length == 0){
      document.getElementById("email_txt").style.visibility="visible";
    }
  });

  $("#pwd_input").focus(function(){
    document.getElementById("pwd_txt").style.visibility="hidden";
  });
  $("#pwd_input").blur(function(){
    if(document.getElementById("pwd_input").value.length == 0){
      document.getElementById("pwd_txt").style.visibility="visible";
    }
  });

	$("#Search_login").click(function(){
		$("#Login_containt").fadeIn(1000);
    $("#Login_body").fadeIn(1000);
	});
  $("#Login_body").click(function(){
    document.getElementById("Face_login_page").style.visibility="hidden";
    document.getElementById("Face_login_bgd").style.visibility="hidden";
    $("#Login_body").fadeOut(1000);
    $("#Login_containt").fadeOut(1000);
  });
  $("#Login_button").click(function(){
    $.post("/login/", {username: $("#email_input").val(), password: $("#pwd_input").val()}, function(ret){
    if(ret=='T'){
      document.getElementById("Face_login_page").style.visibility="hidden";
      document.getElementById("Face_login_bgd").style.visibility="hidden";
      document.getElementById("Search_login").style.visibility="hidden";
      document.getElementById("User_name").innerHTML = document.cookie.split("=")[1]
      document.getElementById("User").style.visibility="visible";
      $("#Login_body").fadeOut(1000);
      $("#Login_containt").fadeOut(1000);
    }else{
      alert("Oops!! Password is Wrong.");
    }
  });
  });

  $("#Face_button").click(function(){
    document.getElementById("Face_login_page").style.visibility="visible";
    document.getElementById("Face_login_bgd").style.visibility="visible";
  });

  $("#Face_login_close").click(function(){
    document.getElementById("Face_login_page").style.visibility="hidden";
    document.getElementById("Face_login_bgd").style.visibility="hidden";
  });

  $("#Face_login_button").click(function(){
    document.getElementById("Face_login_page").style.visibility="hidden";
    document.getElementById("Face_login_bgd").style.visibility="hidden";
    $("#Login_body").fadeOut(1000);
    $("#Login_containt").fadeOut(1000);
    document.getElementById("Search_login").style.visibility="hidden";
    document.getElementById("User").style.visibility="visible";
  });

  $("#User_logout").click(function(){
    $.post("/login/logout", {username: $("#email_input").val(), password: $("#pwd_input").val()}, function(ret){
    document.getElementById("Search_login").style.visibility="visible";
      document.getElementById("User").style.visibility="hidden";
    });
  });

  var pos = 0, up_url = "http://127.0.0.1:8000/login/recog_login";
  var canvas = document.createElement("canvas");
  canvas.setAttribute('width', 320);
  canvas.setAttribute('height', 240);

jQuery("#webcam").webcam({
    width: 320,
    height: 240,
    mode: "callback",
    swffile: "js/jscam_canvas_only.swf", // canvas only doesn't implement a jpeg encoder, so the file is much smaller
    onTick: function(remain) {
        if (0 == remain) {
            jQuery("#status").text("Cheese!");
        } else {
            jQuery("#status").text(remain + " seconds remaining...");
        }
    },

    onSave: function(data) {
  　　if (canvas.toDataURL) {
    ctx = canvas.getContext("2d");
    image = ctx.getImageData(0, 0, 320, 240);
       
    var col = data.split(";");
    var img = image;
  　　  for(var i = 0; i < 320; i++) {
      　　var tmp = parseInt(col[i]);
      　　img.data[pos + 0] = (tmp >> 16) & 0xff;
      　　img.data[pos + 1] = (tmp >> 8) & 0xff;
      　　img.data[pos + 2] = tmp & 0xff;
      　　img.data[pos + 3] = 0xff;
      　　pos+= 4;
  　　  }
    　　if (pos >= 4 * 320 * 240) {
    　　  ctx.putImageData(img, 0, 0);
    　　  $.post(up_url, {type: "data", image: canvas.toDataURL("image/jpeg"), username: $("#username").val()}, function(){
    　　    location.reload();
    　　  });
    　　  pos = 0;
    　　}　  
  　　} else {
      　　image.push(data);
      　　pos+= 4 * 320;
      　　
      　　if (pos >= 4 * 320 * 240) {
        　　$.post(up_url, {type: "data", image: image.join('|')},  function(){
        　　location.reload();
        　　});
        　　pos = 0;
      　　}　　
  　　}
    },

   onCapture: function () {
        webcam.save();
   },

   debug: function (type, string) {},

   onLoad: function () {
        var cams = webcam.getCameraList();
        for(var i in cams) {
            jQuery("#cams").append("<li>" + cams[i] + "</li>");
        }
   }
});

});



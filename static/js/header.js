function getCookie(name)
{
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
    if(arr=document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}
$(document).ready(function(){
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
      document.getElementById("User_name").innerHTML = getCookie("username")
      document.getElementById("User").style.visibility="visible";
      $("#Login_body").fadeOut(1000);
      $("#Login_containt").fadeOut(1000);
        location.reload()
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
    $.post("/login/logout/", {username: $("#email_input").val(), password: $("#pwd_input").val()}, function(ret){
    document.getElementById("Search_login").style.visibility="visible";
    document.getElementById("User").style.visibility="hidden";
  });
  });

    var width=640, height=480;
    var pos = 0, up_url = "/login/recog_login/";
    var canvas = document.createElement("canvas");
    canvas.setAttribute('width', width);
    canvas.setAttribute('height', height);
    ctx = canvas.getContext("2d");
    image = ctx.getImageData(0, 0, width, height);


jQuery("#webcam").webcam({
    width: width,
    height: height,
    mode: "callback",
    swffile: "/static/swf/jscam.swf", // canvas only doesn't implement a jpeg encoder, so the file is much smaller

    onTick: function(remain) {
        if (0 == remain) {
            jQuery("#status").text("Cheese!");
        } else {
            jQuery("#status").text(remain + " seconds remaining...");
        }
    },

    onSave: function(data) {
        if (canvas.toDataURL) {
            var col = data.split(";");
            var img = image;
            for (var i = 0; i < width; i++) {
                var tmp = parseInt(col[i]);
                img.data[pos + 0] = (tmp >> 16) & 0xff;
                img.data[pos + 1] = (tmp >> 8) & 0xff;
                img.data[pos + 2] = tmp & 0xff;
                img.data[pos + 3] = 0xff;
                pos += 4;
            }
            if (pos >= 4 * width * height) {
                ctx.putImageData(img, 0, 0);
                $.post(up_url, {
                    type: "data",
                    image: canvas.toDataURL("image/jpeg"),
                    username: $("#username").val()
                }, function (data) {
                    if(data == "User_not_exist"){
                        alert("用户不存在");
                    }
                    else if(data=="F") alert("没认出来");
                    else location.reload();
                });
                pos = 0;
            } else {
                image.push(data);
                pos += 4 * width;
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




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
	$("#Search_login").click(function(){
		$("#Login_containt").fadeIn(1000);
    $("#Login_body").fadeIn(1000);
	});
  $("#Login_body").click(function(){
    $("#Login_body").fadeOut(1000);
    $("#Login_containt").fadeOut(1000);
  });
  $("#Login_button").click(function(){
    $("#Login_body").fadeOut(1000);
	$.post("/login/", {username: $("#email_input").val(), password: $("#pwd_input").val()}, function(ret){
		if(ret=='T'){
			document.getElementById("Search_login").style.visibility="hidden";
			document.getElementById("User_name").innerHTML = username=document.cookie.split(";")[1].split("=")[1]
    		document.getElementById("User").style.visibility="visible";
			$("#Login_containt").fadeOut(1000);
		}else{
			alert("Oops!! Password is Wrong.");
		}
	});

  });
  $("#Signup_button").click(function(){
    $("#Login_body").fadeOut(1000);
    $.post("/login/register", {username: $("#email_input").val(), password: $("#pwd_input").val()}, function(ret){
		if(ret=='T'){
			document.getElementById("Search_login").style.visibility="hidden";
			document.getElementById("User_name").innerHTML = username=document.cookie.split(";")[1].split("=")[1]
    		document.getElementById("User").style.visibility="visible";
			$("#Login_containt").fadeOut(1000);
		}else{
			alert("Oops!! The username has been registed");
		}
	});
    document.getElementById("Search_login").style.visibility="hidden";
    document.getElementById("User").style.visibility="visible";
  });
  $("#User_logout").click(function(){
	$.post("/login/logout", {username: $("#email_input").val(), password: $("#pwd_input").val()}, function(ret){
		document.getElementById("Search_login").style.visibility="visible";
    	document.getElementById("User").style.visibility="hidden";
	});
  });
});



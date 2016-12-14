$(document).ready(function(){

	$("#upload_cover").click(function(){
		document.getElementById("Upload_image").style.visibility="visible";
	});
	$("#Upload_image_close").click(function(){
		document.getElementById("Upload_image").style.visibility="hidden";
	});

	$("#Title_input").blur(function(){
    if(document.getElementById("Title_input").value.length == 0){
      document.getElementById("Title_hint").style.visibility="visible";
    }else{
      document.getElementById("Title_hint").style.visibility="hidden";
    }
  });
});
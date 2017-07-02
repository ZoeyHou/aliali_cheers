$(document).ready(function(){

	$("#Edit_img").click(function(){
		document.getElementById("Upload_image").style.visibility="visible";
	});
	$("#Upload_image_close").click(function(){
		document.getElementById("Upload_image").style.visibility="hidden";
	});
});
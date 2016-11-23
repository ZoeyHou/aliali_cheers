$(document).ready(function(){

	var index=document.getElementById("Line_audio");
	index.id = "Line_this";
	$("#Line_this").animate({left: '-4px'}, 500); 

	$("#Download_icon").click(function(){
		document.getElementById("Download_page").style.visibility="visible";
	});
	$("#Download_close").click(function(){
		document.getElementById("Download_page").style.visibility="hidden";
	});

	$("#Like_icon").click(function(){
		alert("Like this video.")
	});

	$("#Dislike_icon").click(function(){
		alert("Dislike this video.")
	});

	$("#Collect_icon").click(function(){
		alert("Collect this video.")
	});
});
$(document).ready(function(){

	var index=document.getElementById("Line_image");
	index.id = "Line_this";
	$("#Line_this").animate({left: '-4px'}, 500); 

	$("#Image_download_icon").click(function(){
		document.getElementById("Download_page").style.visibility="visible";
	});
	$("#Download_close").click(function(){
		document.getElementById("Download_page").style.visibility="hidden";
	});

	$("#Image_like_icon").click(function(){
		alert("Like this video.")
	});

	$("#Image_dislike_icon").click(function(){
		alert("Dislike this video.")
	});

	$("#Image_collect_icon").click(function(){
		alert("Collect this video.")
	});
	
	$(".Comments_like_img").click(function(){
		alert("Like this comment.")
	});
});
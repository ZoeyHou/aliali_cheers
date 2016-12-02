$(document).ready(function(){

	var index=document.getElementById("Line_video");
	var like_collect_url = "/like_collect/"
	index.id = "Line_this";
	$("#Line_this").animate({left: '-4px'}, 500); 

	$("#Image_download_icon").click(function(){
		document.getElementById("Download_page").style.visibility="visible";
	});
	$("#Download_close").click(function(){
		document.getElementById("Download_page").style.visibility="hidden";
	});

	$("#Image_like_icon").click(function(){
		alert("like this video");
		$.post(like_collect_url, {"type": "video_like", "video_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经点过赞了")
			}
		})
	});

	$("#Image_dislike_icon").click(function(){
		alert("Dislike this video.")
		$.post(like_collect_url, {"type": "video_dislike", "video_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经嫌弃过了");
			}
		})
	});


	$("#Image_collect_icon").click(function(){
		$.post(like_collect_url, {"type": "video_collect", "video_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经收藏过了");
			}
		})
	});

	$(".Comments_like_img").click(function(){
		alert("Like this comment.")
	});
});
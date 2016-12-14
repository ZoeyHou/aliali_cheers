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
		$.post(like_collect_url, {"type": "like", "mtype":"video", "video_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经表过态了");
			}else if(ret=="T"){
				document.getElementById("Image_like_num").innerHTML =
			 (Number(document.getElementById("Image_like_num").innerHTML)+1).toString()
			}
		})
	});

	$("#Image_dislike_icon").click(function(){
		$.post(like_collect_url, {"type": "dislike","mtype":"video", "video_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经表过态了");
			}else if(ret=="T"){
				document.getElementById("Image_dislike_num").innerHTML =
			 (Number(document.getElementById("Image_dislike_num").innerHTML)+1).toString()
			}
		})
	});


	$("#Image_collect_icon").click(function(){
		alert("collect this video");
		$.post(like_collect_url, {"type": "collect","mtype":"video", "video_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经收藏过了");
			}
		})
	});

	$("#Comment_send").click(function (ret) {
		$.post(like_collect_url, {"type": "comment","mtype":"video",
			"video_name": $("#page_identify").val(),
			"comment_input":$("#Comment_input").val()}, function(ret){
			if(ret=="T"){
				location.reload()
			}else{
				alert("傻逼不要输入空的东西啊！！！")
			}
		})
	})
});
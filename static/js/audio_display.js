$(document).ready(function(){

	var index=document.getElementById("Line_audio");
	var like_collect_url = "/like_collect/"
	index.id = "Line_this";
	$("#Line_this").animate({left: '-4px'}, 500); 

	$("#Download_icon").click(function(){
		document.getElementById("Download_page").style.visibility="visible";
	});
	$("#Download_close").click(function(){
		document.getElementById("Download_page").style.visibility="hidden";
	});

	$("#Like_icon").click(function(){
		$.post(like_collect_url, {"type": "like", "mtype":"audio", "audio_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经表过态了")
			}else if(ret=="T"){
				document.getElementById("Like_num").innerHTML =
			 (Number(document.getElementById("Like_num").innerHTML)+1).toString()
			}
		});
	});

	$("#Dislike_icon").click(function(){
		$.post(like_collect_url, {"type": "dislike","mtype":"audio", "audio_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经表过态了");
			}else if(ret=="T"){
				document.getElementById("Dislike_num").innerHTML =
			 (Number(document.getElementById("Dislike_num").innerHTML)+1).toString()
			}
		});

	});

	$("#Collect_icon").click(function(){
		alert("Collect this audio.")
		$.post(like_collect_url, {"type": "collect","mtype":"audio", "audio_name": $("#page_identify").val()}, function(ret){
			if(ret=="F"){
				alert("你已经收藏过了");
			}
		});
	});

	$("#Comment_send").click(function (ret) {
		$.post(like_collect_url, {"type": "comment","mtype":"audio",
			"audio_name": $("#page_identify").val(),
			"comment_input":$("#Comment_input").val()}, function(ret){
			if(ret=="T"){
				location.reload()
			}else{
				alert("傻逼不要输入空的东西啊！！！")
			}
		})
	});
});
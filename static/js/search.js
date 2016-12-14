$(document).ready(function(){
	var search_url = '/search/'
	$("#Na_video").click(function(){
		document.getElementById("Content_video").style.display="block";
		document.getElementById("Content_audio").style.display="none";
		document.getElementById("Content_image").style.display="none";
		document.getElementById("Content_user").style.display="none";
		document.getElementById("Na_video_img").src="/static/images/search/_video_u61_mouseOver.png";
		document.getElementById("Na_audio_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_image_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_user_img").src="/static/images/search/_video_u61.png";
	});
	$("#Na_audio").click(function(){
		document.getElementById("Content_video").style.display="none";
		document.getElementById("Content_audio").style.display="block";
		document.getElementById("Content_image").style.display="none";
		document.getElementById("Content_user").style.display="none";
		document.getElementById("Na_video_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_audio_img").src="/static/images/search/_video_u61_mouseOver.png";
		document.getElementById("Na_image_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_user_img").src="/static/images/search/_video_u61.png";
	});
	$("#Na_image").click(function(){
		document.getElementById("Content_video").style.display="none";
		document.getElementById("Content_audio").style.display="none";
		document.getElementById("Content_image").style.display="block";
		document.getElementById("Content_user").style.display="none";
		document.getElementById("Na_video_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_audio_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_image_img").src="/static/images/search/_video_u61_mouseOver.png";
		document.getElementById("Na_user_img").src="/static/images/search/_video_u61.png";
	});
	$("#Na_user").click(function(){
		document.getElementById("Content_video").style.display="none";
		document.getElementById("Content_audio").style.display="none";
		document.getElementById("Content_image").style.display="none";
		document.getElementById("Content_user").style.display="block";
		document.getElementById("Na_video_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_audio_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_image_img").src="/static/images/search/_video_u61.png";
		document.getElementById("Na_user_img").src="/static/images/search/_video_u61_mouseOver.png";
	});

	$("#search_btn").click(function(){
		var form = document.createElement('form');
		form.id="signup_form";
		form.action=search_url;
		form.method='post';
		form.name="signup_form";

		var catas=document.getElementsByName("cata_item");
		var n = catas.length;
		var chestr = '';
		for (var i=0;i<n;i++) {
            if (catas[i].checked == true) {
                chestr += catas[i].value + ",";
            }
        }

		var search_input = $("#Search_area");

		form.appendChild(search_input[0]);
		var inp = document.createElement("input");
		inp.value=chestr;
		inp.name="catagory";
		inp.type="text";
		form.appendChild(inp)

		form.submit();
	})
});
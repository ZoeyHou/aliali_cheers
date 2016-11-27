$(document).ready(function(){

	$("#upload_cover").click(function(){
		document.getElementById("Upload_image").style.visibility="visible";
	});
	$("#Upload_image_close").click(function(){
		document.getElementById("Upload_image").style.visibility="hidden";
	});
	$("#Upload_bt").click(function(){
		var upload_url = "/transform/upload/";

		var discript_img = $("#Upload_image_file");
		var file_input = $("#File_input");
		var title_input = $("#Title_input");
		var type_input = $("#Type_input");
		var catagoty_input = $("#Catagory_input");
		var discription_input = $("#Discription_input");

		var form = document.createElement('form');
		form.id="signup_form";
		form.action=upload_url;
		form.method='post';
		form.name="signup_form";
		form.enctype="multipart/form-data";

		form.appendChild(discript_img[0]);
		form.appendChild(file_input[0]);
		form.appendChild(title_input[0]);
		form.appendChild(type_input[0]);
		form.appendChild(catagoty_input[0]);
		form.appendChild(discription_input[0]);

		alert("ready!")
		form.submit();
	});

	$("#Title_input").blur(function(){
    if(document.getElementById("Title_input").value.length == 0){
      document.getElementById("Title_hint").style.visibility="visible";
    }else{
      document.getElementById("Title_hint").style.visibility="hidden";
    }
  });
});
$(document).ready(function(){

	$("#upload_cover").click(function(){
		document.getElementById("Upload_image").style.visibility="visible";
    	document.getElementById("Upload_image_content").style.visibility="visible";
  	});
  	$("#Upload_image_close").click(function(){
    	document.getElementById("Upload_image").style.visibility="hidden";
    	document.getElementById("Upload_image_content").style.visibility="hidden";
  	});

  $("#filter_btn").click(function(){
    var imgObjPreview=document.getElementById("preview");
    var imgObj=document.getElementById("upload_cover_img");
    imgObj.src = imgObjPreview.src;
    document.getElementById("Upload_image").style.visibility="hidden";
    document.getElementById("Upload_image_content").style.visibility="hidden";
  });

	$("#Upload_bt").click(function(){
		var upload_url = "/transform/upload/";

		var discript_img = $("#doc");
		var file_input = $("#File_input");
		var title_input = $("#Title_input");
		var type_input = $("#Type_input");
		var catagoty_input = $("#Catagory_input");
		var discription_input = $("#Discription_input");
		var filter_input = $("#filter_select");

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
		form.appendChild(filter_input[0]);


		alert("ready!")
		$(document.body).append(form);
		form.submit();

	});

	$("#Title_input").blur(function(){
    if(document.getElementById("Title_input").value.length == 0){
      document.getElementById("Title_hint").style.visibility="visible";
    }else{
      document.getElementById("Title_hint").style.visibility="hidden";
    }
  });

  	$('#Type_input').change(function(){
  		switch($(this).children('option:selected').val()){
  			case "Video":
  				document.getElementById("Catagory_video").style.visibility="visible";
  				document.getElementById("Catagory_audio").style.visibility="hidden";
  				document.getElementById("Catagory_image").style.visibility="hidden";
  				break;
  			case "Audio":
  				document.getElementById("Catagory_video").style.visibility="hidden";
  				document.getElementById("Catagory_audio").style.visibility="visible";
  				document.getElementById("Catagory_image").style.visibility="hidden";
  				break;
  			case "Image":
  				document.getElementById("Catagory_video").style.visibility="hidden";
  				document.getElementById("Catagory_audio").style.visibility="hidden";
  				document.getElementById("Catagory_image").style.visibility="visible";
  				break;
  		}
  	});
  	
});

 function setImagePreview(avalue) {
    var docObj=document.getElementById("doc");
     
    var imgObjPreview=document.getElementById("preview");
    if(docObj.files &&docObj.files[0])
    {
      //火狐下，直接设img属性
      imgObjPreview.style.display = 'block';
      imgObjPreview.style.width = '250px';
      imgObjPreview.style.height = '200px'; 
      //imgObjPreview.src = docObj.files[0].getAsDataURL();
       
      //火狐7以上版本不能用上面的getAsDataURL()方式获取，需要一下方式
      imgObjPreview.src = window.URL.createObjectURL(docObj.files[0]);
    }
    else
    {
      //IE下，使用滤镜
      docObj.select();
      var imgSrc = document.selection.createRange().text;
      var localImagId = document.getElementById("localImag");
      //必须设置初始大小
      localImagId.style.width = "250px";
      localImagId.style.height = "200px";
      //图片异常的捕捉，防止用户修改后缀来伪造图片
      try{
        localImagId.style.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale)";
        localImagId.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = imgSrc;
      }
      catch(e)
      {
        alert("您上传的图片格式不正确，请重新选择!");
        return false;
      }
      imgObjPreview.style.display = 'none';
      document.selection.empty();
    }
    return true;
  }
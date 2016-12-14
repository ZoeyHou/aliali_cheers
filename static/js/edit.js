$(document).ready(function(){

	$("#Edit_img").click(function(){
	    document.getElementById("Upload_image").style.visibility="visible";
	    document.getElementById("Upload_image_content").style.visibility="visible";
	});
	$("#Upload_image_close").click(function(){
		document.getElementById("Upload_image").style.visibility="hidden";
    	document.getElementById("Upload_image_content").style.visibility="hidden";
	});

  $("#filter_btn").click(function(){
    var imgObjPreview=document.getElementById("preview");
    var imgObj=document.getElementById("Edit_img");
    imgObj.src = imgObjPreview.src;
    document.getElementById("Upload_image").style.visibility="hidden";
    document.getElementById("Upload_image_content").style.visibility="hidden";
  });
    
  $("#Edit_update").click(function () {
    var edit_url = "/edit_info/"
    var avatar = $("#doc");
    var discription = $("#Edit_discription_input");
    var filter_input = $("#filter_select");

    var form = document.createElement('form');
    form.id="description_form";
    form.action=edit_url;
    form.method='post';
    form.name="description_form";
    form.enctype="multipart/form-data";;

    form.appendChild(avatar[0]);
    form.appendChild(discription[0]);
    form.appendChild(filter_input[0]);

    form.submit();
  })

});

function setImagePreview(avalue) {
    var docObj=document.getElementById("doc");
     
    var imgObjPreview=document.getElementById("preview");
    if(docObj.files &&docObj.files[0])
    {
      //火狐下，直接设img属性
      imgObjPreview.style.display = 'block';
      imgObjPreview.style.width = '250px';
      imgObjPreview.style.height = '250px'; 
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
      localImagId.style.height = "250px";
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



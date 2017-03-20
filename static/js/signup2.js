$(document).ready(function(){

    var width=640, height=480;
    var pos = 0, up_url = "/login/recog_register/";
    var canvas = document.createElement("canvas");
    canvas.setAttribute('width', width);
    canvas.setAttribute('height', height);
    ctx = canvas.getContext("2d");
    image = ctx.getImageData(0, 0, width, height);
    var pic_count=5;
    var photo = 1;
    var img5, img4, img3, img2, img1;


jQuery("#webcam2").webcam({
    width: width,
    height: height,
    mode: "callback",
    swffile: "/static/swf/jscam.swf", // canvas only doesn't implement a jpeg encoder, so the file is much smaller

    onTick: function(remain) {
        if (0 == remain) {
            jQuery("#status").text("Cheese!");
        } else {
            jQuery("#status").text(remain + " seconds remaining...");
        }
    },

    onSave: function(data) {
        if (canvas.toDataURL) {
            var col = data.split(";");
            var img = image;
            for (var i = 0; i < width; i++) {
                var tmp = parseInt(col[i]);
                img.data[pos + 0] = (tmp >> 16) & 0xff;
                img.data[pos + 1] = (tmp >> 8) & 0xff;
                img.data[pos + 2] = tmp & 0xff;
                img.data[pos + 3] = 0xff;
                pos += 4;
            }
            if (pos >= 4 * width * height) {
                ctx.putImageData(img, 0, 0);
                if(pic_count <= 0){
                　　	$.post(up_url, {type: "data", img1: img1, img2: img2, img3: img3, img4: img4, img5: img5},
                        function(return_html){
                                self.location.href='/'
                    　　	});
                }
                if(pic_count==5){
                    img5 = canvas.toDataURL("image/jpeg");
                }
                else if(pic_count==4){
                    img4 = canvas.toDataURL("image/jpeg");
                }
                else if(pic_count==3){
                    img3 = canvas.toDataURL("image/jpeg");
                }
                else if(pic_count==2){
                    img2 = canvas.toDataURL("image/jpeg");
                }
                else if(pic_count==1){
                    img1 = canvas.toDataURL("image/jpeg");
                }
                pic_count -= 1;
                pos = 0;
            } else {
                image.push(data);
                pos += 4 * width;
            }
        }
    },

   onCapture: function () {
        webcam.save();
   },

   debug: function (type, string) {},

   onLoad: function () {
        var cams = webcam.getCameraList();
        for(var i in cams) {
            jQuery("#cams").append("<li>" + cams[i] + "</li>");
        }
   }
});

  $("#Take_photo").click(function(){
      if(pic_count!=0) {
          var photoID = 'Photo_' + photo;
          document.getElementById(photoID).src = "/static/images/personal_page/hint.png";
          photo++;
      }
      webcam.capture();
  });

});



$(document).ready(function(){
   var width=640, height=480;
    var pos = 0;
    var canvas = document.createElement("canvas");
    canvas.setAttribute('width', width);
    canvas.setAttribute('height', height);
    ctx = canvas.getContext("2d");
    image = ctx.getImageData(0, 0, width, height);
    var photo = 1;

jQuery("#webcam2").webcam({
    width: width,
    height: height,
    mode: "callback",
    swffile: "/static/js/jscam_canvas_only.swf", // canvas only doesn't implement a jpeg encoder, so the file is much smaller

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
                $.post(up_url, {
                    type: "data",
                    image: canvas.toDataURL("image/jpeg"),
                    username: $("#username").val()
                }, function (data) {

                });
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
      webcam.capture();
      var photoID='Photo_img_'+photo;
      var Objcanvas=document.getElementById(photoID);
      var Objctx=Objcanvas.getContext('2d');
      Objctx.fillStyle='#DDDDDD';
      Objctx.fillRect(0,0,300,200);
      photo = photo % 5 +1;

      var imgdata = Objctx.getImageData(0,0,300,200);
      var Objpixels = imgdata.data;
      var pixels = image.data;
      var pos = 0, Objpos = 0;
      for(var i=0;i<height;++i){
          for(var j = 0; j < width; ++j){
              Objpixels[Objpos] = pixels[pos];
              Objpixels[Objpos+1] = pixels[pos+1];
              Objpixels[Objpos+2] = pixels[pos+2];
              Objpixels[Objpos+3] = pixels[pos+3];
              pos+=4;
              Objpos+=8;
          }
          Objpos+=4*width;
      }
    Objctx.putImageData(imgdata,0,0);
  });

});
$(document).ready(function(){
  var width=600, height=400;
    var pos = 0, up_url = "/login/recog_login/";
    var canvas = document.createElement("canvas");
    canvas.setAttribute('width', width);
    canvas.setAttribute('height', height);
    ctx = canvas.getContext("2d");
    image = ctx.getImageData(0, 0, width, height);
    var test_count = 0;
    var test_count1 = 0;


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
            test_count++;
            if (pos >= 2 * width * height){
                test_count1++;
            }
            if (pos >= 4 * width * height) {
                ctx.putImageData(img, 0, 0);
                /*
                这里图片已经扫描完了，调用canvas.toDataURL就可以获取到图片。
                $.post(up_url, {
                    type: "data",
                    image: canvas.toDataURL("image/jpeg"),
                    username: $("#username").val()
                }, function (data) {
                    if(data=="F") alert("没认出来");
                    else location.reload();
                });
                */
                alert("这里图片已经扫描完了，调用canvas.toDataURL就可以获取到图片。");
                pos = 0;
            } else {
                image.push(data);
                pos += 4 * width;
            }
        }
    },

   onCapture: function () {
       alert("capture");
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

});



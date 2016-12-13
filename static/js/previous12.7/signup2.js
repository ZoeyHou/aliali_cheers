$(document).ready(function(){
  var pos = 0, up_url = "http://127.0.0.1:8000/login/recog_login";
  var canvas = document.createElement("canvas");
  canvas.setAttribute('width', 600);
  canvas.setAttribute('height', 400);

jQuery("#webcam2").webcam({
    width: 600,
    height: 400,
    mode: "callback",
    swffile: "js/jscam_canvas_only.swf", // canvas only doesn't implement a jpeg encoder, so the file is much smaller
    onTick: function(remain) {
        if (0 == remain) {
            jQuery("#status").text("Cheese!");
        } else {
            jQuery("#status").text(remain + " seconds remaining...");
        }
    },

    onSave: function(data) {
  　　if (canvas.toDataURL) {
    ctx = canvas.getContext("2d");
    image = ctx.getImageData(0, 0, 600, 400);
       
    var col = data.split(";");
    var img = image;
  　　  for(var i = 0; i < 600; i++) {
      　　var tmp = parseInt(col[i]);
      　　img.data[pos + 0] = (tmp >> 16) & 0xff;
      　　img.data[pos + 1] = (tmp >> 8) & 0xff;
      　　img.data[pos + 2] = tmp & 0xff;
      　　img.data[pos + 3] = 0xff;
      　　pos+= 4;
  　　  }
    　　if (pos >= 4 * 600 * 400) {
    　　  ctx.putImageData(img, 0, 0);
    　　  $.post(up_url, {type: "data", image: canvas.toDataURL("image/jpeg"), username: $("#username").val()}, function(){
    　　    location.reload();
    　　  });
    　　  pos = 0;
    　　}　  
  　　} else {
      　　image.push(data);
      　　pos+= 4 * 600;
      　　
      　　if (pos >= 4 * 600 * 400) {
        　　$.post(up_url, {type: "data", image: image.join('|')},  function(){
        　　location.reload();
        　　});
        　　pos = 0;
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

});



/**
 * @license jQuery webcam2 plugin v1.0.0 09/12/2010
 * http://www.xarg.org/project/jquery-webcam2-plugin/
 *
 * Copyright (c) 2010, Robert Eisele (robert@xarg.org)
 * Dual licensed under the MIT or GPL Version 2 licenses.
 **/

(function ($) {

    var webcam2 = {

	"extern": null, // external select token to support jQuery dialogs
	"append": true, // append object instead of overwriting

	"width": 640,
	"height": 480,

	"mode": "callback", // callback | save | stream

	"swffile": "jscam2.swf",
	"quality": 85,

	"debug":	function () {},
	"onCapture":	function () {},
	"onTick":	function () {},
	"onSave":	function () {},
	"onLoad":	function () {}
    };

    window["webcam2"] = webcam2;

    $["fn"]["webcam2"] = function(options) {

	if (typeof options === "object") {
	    for (var ndx in webcam2) {
		if (options[ndx] !== undefined) {
		    webcam2[ndx] = options[ndx];
		}
	    }
	}

	var source = '<object id="Xwebcam2XobjectX" type="application/x-shockwave-flash" data="'+webcam2["swffile"]+'" width="'+webcam2["width"]+'" height="'+webcam2["height"]+'"><param name="movie" value="'+webcam2["swffile"]+'" /><param name="FlashVars" value="mode='+webcam2["mode"]+'&amp;quality='+webcam2["quality"]+'" /><param name="allowScriptAccess" value="always" /></object>';

	if (null !== webcam2["extern"]) {
	    $(webcam2["extern"])[webcam2["append"] ? "append" : "html"](source);
	} else {
	    this[webcam2["append"] ? "append" : "html"](source);
	}

	var run = 3;
	(_register = function() {
	    var cam = document.getElementById('Xwebcam2XobjectX');

	    if (cam && cam["capture"] !== undefined) {

		/* Simple callback methods are not allowed :-/ */
		webcam2["capture"] = function(x) {
		    try {
			return cam["capture"](x);
		    } catch(e) {}
		}
		webcam2["save"] = function(x) {
		    try {
			return cam["save"](x);
		    } catch(e) {}
		}
		webcam2["setCamera"] = function(x) {
		    try {
			return cam["setCamera"](x);
		    } catch(e) {}
		}
		webcam2["getCameraList"] = function() {
		    try {
			return cam["getCameraList"]();
		    } catch(e) {}
		}
		webcam2["pauseCamera"] = function() {
		    try {
			return cam["pauseCamera"]();
		    } catch(e) {}
		}		
		webcam2["resumeCamera"] = function() {
		    try {
			return cam["resumeCamera"]();
		    } catch(e) {}
		}
		webcam2["onLoad"]();
	    } else if (0 == run) {
		webcam2["debug"]("error", "Flash movie not yet registered!");
	    } else {
		/* Flash interface not ready yet */
		run--;
		window.setTimeout(_register, 1000 * (4 - run));
	    }
	})();
    }

})(jQuery);

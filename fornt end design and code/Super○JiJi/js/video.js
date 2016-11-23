$(document).ready(function(){

	var index=document.getElementById("Line_video");
	index.id = "Line_this";
	$("#Line_this").animate({left: '-4px'}, 500); 

});

$.fn.slider = function () {  // 控件的实现
	$(this).addClass('slider');
	var id = $(this).attr('id');
	var lis = $('.slider ul li');
	var len = lis.length;
	var w = $('.slider').width();
	var h = $('.slider').height();
	$(lis).addClass('slideitem').each( function (i) {
		$(this).css({left: !i ? 0 : w, top: -i * h, 'z-index':i});
	});

	var q = [];
	var i;
	for (i = 2; i <= len; ++i){
		var markid = '#markli' + i;
		$(markid).css({left: w, 'z-index':i});
		q.push(i);
	}
    q.push(1);

	$('#li1').addClass('cur');
	$('#markli1').addClass('curmark');
	$(".mark_item").click(function(){
		var cur = 0;
		switch($(this).id){
			case 'marker1': cur = 1;
			case 'marker2': cur = 2;
			case 'marker3': cur = 3;
			default: cur = 4;
		}
		var j = cur+1;
		for (i = 1; i < len; ++i){
			q.shift();
			if(j>len) 
				j=j-len;
			var markid = '#markli' + j;
			$(liid).css({'z-index': i});
			$(markid).css({left: w, 'z-index':i});
			q.push(j);
		}
		var markid = '#markli' + cur;
		$(markid).css({left: w, 'z-index':len});
		q.push(cur);
		var liid = '#li' + cur;

		$('.curmark').css({left: w});
		$(markid).css({left: 0});
		
		$('.cur').animate({left: -w}, 500);
		$(liid).animate({left: 0}, 500, function () {
			$('.cur').removeClass('cur').css({left: w, 'z-index': 0});
			$('.curmark').removeClass('curmark').css({'z-index': 0});
			$(this).addClass('cur');
			$(markid).addClass('curmark');
		})
	});
	$("#pre").click(function(){
		var cur = q.pop();
		var zz = len;
		for (x in q) 
        {
        	var markid = '#markli' + q[x];
			var liid = '#li' + q[x];
			$(markid).css({'z-index': zz--});
			$(liid).css({'z-index': zz--});
		}
		q.unshift(cur);

		var liid = '#li' + cur;
		var markid = '#markli' + cur;
		$('.cur').css({left:0});
		$(llid).css({left:-w, 'z-index': len});

		$('.curmark').css({left: w});
		$(markid).css({left: 0, 'z-index': len});
		
		$('.cur').animate({left: w}, 500);
		$(liid).animate({left: 0}, 500, function () {
			$('.cur').removeClass('cur').css({'z-index': len});
			$('.curmark').removeClass('curmark').css({'z-index': len});
			$(this).addClass('cur');
			$(markid).addClass('curmark');
		})
	});
	$("#next").click(function(){
		var cur = q.shift();
		var zz = len;
		for (x in q)
        {
        	var markid = '#markli' + q[x];
			var liid = '#li' + q[x];
			$(markid).css({'z-index': zz--});
			$(liid).css({'z-index': zz--});
		}
		q.push(cur);

		var liid = '#li' + cur;
		var markid = '#markli' + cur;
		$('.curmark').css({left: w});
		$(markid).css({left: 0});
		$('.cur').animate({left: -w}, 500);
		$(liid).animate({left: 0}, 500, function () {
			$('.cur').removeClass('cur').css({left: w, 'z-index': 0});
			$('.curmark').removeClass('curmark').css({'z-index': 0});
			$(this).addClass('cur');
			$(markid).addClass('curmark');
		})
	});
	setInterval(function(){
		var cur = q.shift();
		var zz = len;
		for (x in q)
        {
        	var markid = '#markli' + q[x];
			var liid = '#li' + q[x];
			$(markid).css({'z-index': zz--});
			$(liid).css({'z-index': zz--});
		}
		q.push(cur);

		var liid = '#li' + cur;
		var markid = '#markli' + cur;
		$('.curmark').css({left: w});
		$(markid).css({left: 0});
		$('.cur').animate({left: -w}, 500);
		$(liid).animate({left: 0}, 500, function () {
			$('.cur').removeClass('cur').css({left: w, 'z-index': 0});
			$('.curmark').removeClass('curmark').css({'z-index': 0});
			$(this).addClass('cur');
			$(markid).addClass('curmark');
		})
	}, 5000);
}



$(document).ready(function(){

	var index=document.getElementById("Line_audio");
	index.id = "Line_this";
	$("#Line_this").animate({left: '-4px'}, 500); 

	var txt = '{ "item" : [' +
	'{ "cover":"images/audio/image_u61.jpg" , "rank":"1" , "change":"images/audio/up.png" , "link":"#" , "title":"Closer" , "singer":"The chainsmokers Featuring Halsey"},' +
	'{ "cover":"images/audio/starboy.jpg" , "rank":"2" , "change":"images/audio/new.png", "link":"#" , "title":"Starboy" , "singer":"The Weekend Featuring Daft Punk" },' +
	'{ "cover":"images/audio/heathens.jpg" , "rank":"3", "change":"images/audio/down.png", "link":"#" , "title":"Heathens" , "singer":"twenty one pilots" },' +
	'{ "cover":"images/audio/heathens.jpg" , "rank":"4" , "change":"images/audio/play_bg_u82.png", "link":"#" , "title":"Heathens" , "singer":"twenty one pilots" } ]}';
	var obj = eval ("(" + txt + ")");
	var k;
	var v= new Array();
	
	v[0] = document.getElementById("music_display");
	v[1] = document.getElementById("audio_display");
	v[2] = document.getElementById("talkshow_display");
	v[3] = document.getElementById("entertainment_display");
	v[4] = document.getElementById("news_display");
	v[5] = document.getElementById("others_display");

	for(var t = 0; t < 6; ++t){
		for (var k = 0; k < 4; ++k){
			var li=document.createElement('li');
			li.id="item"+k;

			var cover_img=document.createElement("img");
			cover_img.src=obj.item[k].cover;
			cover_img.id="item_cover";
			li.appendChild(cover_img);

			var change_img=document.createElement("img");
			change_img.src=obj.item[k].change;
			change_img.id="item_change_img";
			var change_div=document.createElement("div");
			change_div.appendChild(change_img);
			change_div.id="item_change";
			li.appendChild(change_div);

			var rank_p=document.createElement("p");
			var rank_txt=document.createTextNode(obj.item[k].rank);
			rank_p.appendChild(rank_txt);
			rank_p.id="item_rank";
			li.appendChild(rank_p);

			var play_bt_bgd=document.createElement("img");
			play_bt_bgd.src="images/audio/play_bg_u82.png";
			play_bt_bgd.id="play_bg";
			li.appendChild(play_bt_bgd);

			var play_bt_link=document.createElement("a");
			play_bt_link.href=obj.item[k].link;
			var play_bt_tri=document.createElement("img");
			play_bt_tri.src="images/audio/play_tri_u84.png";
			play_bt_tri.id="play_tri";
			play_bt_link.appendChild(play_bt_tri);
			li.appendChild(play_bt_link);

			var title_p=document.createElement("p");
			var title_txt=document.createTextNode(obj.item[k].title);
			title_p.appendChild(title_txt);
			title_p.id="item_title";
			li.appendChild(title_p);

			var singer_p=document.createElement("p");
			var singer_txt=document.createTextNode(obj.item[k].singer);
			singer_p.appendChild(singer_txt);
			singer_p.id="item_singer";
			li.appendChild(singer_p);

			v[t].appendChild(li);
		}
	}
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



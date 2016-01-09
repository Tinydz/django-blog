// Js cookie
//jQuery.cookie=function(b,j,m){if(typeof j!="undefined"){m=m||{};if(j===null){j="";m.expires=-1}var e="";if(m.expires&&(typeof m.expires=="number"||m.expires.toUTCString)){var f;if(typeof m.expires=="number"){f=new Date();f.setTime(f.getTime()+(m.expires*24*60*60*1000))}else{f=m.expires}e="; expires="+f.toUTCString()}var l=m.path?"; path="+(m.path):"";var g=m.domain?"; domain="+(m.domain):"";var a=m.secure?"; secure":"";document.cookie=[b,"=",encodeURIComponent(j),e,l,g,a].join("")}else{var d=null;if(document.cookie&&document.cookie!=""){var k=document.cookie.split(";");for(var h=0;h<k.length;h++){var c=jQuery.trim(k[h]);if(c.substring(0,b.length+1)==(b+"=")){d=decodeURIComponent(c.substring(b.length+1));break}}}return d}};
// start jQuery
jQuery(document).ready(function(){
    var delayTime = [];
    jQuery('#nav li:has(ul)').each(function(index) {
        $(this).hover(function() {
            var _self = this;
            delayTime[index] = setTimeout(function() {
                $(_self).find('ul:eq(0)').slideDown(200)
            },
            400)
        },
        function() {
            clearTimeout(delayTime[index]);
            $('ul', this).slideUp(200)
        });
    });
	
	// Search
	jQuery("input#sear_txt").val("Search...");
	textReplacement(jQuery('input#sear_txt').css("color", "#aaa"));
	function textReplacement(input){ 
	var originalvalue = input.val();
	input.focus( function(){
	if( jQuery.trim(input.val()) == originalvalue ){ input.val("").css("color", "#666"); }
	});
	 input.blur( function(){
	if( jQuery.trim(input.val()) == "" ){ input.val(originalvalue).css("color", "#aaa"); }
	});
	}
});
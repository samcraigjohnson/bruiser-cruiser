
//This function is used to stop propagation of
//some dropdowns so that users can click inside
//of them without closing the dropdowns
$(function(){
    $('.no-prop').click(function(e){
	e.stopPropgation();
    });
});
$(function() {
    $("input").blur(function(event) {		
	tmp = $(this.form.elements).map(function() { return this.value; });
	$.ajax({
	    url:this.form.action,
	    context:this,
	    type:'POST',
	    data:{'ans':tmp.toArray() },
	    dataType:'json',
	    success:function(result) {
		$(this).parents("#question").find("#points").text(result['points']);
		$(this).parents("#question").find("#comments").html(result['comments']);
		i = 0;
		$("input",this.form).each(function(i) {
		    if(result['correct'][i]) {
			$(this).css("backgroundColor","#66FF66");
			$(this).attr("readOnly",true);
		    } else if(tmp[i]) {
			$(this).css("backgroundColor","#FF6666");
		    } else {
			$(this).css("backgroundColor","white");
		    }
		})
		    }
	});
    });
});
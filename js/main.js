$(function() {
    if (Modernizr.touch) {
        $.each($('.section'), function(i, item) {
            $(item).addClass("touch")
        })
    }
})
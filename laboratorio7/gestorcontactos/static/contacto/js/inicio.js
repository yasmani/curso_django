$(document).ready(function() {
    let url = window.location.href;
    let result = url.substring(31);
    $('#navMenu li').each(function() {
        if($(this).find('a').attr('href') === result){
         $(this).find('a').addClass('active');
    }
   })
})
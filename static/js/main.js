function copyToClipboard(text) {
    texts = window.location.origin + text
    window.prompt("Ctrl+C to copy link,  Enter", texts);
    alert("hope that works :)")
}


$('.image-link').click(function () {
    $('#image-name').html($(this).data('name'));
    $('#image-description').html($(this).data('description'));
    $('#image-description').html($(this).data('description'));
    $('#image-category').html($(this).data('category'));
    $('#image-location').html($(this).data('location'));
    $('#image-date').html($(this).data('date'));
    $('#copy').html($(this).data('img'));
    
    let pic = document.getElementById('copy').innerHTML
    let link = window.location.origin + pic;
    $('#image-url').attr('src', link);
});
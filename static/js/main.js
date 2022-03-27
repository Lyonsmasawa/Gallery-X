$('#clickImage').on('show.bs.modal', function (event) {
    let image = $(event.relatedTarget)
    let img_src = image.data("whatever")

    var modal = $(this)
    modal.find('.modal.title').text(img_src)
})

function copyToClipboard(text) {
    texts = window.location.origin + text
    window.prompt("Ctrl+C to copy link,  Enter", texts);
    alert("hope that works :)")
}
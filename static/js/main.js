$('#clickImage').on('show.bs.modal', function (event) {
    let image = $(event.relatedTarget)
    let img_src = image.data("whatever")

    var modal = $(this)
    modal.find('.modal.title').text(img_src)
})

function copyToClipboard(text) {
    window.prompt("Copy to clipboard:  Ctrl+C,  Enter", text);
    alert("Link copied successfully")
}
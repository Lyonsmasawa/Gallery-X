function copyToClipboard(text) {
    texts = window.location.origin + text
    window.prompt("Ctrl+C to copy link,  Enter", texts);
    alert("hope that works :)")
}
function snapShot() {
    var videoElement = document.querySelector('video');
    var canvasElement = document.getElementById('snap')
    var context = canvasElement.getContext('2d');

    context.drawImage(videoElement, 0, 0, videoElement.width, videoElement.height);
    sessionStorage.setItem('snapshot', canvasElement.toDataURL('image/png'));
}

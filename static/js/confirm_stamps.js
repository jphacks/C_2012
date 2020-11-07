function ImageToBase64(img, mime_type) {
    // New Canvas
    var canvas = document.createElement('canvas');
    canvas.width  = img.width;
    canvas.height = img.height;
    // Draw Image
    var ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0, 320, 320);
    // To Base64
    return canvas.toDataURL(mime_type);
};

function setStampsToSession() {
    let husbandStampImage = new Image( 320, 320 ) ;
    let wifeStampImage = new Image( 320, 320 ) ;
    husbandStampImage = document.getElementsByClassName('husband_stamp')[0];
    wifeStampImage = document.getElementsByClassName('wife_stamp')[0];
    husbandStampData = ImageToBase64(husbandStampImage, "image/jpeg");
    wifeStampData = ImageToBase64(wifeStampImage, "image/jpeg");
    sessionStorage.setItem("husbandStampData", husbandStampData);
    sessionStorage.setItem("wifeStampData", wifeStampData);
};

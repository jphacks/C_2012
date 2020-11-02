const FACE = {};

FACE.EXPRESSION = () => {
  const cameraArea = document.getElementById('cameraArea'),
        camera = document.getElementById('camera'),
        canvas = document.getElementById('canvas'),
        emoticon = document.getElementById('emoticon'),
        ctx = canvas.getContext('2d'),
        canvasW = 640,
        canvasH = 480,
        intervalTime = 500,
        emoticonTxt = [':)',':|'];

  const init = async () => {
    setCanvas();
    setCamera();
    await faceapi.nets.tinyFaceDetector.load("static/js/weights/");
    await faceapi.nets.faceExpressionNet.load("static/js/weights/");
  },

  setCanvas = () => {
    canvas.width = canvasW;
    canvas.height = canvasH;
  },

  setCamera = async () => {
    var constraints = {
      audio: false,
      video: {
        width: canvasW,
        height: canvasH,
        facingMode: 'user'
      }
    };
    await navigator.mediaDevices.getUserMedia(constraints)
    .then((stream) => {
      camera.srcObject = stream;
      camera.onloadedmetadata = (e) => {
        playCamera();
      };
    })
    .catch((err) => {
      console.log(err.name + ': ' + err.message);
    });
  },

  playCamera = () => {
    camera.play();
    setInterval(async () => {
      canvas.getContext('2d').clearRect(0, 0, canvasW, canvasH);
      checkFace();
    }, intervalTime);
  },

  checkFace = async () => {
    let faceData = await faceapi.detectAllFaces(
      camera, new faceapi.TinyFaceDetectorOptions()
    ).withFaceExpressions();
    if(faceData.length){
      const setDetection = (num) => {
        let box = faceData[num].detection.box;
            x = box.x,
            y = box.y,
            w = box.width,
            h = box.height;

        ctx.beginPath();
        ctx.rect(x, y, w, h);
        ctx.strokeStyle = '#76FF03';
        ctx.lineWidth = 2;
        ctx.stroke();
      },

      setExpressions = (num) => {
        let happy = faceData[num].expressions.happy,
            color = happy * 150 + 100;
        console.log(String(num) + " " + String(happy));
        emoticon.style.bottom = (canvasH - 40) * happy + 'px';
        emoticon.style.backgroundColor = `rgb(${color}, ${color}, 100)`;
        if(happy > 0.5){
          emoticon.innerHTML = emoticonTxt[0];
        }else{
          emoticon.innerHTML = emoticonTxt[1];
        }
      };
      // 笑顔状態描画
      for (let i = 0; i < faceData.length; i++) {
        setDetection(i);
        setExpressions(i);
      }
    }
  };

  init();
};
FACE.EXPRESSION();

const FACE = {};

FACE.EXPRESSION = () => {
	const cameraArea = document.getElementById('cameraArea'),
			camera = document.getElementById('camera'),
			canvas = document.getElementById('canvas'),
			emoticon1 = document.getElementById('emoticon1'),
			emoticon2 = document.getElementById('emoticon2'),
			ctx = canvas.getContext('2d'),
			intervalTime = 500, // 判定間隔
			emoticonTxt = [':)',':|'];

	const init = async () => {
		await faceapi.nets.tinyFaceDetector.load("static/js/weights/");
		await faceapi.nets.faceExpressionNet.load("static/js/weights/");
		setCamera();
	},

	setCamera = async () => {
		var constraints = {
		audio: false,
		video: {
			width: camera.width,
			height: canvas.height,
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

	playCamera = async() => {
		camera.play();
		// 判定反復処理
		let timer = setInterval(async () => {
		canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
		checkFace(timer)
		}, intervalTime);
	},

	checkFace = async (timer) => {
		let faceDatum = await faceapi.detectAllFaces(
		camera, new faceapi.TinyFaceDetectorOptions()
		).withFaceExpressions();

		// 二人以下でしか動かないようにする
		if(faceDatum.length <= 2){
		// faceDataの座標のarray
		let coordinates = [];
		// 合格happyのカウンタ
		let passed_happy = 0;
		
		// 検出した顔を枠で囲む処理
		const setDetection = (faceDatum) => {
			for (let i = 0; i < faceDatum.length; i++) {
			let box = faceDatum[i].detection.box;
				x = box.x,
				y = box.y,
				w = box.width,
				h = box.height;

			coordinates.push(x);

			ctx.beginPath();
			ctx.rect(x, y, w, h);
			ctx.strokeStyle = '#76FF03';
			ctx.lineWidth = 2;
			ctx.stroke();
			}
		},

		// 笑顔の状態検出場所
		setExpressions = (faceDatum) => {
			for (let i = 0; i < faceDatum.length; i++) {
			let happy = faceDatum[i].expressions.happy;
			// バー顔色
			let color = happy * 150 + 100;
			// console.log(happy); 

			
			if (i == coordinates.indexOf(Math.max(...coordinates))) {
				// 笑顔判定（0.999までは軽く出る、調整必要）
				if (happy <= 0.9000) {
				emoticon1.style.bottom = (canvas.height - 40) * happy + 'px';
				} else if (happy < 0.90) {
				emoticon1.style.bottom = (canvas.height - 40) * 0.9 + 'px';
				} else {
				// 合格笑顔＋１
				passed_happy++;
				emoticon1.style.bottom = (canvas.height - 40) * 1 + 'px';
				}
				// emoticon1の色指定
				// emoticon1.style.backgroundColor = `rgb(${color}, ${color}, 100)`;
				if(happy > 0.5){
				emoticon1.innerHTML = emoticonTxt[0];
				}else{
				emoticon1.innerHTML = emoticonTxt[1];
				}

				// if (coordinates.indexOf(Math.min(...coordinates)) == 0) {
				// console.log(coordinates.indexOf(Math.min(...coordinates)));
				// emoticon2.style.bottom = 0+"px";
				// // emoticon2.style.backgroundColor = `rgb(${100}, ${100}, 100)`;
				// emoticon2.innerHTML = emoticonTxt[1];
				// }
				
			} else {
				// 笑顔判定（0.999までは軽く出る、調整必要）
				if (happy <= 0.9000) {
				emoticon2.style.bottom = (canvas.height - 40) * happy + 'px';
				} else if (happy < 0.90) {
				emoticon2.style.bottom = (canvas.height - 40) * 0.9 + 'px';
				} else {
				// 合格笑顔＋１
				passed_happy++;
				emoticon2.style.bottom = (canvas.height - 40) * 1 + 'px';
				}
				// emoticon2の色指定
				// emoticon2.style.backgroundColor = `rgb(${color}, ${color}, 100)`;
				if(happy > 0.5){
				emoticon2.innerHTML = emoticonTxt[0];
				}else{
				emoticon2.innerHTML = emoticonTxt[1];
				}
			}
			}
		};

		// 顔単位で笑顔状態描画
		setDetection(faceDatum);
		setExpressions(faceDatum);
		
		// この後笑顔値が合格なら何かしらreturnして処理終了。
		if (passed_happy == 2) {
		  // 繰り返し処理を解除
		  clearInterval(timer);
		  // 画面遷移
		  setTimeout(await function(){
			let camera = document.getElementById("camera");
			camera.className = "shutterArea";
			console.log('ok');
			window.location.href = '/stamp';
		  }, 2000);
		}
		}
	};

	init();
};
FACE.EXPRESSION();

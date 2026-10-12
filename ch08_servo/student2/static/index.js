const angleInput = document.getElementById("angle");
const message = document.getElementById("message");

document.getElementById("setAngle").addEventListener("click",async function (){
	const angle = angleInput.value;
	if (angle == "" || angle < 0 || angle>180){
		alert("0 ~ 180 사이의 각도를 입력하세요");
		return;
	};
	const response = await fetch("/api/angle", {
		method : "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ angle: angle })
	});
	const result = await response.json();

	if (!response.ok){
		alert(result.message);
		return;
	}
	message.textContent = result.message;
});

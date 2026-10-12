const led = document.getElementById("led");
const on = document.getElementById("on");
const off = document.getElementById("off");

// ON 버튼 (예시로 완성해둠)
on.addEventListener("click", function () {
    fetch("/on", { method: "POST" })
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            led.src = "/static/on.png";         // 2단계의 이 줄이 여기로 들어옴
        })
        .catch(error => {
            alert(error);
        });
});

// OFF 버튼
off.addEventListener("click", function () {
    fetch("/off", { method: "POST" })
	.then(response => {
		if(!response.ok){
			throw new Error("HTTP error " + response.status);
		}
		led.src = "/static/off.png";
	})
	.catch(error => {
		alert(error);
	});
});
// 페이지가 열리거나 새로고침될 때 LED 상태 확인
fetch("/status")
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json();
    })
    .then(data => {
        if (data.is_on) {
            led.src = "/static/on.png";
        } else {
            led.src = "/static/off.png";
        }
    })
    .catch(error => {
        alert(error);
    });

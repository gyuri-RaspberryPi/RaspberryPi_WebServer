const angleInput = document.getElementById("angle");
const message = document.getElementById("message");

document.getElementById("setAngle").addEventListener("click", async function () {
    const angle = angleInput.value;

    // 빈 값이거나 0~180 범위를 벗어나면 알림을 띄우고 종료
    if (angle === "" || angle < 0 || angle > 180) {
        alert("0 ~ 180 사이의 각도를 입력하세요");
        return;
    }

    // 서버에 각도 보내기
    const response = await fetch("/api/angle", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ angle: angle })
    });

    const result = await response.json();

    // 서버 응답이 실패하면 오류 메시지를 띄우고 종료
    if (!response.ok) {
        alert(result.message);
        return;
    }

    // 성공하면 서버가 보낸 메시지를 화면에 표시
    message.textContent = result.message;
});

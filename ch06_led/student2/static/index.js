document.addEventListener("DOMContentLoaded", function () {

    // LED 제어 요청 함수 (POST /on 또는 POST /off 로 요청)
    function control(color, state) {
        // 1. 클릭 즉시 이미지 URL 변경 (캐시/딜레이 방지)
        const img = document.getElementById(color);
        if (img) {
            img.src = "/static/" + color + "_" + state + ".png?t=";
        }

        // 2. 서버로 상태 전송
        fetch("/" + state, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "color=" + color
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            // 성공 시 DB 테이블 및 최종 상태 반영을 위해 화면 새로고침
            location.reload();
        })
        .catch(error => {
            alert(error);
        });
    }

    // 버튼 이벤트 연결 (red, green, blue)
    const colors = ["red", "green", "blue"];

    colors.forEach(color => {
        const onBtn = document.getElementById(color + "-on");
        const offBtn = document.getElementById(color + "-off");

        if (onBtn) {
            onBtn.addEventListener("click", function () {
                control(color, "on");
            });
        }

        if (offBtn) {
            offBtn.addEventListener("click", function () {
                control(color, "off");
            });
        }
    });

});

const todosBtn = document.getElementById("todos");
const data = document.getElementById("data");

todosBtn.addEventListener("click", function () {
    fetch("https://jsonplaceholder.typicode.com/todos?_limit=10")   // 브라우저가 직접 부름 (10개만)
        .then(function (response) {
            if (!response.ok) {
                throw new Error("HTTP 오류: " + response.status);
            }
            return response.json();             // JSON 글자 → 자바스크립트 배열
        })
        .then(function (todos) {
            let html = "";
            todos.forEach(todo => {
                html += `<tr><td>${todo.id}</td><td>${todo.title}</td><td>${todo.completed}</td></tr>`;
            });
            data.innerHTML = html;
        })
        .catch(function (error) {
            alert("todo를 불러오지 못함");
        });
});

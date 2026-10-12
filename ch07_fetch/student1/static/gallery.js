const gallery = document.getElementById("gallery");
const moreBtn = document.getElementById("more");

let page = 0;

// 사진 목록을 받아 화면에 붙임
function showPhotos(photos) {
    let html = "";
    photos.forEach(photo => {
        html += `
            <div class="card">
                <img src="${photo.img}" alt="${photo.title}">
                <p>${photo.title}</p>
            </div>
        `;
    });
    gallery.insertAdjacentHTML("beforeend", html);
}

function loadPhotos() {
    page = page + 1;

    fetch("/api/photos?page=" + page)
        .then(function (response) {
            if (!response.ok) {
                throw new Error("사진을 불러오지 못함");
            }

            return response.json();
        })
        .then(function (photos) {
            showPhotos(photos);
        })
        .catch(function (error) {
            alert("사진을 불러오지 못함");
        });
}
// 더 보기 버튼을 누르면 다음 페이지 불러오기
moreBtn.addEventListener("click", loadPhotos);

// 페이지를 처음 열었을 때 사진 불러오기
loadPhotos();

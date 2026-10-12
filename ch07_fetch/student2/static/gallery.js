const fakePhotos = [
    { title: "사진 1", img: "https://picsum.photos/seed/1/600" },
    { title: "사진 2", img: "https://picsum.photos/seed/2/600" },
    { title: "사진 3", img: "https://picsum.photos/seed/3/600" }
];

const gallery = document.getElementById("gallery");
const moreBtn = document.getElementById("more");

function showPhotos(photos){
	let html="";
	photos.forEach(photo =>{
		html += `
			<div class="col-4 mb-3">
    				<img src="${photo.img}" class="img-fluid">
    				<p>${photo.title}</p>
			</div>
		`;
	});
	gallery.insertAdjacentHTML("beforeend", html);
}
let page = 0;

function loadPhotos() {
	page = page + 1;
	fetch("/api/photos?page=" + page)
		.then(response => {
			if (!response.ok) throw new error ("HTTP 오류: " + response.status);
			return response.json();
		})
		.then(photos => { 
			showPhotos(photos);
		})
		.catch(function (error) {
			alert("사진을 불러오지 못함");
		});
}

moreBtn.addEventListener("click", loadPhotos);
loadPhotos();

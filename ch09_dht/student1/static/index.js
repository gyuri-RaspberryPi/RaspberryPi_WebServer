// 기록 목록으로 표를 다시 그림
function showRecords(records) {
    let html = "";
    records.forEach(r => {
        html += `<tr><td>${r.id}</td><td>${r.created_at}</td><td>${r.temperature}°C</td><td>${r.humidity}%</td></tr>`;
    });
    document.getElementById("table").innerHTML = html;
}
document.getElementById("now").addEventListener("click", async function () {
    const response = await fetch("/api/records", {
	    method: "POST"
    });
    const data = await response.json();

    if(!response.ok){
	alert(data, message);
	return;
    }

     showRecords([data]);
});

document.getElementById("record").addEventListener("click", async function () {
     const response = await fetch("/api/records");
     const data = await response.json();
     showRecords(data);
});

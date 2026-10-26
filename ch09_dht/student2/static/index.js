

// 기록 목록으로 표를 다시 그림
function showRecords(records) {
    let html = "";
    records.forEach(r => {
	    html+=`<tr class="${r.temperature >= 28 ? 'table-danger' : ''}"><td>${r.id}</td><td>${r.created_at}</td><td>${r.temperature}</td><td>${r.humidity}</td></tr>`;
	   });
    document.getElementById("table").innerHTML = html;
}

document.getElementById("now").addEventListener("click",async function () {
    const response = await fetch("/api/records", {
	    method: "POST",
	    headers: { "Content-Type": "application/json" }
    });
    const data = await response.json();

    if (!response.ok){
	    alert(data.message);
	    return;
    }
    showRecords([data]);
});

document.getElementById("record").addEventListener("click", async function () {
    const response = await fetch("/api/records", {
	    method : "GET",
    	    headers : { "Content-Type" : "application/json" }
    });
    const result =  await response.json();

    if (!response.ok){
	    alert(result.message);
	    return;
    }
    showRecords(result);
});

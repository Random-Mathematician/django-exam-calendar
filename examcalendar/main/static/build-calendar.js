function posMod(x, y) {
    // Modulo operator, positive on single underflow
    return (x+y)%y;
}

function buildAndInsertCalendar(...dateargs) {
    // Get selected time
    let now = new Date(...dateargs);

    // Print current month as calendar title
    let month = now.toLocaleString("gl-ES", {month: "long"});
    month += " " + now.getFullYear();
    document.getElementById("month-name").innerHTML = month[0].toUpperCase() + month.slice(1);

    // Virtualize calendar
    let cal = [];
    let firstMonthDay = new Date(now.getFullYear(), now.getMonth(), 1);
    let lastMonthDay = new Date(now.getFullYear(), now.getMonth()+1, 0);
    for (let i=posMod(firstMonthDay.getDay()-1,7); i>0; i--) {cal.push(null);} // Weekday padding
    for (let i=1; i<=lastMonthDay.getDate(); i++) {cal.push(i);} // Fill days
    let weekedCal = []; // Rearrange week by week
    do {week = cal.splice(0,7); weekedCal.push(week);} while (week.length>0)
    weekedCal = weekedCal.map(e => e.slice(0,5))
        .filter(e=>!e.every(f=>!f))
        .filter(e=>e.length!=0);

    // Create calendar DOM node
    let calendar = document.createElement("table");
    calendar.id = "calendar";
    calendar.innerHTML = `<tr>
    <th>LUN</th>
    <th>MAR</th>
    <th>MÉR</th>
    <th>XOV</th>
    <th>VEN</th>
    </tr>`;
    for (let week of weekedCal) {
        let tr = document.createElement("tr");
        for (let day of week) {
            let cell = document.createElement("td");
            cell.innerHTML = `${day}` ? day : "";
            tr.appendChild(cell);
        }
        calendar.appendChild(tr);
    }
    document.getElementById("calendar-container").appendChild(calendar);
}
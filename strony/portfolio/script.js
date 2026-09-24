const islandTime = document.querySelector("#islandTime");

function updateIslandTime() {
  islandTime.textContent = new Intl.DateTimeFormat([], {
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  }).format(new Date());
}

updateIslandTime();
setInterval(updateIslandTime, 1000);

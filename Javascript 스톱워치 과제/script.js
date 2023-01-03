let miliseconds = 0;
let sec, milisec;
let active = false;
const time = document.querySelector(".time");
const start = document.getElementById("start");
const stop = document.getElementById("stop");
const reset = document.getElementById("reset");

function resetClock() {
  active = false;
  miliseconds = 0;
  time.innerText = "00:00";
  console.log("reset");
}

function startClock() {
  if (active == true) {
    miliseconds++;
    time.innerText = printTime();
  }
}

start.addEventListener("click", () => {
  active = true;
  setInterval(startClock, 1000 / 60);
});

reset.addEventListener("click", resetClock());

// function stopClock() {}

// function clearRecord() {}

function printTime() {
  sec = parseInt(miliseconds / 60);
  milisec = miliseconds % 60;
  return String(sec).padStart(2, "0") + ":" + String(milisec).padStart(2, "0");
}

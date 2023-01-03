function resetClock() {
  const reset = document.getElementById("reset");
  const time = document.querySelector(".time");
  reset.addEventListener("click", () => {
    time.innerText = "00:00";
  });
  console.log("reset");
}

function startClock() {}

function stopClock() {
  const time = document.querySelector(".time");
}

function clearRecord() {}

resetClock();

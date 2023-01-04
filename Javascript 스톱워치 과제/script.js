let count = 0;
let active = false;

const time = document.querySelector(".time");
const start = document.getElementById("start");
const $stop = document.getElementById("stop");
const reset = document.getElementById("reset");
const $checkAll = document.querySelector("#check-all");
const clearBtn = document.querySelector(".clear");

function printTime() {
  let sec = parseInt(count / 60);
  let milisec = count % 60;
  time.textContent =
    String(sec).padStart(2, "0") + ":" + String(milisec).padStart(2, "0");
}

function startClock() {
  if (active) {
    count++;
    printTime();
    setTimeout(startClock, 1000);
  }
}

function resetClock() {
  time.textContent = "00:00";
  count = 0;
}

function stopClock() {
  active = false;
  const record = time.textContent;
  const li = document.createElement("li");

  let checkbox = document.createElement("input");
  checkbox.setAttribute("type", "checkbox");
  checkbox.setAttribute("class", "check");
  const text = document.createTextNode(record);

  li.appendChild(checkbox);
  li.appendChild(text);
  document.getElementById("record-list").appendChild(li);
}

function allCheckRecord() {
  const $check = document.querySelectorAll(".check");

  let checkTurn = false;
  for (let i = 0; i < $check.length; i++) {
    if (!$check[i].checked) {
      checkTurn = true;
    }
  }

  for (let j = 0; j < $check.length; j++) {
    if (checkTurn) {
      $check[j].checked = true;
    } else {
      $check[j].checked = false;
    }
  }
}

function removeRecord() {
  const $check = document.querySelectorAll(".check");

  for (let i = 0; i < $check.length; i++) {
    if ($check[i].checked) {
      $check[i].parentElement.remove();
    }
  }
}

start.addEventListener("click", () => {
  active = true;
  startClock();
});

$stop.addEventListener("click", () => {
  stopClock();
});

reset.addEventListener("click", () => {
  resetClock();
});

$checkAll.addEventListener("click", () => {
  allCheckRecord();
});

clearBtn.addEventListener("click", () => {
  removeRecord();
});

let count = 0;
let active = false;

const time = document.querySelector(".time");
const start = document.getElementById("start");
const $stop = document.getElementById("stop");
const reset = document.getElementById("reset");
const $checkAll = document.querySelector("#check-all");
const clearBtn = document.querySelector(".clear");

function printTime(count) {
  let sec = parseInt(count / 1000);
  let milisec = parseInt(count / 100) % 100;
  time.textContent =
    String(sec).padStart(2, "0") + ":" + String(milisec).padStart(2, "0");
}

function startClock() {
  if (active) {
    count++;
    printTime(count);
    timerId = setTimeout(startClock, 1);
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

// function clearRecord() {
//   const recordList = document.getElementById("record-list");
//   recordList.forEach((element) => {
//     console.log(element);
//   });
// }

// const clear = document.querySelector(".clear");

// clear.addEventListener("click", () => {
//   clearRecord();
// });

// let miliseconds = 0;
// let sec, milisec;
// let active = false;
// const time = document.querySelector(".time");
// const start = document.getElementById("start");
// const stop = document.getElementById("stop");
// const reset = document.getElementById("reset");

// function resetClock() {
//   active = false;
//   miliseconds = 0;
//   reset.addEventListener("click", resetClock());
//   time.innerText = "00:00";
//   console.log("reset");
// }

// function startClock() {
//   if (active == true) {
//     miliseconds++;
//     time.innerText = printTime();
//   }
// }

// resetClock();

// reset.addEventListener("click", resetClock());

// // function stopClock() {}

// // function clearRecord() {}

// function printTime() {
//   sec = parseInt(miliseconds / 1000);
//   milisec = miliseconds % 1000;
//   return String(sec).padStart(2, "0") + ":" + String(milisec).padStart(2, "0");
// }

// start.addEventListener("click", () => {
//   active = true;
//   setInterval(startClock, 1);
// });

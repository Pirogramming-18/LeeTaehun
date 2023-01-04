let count = 0;
let active = false; //flag for start and stop interaction

//set as a variable for convenience
const $time = document.querySelector(".time");
const $start = document.getElementById("start");
const $stop = document.getElementById("stop");
const $reset = document.getElementById("reset");
const $checkAll = document.querySelector("#check-all");
const $clearBtn = document.querySelector(".clear");

// represent minutes and seconds in text
function printTime() {
  let min = parseInt(count / 60);
  let sec = count % 60;
  $time.textContent =
    String(min).padStart(2, "0") + ":" + String(sec).padStart(2, "0");
}

// start button eventHandler
function startClock() {
  if (active) {
    count++;
    printTime();
    setTimeout(startClock, 1000); //startClock call itself recursive per 1 second
  }
}

// reset button eventHandler
function resetClock() {
  $time.textContent = "00:00";
  count = 0;
}

// stop button eventHandler
function stopClock() {
  active = false; // stop recursion of startClock()
  // store current time record
  const timeRecord = $time.textContent;
  const text = document.createTextNode(timeRecord);

  // make a list element with checkbox type input
  const li = document.createElement("li");
  let checkbox = document.createElement("input");
  checkbox.setAttribute("type", "checkbox");
  checkbox.setAttribute("class", "check");

  //add list element
  li.appendChild(checkbox);
  li.appendChild(text);
  document.getElementById("record-list").appendChild(li);
}

// all check eventHandler
function allCheckRecord() {
  const $check = document.querySelectorAll(".check"); //list with checkbox

  let checkTurn = false; //all check flag
  for (let i = 0; i < $check.length; i++) {
    // all check case
    if (!$check[i].checked) {
      checkTurn = true;
    }
  }

  // all uncheck case
  for (let j = 0; j < $check.length; j++) {
    if (checkTurn) {
      $check[j].checked = true;
    } else {
      $check[j].checked = false;
    }
  }
}

//remove record eventHandler
function removeRecord() {
  const $check = document.querySelectorAll(".check");

  for (let i = 0; i < $check.length; i++) {
    if ($check[i].checked) {
      $check[i].parentElement.remove();
    }
  }
}

// link eventHandler to each button
$start.addEventListener("click", () => {
  active = true;
  startClock();
});

$stop.addEventListener("click", () => {
  stopClock();
});

$reset.addEventListener("click", () => {
  resetClock();
});

$checkAll.addEventListener("click", () => {
  allCheckRecord();
});

$clearBtn.addEventListener("click", () => {
  removeRecord();
});

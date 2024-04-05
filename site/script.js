const ball = document.getElementById('ball');
const bodyWidth = document.body.clientWidth;
const bodyHeight = document.body.clientHeight;
const ballWidth = ball.offsetWidth;
const ballHeight = ball.offsetHeight;
const maxX = bodyWidth - ballWidth;
const maxY = bodyHeight - ballHeight;
const speedX = 2;
const speedY = 2;

let posX = 0;
let posY = 0;
let directionX = 1;
let directionY = 1;

function moveBall() {
  posX += speedX * directionX;
  posY += speedY * directionY;
  
  if (posX >= maxX || posX <= 0) {
    directionX *= -1;
  }
  
  if (posY >= maxY || posY <= 0) {
    directionY *= -1;
  }
  
  ball.style.top = posY + 'px';
  ball.style.left = posX + 'px';
  
  requestAnimationFrame(moveBall);
}

moveBall();


// Define the target date (YYYY-MM-DD format)
const targetDate = new Date('2024-04-03');

// Get the current date
const currentDate = new Date();

// Set both dates to the start of the day to avoid issues with timezones
targetDate.setHours(0, 0, 0, 0);
currentDate.setHours(0, 0, 0, 0);

// Calculate the difference in days between the current date and target date
const differenceInDays = Math.floor((currentDate - targetDate) / (1000 * 3600 * 24)) + 1;

// Display the number of days since the target date
document.getElementById('counter').textContent = `Day ${differenceInDays}`;

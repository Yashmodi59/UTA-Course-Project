// Student ID : 1002086296
// Name: Yash Modi

// Define global variables
let court, balls, ballSpeed, animationInterval, isAnimating;
isAnimating = false;

// Function to initialize the animation
function initialize() {
  // Function initialize is used to initialize the variable as well clearing the court
  // First clear the court
  // Add first ball in the court

  court = document.getElementById("court"); // get the court using Id: Court
  balls = []; // initialize the balls array
  ballSpeed = 0; // 0: slowest, 1: medium, 2: fastest
  clearCourt(); // Clear the court
  setBallNum(); // set  ball num will add the number of balls get from the 
}

function setBallNum() {
  // Function to set the number of soccer balls
  // if (!isAnimating) {
    const numBalls = parseInt(document.getElementById("ballNums").value); //parsing the number of ball using get element by id "ball nums"
    clearCourt(); // clear the court
    createBalls(numBalls); // generate the number of balls get in court 
  // }
}
function getRandomAngle(){ // get random angle between 0 to 360
  return angle = Math.random() * 2 * Math.PI;
}
function getRandomSpeed(){ // get random speed according to ballspeed
 return (Math.random() * (ballSpeed + 1) * 2 - ballSpeed);
}
function setSpeed(speed) {
  // Function to set the ball speed
  ballSpeed = speed;
  // speedVxForAll = getRandomSpeed(ballSpeed);
  // speedVyForAll = getRandomSpeed(ballSpeed);
  // balls.forEach(ball => {
  //   ball.vx = speedVxForAll;
  //   ball.vy = speedVyForAll;
  // });

}

function resumeOrSuspend(event) {
  // Function to resume or suspend the animation
  // check if it is animating than clear the interval else start animation
  if (isAnimating) { 
    clearInterval(animationInterval);  // clearing the interval which we have set in start animation function
  } else {
    startAnimation(); // called function
  }
  isAnimating = !isAnimating;
}


function clearCourt() { // Function to clear the court which we have initialized in beginning or in between 
  while (court.firstChild) { // remove all the child till we find court empty
    court.removeChild(court.firstChild); // removing the child
  }
}

function createBall() { // Function to create a single ball element
  // creaate the ball element set the src, height, position, left and top cordinates
  const ball = document.createElement("img"); // create image element
  ball.src = "soccer-ball.gif"; // initialize the source
  ball.style.position = "absolute"; // set absolute position if we are changing to relative then remove offset in get random function and change many thing
  ball.style.height = "40px"; // initialize the height to 40 
  ball.style.left = getRandomLeftPixel() + "px"; // call the function append "px" 
  ball.style.top = getRandomTopPixel() + "px"; // call the function append "px" 
  console.log("initial",ball.style.top,ball.style.left); 
  return ball; // return ball element
}

function getRandomTopPixel() { // 600 is client height so -40 for the ball height so range of it from (560, offsetTopValue) 
  return Math.floor(Math.random() * (560 - court.offsetTop + 1)) + court.offsetTop;
}

function getRandomLeftPixel() { // 1000 is client width so -40 for the ball height so range of it from (960, offsetLeftValue) 
  return Math.floor(Math.random() * (960 - court.offsetLeft + 1)) + court.offsetLeft;
}


function createBalls(numBalls) { // Function to create multiple soccer element by iterating the loop till it go to numballs
  initialSpeed = getRandomSpeed(); // get random speed bassed on ballspeed
  let i = 0; // initialize for iteration
  while(i<numBalls){ // iterate till i < numBalls
  // for (let i = 0; i < numBalls; i++) {
    const ball = createBall(); // get one ball 
    // const dt = 10 * (3 - ballSpeed); // Adjust speed
    court.appendChild(ball); // appending each ball element created to the court
    console.log(i); // log function for debug
    angle = getRandomAngle(); // get random angle ranging 0,360 to move in random direction with same speed
    // console.log("sx",speedX,speedY);
    // add each ball to balls array
    balls.push({
      id:i,//set id 
      element: ball, //set html element
      vx: initialSpeed * Math.cos(angle),// set random velocity by multiply initial speed with costheta for X coordinate 
      vy: initialSpeed * Math.sin(angle)// set random velocity by multiply initial speed with costheta for Y coordinate
    });
    i++; // increment i
  }
}

// iterate each ball in balls array
// get left,right,top,bottom pixel values
// update left co-ordinate value by X = X + vx*dt; and top co-ordiante by Y= Y+ vy*dt
// check for collision with the walls if yes upadte X,Y and vx,vy value accordingly
// check Ball for the collission and upadte the co-ordinated

function updateBalls(ballSpeed) { // Function to move the position of the soccer balls
  balls.forEach((ball,index) => { 
    let x = parseInt(ball.element.style.left.slice(0, -2)); // get left only in integer value so slice it from the back by -2 and parse it with parseInt
    let y = parseInt(ball.element.style.top.slice(0, -2)); // get top only in integer value so slice it from the back by -2 and parse it with parseInt
    const court = document.getElementById("court"); // getelementbyd get courd
    const courtLeft = court.offsetLeft; // get the length of left white space
    const courtTop = court.offsetTop; // get the length of upper white space
    speedDt= (ballSpeed*10) + 10; // dt value changing with ball speed

    // Update position based on speed and direction
    // const dt = 10 * (3 - ballSpeed); // Adjust speed
    // console.log(rect.top,rect.left,rect.right,rect.bottom);
    // console.log(x,y,ballSpeed,'vx',ball.vx,'vy',ball.vy);
    // console.log(x+ball.vx*dt,y+ball.vy*dt);
    console.log('1i',index,x,y,ballSpeed,speedDt);
    x = x + ball.vx * speedDt ; // update x with given formula
    y = y + ball.vy * speedDt ; // update y with given formula
    console.log(index,x,y);

    // code for collisions with walls
    // call each left right top bottom method 
    const ballWidth = 40; //  the ball width is 40px
    checkForLeftWall(); //for left wall
    checkForRightWall(); // for right wall
    // checkBottomOrRightWall(courtTop,court.clientHeight,y,ball.vy);
    checkForTopWall(); // for top wall
    checkForBottomWall(); // for bottom wall
    ball.element.style.left = x + "px"; // set the x value to ball style
    ball.element.style.top = y + "px"; // set the x value to ball style

    // function checkBottomOrRightWall(offset,size,coordinate,ballVelocity){
    //   if (coordinate > offset + size - 40){
    //     ballVelocity = -ballVelocity;
    //     coordinate = 2 * (offset+size-40) - coordinate -1;
    //   }
    // }

    function checkForBottomWall() { // bottom wall
      // if y value greater than boundary that is court top offset value + total court height - ball width (40) 
      // change  the direction of ball opposite
      // change y value to  2*height-y
      if (y > courtTop + court.clientHeight - ballWidth) { // compare
        ball.vy = -ball.vy; // change dir
        y = 2 * (courtTop + court.clientHeight - ballWidth) - y - 1; // update y value
      }
    }

    function checkForTopWall() { // Top wall
      // if y value less than boundary that is court top offset  
      // change  the direction of ball 
      // change y value to court top offset value

      if (y < courtTop) { // compare
        ball.vy = -ball.vy; // change dir
        y = courtTop + 1; // update y 
      }
    }

    function checkForRightWall() {
      // if x value greater than boundary that is court left offset value + total court widhth - ball width (40) 
      // change  the direction of ball opposite
      // change x value to  2*width-x
      if (x > courtLeft + court.clientWidth - ballWidth) { // compare
        ball.vx = -ball.vx; // change dir
        x = 2 * (courtLeft + court.clientWidth - ballWidth) - x - 1; // update
      }
    }

    function checkForLeftWall() {
      // if y value less than boundary that is court left offset  
      // change  the direction of ball opposite
      // change x value to court top offset value
      if (x < courtLeft) { // compare
        ball.vx = -ball.vx; // change dir
        x = courtLeft + 1; // update
      }
    }
  });

  // use iterative function to check for collisions between balls
  checkBallCollission(); 
}

// To check is the pixel value get overlaped by each other or not
// write a two loop to check for each balls
// for right check the ball1 right greater than ball2 left 
// for left check the ball1 left smaller than ball2 right 
// for bottom check the ball1 bottom greater than ball2 top 
// for top check the ball1 top smaller than ball2 bottom 

function checkBallCollission() {
  // iterate all balls in array
  for (let i = 0; i < balls.length; i++) {
    for (let j = i + 1; j < balls.length; j++) {
      const ball1 = balls[i]; // first ball
      const ball2 = balls[j]; // second ball
      const rect1 = ball1.element.getBoundingClientRect(); // get all co-ordinate for first ball
      const rect2 = ball2.element.getBoundingClientRect(); // get all co-ordinate for second ball

      if (checkForleftAndRightBoundaryOfBall(rect1, rect2) &&
        checkForTopAndBottomBoundaryOfBall(rect1,rect2)) { // call the function to check the collision
        exchangeVelocity(ball1, ball2);         // Collision detected, exchange velocities
      }
    }
  }
}
function checkForTopAndBottomBoundaryOfBall(rect1, rect2) {
  // if the ball1 bottom greater than ball2 top and ball1 top smaller than ball2 bottom return true
  return rect1.bottom > rect2.top &&
    rect1.top < rect2.bottom;
}

function checkForleftAndRightBoundaryOfBall(rect1, rect2) { 
  // if the  ball1 right greater than ball2 left and the ball1 left smaller than ball2 right
  return rect1.right > rect2.left &&
    rect1.left < rect2.right;
}

function exchangeVelocity(ball1, ball2) {
  // Exchange the velocity of both the ball using destructuring assignment  
  [ball1.vx,ball2.vx] = [ball2.vx,ball1.vx] // swap vx value
  [ball1.vy,ball2.vy] = [ball2.vy,ball1.vy] // swap vy value
}

// Function to start the animation using setInterval and time will be change according to ball speed as well
function startAnimation() {
  animationInterval = setInterval(() => { // first argument  call updateBall function and second will be time function
    updateBalls(ballSpeed); // call update function
  }, 100 - 20 * (ballSpeed + 1));
}

// Initialize the animation on page load
window.onload = initialize; // use to load 

// Assignment Goals:
//     If the car’s speed is less than 70 -> print "Ok".
//     If the car’s speed is 70 or more:
//        a. For every 5 km more than 70, give 1 demerit point and then print number of demerit points "Points: X".
//           e.g. 80 - 70 = 10 >>> 10/5 = 2 Demerit Points 
//        b. If the points are more than 12, print "License Suspended".

function checkSpeed(speed) {

  // Step 1: If speed is less than 70

  if (speed < 70) {
    console.log("Ok"); // Print "Ok"
  } else {

    // Step 2: Calculate how many points the driver gets
    // Math.floor() is an in-built method that makes sure we get a whole number (no decimals)
        let points = Math.floor((speed - 70) / 5); 
  

    // Step 3: If points are more than 12, license is suspended
        if (points > 12) {
            console.log("License suspended");
        } else {
      // Otherwise, just print how many points they have
            console.log("Points:", points);
    }
  }
}


// --- Example runs ---
// If speed is 80 -> "Points: 2"
checkSpeed(80);

// If speed is 65 -> "Ok"
checkSpeed(65);

// If speed is 135 -> "License suspended"
checkSpeed(135);
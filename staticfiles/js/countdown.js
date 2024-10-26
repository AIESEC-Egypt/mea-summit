const countdownDate = new Date("2024-09-29T23:59:59").getTime();

// Update the countdown every 1 second
function startCountdown() {
  const x = setInterval(function () {
    // Get the current date and time
    const now = new Date().getTime();

    // Calculate the remaining time
    const distance = countdownDate - now;

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the countdown div
    document.getElementById("countdown").innerHTML =
      days + " Days " + hours + " Hours " + minutes + " Minutes " + seconds + " Seconds";

    // If the countdown is over, display a message
    if (distance < 0) {
      clearInterval(x);
      document.getElementById("countdown").innerHTML = "REGISTRATION IS CLOSED!";
    }
  }, 1000);
}

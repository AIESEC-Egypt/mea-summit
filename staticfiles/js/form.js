document.getElementById('nextButton').addEventListener('click', function() {
  document.getElementById('step1').style.display = 'none';
  document.getElementById('step2').style.display = 'block';
});

function showPage(step) {
  if (step === 1) {
    document.getElementById('step1').style.display = 'block';
    document.getElementById('step2').style.display = 'none';
  }
}

// Function to validate all fields in the current step
function validateStep(step) {
  let isValid = true;
  
  // Select all input, select, and file elements in the current step
  let fields = document.querySelectorAll(`#${step} input, #${step} select`);
  
  fields.forEach(function(field) {
    // Check if the field is required and empty
    if (field.hasAttribute('required')) {
      console.log(`Validating field: ${field.name}, value: ${field.value}`);

      // Special check for date input fields
      if (field.type === 'date' && field.value === "") {
        field.classList.add('error');
        console.log(`${field.name} (date) is empty.`);
        isValid = false;
      } 
      // Check for file input
      else if (field.type === 'file' && field.files.length === 0) {
        field.classList.add('error');
        console.log(`${field.name} (file) is empty.`);
        isValid = false;
      } 
      // Check for other input types (text, email, etc.)
      else if (field.value.trim() === "") {
        field.classList.add('error');
        console.log(`${field.name} is empty.`);
        isValid = false;
      } else {
        field.classList.remove('error');
        console.log(`${field.name} is valid.`);
      }
    }
  });

  return isValid;
}

// Next button for Step 1 to Step 2
document.getElementById('nextButton').addEventListener('click', function() {
  if (validateStep('step1')) {
    console.log('Step 1 validated successfully. Moving to Step 2.');
    document.getElementById('step1').style.display = 'none';
    document.getElementById('step2').style.display = 'block';
  } else {
    console.log('Step 1 validation failed.');
  }
});

// Next button for Step 2 to Step 3
document.getElementById('nextButton1').addEventListener('click', function() {
  if (validateStep('step2')) {
    console.log('Step 2 validated successfully. Moving to Step 3.');
    document.getElementById('step2').style.display = 'none';
    document.getElementById('step3').style.display = 'block';
  } else {
    console.log('Step 2 validation failed.');
  }
});


function showPage(step) {
  if (step === 1) {
    document.getElementById('step1').style.display = 'block';
    document.getElementById('step2').style.display = 'none';
  }
    if (step === 2) {
      document.getElementById('step2').style.display = 'block';
      document.getElementById('step3').style.display = 'none';
    }
}


// Get elements
const modal = document.getElementById('privacyModal');
const sexualModal = document.getElementById('modal-content');
const subtanceModal = document.getElementById('modal-content1');
const sexualLink = document.getElementById('sexualLink');
const subtanceLink = document.getElementById('subtanceLink');
const closeModal = document.querySelector('.close');
const close = document.getElementById('close');
const submitButton = document.getElementById('submitButton');
const privacyCheckbox = document.getElementById('privacyCheckbox');

// Show the modal when the privacy policy link is clicked
sexualLink.addEventListener('click', function(event) {
  event.preventDefault();
  sexualModal.style.display = 'block';
  modal.style.display = 'block';

});

subtanceLink.addEventListener('click', function(event) {
  event.preventDefault();
  subtanceModal.style.display = 'block';
  modal.style.display = 'block';
});

// Close the modal when the close button is clicked
closeModal.addEventListener('click', function() {
  sexualModal.style.display = 'none';
  modal.style.display = 'none';

});

// Close the modal when the user clicks outside of the modal content
window.addEventListener('click', function(event) {
  if (event.target == modal) {
    sexualModal.style.display = 'none';
    modal.style.display = 'none';

  }
});
// Close the modal when the close button is clicked
closeModal.addEventListener('click', function() {
  subtanceModal.style.display = 'none';
  modal.style.display = 'none';

});

// Close the modal when the user clicks outside of the modal content
window.addEventListener('click', function(event) {
  if (event.target == modal) {
    subtanceModal.style.display = 'none';
    modal.style.display = 'none';

  }
});
// Validate checkbox before submission
submitButton.addEventListener('click', function(event) {
  if (!privacyCheckbox.checked) {
    alert('Please accept the Privacy Policy to proceed.');
    event.preventDefault();
  }
});

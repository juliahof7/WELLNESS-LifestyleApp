// Mock search function
function searchClasses() {
    const searchTerm = document.getElementById('classSearch').value;
    const results = document.getElementById('classResults');

    results.innerHTML = `<p>Showing results for: ${searchTerm}</p>`;
}

// Handle workout logging
document.getElementById('workoutForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const type = document.getElementById('workoutType').value;
    const duration = document.getElementById('workoutDuration').value;
    const date = document.getElementById('workoutDate').value;

    const log = document.getElementById('workoutLog');
    const workoutEntry = `<p>Workout: ${type}, Duration: ${duration} minutes, Date: ${date}</p>`;
    
    log.innerHTML += workoutEntry;
    this.reset();
});

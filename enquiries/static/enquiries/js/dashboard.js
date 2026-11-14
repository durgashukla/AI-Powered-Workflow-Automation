
// Get Category Data from Django
const categoryData = JSON.parse(
    document.getElementById('category-data').textContent
);

// Extract Category Labels and Values
const categoryLabels = categoryData.map(item => item.label);
const categoryValues = categoryData.map(item => item.total);


// Create Category Doughnut Chart
new Chart(document.getElementById('categoryChart'), {

    type: 'doughnut',

    data: {
        labels: categoryLabels,

        datasets: [{
            label: 'Total Enquiries',

            data: categoryValues,

            backgroundColor: [
                '#2563eb',
                '#06b6d4',
                '#8b5cf6',
                '#f59e0b',
                '#10b981',
                '#ef4444',
                '#64748b'
            ],

            borderWidth: 2
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false
    }

});


// Get Priority Data from Django
const priorityData = JSON.parse(
    document.getElementById('priority-data').textContent
);

// Extract Priority Labels and Values
const priorityLabels = priorityData.map(item => item.label);
const priorityValues = priorityData.map(item => item.total);


// Create Priority Bar Chart
new Chart(document.getElementById('priorityChart'), {

    type: 'bar',

    data: {
        labels: priorityLabels,

        datasets: [{
            label: 'Number of Enquiries',

            data: priorityValues,

            backgroundColor: [
                '#10b981',
                '#f59e0b',
                '#ef4444'
            ],

            borderRadius: 6
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        scales: {
            y: {
                beginAtZero: true,

                ticks: {
                    precision: 0
                }
            }
        }
    }

});

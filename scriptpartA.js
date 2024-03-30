// script.js

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('diceForm');
    const resultsDiv = document.getElementById('results');
    const combinationsTable = document.getElementById('combinationsTable');
    const probabilitiesTable = document.getElementById('probabilitiesTable');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const dieA = document.getElementById('dieA').value;
        const dieB = document.getElementById('dieB').value;

        fetch(`/roll-dice?dieA=${dieA}&dieB=${dieB}`)
            .then(response => response.json())
            .then(data => {
                updateResults(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    function updateResults(data) {
        combinationsTable.innerHTML = `
            <tr>
                <th>Sum</th>
                <th>Frequency</th>
            </tr>
        `;
        probabilitiesTable.innerHTML = `
            <tr>
                <th>Sum</th>
                <th>Probability</th>
            </tr>
        `;

        for (const [sum, frequency] of Object.entries(data.combinations)) {
            combinationsTable.innerHTML += `
                <tr>
                    <td>${sum}</td>
                    <td>${frequency}</td>
                </tr>
            `;
        }

        for (const [sum, probability] of Object.entries(data.probabilities)) {
            probabilitiesTable.innerHTML += `
                <tr>
                    <td>${sum}</td>
                    <td>${probability.toFixed(4)}</td>
                </tr>
            `;
        }

        resultsDiv.style.display = 'block';
    }
});

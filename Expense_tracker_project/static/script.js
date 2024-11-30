document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const filterSelect = document.getElementById('filterSelect');
    const table = document.getElementById('expenseTable');
    const rows = Array.from(table.getElementsByTagName('tbody')[0].getElementsByTagName('tr'));

    searchInput.addEventListener('input', () => {
        const searchTerm = searchInput.value.toLowerCase();
        rows.forEach(row => {
            const description = row.cells[1].textContent.toLowerCase();
            row.style.display = description.includes(searchTerm) ? '' : 'none';
        });
    });

    filterSelect.addEventListener('change', () => {
        const filterValue = filterSelect.value;
        const tbody = table.getElementsByTagName('tbody')[0];
        const sortedRows = [...rows];

        if (filterValue === 'date') {
            sortedRows.sort((a, b) => new Date(a.cells[0].textContent) - new Date(b.cells[0].textContent));
        } else if (filterValue === 'alphabet') {
            sortedRows.sort((a, b) => a.cells[1].textContent.localeCompare(b.cells[1].textContent));
        } else if (filterValue === 'price') {
            sortedRows.sort((a, b) => parseFloat(a.cells[3].textContent) - parseFloat(b.cells[3].textContent));
        }

        tbody.innerHTML = '';
        sortedRows.forEach(row => tbody.appendChild(row));
    });
});
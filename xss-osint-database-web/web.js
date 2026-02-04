document.addEventListener('DOMContentLoaded', function () {
    let databases = [];
    let currentSort = 'name';

    const databasesList = document.getElementById('databasesList');
    const modal = document.getElementById('databaseModal');
    const closeModalBtn = document.getElementById('closeModal');
    const closeModalBtn2 = document.getElementById('closeModalBtn');
    const modalTitle = document.getElementById('modalTitle');
    const modalCount = document.getElementById('modalCount');
    const modalDesc = document.getElementById('modalDesc');
    const requestAccessBtn = document.getElementById('requestAccessBtn');

    fetchDatabases();

    async function fetchDatabases() {
        try {
            const response = await fetch('/api/databases');
            databases = await response.json();
            displayDatabases(databases);
        } catch (error) {
            console.error('Error fetching databases:', error);
            databasesList.innerHTML = '<div class="error">Ошибка загрузки данных</div>';
        }
    }

    function displayDatabases(dbs) {
        databasesList.innerHTML = '';

        if (dbs.length === 0) {
            databasesList.innerHTML = '<div class="no-results">Базы данных не найдены</div>';
            return;
        }

        const sortedDbs = sortDatabases(dbs, currentSort);

        sortedDbs.forEach(db => {
            const card = document.createElement('div');
            card.className = 'database-card';
            card.innerHTML = `
                <h3>
                    ${db.name}
                    <span class="database-count">${db.count}</span>
                </h3>
                <p class="database-desc">${db.desc}</p>
                <div class="database-meta">
                    <span class="database-type">${getDatabaseType(db.name)}</span>
                    <span class="database-access">Premium</span>
                </div>
            `;

            card.addEventListener('click', () => openModal(db));
            databasesList.appendChild(card);
        });
    }

    function getDatabaseType(name) {
        if (name.includes('банк') || name.includes('Банк')) return 'Финансы';
        if (name.includes('сотрудник') || name.includes('персонал')) return 'Персонал';
        if (name.includes('клиент') || name.includes('пользователь')) return 'Клиенты';
        if (name.includes('авиа') || name.includes('железнодорож')) return 'Транспорт';
        if (name.includes('медицин') || name.includes('лаборатор')) return 'Медицина';
        if (name.includes('соц') || name.includes('сеть') || name.includes('VK')) return 'Соцсети';
        return 'Данные';
    }

    function sortDatabases(dbs, sortBy) {
        return [...dbs].sort((a, b) => {
            if (sortBy === 'name') {
                return a.name.localeCompare(b.name);
            } else if (sortBy === 'count') {
                const countA = parseCount(a.count);
                const countB = parseCount(b.count);
                return countB - countA;
            }
            return 0;
        });
    }

    function parseCount(countStr) {
        if (!countStr || countStr === 'неизв') return 0;

        const str = countStr.toLowerCase();
        const num = parseFloat(str.replace(/[^0-9.]/g, ''));

        if (str.includes('млн') || str.includes('million')) return num * 1000000;
        if (str.includes('тыс') || str.includes('thousand')) return num * 1000;
        if (str.includes('~')) return num * 1000000;
        if (str.includes('b') || str.includes('млрд')) return num * 1000000000;

        return num;
    }

    function openModal(db) {
        modalTitle.textContent = db.name;
        modalCount.textContent = db.count;
        modalDesc.textContent = db.desc;
        modal.style.display = 'flex';
    }

    function closeModal() {
        modal.style.display = 'none';
    }

    closeModalBtn.addEventListener('click', closeModal);
    closeModalBtn2.addEventListener('click', closeModal);

    requestAccessBtn.addEventListener('click', () => {
        alert('Функция запроса доступа находится в разработке');
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
});

const API_NUVEM = ""; 
const API_MYSQL = "";

const tbodyNuvem = document.querySelector(".table-nuvem tbody");
const tbodySql = document.querySelector(".table-sql tbody");
const btn = document.querySelector(".btn-leitura");

async function atualizaTableNuvem() {
    try {
        const response = await fetch(API_NUVEM);
        const data = await response.json();

        tbodyNuvem.innerHTML = ""; 

        data.forEach(dados => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${dados.id || '--'}</td>
                <td>${dados.created_at || '--'}</td>
                <td>${dados.entry_id || '--'}</td>
                <td>${dados.field1 || '°C'}°C</td>
                <td>${dados.field2 || '%'}%</td>
            `;
            tbodyNuvem.appendChild(tr);
        });
    } catch (error) {
        console.error("Erro ao buscar os dados do ThingSpeak:", error);
    }
}

async function atualizaTableSql() {
    try {
        const response = await fetch(API_MYSQL);
        const data = await response.json();

        tbodySql.innerHTML = ""; 

        data.forEach(dados => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${dados.id}</td>
                <td>${dados.entry}</td>
                <td>${dados.data}</td>
                <td>${dados.temperatura}°C</td>
                <td>${dados.umidade}%</td>
            `;
            tbodySql.appendChild(tr);
        });
    } catch (error) {
        console.error("Erro ao buscar os dados do MySQL:", error);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    atualizaTableNuvem();
    atualizaTableSql();

    btn.addEventListener('click', async () => {
        btn.textContent = "Carregando...";
        btn.disabled = true;

        await (atualizaTableNuvem(), atualizaTableSql());

        btn.textContent = "Nova Leitura";
        btn.disabled = false;
    });

});
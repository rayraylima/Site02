function filterDivs() {
    const searchValue = document.getElementById('search-bar').value.toLowerCase();
    const divs = document.querySelectorAll('.produto-item');

    divs.forEach(div => {
        if (div.textContent.toLowerCase().includes(searchValue)) {
            div.classList.remove('hidden');
        } else {
            div.classList.add('hidden');
        }
    });
}
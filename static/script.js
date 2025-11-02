// fetch medicine list from backend API
fetch('/api/medicines')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('medicine-list');
    container.innerHTML = '';

    data.forEach(med => {
      const li = document.createElement('li');
      li.className = 'list-item';
      li.innerHTML = `<span class="name">${med.name}</span> <span class="price">$${med.price}</span>`;
      container.appendChild(li);
    });
  })
  .catch(err => console.error('Error:', err));

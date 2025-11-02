fetch("/api/medicines")
  .then(res => res.json())
  .then(data => {
    const box = document.getElementById("medicine-container");

    data.medicines.forEach(m => {
      const row = document.createElement("div");
      row.innerHTML = `<b>${m.name}</b> – $${m.price.toFixed(2)}`;
      box.appendChild(row);
    });
  })
  .catch(err => console.error(err));

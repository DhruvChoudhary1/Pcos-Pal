document.getElementById('pcos-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const formData = new FormData(this);

  const data = {
    age: Number(formData.get("age")),
    bmi: Number(formData.get("bmi")),
    menstrual_irregularity: Number(formData.get("menstrual_irregularity")),
    testosterone: Number(formData.get("testosterone")),
    follicle_count: Number(formData.get("follicle_count"))
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById('result').textContent = result.result || result.error;

  } catch (error) {
    document.getElementById('result').textContent = "Error: " + error.message;
  }
});

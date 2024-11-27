document.getElementById("calculate-btn").addEventListener("click", async () => {
    const formData = {
        income: parseFloat(document.getElementById("income").value),
        savings: parseFloat(document.getElementById("savings").value),
        food: parseFloat(document.getElementById("food").value),
        travel: parseFloat(document.getElementById("travel").value),
        education: parseFloat(document.getElementById("education").value),
        entertainment: parseFloat(document.getElementById("entertainment").value),
        utilities: parseFloat(document.getElementById("utilities").value),
        groceries: parseFloat(document.getElementById("groceries").value),
        healthcare: parseFloat(document.getElementById("healthcare").value),
        loan_payments: parseFloat(document.getElementById("loan_payments").value),
        credit_card_spending: parseFloat(document.getElementById("credit_card_spending").value),
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/score", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error("Error calculating financial score");
        }

        const result = await response.json();

        document.getElementById("financial-score").textContent = `Financial Score: ${result.financial_score}`;
        document.getElementById("insights").textContent = `Insights: ${result.insights}`;
        document.getElementById("results").style.display = "block";
    } catch (error) {
        document.getElementById("financial-score").textContent = "Error occurred!";
        document.getElementById("insights").textContent = error.message;
        document.getElementById("results").style.display = "block";
    }
});

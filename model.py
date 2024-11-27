def calculate_financial_score(data):
    """
    Calculate a financial score based on the input data.
    Input:
        data: Dictionary containing family-level and transaction-level data.
    Output:
        financial_score: Numeric financial score.
        insights: Insights as a string.
    """
    # Extract individual fields
    income = data.get("income", 0)
    savings = data.get("savings", 0)
    
    # Expenditure categories
    food = data.get("food", 0)
    travel = data.get("travel", 0)
    education = data.get("education", 0)
    entertainment = data.get("entertainment", 0)
    utilities = data.get("utilities", 0)
    groceries = data.get("groceries", 0)
    healthcare = data.get("healthcare", 0)
    loan_payments = data.get("loan_payments", 0)
    credit_card_spending = data.get("credit_card_spending", 0)

    # Calculate total expenditures
    total_expenditures = (
        food + travel + education + entertainment +
        utilities + groceries + healthcare
    )

    score = 100

    # Calculate key financial ratios
    savings_to_income_ratio = savings / income if income > 0 else 0
    expenses_to_income_ratio = total_expenditures / income if income > 0 else 0
    loan_to_income_ratio = loan_payments / income if income > 0 else 0
    credit_card_ratio = credit_card_spending / income if income > 0 else 0

    # Apply penalties based on ratios and values
    if savings_to_income_ratio < 0.2:
        score -= 10  # Penalty for low savings
    if expenses_to_income_ratio > 0.6:
        score -= 15  # High expenses penalty
    if loan_to_income_ratio > 0.3:
        score -= 10  # Penalty for high loan payments
    if credit_card_ratio > 0.2:
        score -= 10  # Penalty for high credit card spending

    # Insights generation
    insights = []

    if savings_to_income_ratio < 0.2:
        insights.append("Savings are below recommended levels, which affects your score.")
    else:
        insights.append("Savings are at a healthy level.")

    if expenses_to_income_ratio > 0.6:
        insights.append("Expenses are too high compared to your income, consider optimizing them.")
    else:
        insights.append("Your expenses are within a manageable range.")

    if loan_to_income_ratio > 0.3:
        insights.append("Loan payments are too high relative to your income, consider reducing debt.")
    else:
        insights.append("Loan payments are manageable.")

    if credit_card_ratio > 0.2:
        insights.append("Credit card spending is higher than recommended, consider reducing it.")
    else:
        insights.append("Credit card spending is under control.")

    # Category-specific insights
    if food > (0.1 * income):
        insights.append("Food expenditure is higher than recommended.")
    if travel > (0.05 * income):
        insights.append("Travel expenditure is higher than recommended.")
    if education > (0.1 * income):
        insights.append("Education expenses might be straining your budget.")
    if entertainment > (0.05 * income):
        insights.append("Consider limiting entertainment expenses.")
    if utilities > (0.1 * income):
        insights.append("Utility expenses are higher than usual.")
    if groceries > (0.15 * income):
        insights.append("Groceries spending is higher than average.")
    if healthcare > (0.1 * income):
        insights.append("Healthcare expenses might need attention.")

    return score, ". ".join(insights)

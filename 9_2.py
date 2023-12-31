import numpy as np
import pandas as pd
import statsmodels.api as sm

# Generate sample data
np.random.seed(42)
X = 2 * np.random.rand(100, 3)  # Assuming 3 features for demonstration
y = 4 + 3 * X[:,0] + 2 * X[:,1] + 1.5 * X[:,2] + np.random.randn(100)

# Create a DataFrame from the generated data
data = pd.DataFrame(X, columns=['X1', 'X2', 'X3'])
data['y'] = y

# Stepwise regression using forward selection
def forward_selected(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float('inf'), float('inf')
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response, ' + '.join(selected + [candidate]))
            score = sm.OLS.from_formula(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = scores_with_candidates.pop(0)
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {}".format(response, ' + '.join(selected))
    model = sm.OLS.from_formula(formula, data).fit()
    return model

# Perform stepwise regression
model = forward_selected(data, 'y')

# Print summary of the model
print(model.summary())

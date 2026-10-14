# Machine Faiure Predictor

## What this project does 
This program looks at a machine's temperature, vibration and pressure 
and predicts whether the macine is likely to fail.

## How it works 
1. I created 300 sample machine readings (the data is made up for practice).
2. I trained a Random Forest model on 80% of the data.
3. I tested it on the other 20%, which model had never seen.
4. I used recall as my main measure, because a missed failure is worse than a false alsrm.

## Results
- The model catches about 77% of the machines that fail.
- It chose this trade-off on purpose, because missing a real failure costs more than an extra inspection. 

## Limitations
- The data is synthetic, not from real machines.
- The test set only had 13 failures, so the results are rough. 

## What I learned
Accuracy alone can hide problems. Checking recall showed me how many failures the model was missing. 

## Tools used 
Python, pandas, scikit-learn, matplotlib

## Author
Emanuel
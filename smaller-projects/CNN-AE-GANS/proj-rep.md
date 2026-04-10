**Progress Report: Predicting NBA Shot Outcomes using Spatial Data and Generic Player Characteristics**

**Team:** Joseph Fodera (Data Collector & Preprocessing), Harman Aujla (Written Analysis), Ryan Styron (Ensemble Models), Matthew Voynovich (Deep NN Models)  


**1. Data Collection & Preprocessing**  
We fully implemented the data pipeline outlined in the proposal.  

- **Shot data:** Downloaded the complete Kaggle repository (mexwell/nba-shots) containing ~1.5M+ individual shot records across all seasons 2004–2024 (files: NBA_2004_Shots.csv … NBA_2024_Shots.csv). Each record includes spatial features (LOC_X, LOC_Y, SHOT_DISTANCE, BASIC_ZONE, ZONE_RANGE, ZONE_NAME) plus contextual variables (QUARTER, MINS_LEFT, SECS_LEFT, ACTION_TYPE, SHOT_TYPE).  
- **Player biometric data:** Created and hosted our own public Kaggle dataset (joefodera/biometric-attributes-of-nba-players-per-season) using the nba_api. For every season we pulled generalized, anonymized player attributes: AGE, PLAYER_HEIGHT_INCHES, PLAYER_WEIGHT, DRAFT_YEAR, POSITION_GROUP, POSITION. Player names and PLAYER_ID were intentionally dropped to enforce the “generic player characteristics” requirement.  
- **Merging & cleaning:** Season-by-season inner merge on PLAYER_ID + SEASON_1, then concatenated into a single master DataFrame. Engineered one new feature: SECONDS_REMAINING_IN_QTR = (MINS_LEFT × 60) + SECS_LEFT. All non-generalized columns (TEAM_ID, TEAM_NAME, GAME_DATE, GAME_ID, PLAYER_NAME, PLAYER_ID) were removed.  
- **Class distribution:** SHOT_MADE is slightly imbalanced (≈54 % misses, 46 % makes), which we addressed with class_weight='balanced' (logistic baseline) and balanced_subsample (Random Forest).

The resulting dataset is exactly as proposed: spatial shot features + generalized player biometrics + outcome label, spanning the full 20-year period.

**2. Modeling & Preliminary Results (Completed – Feb 28–Mar 20 timeline)**  
We followed the proposed supervised-learning pipeline:

- **Baseline:** Logistic Regression (solver='liblinear', max_iter=500, class_weight='balanced').  
  Validation accuracy: **0.590**; macro F1: **0.59**. Serves as the reference point.

- **Advanced models** (tuned via RandomizedSearchCV on a 120 k-row training subset for computational feasibility):  
  - **Random Forest** (ensemble – Ryan): Best CV F1 = 0.5043. Final validation accuracy **0.613**, F1 **0.511**.  
  - **XGBoost** (ensemble): Best CV F1 = 0.5006. Validation accuracy **0.609**, F1 **0.499**.  
  - **MLP Neural Network** (deep NN – Matthew) with StandardScaler pipeline: Best CV F1 = 0.5461. Validation accuracy **0.614**, F1 **0.509**.  

**Selected best model:** Random Forest (highest validation F1).  
Test-set performance (held-out 2024 season slice): accuracy **0.609**, precision 0.60 (made), recall 0.44 (made), F1 **0.507**.  
Confusion matrix shows the model is better at identifying misses than makes, consistent with the class distribution and the inherent stochasticity of NBA shooting.

These results already exceed the logistic baseline and confirm that spatial features (SHOT_DISTANCE, LOC_X/Y, ZONE) combined with generic player traits (AGE, HEIGHT, WEIGHT, POSITION) provide predictive signal. We have not yet run the explicit sliding-window vs. full-history temporal experiments, but the unified 20-year dataset is ready for that analysis.

**3. Next Steps (Mar 21–Apr 10 timeline – on schedule)**  
We are now entering the final two weeks of active development:

- **Visualization & Interpretation (Mar 21–27):**  
  - Feature-importance plots (Random Forest + permutation importance for MLP).  
  - Spatial heatmaps of predicted shot probability (“expected shot value”) by court location (LOC_X, LOC_Y) and zone.  
  - All metric comparison charts (accuracy, precision, recall, F1 across models and seasons).

- **Temporal Influence Analysis (critical for proposal goal):**  
  - Train the best model on (a) full 2004–2023 history vs. (b) sliding windows (e.g., last 5 seasons only).  
  - Evaluate on 2024 test set to quantify how much older data helps vs. hurts performance, especially given the documented shift toward 3-point emphasis.  
  - Report the “small margin of temporal influence” anticipated in the abstract.

- **Report & Presentation (Mar 28–Apr 11):**  
  - Harman will draft the full written analysis and conclusions.  
  - Insert all plots/figures into the final report.  
  - Divide report sections by individual contributions per team roles.  
  - Create and rehearse presentation slides summarizing problem, approach, results, and temporal findings.  

We expect to deliver a model with ≈61 % accuracy, clear feature insights, and quantitative evidence on whether all-season training or a recent sliding window is optimal—directly answering the core research question in the proposal.

The project remains on track for a strong final deliverable and potential conference submission.  

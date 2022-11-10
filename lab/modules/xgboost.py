def classifier(data,target_column):
  from sklearn.model_selection import train_test_split
  from xgboost import XGBClassifier
  from sklearn.metrics import accuracy_score
  from sklearn.metrics import confusion_matrix
  from datetime import datetime
  from matplotlib import pyplot as plt
  import numpy as np
  from mlxtend.plotting import plot_confusion_matrix
  import pandas as pd

  # TRAIN TEST SPLIT 1(example without timeseries)
  data_numeric = data.select_dtypes(include=["number"])# Force only numeric columns
  X = data_numeric.drop(target_column, axis = 1)
  y = data_numeric[target_column]
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3,random_state = 5,stratify=y)

  # TRAIN TEST SPLIT 2(example with timeseries)
  # train = data.loc[data['date']<datetime(2020,1,1)]
  # train_numeric = train.select_dtypes(include=["number"]) # Force only numeric columns
  # X_train = train_numeric.drop(target_column, axis = 1)
  # y_train = train_numeric[target_column]
  # test = data.loc[data['date']>=datetime(2020,1,1)]
  # test_numeric = test.select_dtypes(include=["number"]) # Force only numeric columns
  # X_test = test_numeric.drop(target_column, axis = 1)
  # y_test = test_numeric[target_column]

  # XGBOOST
  model = XGBClassifier()
  model.fit(X_train, y_train)

  # TEST EVALUATION
  y_pred = model.predict(X_test)
  print("Accuracy: %.2f%%" % (accuracy_score(y_test, y_pred)*100))

  # SAVE TEST RESULTS
  result = pd.concat([X_test, pd.DataFrame({"predicted":y_pred,target_column:y_test})], axis = 'columns')
  result['error'] = result['predicted']-result[target_column]
  result['error_abs'] = abs(result['predicted']-result[target_column])
  result.to_csv("test_result.csv",index=None,decimal=",",sep=";")
  
  # PLOT FEATURE IMPORTANCES
  result = {}
  for i, feature in enumerate(X.columns):
      result[feature] = model.feature_importances_[i]
  f_importances = sorted(result.items(), key=lambda x: x[1], reverse=True)

  feat_names =[a_tuple[0] for a_tuple in f_importances]
  score = [a_tuple[1] for a_tuple in f_importances]

  fig, ax = plt.subplots(figsize=(6, 6))
  ax.barh(np.arange(len(f_importances)), score, left=0.001)
  ax.set_yticks(np.arange(len(f_importances)))
  ax.set_yticklabels(feat_names)
  ax.invert_yaxis()  # feat read top-to-bottom
  ax.set_xlabel('Score')
  ax.set_ylabel('Feature')
  ax.set_title('Features importances')
  plt.show()

  df_feat_importances = pd.DataFrame()
  df_feat_importances['feature'] = feat_names
  df_feat_importances['score'] = score

  # PLOT CONFUSION MATRIX
  fig, ax = plot_confusion_matrix(conf_mat=confusion_matrix(y_test, y_pred))
  plt.xlabel('Predictions')
  plt.ylabel('Real')
  plt.title('Confusion Matrix')
  plt.show()

  return zip(feat_names, score)
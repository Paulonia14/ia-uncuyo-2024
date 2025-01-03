## Código función create_folds

create_folds <- function(dataframe, k) {
  folds <- createFolds(dataframe$inclinacion_peligrosa, k = k, list = TRUE, returnTrain = FALSE)
  return(folds)
}

## Código función cross_validation

cross_validation <- function(df, k) {
  folds <- create_folds(df, k)
  
  train_formula <- formula(inclinacion_peligrosa ~ altura + circ_tronco_cm + lat + long + seccion + especie)
  accuracy_list <- c()
  precision_list <- c()
  sensitivity_list <- c()
  specificity_list <- c()
  
  for (i in 1:k) {
    test_indices <- folds[[i]]
    data_train <- df[-test_indices, ]
    data_val <- df[test_indices, ]
    
    data_train$especie <- factor(data_train$especie, levels = levels(df$especie))
    data_val$especie <- factor(data_val$especie, levels = levels(df$especie))

    tree_model <- rpart(train_formula, data = data_train, method = "class")
    predictions_prob <- predict(tree_model, data_val, type = 'prob')[,2] 
    predictions <- ifelse(predictions_prob > 0.5, 1, 0)
    
    TP <- sum(predictions == 1 & data_val$inclinacion_peligrosa == 1)
    TN <- sum(predictions == 0 & data_val$inclinacion_peligrosa == 0)
    FP <- sum(predictions == 1 & data_val$inclinacion_peligrosa == 0)
    FN <- sum(predictions == 0 & data_val$inclinacion_peligrosa == 1)
    
    accuracy <- (TP + TN) / (TP + TN + FP + FN)
    precision <- if ((TP + FP) > 0) TP / (TP + FP) else 0
    sensitivity <- if ((TP + FN) > 0) TP / (TP + FN) else 0
    specificity <- if ((TN + FP) > 0) TN / (TN + FP) else 0
    
    accuracy_list <- c(accuracy_list, accuracy)
    precision_list <- c(precision_list, precision)
    sensitivity_list <- c(sensitivity_list, sensitivity)
    specificity_list <- c(specificity_list, specificity)
  }
  metrics_summary <- list(
    Accuracy = list(mean = mean(accuracy_list), sd = sd(accuracy_list)),
    Precision = list(mean = mean(precision_list), sd = sd(precision_list)),
    Sensitivity = list(mean = mean(sensitivity_list), sd = sd(sensitivity_list)),
    Specificity = list(mean = mean(specificity_list), sd = sd(specificity_list))
  )
  return(metrics_summary)
}


|             | Media     | Desviación Estándar |
|-------------|-----------|---------------------|
| Accuracy    | 0.8878478 | 9.882855e-5         |
| Precision   | 0         | 0                   |
| Sensitivity | 0         | 0                   |
| Specificity | 1         | 0                   |
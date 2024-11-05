suppressMessages(library(caret))
suppressMessages(library(rpart))
suppressMessages(library(dplyr))

arbolado_data <- read.csv('D:/Paula/Facultad/2024 segundo semestre/Inteligencia Artificial/Repo/ia-uncuyo-2024/tp7-ml/data/arbolado-mza-dataset.csv')

# Checkeo
arbolado_data$inclinacion_peligrosa <- as.factor(arbolado_data$inclinacion_peligrosa)
arbolado_data$especie <- as.factor(arbolado_data$especie)

create_folds <- function(dataframe, k) {
  # Particiones aleatorias para k folds
  folds <- createFolds(dataframe$inclinacion_peligrosa, k = k, list = TRUE, returnTrain = FALSE)
  return(folds)
}

cross_validation <- function(df, k) {
  # Crear los folds
  folds <- create_folds(df, k)
  
  train_formula <- formula(inclinacion_peligrosa ~ altura + circ_tronco_cm + lat + long + seccion + especie)
  accuracy_list <- c()
  precision_list <- c()
  sensitivity_list <- c()
  specificity_list <- c()
  
  for (i in 1:k) {
    # Dividir en datos de entrenamiento y test
    test_indices <- folds[[i]]
    data_train <- df[-test_indices, ]
    data_val <- df[test_indices, ]
    
    data_train$especie <- factor(data_train$especie, levels = levels(df$especie))
    data_val$especie <- factor(data_val$especie, levels = levels(df$especie))

    tree_model <- rpart(train_formula, data = data_train, method = "class")
    predictions_prob <- predict(tree_model, data_val, type = 'prob')[,2] 
    predictions <- ifelse(predictions_prob > 0.5, 1, 0)
    
    # Matriz de confusion
    TP <- sum(predictions == 1 & data_val$inclinacion_peligrosa == 1)
    TN <- sum(predictions == 0 & data_val$inclinacion_peligrosa == 0)
    FP <- sum(predictions == 1 & data_val$inclinacion_peligrosa == 0)
    FN <- sum(predictions == 0 & data_val$inclinacion_peligrosa == 1)
    
    # Calcular metricas
    accuracy <- (TP + TN) / (TP + TN + FP + FN)
    precision <- if ((TP + FP) > 0) TP / (TP + FP) else 0
    sensitivity <- if ((TP + FN) > 0) TP / (TP + FN) else 0
    specificity <- if ((TN + FP) > 0) TN / (TN + FP) else 0
    
    accuracy_list <- c(accuracy_list, accuracy)
    precision_list <- c(precision_list, precision)
    sensitivity_list <- c(sensitivity_list, sensitivity)
    specificity_list <- c(specificity_list, specificity)
  }
  
  # Media y desviación estandar 
  metrics_summary <- list(
    Accuracy = list(mean = mean(accuracy_list), sd = sd(accuracy_list)),
    Precision = list(mean = mean(precision_list), sd = sd(precision_list)),
    Sensitivity = list(mean = mean(sensitivity_list), sd = sd(sensitivity_list)),
    Specificity = list(mean = mean(specificity_list), sd = sd(specificity_list))
  )
  return(metrics_summary)
}


set.seed(42)
metrics <- cross_validation(arbolado_data, 10) # para probar con 10
print(metrics)

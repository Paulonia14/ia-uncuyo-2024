suppressMessages(library(dplyr))

set.seed(42)

data <- read.csv('D:/Paula/Facultad/2024 segundo semestre/Inteligencia Artificial/Repo/ia-uncuyo-2024/tp7-ml/data/arbolado-mendoza-dataset-validation.csv')

# ----- Ejercicio 4 - Clasificador Aleatorio -----

random_classifier <- function(df) {
  df$prediction_prob <- runif(nrow(df))
  df$prediction_class <- ifelse(df$prediction_prob > 0.5, 1, 0)
  return(df)
}
data_random <- random_classifier(data)

true_positive <- nrow(filter(data_random, inclinacion_peligrosa == 1 & prediction_class == 1))
true_negative <- nrow(filter(data_random, inclinacion_peligrosa == 0 & prediction_class == 0))
false_positive <- nrow(filter(data_random, inclinacion_peligrosa == 0 & prediction_class == 1))
false_negative <- nrow(filter(data_random, inclinacion_peligrosa == 1 & prediction_class == 0))

cat("---- Clasificador Aleatorio ----\n")
cat("True Positive (Correctamente predicho como peligroso): ", true_positive, "\n")
cat("True Negative (Correctamente predicho como no peligroso): ", true_negative, "\n")
cat("False Positive (Incorrectamente predicho como peligroso): ", false_positive, "\n")
cat("False Negative (Incorrectamente predicho como no peligroso): ", false_negative, "\n")

# Matriz de confusión
confusion_matrix_random <- matrix(c(true_negative, false_positive, false_negative, true_positive),
                                  nrow = 2, byrow = TRUE,
                                  dimnames = list("Actual" = c("No", "Yes"),
                                                  "Predicted" = c("No", "Yes")))
print(confusion_matrix_random)

# ----- Ejercicio 5 - Clasificador por Clase Mayoritaria -----

biggerclass_classifier <- function(df) {
  # Encontrar la clase mayoritaria
  major_class <- df %>%
    count(inclinacion_peligrosa) %>%
    arrange(desc(n)) %>%
    slice(1) %>%
    pull(inclinacion_peligrosa)
  # Crear la columna prediction_class
  df <- df %>%
    mutate(prediction_class = major_class)
  return(df)
}

df_biggerclass <- biggerclass_classifier(data)

# Matriz de confusión
confusion_matrix_biggerclass <- df_biggerclass %>%
  summarise(
    True_Positive = sum(inclinacion_peligrosa == 1 & prediction_class == 1),
    True_Negative = sum(inclinacion_peligrosa == 0 & prediction_class == 0),
    False_Positive = sum(inclinacion_peligrosa == 0 & prediction_class == 1),
    False_Negative = sum(inclinacion_peligrosa == 1 & prediction_class == 0)
  )

cat("\n---- Clasificador por Clase Mayoritaria ----\n")
print(confusion_matrix_biggerclass)

confusion_matrix_biggerclass_matrix <- matrix(c(confusion_matrix_biggerclass$True_Negative,
                                                confusion_matrix_biggerclass$False_Positive,
                                                confusion_matrix_biggerclass$False_Negative,
                                                confusion_matrix_biggerclass$True_Positive),
                                              nrow = 2, byrow = TRUE,
                                              dimnames = list("Actual" = c("No", "Yes"),
                                                              "Predicted" = c("No", "Yes")))
print(confusion_matrix_biggerclass_matrix)


# ----- Ejercicio 6 -----

accuracy <- function(TP, TN, FP, FN) {
  (TP + TN) / (TP + TN + FP + FN)
}

precision <- function(TP, FP) {
  if ((TP + FP) == 0) {
    return(0)
  } else {
    return(TP / (TP + FP))
  }
}


sensitivity <- function(TP, FN) {
  TP / (TP + FN)
}

specificity <- function(TN, FP) {
  TN / (TN + FP)
}

# Valores de la matriz de confusión (aleatorio)
TP_4 <- true_positive 
TN_4 <- true_negative  
FP_4 <- false_positive 
FN_4 <- false_negative 

# Calcular métricas para el clasificador aleatorio
cat("Métricas para el clasificador aleatorio:\n")
cat("Accuracy:", accuracy(TP_4, TN_4, FP_4, FN_4), "\n")
cat("Precision:", precision(TP_4, FP_4), "\n")
cat("Sensitivity:", sensitivity(TP_4, FN_4), "\n")
cat("Specificity:", specificity(TN_4, FP_4), "\n\n")

# Valores de la matriz de confusión (clase mayoritaria)
TP_5 <- confusion_matrix_biggerclass$True_Positive  
TN_5 <- confusion_matrix_biggerclass$True_Negative  
FP_5 <- confusion_matrix_biggerclass$False_Positive 
FN_5 <- confusion_matrix_biggerclass$False_Negative 

# Calcular métricas para el clasificador por clase mayoritaria
cat("Métricas para el clasificador por clase mayoritaria:\n")
cat("Accuracy:", accuracy(TP_5, TN_5, FP_5, FN_5), "\n")
cat("Precision:", precision(TP_5, FP_5), "\n")
cat("Sensitivity:", sensitivity(TP_5, FN_5), "\n")
cat("Specificity:", specificity(TN_5, FP_5), "\n")

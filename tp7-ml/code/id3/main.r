suppressMessages(library(dplyr))
getwd()  # Muestra el directorio de trabajo actual

tennis_data <- read.csv("d:/Paula/Facultad/2024 segundo semestre/Inteligencia Artificial/Repo/ia-uncuyo-2024/tp7-ml/code/id3/data/tennis.csv")
print(tennis_data)

entropy <- function(data, target_column) {
  probs <- prop.table(table(data[[target_column]]))
  -sum(probs * log2(probs + 1e-9)) # Evita log(0)
}

information_gain <- function(data, attribute, target_column) {
  total_entropy <- entropy(data, target_column)
  # Dividir datos
  values <- unique(data[[attribute]])
  weighted_entropy <- 0
  
  for (value in values) {
    subset_data <- subset(data, data[[attribute]] == value)
    prob <- nrow(subset_data) / nrow(data)
    weighted_entropy <- weighted_entropy + prob * entropy(subset_data, target_column)
  }
  total_entropy - weighted_entropy
}

id3 <- function(data, target_column, attributes) {
  if (nrow(data) == 0) {
    return("No Data")
  }
  
  # Si tienen la misma clasificación
  unique_classes <- unique(data[[target_column]])
  if (length(unique_classes) == 1) {
    return(unique_classes[1])
  }
  
  # si no quedan atributos, devuelve la clase mas común
  if (length(attributes) == 0) {
    return(names(sort(table(data[[target_column]]), decreasing = TRUE))[1])
  }
  
  # Elegir el mejor atributo
  best_attr <- attributes[which.max(sapply(attributes, function(attr) {
    information_gain(data, attr, target_column)
  }))]
  
  # Crear el nodo con el mejor atributo
  tree <- list()
  tree[[best_attr]] <- list()
  
  # Hacer el árbol
  for (value in unique(data[[best_attr]])) {
    subset_data <- subset(data, data[[best_attr]] == value)
    subtree <- id3(subset_data, target_column, setdiff(attributes, best_attr))
    tree[[best_attr]][[as.character(value)]] <- subtree
  }
  return(tree)
}

target_column <- "PlayTennis"
attributes <- setdiff(names(tennis_data), target_column)
decision_tree <- id3(tennis_data, target_column, attributes)
print(decision_tree)

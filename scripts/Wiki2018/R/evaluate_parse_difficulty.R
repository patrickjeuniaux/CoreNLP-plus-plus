INPUT_PATH <- "/home/patrick/Documents/data/Wiki20180203_TEST/6_evaluate_parse_difficulty.py.log"

DATA <- read.table(INPUT_PATH, header = TRUE, sep = "\t"); DATA


analysis <- function(data){
  
  fit <- lm(processing_time ~ input_size, data = data)
  
  plot(data$input_size, data$processing_time, xlab = 'file size (bytes)', ylab = 'parsing time (s)')
  
  abline(fit)
  
  results <- coefficients(fit)
  
  cost <- unname(results[2])
  
  return(cost)
  
}


cost <- analysis(DATA); cost



# remove the first time, that includes the time the server must load..

outlier <- which(DATA$processing_time == max(DATA$processing_time) ) 

DATA <- DATA[-outlier,]; DATA

cost <- analysis(DATA); cost


(12.29 * (10^9) * cost) / (60*60*24)


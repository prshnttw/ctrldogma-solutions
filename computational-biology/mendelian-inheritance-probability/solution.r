# Read all input values
values <- as.integer(
  strsplit(
    trimws(paste(readLines("stdin"), collapse = " ")),
    "\\s+"
  )[[1]]
)

k <- values[1]
m <- values[2]
n <- values[3]


solve <- function(k, m, n) {

  total <- k + m + n

  # Probability of aa offspring
  p_aa <- 0

  # Aa x Aa -> aa with probability 1/4
  p_aa <- p_aa +
    (m / total) *
    ((m - 1) / (total - 1)) *
    0.25

  # Aa x aa -> aa with probability 1/2
  p_aa <- p_aa +
    (m / total) *
    (n / (total - 1)) *
    0.5

  # aa x Aa -> aa with probability 1/2
  p_aa <- p_aa +
    (n / total) *
    (m / (total - 1)) *
    0.5

  # aa x aa -> aa with probability 1
  p_aa <- p_aa +
    (n / total) *
    ((n - 1) / (total - 1))

  # Dominant phenotype = not aa
  p_dominant <- 1 - p_aa

  return(p_dominant)
}


answer <- solve(k, m, n)

cat(sprintf("%.5f\n", answer))
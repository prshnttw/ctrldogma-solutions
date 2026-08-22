lines <- readLines("stdin")

n <- as.integer(trimws(lines[1]))
sequences <- trimws(lines[2:(n + 1)])


solve <- function(n, sequences) {

  length <- nchar(sequences[1])

  # Profile matrix
  profile <- list(
    A = integer(length),
    C = integer(length),
    G = integer(length),
    T = integer(length)
  )

  # Count bases at each position
  for (sequence in sequences) {

    for (i in seq_len(length)) {

      base <- substr(sequence, i, i)

      profile[[base]][i] <-
        profile[[base]][i] + 1
    }
  }

  # Build consensus
  consensus <- ""

  for (i in seq_len(length)) {

    counts <- c(
      A = profile$A[i],
      C = profile$C[i],
      G = profile$G[i],
      T = profile$T[i]
    )

    # which.max returns the first maximum,
    # giving A < C < G < T tie-breaking.
    consensus <- paste0(
      consensus,
      names(counts)[which.max(counts)]
    )
  }

  # Print output
  cat(consensus, "\n")

  for (base in c("A", "C", "G", "T")) {

    cat(
      base,
      ": ",
      paste(profile[[base]], collapse = " "),
      "\n",
      sep = ""
    )
  }
}


solve(n, sequences)
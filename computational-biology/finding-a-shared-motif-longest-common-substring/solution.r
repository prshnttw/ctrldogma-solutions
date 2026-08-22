lines <- readLines(file("stdin"))
n <- as.integer(trimws(lines[1]))
sequences <- trimws(lines[2:(n + 1)])

solve <- function(n, sequences) {

  # Use the shortest sequence as the reference
  reference <- sequences[[which.min(nchar(sequences))]]
  m <- nchar(reference)

  # common[i] = longest substring ending at position i
  # common to all sequences processed so far
  common <- rep(m, m)

  for (sequence in sequences) {

    previous <- rep(0, m + 1)
    max_common <- rep(0, m)

    for (j in seq_len(nchar(sequence))) {

      current <- rep(0, m + 1)
      seq_char <- substr(sequence, j, j)

      for (i in seq_len(m)) {

        if (substr(reference, i, i) == seq_char) {
          current[i + 1] <- previous[i] + 1

          max_common[i] <- max(
            max_common[i],
            current[i + 1]
          )
        }
      }

      previous <- current
    }

    common <- pmin(common, max_common)
  }

  best <- ""

  for (i in seq_len(m)) {

    length <- common[i]

    if (length > 0) {

      start <- i - length + 1
      candidate <- substr(reference, start, i)

      if (
        nchar(candidate) > nchar(best) ||
        (
          nchar(candidate) == nchar(best) &&
          candidate < best
        )
      ) {
        best <- candidate
      }
    }
  }

  cat(best, "\n")
}

solve(n, sequences)
# generate_demo_data.R
# Generates docs/Day1/data/rnaseq_demo.csv
# 1 000 genes × 6 samples (3 ctrl + 3 treated), 10% truly DE
# Dispersion model: phi = 4/mean + 0.08  (Love et al. 2014, Genome Biology)
#
# To replace with real data (e.g. pasilla):
#   library(pasilla)
#   data("pasillaGenes")
#   counts <- counts(pasillaGenes)[, c("treated1fb","treated2fb","treated3fb",
#                                      "untreated1fb","untreated2fb","untreated3fb")]
#   ... then adapt the write.csv call below

set.seed(2024)
n   <- 1000L
mu  <- exp(rnorm(n, 2.5, 2.2))       # log-normal means (realistic RNA-seq)
phi <- 4 / mu + 0.08                  # mean-dependent dispersion

de  <- logical(n)
de[sample(n, 100L)] <- TRUE
fc_mag <- ifelse(de, 2^(runif(n, 0.8, 2) * sample(c(-1L, 1L), n, TRUE)), 1)

ctrl <- matrix(rnbinom(n * 3, mu = mu,        size = 1 / phi), n, 3)
trt  <- matrix(rnbinom(n * 3, mu = mu * fc_mag, size = 1 / phi), n, 3)
mat  <- cbind(ctrl, trt)
colnames(mat) <- c("ctrl_1", "ctrl_2", "ctrl_3", "trt_1", "trt_2", "trt_3")

df <- data.frame(
  gene      = paste0("gene_", seq_len(n)),
  de_status = de,
  mat,
  check.names = FALSE
)

outfile <- file.path(dirname(sys.frame(1)$ofile), "data", "rnaseq_demo.csv")
if (!dir.exists(dirname(outfile))) dir.create(dirname(outfile))
write.csv(df, outfile, row.names = FALSE)
message("Written: ", outfile, "  (", nrow(df), " genes × 6 samples, ", sum(de), " DE)")

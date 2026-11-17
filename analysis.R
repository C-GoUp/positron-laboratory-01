# ============================================================
# POSITRON LABORATORY 01
# Statistical Analysis and Data Visualization
# Language: R
# Dataset: mtcars
# ============================================================

# 1. Load required package
library(ggplot2)

# 2. Load dataset
data(mtcars)

# 3. Inspect data
cat("Number of observations:", nrow(mtcars), "\n")
cat("Number of variables:", ncol(mtcars), "\n")

print(head(mtcars))

# 4. Fit linear regression model
model <- lm(mpg ~ wt, data = mtcars)

# 5. Display model results
print(summary(model))

# 6. Create visualization
plot <- ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point(size = 3, color = "steelblue") +
  geom_smooth(method = "lm", se = TRUE) +
  labs(
    title = "Vehicle Weight and Fuel Efficiency",
    subtitle = "Positron Laboratory 01",
    x = "Weight (1,000 lbs)",
    y = "Miles per Gallon"
  ) +
  theme_minimal()

# 7. Display visualization
print(plot)

# 8. Save visualization
ggsave(
  filename = "vehicle_analysis.png",
  plot = plot,
  width = 8,
  height = 5,
  units = "in",
  dpi = 300
)

cat("Laboratory 01 analysis completed successfully.\n")


# ============================================================
# 9. Export Full-Precision R Regression Reference
# ============================================================

# Load the same CSV used by Python
validation_data <- read.csv("mtcars.csv")

# Validate the dataset
stopifnot(
  nrow(validation_data) == 32,
  all(c("mpg", "wt") %in% names(validation_data)),
  all(complete.cases(validation_data[, c("mpg", "wt")]))
)

# Independently fit the reference model
validation_model <- lm(
  mpg ~ wt,
  data = validation_data
)

# Extract full-precision statistics
r_reference <- data.frame(
  metric = c("intercept", "slope", "r_squared"),
  value = c(
    unname(coef(validation_model)[1]),
    unname(coef(validation_model)[2]),
    unname(summary(validation_model)$r.squared)
  )
)


write.table(
  data.frame(
    metric = r_reference$metric,
    value = sprintf("%.17g", r_reference$value)
  ),
  file = "r_reference.csv",
  sep = ",",
  row.names = FALSE,
  col.names = TRUE,
  quote = TRUE
)


# Verify the saved reference
saved_reference <- read.csv("r_reference.csv")

stopifnot(
  identical(saved_reference$metric, r_reference$metric),
  isTRUE(all.equal(
    saved_reference$value,
    r_reference$value,
    tolerance = 1e-14
  ))
)

# Display results
print(r_reference, digits = 17)

cat("\nR reference export: PASSED\n")


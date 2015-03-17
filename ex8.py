# Formatter is s variable that contains the formatting "%r %r %r %r"

formatter = "%r %r %r %r"

# Here we will be printing to the screen various values within the formatter 
# variable

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I has this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
